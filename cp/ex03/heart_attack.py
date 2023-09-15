"""Exercise 3.8: Heart attack."""

def heart_attack(age:int, weight:int, smoker:bool) -> str:
    """Return a string indicating the risk of a person for having heart attack.

    :param age: The age of the person.
    :param weight: The weight of the person in kilograms.
    :param smoker: Does the person smoke cigarettes?
    :return: A string, either "low" or "high", indicating the risk for having heart attack.
    """
    if (age < 18 and weight < 60) or (18 <= age <= 30) or (age > 30 and not(smoker)) :
        return 'low'
    
    elif (age < 18 and weight >= 60) or (age > 30 and smoker) :
        return "high"