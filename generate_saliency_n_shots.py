"""Creates n-shot prompts without having the original question duplicated """
import sys

sys.path.append("..")
import argparse
import pandas as pd
import src.create_n_shots as cns
from tqdm import tqdm
from pathlib import Path

OPENAI = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with 'Unknown'."


def format_n_shots(preprompt: str, prompt: str) -> str:
    """ Util function to get rid of openai preprompt"""
    join_prompt = "\n".join([preprompt, prompt])
    split_prompt = join_prompt.split("\n", 1)
    no_openai_prompt = split_prompt[1].replace(OPENAI, "")
    return "\n".join([split_prompt[0], no_openai_prompt])


def main(args: argparse.Namespace) -> None:
    N = args.n
    FILE_NAME = args.filename
    filepath = Path("data") / FILE_NAME
    assert filepath.exists(), f"{filepath} does not exist"
    df = pd.read_csv(filepath)
    for idx, row in tqdm(df.iterrows()):
        preprompt = cns.create_n_shot_preprompt(row["prompt"], df, n=N)
        df.loc[idx, "prompt"] = format_n_shots(preprompt, row["prompt"])
        df.loc[idx, "other_prompt"] = format_n_shots(preprompt, row["other_prompt"])

    df.to_csv(f"data/all_saliency_big_{N}shot.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate n-shot prompts",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--filename", type=str, default="all_saliency_big.csv")
    parser.add_argument("--n", type=int, default=2, help="Number of shots")
    args = parser.parse_args()
    main(args)
