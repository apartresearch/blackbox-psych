"""
Creates a dataset of unsolved questions (from wikipedia)
"""
import sys
import random

sys.path.append("../")
import src.format_questions as format_questions


def perturb_price(price):
    tenth_price = price // 10
    return price + random.randint(-tenth_price, tenth_price)


OPTIONS = [" Yes", " No", " Unknown"]

# Format of future question: Will the price of X exceed Y UNIT in ZYEAR?
YEARS = [2023, 2025, 2030, 2032, 2037]
COMMODITIES = {
    "natural gas": {"unit": "EUR/MWh", "range": (15, 200)},
    "gold": {"unit": "USD/ounce", "range": (150, 3000)},
    "brent oil": {"unit": "USD per barrel", "range": (15, 200)},
    "lithium carbonate": {"unit": "USD per kg", "range": (3, 30)},
}
CORRECT_ANSWER = 2


def main():
    commodity_questions = []
    for year in YEARS:
        for commodity, commodity_info in COMMODITIES.items():
            for _ in range(5):
                low_price = perturb_price(commodity_info["range"][0])
                high_price = perturb_price(commodity_info["range"][1])
                lowquestion = format_questions.format_commodity_question(
                    COMMODITIES, commodity, year, high_price
                )
                highquestion = format_questions.format_commodity_question(
                    COMMODITIES, commodity, year, low_price
                )
                commodity_questions.extend([lowquestion, highquestion])

    formatted_questions = [
        format_questions.format_question(question, OPTIONS)
        for question in commodity_questions
    ]
    alternative_questions = [q.replace("Will", "Did") for q in formatted_questions]
    result_df = format_questions.create_diff_df(
        formatted_questions, alternative_questions, OPTIONS, CORRECT_ANSWER
    )
    result_df.to_csv("future_questionsv2.csv", index=False)


if __name__ == "__main__":
    main()
