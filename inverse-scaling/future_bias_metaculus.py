"""
Creates a dataset of metaculus questions for testing past/future framing bias
"""
import sys

sys.path.append("..")

import src.format_questions as format_questions
import re
import pandas as pd

OPTIONS = [" Yes", " No", " Unknown"]


def future_to_past(text: str) -> str:
    if "Will" in text and re.search(r"\bbe\b", text):
        new_text = text.replace("Will", "Was")
        return re.sub(r"\sbe", "", new_text)
    elif "Will" in text:
        return text.replace("Will", "Did")
    return text


def map_answer_index(rescol: pd.Series) -> pd.Series:
    """Sneaky way to map the resolutions from metaculus into the answer index of OPTIONS"""
    return ((rescol - 1) * -1).fillna(2)


def main():
    filename = "metaculus_raw.csv"
    df = pd.read_csv(f"data/{filename}")
    df = df.assign(
        prompt=df["title"].apply(lambda x: format_questions.format_question(x, OPTIONS))
    )
    df = df.assign(
        other_prompt=df["prompt"].apply(lambda x: future_to_past(x)),
        classes=[OPTIONS for _ in range(df.shape[0])],
        answer_index=map_answer_index(df["resolution"]),
    )[["prompt", "other_prompt", "classes", "answer_index"]]

    df.to_csv("data/future_bias_metaculus.csv", index=False)
    df.sample(n=100).to_csv("data/future_bias_metaculus_sample.csv", index=False)
    pass


if __name__ == "__main__":
    main()
