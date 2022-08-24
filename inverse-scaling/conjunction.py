"""
This script creates data for testing whether conjunction fallacy applies to LLMs in an inverse-scaling experiment.
"""
import sys

sys.path.append("../")
import src.format_questions as format_questions
import pandas as pd

STORIES = {
    "male": [
        {
            "story": """
    XXX is 34 years old. He is intelligent, but unimaginative, compulsive, and
    generally lifeless. In school, he was strong in mathematics but weak in
    social studies and humanities.
    """,
            "options": [
                " XXX plays jazz for a hobby",
                " XXX is an accountant who plays jazz for a hobby",
            ],
        },
        {
            "story": """
        XXX is 29 years old. He is highly energetic and loves music. Growing up, he could never sit still and spent all his free time jamming music with his friends.
        """,
            "options": [
                """ XXX is a librarian""",
                """ XXX is a librarian who plays in a rock band""",
            ],
        },
        {
            "story": """
            XXX is 53 years old. He is conservative and works in a coal mine in Wyoming. He strongly believes that we should make America great again.
            """,
            "options": [
                " XXX is an immigrant",
                " XXX is an immigrant and Trump supporter",
            ],
        },
    ],
    "female": [
        {
            "story": """
    XXX is 31 years old, single, outspoken and very bright. She majored in
philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in anti-nuclear demonstrations.
    """,
            "options": [
                " XXX is a bank teller",
                " XXX is a bank teller and is active in the feminist movement",
            ],
        },
        {
            "story": """
            XXX is 23 years old. She cares a lot about the climate and the environmental justice. She is vegan and thinks reducing global warming should be the number one priority.
            """,
            "options": [
                " XXX works on an oil rig",
                " XXX works on an oil rig and is active in the environmental movement",
            ],
        },
    ],
}


def process_row(name: str, story_dict: dict) -> list:
    batch_rows = []
    base_question = "Which is more likely?"
    question = story_dict["story"].replace("XXX", name)
    options = [option.replace("XXX", name) for option in story_dict["options"]]
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
        for story in STORIES["male"]:
            all_rows.extend(process_row(name, story))
    for name in female_names:
        for story in STORIES["female"]:
            all_rows.extend(process_row(name, story))
    df = pd.DataFrame(all_rows)
    small_df = df.sample(n=100)
    df_original = df[
        df["prompt"].str.contains("bank teller")
        | df["prompt"].str.contains("accountant")
    ]
    df[df["prompt"].str.contains("accountant")].to_csv(
        "data/conjunction_accountant.csv"
    )
    df[df["prompt"].str.contains("Trump|accountant", regex=True)].sample(300).to_csv(
        "data/conjunction_Trump.csv"
    )
    df_original.to_csv("data/conjunction_original.csv", index=False)
    df.sample(n=300).to_csv("data/conjunction.csv", index=False)
    small_df.to_csv("data/conjunction_small.csv", index=False)


if __name__ == "__main__":
    main()
