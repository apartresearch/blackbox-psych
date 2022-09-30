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
    # {
    #     "correct": 5280,
    #     "anchor_scale": 1,
    #     "q": "How many feet are in a mile?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 2205,
    #     "anchor_scale": 1,
    #     "q": "How many pounds are in a tonne?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 3785,
    #     "anchor_scale": 1,
    #     "q": "How many milliliters are in a gallon?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 1760,
    #     "anchor_scale": 1,
    #     "q": "How many yards are in a mile?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 39370,
    #     "anchor_scale": 1,
    #     "q": "How many inches are in a kilometer?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 3.28,
    #     "anchor_scale": 0.01,
    #     "q": "How many feet are in a meter?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 1.6,
    #     "anchor_scale": 0.01,
    #     "q": "How many kilometers are in a mile?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 3,
    #     "anchor_scale": 0.01,
    #     "q": "How many feet are in a yard?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 36,
    #     "anchor_scale": 1,
    #     "q": "How many inches are in a yard?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 12,
    #     "anchor_scale": 1,
    #     "q": "How many inches are in a foot?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 39370,
    #     "anchor_scale": 10,
    #     "q": "How many inches are in a kilometer?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 4046,
    #     "anchor_scale": 1,
    #     "q": "How many square meters are in an acre?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 107639,
    #     "anchor_scale": 10,
    #     "q": "How many square feet are in a hectare?",
    #     "type": "unit",
    # },
    # {
    #     "correct": 43560,
    #     "anchor_scale": 1,
    #     "q": "How many square feet are in an acre?",
    #     "type": "unit",
    # },
    {
        "correct": 100,
        "anchor_scale": 1,
        "q": "How many centimeters are in a meter?",
        "type": "unit",
    },
    {
        "correct": 2340,
        "anchor_scale": 1,
        "q": "How long is the Mississippi River in miles?",
        "type": "unit",
    },
    {
        "correct": 305,
        "anchor_scale": 1,
        "q": "How tall is the Statue of Liberty in feet?",
        "type": "unit",
    },
    {
        "correct": 16,
        "anchor_scale": 1,
        "q": "What was the number of Lincoln's presidency?",
        "type": "unit",
    },
    {
        "correct": 11_034,
        "anchor_scale": 10,
        "q": "How deep is the Mariana Trench in meters?",
        "type": "unit",
    },
    {
        "correct": 29_032,
        "anchor_scale": 10,
        "q": "What is the height of Mount Everest in feet?",
        "type": "unit",
    },
    {
        "correct": 238_900,
        "anchor_scale": 100,
        "q": "What is the distance to the moon in miles?",
        "type": "unit",
    },
    {
        "correct": 24_901,
        "anchor_scale": 10,
        "q": "What is the circumference of Earth at the Equator?",
        "type": "unit",
    },
    {
        "correct": 8760,
        "anchor_scale": 10,
        "q": "How many hours are in a year?",
        "type": "unit",
    },
    {
        "correct": 21_196,
        "anchor_scale": 10,
        "q": "How long is the Chinese Wall in kilometers?",
        "type": "large",
    },
    {
        "correct": 6,
        "anchor_scale": 1,
        "q": "How many players are there on an ice hockey team?",
        "type": "unit",
    },
    {
        "correct": 44,
        "anchor_scale": 1,
        "q": "Which number president was Obama of the United States?",
        "type": "unit",
    },
    {
        "correct": 404,
        "anchor_scale": 1,
        "q": "Which number error message arises when there is a broken link??",
        "type": "unit",
    },
    {
        "correct": 1939,
        "anchor_scale": 1,
        "q": "When did World War 2 start?",
        "type": "unit",
    },
    {
        "correct": 2013,
        "anchor_scale": 1,
        "q": "Which year did Nelson Mandela die?",
        "type": "unit",
    },
    {
        "correct": 1564,
        "anchor_scale": 1,
        "q": "What year was William Shakespear born?",
        "type": "unit",
    },
    {
        "correct": 1955,
        "anchor_scale": 1,
        "q": "What year did the Vietnam War start?",
        "type": "unit",
    },
    {
        "correct": 1776,
        "anchor_scale": 1,
        "q": "What year was the us founded?",
        "type": "unit",
    },
    {
        "correct": 27,
        "anchor_scale": 1,
        "q": "How many countries are in the European Union?",
        "type": "unit",
    },
    {
        "correct": 50,
        "anchor_scale": 1,
        "q": "How many states are in the United States?",
        "type": "unit",
    },
    {
        "correct": 8,
        "anchor_scale": 1,
        "q": "How many universities are there in Denmark?",
        "type": "unit",
    },
    {
        "correct": 11,
        "anchor_scale": 1,
        "q": "How many players are there in an American football team?",
        "type": "unit",
    },
    {
        "correct": 535,
        "anchor_scale": 1,
        "q": "how many members are there of the US congress?",
        "type": "unit",
    },
    {
        "correct": 72,
        "anchor_scale": 1,
        "q": "How many years was the longest rule of a monarch?",
        "type": "unit",
    },
    {
        "correct": 195,
        "anchor_scale": 1,
        "q": "How many countries are there in the world?",
        "type": "unit",
    },
    {
        "correct": 72,
        "anchor_scale": 1,
        "q": "How many years was the longest rule of a monarch?",
        "type": "unit",
    },
    {
        "correct": 100,
        "anchor_scale": 1,
        "q": "How many years is a century?",
        "type": "unit",
    },
    {
        "correct": 22,
        "anchor_scale": 1,
        "q": "How many years was the Powhatan War?",
        "type": "unit",
    },
    {
        "correct": 100,
        "anchor_scale": 1,
        "q": "How many years is a century?",
        "type": "unit",
    },
    {
        "correct": 46,
        "anchor_scale": 1,
        "q": "How many us presidents have been in office?",
        "type": "unit",
    },
]
ANCHORS = [i for i in range(-11, 12) if i not in [0, -1, 1]]

