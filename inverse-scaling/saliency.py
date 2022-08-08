"""
This tests the effects of saliency (https://en.wikipedia.org/wiki/Salience_(neuroscience)#Salience_bias) - a bias to overestimate the prevelance of salient events.
This will test causes of death.
"""

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
    " Plane Accident",
    " Road Accident",
    " Homicide",
    " AIDS",
    " Suicide",
    " Terrorism",
    " Ebola",
    " Drug overdose",
    " Shooting",
    " Terror Attack",
    " Murder",
    " Accident",
    " School shooting",
    " Traffic Accident",
}


def create_question(cause1, cause2) -> str:
    return (
        f"Which cause of death is more probable: {cause1.strip()} or {cause2.strip()}?"
    )


def main():
    half_combinations = {
        (prob, salient): 0 for prob in PROBABLE_CAUSES for salient in SALIENT_CAUSES
    }
    reversed_combinations = {(x[1], x[0]): 1 for x in half_combinations}
    all_combinations = {**half_combinations, **reversed_combinations}
    print(all_combinations)


if __name__ == "__main__":
    main()

