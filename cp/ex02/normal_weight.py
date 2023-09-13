"""Exercise 2.5: Calculate the normal weight range for a given height."""
import math

def normal_weight(height:float):
    """Calculate and print the range of normal weights for a given height.

    :param height: the height.
    """
    lower_limit = math.ceil(18.5 * height**2)
    higher_limit = math.floor(25 * height**2)
    
    print(f'Normal weight is between {lower_limit} and {higher_limit} kg.')
normal_weight(1.47)     # Output : 'Normal weight is between 40 and 54 kg.'
normal_weight(1.96)     # Output : 'Normal weight is between 72 and 96 kg.'