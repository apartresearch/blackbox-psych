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
    return add_options(question, options) + "\nAnswer:"
