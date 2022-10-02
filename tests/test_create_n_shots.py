import pandas as pd
import src.create_n_shots as cns


def test_create_one_shot():
    prompt = "Question: What is bigger?\n1: milimetre \n2: nanometre?\nAnswer:"
    alternative_df = pd.DataFrame(
        {
            "prompt": [
                "Question: What is larger?\n1: milimetre \n2: nanometre?\nAnswer:",
                "Question: What is the biggest?\n1: metre \n2: yard?\nAnswer:",
                "Question: Which is larger?\n1: kilometre\n2: mile?\nAnswer:",
            ],
            "answer_index": [0, 0, 1],
        }
    )
    result = cns.create_n_shots(prompt, alternative_df, n=1)
    assert result.count("Question") == 2
    assert result.count("milimetre") < 2 or result.count("nanometre") < 2
    assert result.count("Answer: 1") == 1 or result.count("Answer: 2") == 1


def test_create_two_shots():
    prompt = "Question: What is bigger?\n1: milimetre \n2: nanometre?\nAnswer:"
    alternative_df = pd.DataFrame(
        {
            "prompt": [
                "Question: What is larger?\n1: milimetre \n2: nanometre?\nAnswer:",
                "Question: What is the biggest?\n1: metre \n2: yard?\nAnswer:",
                "Question: Which is larger?\n1: kilometre\n2: mile?\nAnswer:",
            ],
            "answer_index": [0, 0, 1],
        }
    )
    result = cns.create_n_shots(prompt, alternative_df, n=2)
    assert result.count("Question") == 3
    assert alternative_df.loc[0, "prompt"] not in result
