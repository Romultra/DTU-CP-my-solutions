"""Exercise 2.6: Calculate the lowest survival temperature."""
def survival_temperature(metabolic_heat:int, thermal_conductance:float):
    """Calculate and print the lowest survival temperature.

    :param metabolic_heat: the metabolic heat production.
    :param thermal_conductance: the thermal conductance.
    """
    survival_temperature = round( 36 - (0.9*metabolic_heat - 12) * (thermal_conductance+0.95)/(27.8*thermal_conductance), 1)
    print(f'Survival temperature is {survival_temperature} degrees.')

survival_temperature(200, 0.1)      # Output : 'Survival temperature is -27.5 degrees.'