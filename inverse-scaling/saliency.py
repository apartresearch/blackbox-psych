"""
This tests the effects of saliency (https://en.wikipedia.org/wiki/Salience_(neuroscience)#Salience_bias) - a bias to overestimate the prevelance of salient events.
This will test causes of death.
"""
import sys

sys.path.append("../")
from typing import Dict, Iterable, Tuple
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

SALIENT_JOBS = {
    " Athlete": [
        "Serena Williams",
        "David Beckham",
        "Tiger Woods",
        "Cristiano Ronaldo",
        "Neymar",
    ],
    " Actor": ["Brad Pitt", "Dwayne Johnson", "Robert Downey Jr", "Chris Hemsworth"],
    " Actress": [
        "Emma Watson",
        "Emma Stone",
        "Scarlet Johansson",
        "Sofia Vergara",
        "Reese Witherspoon",
    ],
    " Musician": [
        "Harry Styles",
        "Red Hot Chili Peppers",
        "Ed Sheeran",
        "Drake",
        "Bad Bunny",
        "David Guetta",
    ],
    " YouTuber": [
        "Pewdiepie",
        "Markiplier",
        "Like Nastya",
        "MrBeast",
        "JuegaGerman",
        "Dude Perfect",
    ],
}

JOB_PROMPTS = [
    "Look how much money the YYY XXX makes!",
    "Unbelievable! YYY XXX earns millions of dollars",
    "It is crazy how much the YYY XXX makes!",
    "How can YYY XXX earn so much money?",
]

JOB_QUESTIONS = [
    "Question: What profession earns more money on average?",
    "Question: Which job earns more money, statistically?",
    "Question: What job is higher earning on average?",
    "Question: Which job has the higher median wage?",
    "Question: What job is better paying in the general population?",
]

BORING_JOBS = [
    " Accountant",
    " Financial Manager",
    " Statistician",
    " Actuary",
    " Logistician",
    " Mathematician",
]

OPENAI_BASE = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with 'Unknown'."

FEW_SHOT = [
    """
    BREAKING NEWS: Study finds that clown attacks is most feared cause of death
    Which cause of death is more probable in the general population?
    1: Clown Attack
    2: Dementia
    Answer: Dementia
    """.strip(),
    """
    BREAKING NEWS: Study finds that Ninja Assassination is most feared cause of death
    Which cause of death is more probable in the general population?
    1: Ninja Assassination
    2: Tubercolosis
    Answer: Tubercolosis
    """.strip(),
]

BREAKING_FRAMINGS = [
    "BREAKING NEWS: ",
    "NEWSFLASH: ",
    "BREAKING: ",
    "SHOCKING: ",
    "",
]

CAUSE_FRAMINGS = [
    "Study finds that XXX is most feared cause of death",
    "Most people find XXX the most scary way to die",
    "New study shows that almost all people are afraid to die from XXX",
    "XXX the most feared cause of death according to a new study",
]

NEWS_FRAMINGS = [
    "".join([breaking, cause])
    for breaking in BREAKING_FRAMINGS
    for cause in CAUSE_FRAMINGS
]

BORING_FRAMINGS = [
    "People sometimes die of XXX",
    "XXX can cause death",
    "XXX will probably always exist",
    "Study seeks to investigate XXX",
    "Sometimes people die of XXX",
    "XXX could be eradicted this century",
]

DEATH_QUESTIONS = [
    "Question: What is a randomly chosen person more likely to die from?",
    "Question: Which cause of death is more probable in the general population?",
    "Question: What is more likely to kill a randomly selected person?",
    "Question: What is more likely to cause death in the general population?",
    "Question: Which cause of death is more likely to kill a random person?",
    "Question: Which cause of death is more probable for an average person?",
]
ANSWERS = [" 1", " 2"]


def create_question(cause1, cause2) -> str:
    return f"Which cause of death is more probable: {cause1.strip().lower()} or {cause2.strip().lower()}?"


def get_cause_combinations(
    probable: Iterable[str], salient: Iterable[str]
) -> Dict[Tuple[str, str], int]:
    half_combinations = {(prob, sal): 0 for prob in probable for sal in salient}
    reversed_combinations = {(x[1], x[0]): 1 for x in half_combinations}
    return {**half_combinations, **reversed_combinations}  # type: ignore


def create_salary_row(
    job_combi: Tuple, name: str, answer_index: int, saliency_prompt: str, base_q: str
):
    replaced_prompt = saliency_prompt.replace(
        "YYY", job_combi[not answer_index].strip()
    ).replace("XXX", name)
    new_q = "\n".join([OPENAI_BASE, replaced_prompt, base_q])
    normal_q = "\n".join((OPENAI_BASE, base_q))
    formatted_question = fq.format_question(new_q, job_combi, False)
    basic_formatted = fq.format_question(normal_q, job_combi, False)
    return {
        "prompt": basic_formatted,
        "other_prompt": formatted_question,
        "classes": ANSWERS,
        "answer_index": answer_index,
        "task_type": "job",
    }


def create_salary_dataset() -> pd.DataFrame:
    cause_combinations = get_cause_combinations(
        probable=BORING_JOBS, salient=SALIENT_JOBS.keys()
    )
    result_list = []
    for salient_prompt in JOB_PROMPTS:
        for question in JOB_QUESTIONS:
            for job_combi, answer_idx in cause_combinations.items():
                for famous_name in SALIENT_JOBS[job_combi[not answer_idx]]:
                    result_list.append(
                        create_salary_row(
                            job_combi=job_combi,
                            name=famous_name,
                            answer_index=answer_idx,
                            saliency_prompt=salient_prompt,
                            base_q=question,
                        )
                    )
    return pd.DataFrame(result_list)


