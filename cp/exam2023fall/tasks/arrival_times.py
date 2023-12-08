"""Task 2: Arrival times."""

def arrival_times(schedule: list, delay: int) -> list:
    """Return the arrival times given scheduled times and delay.

    :param schedule: A list of strings, the scheduled times.
    :param delay: A positive integer, the delay (in minutes).
    :return: The arrival times, a list of strings.
    """
    new_schedule = []
    for train in schedule:
        minutes = 0
        hours = 0

        minutes += delay
        minutes += int(train[3:])
        minutes += int(train[:2])*60

        hours = minutes // 60
        minutes = minutes % 60

        while hours > 23:
            hours = hours - 24
        
        if hours < 10:
            hours = f"0{hours}"
        else:
            hours = f"{hours}"
        

        if minutes < 10:
            minutes = f"0{minutes}"
        else:
            minutes = f"{minutes}"
        
        new_schedule.append(f"{hours}:{minutes}")
    
    return new_schedule

if __name__ == '__main__':
    print(arrival_times(['12:37', '08:10'], 25))
