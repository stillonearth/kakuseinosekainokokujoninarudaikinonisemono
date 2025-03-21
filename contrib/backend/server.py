import base64
import io
import uuid
import subprocess
import sqlite3
import uuid
import json
import os

from flask import Flask, request, jsonify, send_file
from together import Together
from PIL import Image


API_KEY = "5dad429861935a07b26c1cb4033aa3ef8651d2acd16eb729939aa1b739f87d9d"
LLM_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
TOGETHER_CLIENT = Together(api_key=API_KEY)

app = Flask(__name__)


@app.route("/api/llm", methods=["POST"])
def llm():
    data = request.get_json()
    prompt = data.get("prompt", "")

    messages = [
        {"role": "user", "content": prompt},
    ]

    response = TOGETHER_CLIENT.chat.completions.create(
        model=LLM_MODEL, messages=messages
    )
    response = response.choices[0].message.content

    return jsonify({"response": response}), 200


@app.route("/api/image", methods=["GET"])
def generate_image():
    prompt = request.args.get("prompt", "")
    response = TOGETHER_CLIENT.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell-Free",
        width=1792,
        height=1008,
        steps=4,
        n=1,
        response_format="b64_json",
        update_at="2024-11-20T09:27:43.295Z",
    )

    image_bytes = base64.b64decode(response.data[0].b64_json)
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)

    file_extension = image.format.lower()
    unique_filename = f"{uuid.uuid4()}.{file_extension}"

    image_path = f"images/{unique_filename}"
    image.save(image_path)

    return send_file(image_path, mimetype="image/jpeg")

@app.route("/api/image/v2", methods=["GET"])
def generate_image_v2():
    prompt = request.args.get("prompt", "")
    response = TOGETHER_CLIENT.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell-Free",
        width=1792,
        height=1008,
        steps=4,
        n=1,
        response_format="b64_json",
        update_at="2024-11-20T09:27:43.295Z",
    )

    image_bytes = base64.b64decode(response.data[0].b64_json)
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)

    file_extension = image.format.lower()
    unique_filename = f"{uuid.uuid4()}.{file_extension}"

    image_path = f"images/{unique_filename}"
    image.save(image_path)

    return {'hash': unique_filename}

@app.route("/api/image/v2/<image_name>", methods=["GET"])
def serve_image_by_hash(image_name):
    image_path = f"images/{image_name}"

    if not os.path.exists(image_path) or not os.path.isfile(image_path):
        return jsonify({"error": "Image not found"}), 404

    return send_file(image_path, mimetype="image/jpeg")


def save_scenario(scenario, nft_id):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS scenarios (nft_id INTEGER PRIMARY KEY, data TEXT)"""
        )

        uuid_key = str(uuid.uuid4())
        cursor.execute("INSERT INTO scenarios VALUES (?, ?)", (nft_id, scenario))
        conn.commit()

    return uuid_key


@app.route("/api/nft/create", methods=["POST"])
def create_story_nft():
    data = request.get_json()

    scenario = data.get("scenario", "")
    owner = data.get("owner", "")

    command = ["node", "mint.js", "mint", owner]
    result = subprocess.run(command, capture_output=True, text=True).stdout.strip("\n")

    nft_id = int(result)

    save_scenario(scenario, nft_id)

    return jsonify({"nft_id": nft_id}), 200


@app.route("/api/nft/<nft_id>", methods=["GET"])
def get_story_nft(nft_id):
    if not nft_id:
        return

    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()

        # Query the scenario_nfts table for the given uuid
        query = "SELECT data FROM scenarios WHERE nft_id = ?"
        cursor.execute(query, (nft_id,))

        # Check if a record was found
        result = cursor.fetchone()
        if not result:
            return jsonify({"error": "NFT not found"}), 404

        scenario = result[0]

        # Create a standard NFT JSON response
        nft_response = {
            "name": f"NFT {nft_id}",
            "description": "nft decription",
            "image": None,  # Create image
            "metadata": {"scenario": scenario},
        }

        return jsonify(nft_response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
