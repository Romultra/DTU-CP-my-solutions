"""Exercise 12.1.: CPR-check."""

def cpr_check(cpr : str) -> bool:
    """Check if CPR number is valid based on check digit.
    
    :param cpr: CPR number as str.
    :return: Boolean whether CPR is valid or not.
    """
    control = "432765432"
    check_digit = 0
    for i in range(9):
        check_digit += int(control[i]) * int(cpr[i])
    
    check_digit = check_digit % 11
    check_digit = 11 - check_digit
    
    if check_digit == int(cpr[9]):
        return True
    
    else:
        return False