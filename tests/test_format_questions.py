import src.format_questions as format_questions


def test_add_options():
    question = "What is the answer to this question?"
    options = ["Yes", "No", "Unknown"]
    expected = "What is the answer to this question?\n1: Yes\n2: No\n3: Unknown"
    actual = format_questions.add_options(question, options)
    assert actual == expected


def test_format_questions():
    question = "What is the answer to this question?"
    options = ["Yes", "No", "Unknown"]
    expected = (
        "What is the answer to this question?\n1: Yes\n2: No\n3: Unknown\nAnswer:"
    )
    actual = format_questions.format_question(question, options)
    assert actual == expected
