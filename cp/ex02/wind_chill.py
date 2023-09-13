"""Exercise 2.4: Wind chill."""
def wind_chill(temperature:int, windspeed:float):
    """Calculate and print the wind chill temperatures.

    :param temperature: the actual temperature.
    :param windspeed: the wind speed.
    """
    perceived_temperature = round(13.12 + 0.6215*temperature - 11.37*pow(windspeed,0.16) + 0.3965*temperature*pow(windspeed,0.16))
    print(f'Temperature: {temperature} degrees feels like {perceived_temperature} degrees.')

wind_chill(8, 12.8)     # Output : 'Temperature: 8 degrees feels like 6 degrees.'