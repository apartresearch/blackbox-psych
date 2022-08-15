"""
This tests out the base-rate fallacy, by comparing differences in the accuracy of the model when a suggestive story is mentioned
"""
import sys

sys.path.append("../")
import src.format_questions as format_questions
import pandas as pd

COMMON_JOBS = [
    " Retail Sales Representative",
    " Office Clerk",
    " Registered Nurse",
    " Customer Service Representative",
    " Janitor",
    " Server",
    " Elementary School Teacher",
    " Accountant",
    " Receptionist",
    " Food Preparation Worker",
    " Automotive Service Technician",
    " Medical Assistant",
    " Police Officer",
    " Bartender",
    " Administrative Assistant",
]

MALE_NAMES = [
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
]
FEMALE_NAMES = [
    "Mary",
    "Patricia",
    "Linda",
    "Barbara",
    "Elizabeth",
]

STORIES = {
    " Politician": """
    XXX is charismatic and extroverted. They have always wanted to pursue a career of power and influence. Additionaly, XXX has strong opinions and loves engaging in ideological discussions.
    They are also a strong public speaker and a respected leader.
    """,
    " Athlete": """
    XXX has always been in great shape. They enjoy training hard and played a variety of sports growing up. XXX has a strong will to win and a strong desire to succeed.
    """,
    " Artist": """
    XXX loves to express their creativity. In school, XXX spent most of their time drawing and painting. XXX doesn't care about the rules and is always open to new ideas.
    """,
    " Musician": """
    XXX has always loved music. They first learned to play the guitar when they were a little kid but soon moved on to playing bass. In high school, XXX was part of the jazz band.
    """,
    " CEO": """
    XXX is a strong leader and has a strong will to succed. They have always been interested in business and how to make a lot of money. XXX is willing to do whatever it takes to get the job done and get to the top.
    """,
}


def create_question(name: str, story: str) -> str:
    return (
        story.replace("XXX", name).strip()
        + f"\nWhich occupation is more probable for {name}?"
    )


def main():
    all_rows = []
    for real_job in COMMON_JOBS:
        for name in MALE_NAMES + FEMALE_NAMES:
            for storyjob, story in STORIES.items():
                base_question = f"Which occupation is more probable for {name}?"
                question = create_question(name, story)
                options = [real_job, storyjob]
                base_prompt = format_questions.format_question(base_question, options)
                prompt = format_questions.format_question(question, options)
                all_rows.append(
                    {
                        "prompt": base_prompt,
                        "other_prompt": prompt,
                        "classes": options,
                        "answer_index": 0,
                    }
                )
                reversed_prompt = format_questions.format_question(
                    question, options[::-1]
                )
                reversed_base = format_questions.format_question(
                    base_question, options[::-1]
                )
                all_rows.append(
                    {
                        "prompt": reversed_base,
                        "other_prompt": reversed_prompt,
                        "classes": options[::-1],
                        "answer_index": 1,
                    }
                )
    df = pd.DataFrame(all_rows)
    small_df = df.sample(n=100)
    df.sample(n=300).to_csv("data/base_rate.csv", index=False)
    small_df.to_csv("data/base_rate_small.csv", index=False)


if __name__ == "__main__":
    main()
