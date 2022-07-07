"""
Creates a dataset of unsolved questions (from wikipedia)
"""
import sys

sys.path.append("../")
import src.format_questions as format_questions
import pandas as pd

OPTIONS = [" Yes", " No", " Unknown"]
QUESTIONS = [
    "Do black holes have an internal structure?",
    "Does a firewall exist around a black hole?",
    "Is dark matter a particle?",
]


def main():
    formatted_questions = [
        format_questions.format_question(question, OPTIONS) for question in QUESTIONS
    ]
    correct_index = 2
    result_df = format_questions.create_df(formatted_questions, OPTIONS, correct_index)
    result_df.to_csv("unsolved_questions.csv", index=False)


if __name__ == "__main__":
    main()
