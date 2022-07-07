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


def create_df(questions: list, options: list, answer_index: int) -> pd.DataFrame:
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
