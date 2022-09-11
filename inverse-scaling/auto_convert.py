from __future__ import annotations
import argparse
from datetime import datetime
import json
import sys
from typing import Union, cast
import csv
import logging
import shutil
import pandas as pd
from pathlib import Path
import torch
from tqdm.autonotebook import tqdm


def main(path: str):
    df = pd.read_csv(path)
    df["prompt"] = df["other_prompt"]
    df.to_csv(path.replace(".csv", "_classification.csv"), index=False)


def parse_args(args):
    parser = argparse.ArgumentParser(description="Convert")
    parser.add_argument(
        "--dataset",
        type=str,
        help="The name of the file containing the dataset (must be in the directory 'data'). Superseded by --dataset-path",
        required=False,
    )


if __name__ == "__main__":
    main(
        "/Users/esben/Desktop/apart/blackbox-psych/inverse-scaling/data/anchoring_raw_kshot0_nopreprompt_num.csv"
    )
