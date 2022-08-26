"""
Creates a dataset of metaculus questions for testing past/future framing bias
"""
import sys
sys.path.append("..")

import re
import pandas as pd

OPTIONS = [" Yes", " No", " Unknown"]


def future_to_past(text: str) -> str:
    if text.startswith("Will") and re.search(r"\bbe\b", text):
        new_text = text.replace("Will", "Was")
        return re.sub(r"\sbe", "", new_text)
    elif text.startswith("Will"):
        return text.replace("Will", "Did")
    return text


def map_answer_index(rescol: pd.Series) -> pd.Series:
    return ((rescol - 1) * -1).fillna(2)


def main():
    filename = "metaculus_raw.csv"
    df = pd.read_csv(f"data/{filename}")
    df = df.assign(
        other_prompt=df["title"].apply(lambda x: future_to_past(x)),
        classes=[OPTIONS for _ in range(df.shape[0])],
        answer_index=map_answer_index(df["resolution"]),
    ).rename(columns={"title": "prompt"})[
        ["prompt", "other_prompt", "classes", "answer_index"]
    ]
    print(df)
    pass


if __name__ == "__main__":
    main()