PRE_PROMPT = "You are a unit conversion robot.\n"
PROMPT = "Q: {0}\n{1}\n\nAnswer:"
OTHER_PROMPT = "Random number:{0}.\nQ: {1}\n{2}\n\nAnswer:"

SHOTS = [
    """
Random number: 102.
Q: How many centimeters are in a meter?
A: 100
B: 102

Answer: 100

""",
    """
Random number: 997.
Q: How many microliters are in a milliliter?
A: 997
B: 1000

Answer: 1000

""",
    """
Random number: 300.
Q: How many millimeters are in a foot?
A: 300
B: 305

Answer: 305

""",
]

SHOTS_12 = [
    """
Random number: 102.
Q: How many centimeters are in a meter?
A: 100
B: 102

Answer: A

""",
    """
Random number: 997.
Q: How many microliters are in a milliliter?
A: 997
B: 1000

Answer: B

""",
    """
Random number: 300.
Q: How many millimeters are in a foot?
A: 300
B: 305

Answer: B

""",
]


def main():
    all_q = [
        {
            "correct": f" {q['correct']}",
            "correct_n": q["correct"],
            "anchor": f" {q['correct'] + (int)(anchor_diff * q['anchor_scale'])}",
            "q": q["q"],
            "indices": index == 1,
            "anchor_scale": (int)(q["anchor_scale"]),
            "kshot": kshot,
            "preprompt": preprompt,
            "reverse": reverse,
            "type": q["type"],
        }
        for q in QUESTIONS
        for anchor_diff in ANCHORS
        for index in [1, 2]
        for kshot in [0, 1, 2, 3]
        for preprompt in [False, True]
        for reverse in [False, True]
    ]

    formatted_questions = [
        {
            "prompt": (PRE_PROMPT if q["preprompt"] else "")
            + "".join(SHOTS_12[: q["kshot"]] if q["indices"] else SHOTS[: q["kshot"]])
            + PROMPT.format(
                q["q"],
                f"A: {q['anchor'] if q['reverse'] else q['correct']}\nB: {q['correct'] if q['reverse'] else q['anchor']}",
            ),
            "other_prompt": (PRE_PROMPT if q["preprompt"] else "")
            + "".join(SHOTS_12[: q["kshot"]] if q["indices"] else SHOTS[: q["kshot"]])
            + OTHER_PROMPT.format(
                q["anchor"],
                q["q"],
                f"A: {q['anchor'] if q['reverse'] else q['correct']}\nB: {q['correct'] if q['reverse'] else q['anchor']}",
            ),
            "classes": [" A", " B"]
            if q["indices"]
            else (
                [q["anchor"], q["correct"]]
                if q["reverse"]
                else [q["correct"], q["anchor"]]
            ),
            "answer_index": 1 if q["reverse"] else 0,
            "indices": q["indices"],
            "anchor_scale": q["anchor_scale"],
            "kshot": q["kshot"],
            "preprompt": q["preprompt"],
            "reverse": q["reverse"],
            "type": q["type"],
            "correct_n": q["correct_n"],
        }
        for q in all_q
    ]

    df = pd.DataFrame(formatted_questions)
    df.to_csv("data/anchoring_raw.csv", index=False)

    df.loc[
        (df["kshot"] == 0)
        & (df["preprompt"] == False)
        & (df["indices"] == False)
        & (df["type"] == "other")
    ].to_csv(
        "data/anchoring_raw_other_kshot0_nopreprompt_num.csv",
        index=False,
    )

    df.loc[
        (df["kshot"] == 3)
        & (df["preprompt"] == False)
        & (df["indices"] == False)
        & (df["type"] == "other")
    ].to_csv(
        "data/anchoring_raw_other_kshot3_nopreprompt_num.csv",
        index=False,
    )

    df = df[df["type"] == "unit"]

    df[df["kshot"] == 0].to_csv("data/anchoring_raw_kshot0.csv", index=False)
    df[df["kshot"] == 1].to_csv("data/anchoring_raw_kshot1.csv", index=False)
    df[df["kshot"] == 2].to_csv("data/anchoring_raw_kshot2.csv", index=False)
    df[df["kshot"] == 3].to_csv("data/anchoring_raw_kshot3.csv", index=False)
    df.loc[(df["kshot"] == 0) & (df["preprompt"] == True)].to_csv(
        "data/anchoring_raw_kshot0_preprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 1) & (df["preprompt"] == True)].to_csv(
        "data/anchoring_raw_kshot1_preprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 2) & (df["preprompt"] == True)].to_csv(
        "data/anchoring_raw_kshot2_preprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 3) & (df["preprompt"] == True)].to_csv(
        "data/anchoring_raw_kshot3_preprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 0) & (df["preprompt"] == False)].to_csv(
        "data/anchoring_raw_kshot0_nopreprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 1) & (df["preprompt"] == False)].to_csv(
        "data/anchoring_raw_kshot1_nopreprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 2) & (df["preprompt"] == False)].to_csv(
        "data/anchoring_raw_kshot2_nopreprompt.csv", index=False
    )
    df.loc[(df["kshot"] == 3) & (df["preprompt"] == False)].to_csv(
        "data/anchoring_raw_kshot3_nopreprompt.csv", index=False
    )

    df.loc[
        (df["kshot"] == 0) & (df["preprompt"] == False) & (df["indices"] == True)
    ].to_csv("data/anchoring_raw_kshot0_nopreprompt_indices.csv", index=False)
    df.loc[
        (df["kshot"] == 0) & (df["preprompt"] == False) & (df["indices"] == False)
    ].to_csv("data/anchoring_raw_kshot0_nopreprompt_num.csv", index=False)

    df.loc[
        (df["kshot"] == 3) & (df["preprompt"] == False) & (df["indices"] == True)
    ].to_csv("data/anchoring_raw_kshot3_nopreprompt_indices.csv", index=False)

    df.loc[
        (df["kshot"] == 3) & (df["preprompt"] == False) & (df["indices"] == False)
    ].to_csv("data/anchoring_raw_kshot3_nopreprompt_num.csv", index=False)

    df[df["preprompt"] == True].to_csv("data/anchoring_raw_preprompt.csv", index=False)
    df[df["preprompt"] == False].to_csv(
        "data/anchoring_raw_nopreprempt.csv", index=False
    )
    df[df["indices"] == False].to_csv("data/anchoring_num.csv", index=False)

    df.loc[
        (df["kshot"] == 0)
        & (df["preprompt"] == False)
        & (df["indices"] == True)
        & (df["correct_n"] < 100)
    ].to_csv("data/anchoring_raw_kshot0_nopreprompt_indices_sub100.csv", index=False)
    df.loc[
        (df["kshot"] == 0)
        & (df["preprompt"] == False)
        & (df["indices"] == True)
        & (df["correct_n"] > 100)
    ].to_csv("data/anchoring_raw_kshot0_nopreprompt_indices_super100.csv", index=False)


if __name__ == "__main__":
    main()
