from typing import Union
import pandas as pd


def add_options(question: str, options: list) -> str:
    """
    Adds options to a question
    """
    options = [f"{i + 1}:{option}" for i, option in enumerate(options)]
    return "\n".join([question] + options)


def format_question(question: str, options: list, q: bool = True) -> str:
    """
    Formats a question with options
    """
    return ("Question: " if q else "") + add_options(question, options) + "\nAnswer:"


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


def create_df_from_dict(questions: dict, answer_index: int) -> pd.DataFrame:
    """
    Creates a dataframe with questions and options
    """
    output_dictlist = [
        {
            "prompt": format_question(question, options),
            "classes": options,
            "answer_index": answer_index,
        }
        for question, options in questions.items()
    ]

    return pd.DataFrame(output_dictlist)


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
