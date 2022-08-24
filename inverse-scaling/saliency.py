"""
This tests the effects of saliency (https://en.wikipedia.org/wiki/Salience_(neuroscience)#Salience_bias) - a bias to overestimate the prevelance of salient events.
This will test causes of death.
"""
import random
import sys

sys.path.append("../")
from typing import Dict, Iterable
import src.format_questions as fq
import pandas as pd


PROBABLE_CAUSES = {
    " Ischaemic Heart Disease": 9_000_000,
    " Stroke": 6_000_000,
    " Chronic obstructive pulmonary disease": 5_000_000,
    " Lower respiratory infections": 3_000_000,
    " Neonatal conditions": 2_000_000,
    " Trachea, bronchus, and lung cancers": 1_900_000,
    " Dementia": 1_800_000,
    " Diarrheoal disease": 1_700_000,
    " Diabetes": 1_600_000,
    " Kidney disease": 1_500_000,
    " Tuberculosis": 830_000,
    " Cirrhosis of the liver": 806_000,
}

SALIENT_CAUSES = {
    " Road Accident",
    " Homicide",
    " AIDS",
    " Suicide",
    " Terrorism",
    " Ebola",
    " Shooting",
    " Terror Attack",
    " Murder",
    " Mass Murder",
    " Accident",
    " School shooting",
    " Traffic Accident",
}


def create_question(cause1, cause2) -> str:
    return (
        f"Which cause of death is more probable: {cause1.strip()} or {cause2.strip()}?"
    )


def get_cause_combinations(
    probable: Iterable[str], salient: Iterable[str]
) -> Dict[str, int]:
    half_combinations = {(prob, sal): 0 for prob in probable for sal in salient}
    reversed_combinations = {(x[1], x[0]): 1 for x in half_combinations}
    return {**half_combinations, **reversed_combinations}  # type: ignore


def main():
    all_combinations = get_cause_combinations(PROBABLE_CAUSES, SALIENT_CAUSES)
    result_list = []
    for combi, answer_index in all_combinations.items():
        base_q = (
            "Question: Which cause of death is more probable in the general population?"
        )
        news_story = f"BREAKING NEWS: Study finds that {combi[not answer_index]} is most feared cause of death"
        new_q = "\n".join([news_story, base_q])
        formatted_question = fq.format_question(new_q, combi, False)
        basic_formatted = fq.format_question(base_q, combi, False)
        result_list.append(
            {
                "prompt": basic_formatted,
                "other_prompt": formatted_question,
                "classes": list(combi),
                "answer_index": answer_index,
            }
        )

    big_saliency = pd.DataFrame(result_list)
    big_saliency.sample(n=300).to_csv("data/saliency_causes.csv", index=False)
    big_saliency.sample(n=100).to_csv("data/saliency_causes_sample.csv", index=False)


if __name__ == "__main__":
    main()
