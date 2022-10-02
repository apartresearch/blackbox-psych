import pandas as pd


def create_n_shots(df: pd.DataFrame, n=1) -> pd.DataFrame:
    """Add n-shots to a dataframe"""
    copy_df = df.copy()
    for i, row in copy_df.iterrows():
        # Sample n rows from the dataframe that doesn't contain the current row's "classes"
        new_rows = df[~df["prompt"].str.contains("|".join(row["classes"]))].sample(n=n)
        # Add the correct answer to the new rows "prompt" column
        new_rows["prompt"] = new_rows.apply(
            lambda nr: nr["prompt"] + f"{nr['classes'][nr['answer_index']]} ", axis=1
        )
        # Prepend the new_rows to the original row "prompt"
        row["prompt"] = new_rows["prompt"].str.cat(sep="\n") + "\n" + row["prompt"]
        # Prepend the new_rows to the original row "other_prompt"
        row["other_prompt"] = (
            new_rows["other_prompt"].str.cat(sep="\n") + "\n" + row["other_prompt"]
        )
        print(f"{row['prompt']=}")

    return copy_df

