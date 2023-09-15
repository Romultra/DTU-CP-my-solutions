"""Exercise 3.4: Body Temperature."""

def body_temperature(temperature):
    """Calculate the body's response based on the given temperature.
    
    :param temperature: The temperature in degrees Celsius.
    :return: The body's response as a string.
    """
    if temperature < 35:
        return "Hypothermia"
    elif 35 <=temperature <= 37:
        return "Normal"
    elif 37 < temperature <= 38:
        return "Slight fever"
    elif 38 <temperature <= 39:
        return "Fever"
    elif temperature > 39:
        return "Hyperthermia"