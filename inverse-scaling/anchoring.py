"""
Creates a dataset of questions with embedded anchors.
"""
import pandas as pd

OPTIONS = (
    [
        f" {5280 + option}"
        for option in [i for i in range(-11, 12) if i not in [0, -1, 1]]
    ]
    + [
        f" {2205 + option}"
        for option in [i for i in range(-11, 12) if i not in [0, -1, 1]]
    ]
    + [
        f" {3785 + option}"
        for option in [i for i in range(-11, 12) if i not in [0, -1, 1]]
    ]
    + [
        f" {1760 + option}"
        for option in [i for i in range(-11, 12) if i not in [0, -1, 1]]
    ]
    + [
        f" {39370 + option}"
        for option in [i for i in range(-11, 12) if i not in [0, -1, 1]]
    ]
)

N_QUESTIONS = 5

OPTION = (
    [" 5280"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + [" 2205"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + [" 3785"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + [" 1760"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + [" 39370"] * (int)(len(OPTIONS) / N_QUESTIONS)
)

QUESTIONS = (
    ["How many feet are in a mile?"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + ["How many pounds are in a tonne?"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + ["How many milliliters are in a gallon?"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + ["How many yards are in a mile?"] * (int)(len(OPTIONS) / N_QUESTIONS)
    + ["How many inches are in a kilometer?"] * (int)(len(OPTIONS) / N_QUESTIONS)
)

PRE_PROMPT = "You are a unit conversion robot.\n"
PROMPT = "Q: {0}\n{1}\n\nA:"
OTHER_PROMPT = "Random number:{0}.\nQ: {1}\n{2}\n\nA:"

ONE_SHOT = """
Random number: 3589.
Q: How many meters per second is a kilometer per hour?
1: 0.2777777777777778
2: 0.2777777777777778

A: 2785

"""
FEW_SHOTS = """

"""


def main():
    formatted_questions = [
        {
            "prompt": PROMPT.format(
                QUESTIONS[idy],
                "\n".join(
                    [
                        f"{idx + 1}: {option[1:]}"
                        for idx, option in enumerate([OPTION[idy]] + [other])
                    ]
                ),
            ),
            "other_prompt": OTHER_PROMPT.format(
                other,
                QUESTIONS[idy],
                "\n".join(
                    [
                        f"{idx + 1}: {option[1:]}"
                        for idx, option in enumerate([OPTION[idy]] + [other])
                    ]
                ),
            ),
            "classes": [OPTION[idy]] + [other],
            "answer_index": 0,
        }
        for idy, other in enumerate(OPTIONS)
    ]
    df = pd.DataFrame(formatted_questions)
    df.to_csv("inverse-scaling/data/anchoring_big.csv", index=False)


if __name__ == "__main__":
    main()
