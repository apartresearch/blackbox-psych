import sys

sys.path.append("../")
import src.format_questions as format_questions
import random
import pandas as pd

SEQ_LEN = 100
N_PROMPTS = 300


def generate_random_ht(seq_len: int):
    return "".join(random.choices(population=["H", "T"], k=seq_len))


def random_seq_prompt(random_seq: str, random_cont: str, all_one: str):
    question = f"{random_seq}\nWhich continuation is more probable?"
    options = [f" {random_cont}", f" {all_one}", " Neither"]
    return {format_questions.format_question(question, options): options}


def create_random_prompt(seq_len: int, answer_len: int):
    random_seq = generate_random_ht(seq_len)
    random_cont = generate_random_ht(answer_len)
    all_one = random.choice(["T" * answer_len, "H" * answer_len])
    return random_seq_prompt(random_seq, random_cont, all_one)


def main():
    prompts = [create_random_prompt(SEQ_LEN, 5) for _ in range(N_PROMPTS)]
    result_df = pd.DataFrame(
        {
            "prompt": [prompt for promptdict in prompts for prompt in promptdict],
            "classes": [opval for option in prompts for opval in option.values()],
            "answer_index": 2,
        }
    )
    result_df.to_csv("data/random_prompts.csv", index=False)


if __name__ == "__main__":
    main()
