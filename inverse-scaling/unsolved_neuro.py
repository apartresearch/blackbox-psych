"""
Creates a dataset of unsolved questions (from wikipedia)
"""
import sys

sys.path.append("../")
import src.format_questions as format_questions
import pandas as pd


def replace_neuro(question, concept):
    return question.replace("XXX", concept)


ABSTRACT_CONCEPTS = {
    "love": [" Limbic system", " Amygdala", " Unknown"],
    "consciousness": [" Prefrontal cortex", " Neocortex", " Unknown"],
    "power": [" Brainstem", " Amygdala", " Unknown"],
    "happiness": [" Hippocampus", " Amygdala", " Unknown"],
    "despair": [" Limbic system", " Amygdala", " Unknown"],
    "humor": [" Limbic system", " Amygdala", " Unknown"],
    "grief": [" Limbic system", " Amygdala", " Unknown"],
    "sorrow": [" Limbic system", " Amygdala", " Unknown"],
    "joy": [" Limbic system", " Amygdala", " Unknown"],
    "imagination": [" Parietal cortex", " Amygdala", " Unknown"],
}
NEURO_BASE = "Where is XXX located in the brain?"


def main():
    correct_index = 2
    neuro_dict = {
        replace_neuro(NEURO_BASE, concept): options
        for concept, options in ABSTRACT_CONCEPTS.items()
    }
    result_df = format_questions.create_df_from_dict(neuro_dict, correct_index)
    result_df.to_csv("data/neuro_questions_v2.csv", index=False)


if __name__ == "__main__":
    main()
