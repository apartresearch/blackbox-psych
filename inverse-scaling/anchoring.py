"""
Creates a dataset of questions with embedded anchors.
"""
from numpy import indices
import pandas as pd

# Different questions
# ...with different scales of numbers...
# ...and different scales of anchoring...
# ...in two versions of 1/2 and answer/anchor...
# ...with few-shot and one-shot.

QUESTIONS = [
    {
        "correct": 5280,
        "anchor_scale": 1,
        "q": "How many feet are in a mile?",
    },
    {
        "correct": 2205,
        "anchor_scale": 1,
        "q": "How many pounds are in a tonne?",
    },
    {
        "correct": 3785,
        "anchor_scale": 1,
        "q": "How many milliliters are in a gallon?",
    },
    {
        "correct": 1760,
        "anchor_scale": 1,
        "q": "How many yards are in a mile?",
    },
    {
        "correct": 39370,
        "anchor_scale": 1,
        "q": "How many inches are in a kilometer?",
    },
    {
        "correct": 3.28,
        "anchor_scale": 0.01,
        "q": "How many feet are in a meter?",
    },
    {
        "correct": 1.6,
        "anchor_scale": 0.01,
        "q": "How many kilometers are in a mile?",
    },
    {
        "correct": 3,
        "anchor_scale": 0.01,
        "q": "How many feet are in a yard?",
    },
    {
        "correct": 36,
        "anchor_scale": 0.1,
        "q": "How many inches are in a yard?",
    },
    {
        "correct": 12,
        "anchor_scale": 0.1,
        "q": "How many inches are in a foot?",
    },
    {
        "correct": 100,
        "anchor_scale": 0.1,
        "q": "How many centimeters are in a meter?",
    },
]
ANCHORS = [i for i in range(-11, 12) if i not in [0, -1, 1]]

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
FEW_SHOT = """

"""


def main():
    all_q = [
        {
            "correct": f" {q['correct']}",
            "anchor": f" {q['correct'] + anchor_diff * q['anchor_scale']}",
            "q": q["q"],
            "indices": index == 1,
            "anchor_scale": q["anchor_scale"],
        }
        for q in QUESTIONS
        for anchor_diff in ANCHORS
        for index in list(range(0, 2))
    ]

    formatted_questions = [
        {
            "prompt": PROMPT.format(q["q"], f"1: {q['correct']}\n2: {q['anchor']}"),
            "other_prompt": OTHER_PROMPT.format(
                q["anchor"], q["q"], f"1: {q['correct']}\n2: {q['anchor']}"
            ),
            "classes": [" 1", " 2"] if q["indices"] else [q["correct"], q["anchor"]],
            "answer_index": 0,
            "indices": q["indices"],
            "anchor_scale": q["anchor_scale"],
        }
        for q in all_q
    ]
    df = pd.DataFrame(formatted_questions)
    df.to_csv("inverse-scaling/data/anchoring_raw.csv", index=False)


if __name__ == "__main__":
    main()
