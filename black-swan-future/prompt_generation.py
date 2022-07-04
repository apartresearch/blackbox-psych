"""
Script for generating prompts and answers for black swans
"""
import sys

sys.path.append("../")
import src.prompts as prompts
import pandas as pd
import re
import random
import argparse
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def read_txt(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def create_date(month, year):
    return month + " " + year


def create_dates(years, n=3):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    dates = []
    for year in years:
        for _ in range(n):
            month = random.choice(months)
            dates.append(create_date(month, year))
    return set(dates)


def create_prompt(baseprompt: str, date: str):
    return baseprompt + f"Q: What significant event happened in {date}?\n"


def clean_answer(answer: str):
    """
    Removes the A: from the answer and splits by first newline 
    """
    answer = answer.replace("A: ", "")
    answer = answer.split("\n")[0]
    return answer


def answers_to_df(answers: dict) -> pd.DataFrame:
    answer_df = pd.DataFrame.from_dict(answers, orient="index").reset_index()
    melted_df = answer_df.melt(id_vars="index", value_name="answer")
    return melted_df


def main(args: argparse.Namespace):
    """
    Main function
    """
    model_name = args.model
    minyear = args.minyear
    maxyear = args.maxyear
    n_completions = args.n
    prompts.authenticate_goose("../config.json")
    baseprompt = read_txt("question_prompt.txt")
    baseprompt = re.sub(r"^.*?I", "I", baseprompt)
    years = [str(x) for x in range(minyear, maxyear + 1)]

    # all_dates = create_dates(years)
    all_prompts = {date: create_prompt(baseprompt, date) for date in years}
    logging.info("Generating answers...")
    raw_prompts = {
        key: prompts.generate_n_prompts(
            prompt, model_name=model_name, n_completions=n_completions, stop_token="\n"
        )
        for key, prompt in tqdm(all_prompts.items())
    }
    clean_answers = {
        key: [clean_answer(answer) for answer in answers]
        for key, answers in raw_prompts.items()
    }
    logging.info("Done generating answers!")

    answer_df = answers_to_df(clean_answers).assign(evaluation=None)

    logging.info("Writing to csv...")
    answer_df.to_csv(f"output/{model_name}_answers_years.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate prompts and answers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-j-6b",
        help="Model to use",
        choices=["gpt-j-6b", "gpt-neo-20b"],
    )
    parser.add_argument("--minyear", type=int, default=2017, help="Minimum year")
    parser.add_argument("--maxyear", type=int, default=2024, help="Maximum year")
    parser.add_argument(
        "-n", type=int, default=5, help="Number of prompts to generate per question"
    )
    args = parser.parse_args()
    main(args)
