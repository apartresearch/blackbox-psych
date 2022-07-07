import src.format_questions as format_questions
import pandas as pd


def test_add_options():
    question = "What is the answer to this question?"
    options = ["Yes", "No", "Unknown"]
    expected = "What is the answer to this question?\n1: Yes\n2: No\n3: Unknown"
    actual = format_questions.add_options(question, options)
    assert actual == expected


def test_format_questions():
    question = "What is the answer to this question?"
    options = ["Yes", "No", "Unknown"]
    expected = "Question: What is the answer to this question?\n1: Yes\n2: No\n3: Unknown\nAnswer:"
    actual = format_questions.format_question(question, options)
    assert actual == expected


def test_create_df():
    questions = [
        "What is the answer to this question?",
        "What is the answer to that question?",
    ]
    options = [" Yes", " No", " Unknown"]
    answer_index = 2
    expected = pd.DataFrame(
        {
            "prompt": questions,
            "classes": [options, options],
            "answer_index": answer_index,
        }
    )
    actual = format_questions.create_df(questions, options, answer_index)
    assert actual.equals(expected)
    assert actual.columns[1] == "classes"

