import pandas as pd
import re


def create_n_shot_preprompt(
    prompt: str, alternative_df: pd.DataFrame, n: int = 1
) -> str:
    prompt_options = [option[2:] for option in re.findall(r"\d:\s\w+", prompt)]
    # sample n rows from alternative that don't have both prompt options
    sample_rows = alternative_df[
        ~alternative_df["prompt"].str.contains(prompt_options[0])
        & ~alternative_df["prompt"].str.contains(prompt_options[1])
    ].sample(n=n)
    # add the answer to the sample rows
    sample_rows["prompt"] = (
        sample_rows["prompt"] + " " + (sample_rows["answer_index"] + 1).astype(str)
    )
    return "\n".join(sample_rows["prompt"].tolist())


def create_n_shots(prompt: str, alternative_df: pd.DataFrame, n: int = 1) -> str:
    """Transforms the prompt into an n-shot task without duplicating the options"""
    preprompt = create_n_shot_preprompt(prompt, alternative_df, n=n)
    return "\n".join([preprompt, prompt])
