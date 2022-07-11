from typing import Union
import pandas as pd


def add_options(question: str, options: list) -> str:
    """
    Adds options to a question
    """
    options = [f"{i + 1}: {option}" for i, option in enumerate(options)]
    return "\n".join([question] + options)


def format_question(question: str, options: list) -> str:
    """
    Formats a question with options
    """
    return "Question: " + add_options(question, options) + "\nAnswer:"


def create_df(
    questions: list, options: list, answer_index: Union[int, list]
) -> pd.DataFrame:
    """
    Creates a dataframe with questions and options
    """
    return pd.DataFrame(
        {
            "prompt": questions,
            "classes": [options for _ in questions],
            "answer_index": answer_index,
        }
    )


def create_diff_df(
    questions: list, other_qs: list, options: list, answer_index: int
) -> pd.DataFrame:
    """
    Creates a dataframe with questions and options
    """
    return create_df(questions, options, answer_index).assign(other_prompt=other_qs)[
        ["prompt", "other_prompt", "classes", "answer_index"]
    ]


def format_commodity_question(
    commodity_dict: dict, commodity: str, year: int, price: int
) -> str:
    """
    Formats a question for a commodity
    """
    return f"Will the price of {commodity} exceed {price} {commodity_dict[commodity]['unit']} in {year}?"
