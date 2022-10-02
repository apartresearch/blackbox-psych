import pandas as pd
import src.create_n_shots as cns


def test_create_one_shot():
    df = pd.DataFrame(
        {
            "prompt": [
                "Question: What is this?:\n1. A\n2. B\nAnswer:",
                "Question: Why is that?\n1. D\n 2. C\nAnswer:",
                "Question: Who is this\n1. B\n2. A\nAnswer:",
            ],
            "other_prompt": [
                "boink Question: What is this\n1. A\n2. B\nAnswer:",
                "boink Question: Why is that\n1. D\n2. C\nAnswer:",
                "boink Question: Who is this\n1. B\n2. A\nAnswer:",
            ],
            "classes": [[" A", " B"], [" D", " C"], [" B", " A"]],
            "answer_index": [0, 1, 1],
        }
    )
    result = cns.create_n_shots(df, n=1)
    assert result.shape == (3, 4)
    assert result.loc[0, "prompt"].count("Question") == 2
    assert result.loc[0, "prompt"].count("B") == 1

