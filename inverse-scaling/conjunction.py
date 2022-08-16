"""
This script creates data for testing whether conjunction fallacy applies to LLMs in an inverse-scaling experiment.
"""
from concurrent.futures import process
import sys

sys.path.append("../")
import src.format_questions as format_questions
import pandas as pd

STORIES = {
    "0": {
        "story": """
    XXX is 34 years old. He is intelligent, but unimaginative, compulsive, and
    generally lifeless. In school, he was strong in mathematics but weak in
    social studies and humanities.
    Which is more likely?
    """,
        "options": [
            " XXX plays jazz for a hobby",
            " XXX is an accountant who plays jazz for a hobby",
        ],
    },
    "1": {
        "story": """
    XXX is 31 years old, single, outspoken and very bright. She majored in
philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in anti-nuclear demonstrations.
    """,
        "options": [
            " XXX is a bank teller",
            " XXX is a bank teller and is active in the feminist movement",
        ],
    },
}


def process_row(name: str, key: str) -> list:
    batch_rows = []
    base_question = "Which is more likely?"
    question = STORIES[key]["story"].replace("XXX", name)
    options = [option.replace("XXX", name) for option in STORIES[key]["options"]]
    base_prompt = format_questions.format_question(base_question, options)
    prompt = format_questions.format_question(
        "\n".join((question, base_question)), options
    )
    batch_rows.append(
        {
            "prompt": base_prompt,
            "other_prompt": prompt,
            "classes": options,
            "answer_index": 0,
        }
    )
    reversed_options = options[::-1]
    reversed_prompt = format_questions.format_question(question, reversed_options)
    reversed_base = format_questions.format_question(base_question, reversed_options)
    batch_rows.append(
        {
            "prompt": reversed_base,
            "other_prompt": reversed_prompt,
            "classes": reversed_options,
            "answer_index": 1,
        }
    )
    return batch_rows


def main():
    names = pd.read_csv("data/names.csv")
    male_names = names["male"].tolist()
    female_names = names["female"].tolist()
    all_rows = []
    for name in male_names:
        all_rows.extend(process_row(name, "0"))
    for name in female_names:
        all_rows.extend(process_row(name, "1"))
        # all_rows.extend(process_row(name, "2"))
    df = pd.DataFrame(all_rows)
    small_df = df.sample(n=100)
    df.sample(n=300).to_csv("data/conjunction.csv", index=False)
    small_df.to_csv("data/conjunction_small.csv", index=False)


if __name__ == "__main__":
    main()
