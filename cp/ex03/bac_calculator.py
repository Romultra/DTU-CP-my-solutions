"""Exercise 3.6: BAC Calculator."""

def bac_calculator(alcohol_consumed: float, weight: float, gender: str, time: float) -> float:
    """Calculate the blood alcohol concentration based on the alcohol consumed, body weight, and time since consumption.
    
    :param alcohol_consumed: The total amount of alcohol consumed in grams (float)
    :param weight: The person's body weight in kilograms (float)
    :param gender: The person's gender, which must be a string of either "male" or "female" (str)
    :param time: The time elapsed since alcohol consumption in hours (float)
    :return: The calculated blood alcohol concentration (BAC) as a float value.
    """
    if gender == "male":
        distribution_ratio = 0.68
        rate_of_metabolization = 0.015
    elif gender == "female":
        distribution_ratio = 0.55
        rate_of_metabolization = 0.017
    return alcohol_consumed/(distribution_ratio*weight) * 100 - rate_of_metabolization*time