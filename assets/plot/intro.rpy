label start:
    jump chapter1_1

label chapter1_1:

    "PRESS SPACE"

    scene intro_1

    "This world has lost all meaning."
    "All narratives are gone."
    "I am here to fix this world."

    scene intro_2

    "Play Poker Solitaire to earn score."
    "Each turn you place one card on any free place on table."
    "Your goal is to maximize score by making poker combinations."

    game_mechanic "card play poker"

    "You can spend your score to buy action cards."
    "There is 3 types of action cards that affect story narrative."
    "Setting, Plot Twist and Conflict"

    game_mechanic "card shop"

    game_mechanic "card play narrative characters"

    game_mechanic "card play narrative setting"

    llm_generate storyteller "{PROMPT} Setting of novel is: ```{SETTING}```. Characters are: ```{CHARACTERS}."

    game_mechanic "card play narrative conflict"

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a conflict: ```{CONFLICT}```."
yo
    game_mechanic "card play narrative plot twist"

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    scene intro_1

    game_mechanic "card play poker"
    game_mechanic "card shop"

    game_mechanic "card play narrative character"
    game_mechanic "card play narrative setting"

    llm_generate storyteller "{PROMPT} Setting of novel is: ```{SETTING}```. Characters are: ```{CHARACTERS}."

    game_mechanic "card play narrative conflict"

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a conflict: ```{CONFLICT}```."

    game_mechanic "card play narrative plot twist"

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    scene intro_1

    game_mechanic "card play poker"
    game_mechanic "card shop"

    game_mechanic "card play narrative character"
    game_mechanic "card play narrative setting"

    llm_generate storyteller "{PROMPT} Setting of novel is: ```{SETTING}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    llm_generate storyteller "{PROMPT} Story so far ```{STORY}```. Characters are: ```{CHARACTERS}. Continue this story with a plot twist: ```{PLOT TWIST}```."

    "THE END OF DEMO VERSION"
    