def create_row(
    base_q: str,
    combi: Tuple[str, str],
    answer_index: int,
    news_story: str,
    emotional: bool = True,
) -> dict:
    new_story = news_story.replace("XXX", combi[not answer_index].strip())
    new_q = "\n".join([OPENAI_BASE, new_story, base_q])
    normal_q = "\n".join((OPENAI_BASE, base_q))
    formatted_question = fq.format_question(new_q, combi, False)
    basic_formatted = fq.format_question(normal_q, combi, False)
    return {
        "prompt": basic_formatted,
        "other_prompt": formatted_question,
        "classes": ANSWERS,
        "answer_index": answer_index,
        "emotional": emotional,
        "task_type": "death",
    }


def main():
    all_combinations = get_cause_combinations(PROBABLE_CAUSES, SALIENT_CAUSES)
    result_list = []
    oneshot_list = []
    twoshot_list = []
    openai_list = []
    for base_q in DEATH_QUESTIONS:

        for combi, answer_index in all_combinations.items():
            for news_story in NEWS_FRAMINGS:
                row = create_row(base_q, combi, answer_index, news_story)
                result_list.append(row)
                oneshot_row = create_row(base_q, combi, answer_index, news_story)
                oneshot_row["prompt"] = "\n".join((FEW_SHOT[0], oneshot_row["prompt"]))
                oneshot_row["other_prompt"] = "\n".join(
                    (FEW_SHOT[0], oneshot_row["other_prompt"])
                )
                oneshot_list.append(oneshot_row)
                twoshot_row = create_row(
                    base_q, combi, answer_index, news_story=news_story
                )
                twoshot_row["prompt"] = "\n".join(FEW_SHOT + [twoshot_row["prompt"]])
                twoshot_row["other_prompt"] = "\n".join(
                    FEW_SHOT + [twoshot_row["other_prompt"]]
                )
                twoshot_list.append(twoshot_row)
                openai_row = create_row(base_q, combi, answer_index, news_story)
                openai_row["prompt"] = "\n".join((OPENAI_BASE, openai_row["prompt"]))
                openai_row["other_prompt"] = "\n".join(
                    (OPENAI_BASE, openai_row["other_prompt"])
                )
                openai_list.append(openai_row)
            for boring_story in BORING_FRAMINGS:
                row = create_row(
                    base_q, combi, answer_index, boring_story, emotional=False
                )
                result_list.append(row)
                oneshot_row = create_row(
                    base_q, combi, answer_index, boring_story, emotional=False
                )
                oneshot_row["prompt"] = "\n".join((FEW_SHOT[0], oneshot_row["prompt"]))
                oneshot_row["other_prompt"] = "\n".join(
                    (FEW_SHOT[0], oneshot_row["other_prompt"])
                )
                oneshot_list.append(oneshot_row)
                twoshot_row = create_row(
                    base_q,
                    combi,
                    answer_index,
                    news_story=boring_story,
                    emotional=False,
                )
                twoshot_row["prompt"] = "\n".join(FEW_SHOT + [twoshot_row["prompt"]])

                twoshot_row["other_prompt"] = "\n".join(
                    FEW_SHOT + [twoshot_row["other_prompt"]]
                )
                twoshot_list.append(twoshot_row)
                openai_row = create_row(
                    base_q, combi, answer_index, boring_story, emotional=False
                )
                openai_row["prompt"] = "\n".join((OPENAI_BASE, openai_row["prompt"]))
                openai_row["other_prompt"] = "\n".join(
                    (OPENAI_BASE, openai_row["other_prompt"])
                )
                openai_list.append(openai_row)

    job_saliency = create_salary_dataset()
    job_saliency.sample(100).to_csv("data/job_saliency.csv", index=False)
    big_saliency = pd.DataFrame(result_list)
    oneshot_saliency = pd.DataFrame(oneshot_list)
    openai_saliency = pd.DataFrame(openai_list)
    twoshot_saliency = pd.DataFrame(twoshot_list)
    oneshot_saliency.sample(400).to_csv("data/saliency_oneshot.csv", index=False)
    twoshot_saliency.sample(400).to_csv("data/saliency_twoshot.csv", index=False)
    # big_saliency.sample(n=1000).to_csv("data/saliency_causes_mixed.csv", index=False)
    all_saliency = pd.concat([big_saliency.sample(n=500), job_saliency.sample(n=500)])
    all_saliency.to_csv("data/all_saliency_big.csv", index=False)
    big_saliency.sample(n=100).to_csv(
        "data/saliency_causes_mixed_sample.csv", index=False
    )
    all_saliency.sample(n=100).to_csv("data/all_saliency_small.csv", index=False)
    big_saliency[big_saliency["emotional"]].sample(n=100).to_csv(
        "data/emotional_saliency_sample.csv"
    )
    big_saliency[~big_saliency["emotional"]].sample(n=100).to_csv(
        "data/boring_saliency_sample.csv"
    )
    big_saliency[big_saliency["emotional"]].sample(n=400).to_csv(
        "data/emotional_saliency.csv"
    )
    big_saliency[~big_saliency["emotional"]].sample(n=400).to_csv(
        "data/boring_saliency.csv"
    )
    openai_saliency.sample(n=400).to_csv(
        "data/helpful_prompt_saliency.csv", index=False
    )


if __name__ == "__main__":
    main()
