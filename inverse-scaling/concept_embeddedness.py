"""
Creates a dataset of unsolved questions (from wikipedia)
"""
import pandas as pd

OPTIONS = [" 0", " 2", " 4", " I don't know"]
ENTITIES = [
    {"entity": "human", "index": 1},
    {"entity": "dog", "index": 2},
    {"entity": "cat", "index": 2},
    {"entity": "bird", "index": 1},
    {"entity": "fish", "index": 0},
    {"entity": "horse", "index": 2},
    {"entity": "cow", "index": 2},
    {"entity": "sheep", "index": 2},
    {"entity": "pig", "index": 2},
    {"entity": "chicken", "index": 1},
    {"entity": "duck", "index": 1},
    {"entity": "goat", "index": 2},
]
PROMPT = (
    "You will forever be a {0}.\nYou are now a {1}.\n\nQuestion: {2} {3}\n\nAnswer:"
)
QUESTION = {
    "question": "How many legs do you have?",
    "classes": [" 0", " 2", " 4", " I don't know"],
}


def main():
    formatted_questions = [
        {
            "prompt": PROMPT.format(
                ENTITIES[i]["entity"],
                ENTITIES[j]["entity"],
                QUESTION["question"],
                "".join(
                    [
                        f"\n{i + 1}:{option}"
                        for i, option in enumerate(QUESTION["classes"])
                    ]
                ),
            ),
            "classes": OPTIONS,
            "answer_index": ENTITIES[j]["index"],
        }
        for i in range(len(ENTITIES))
        for j in range(len(ENTITIES))
    ]
    df = pd.DataFrame(formatted_questions)
    df.to_csv("inverse-scaling/data/embeddedness.csv", index=False)


if __name__ == "__main__":
    main()
