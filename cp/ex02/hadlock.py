"""Exercise: Estimate fetal weight using Hadlock formula."""
import math

def hadlock(head_circ:float,abdominal_circ:float,femur_length:float):
    """Estimate fetal weight using Hadlock formula.

    :param head_circ: head circumference in cm.
    :param abdominal_circ: abdominal circumference in cm.
    :param femur_length: femur length in cm.
    """
    EFW = round(pow(10, (1.326 + 0.0107*head_circ + 0.0438*abdominal_circ + 0.158*femur_length - 0.00326*abdominal_circ*femur_length)), 1)
    print(f'The estimated fetal weight is {EFW} g.')

hadlock(31.1, 30.2, 8.3)     # Output : 'The estimated fetal weight is 2990.7 g.'