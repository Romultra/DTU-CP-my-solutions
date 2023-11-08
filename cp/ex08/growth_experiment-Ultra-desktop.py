"""Exercise 8.9: Bacteria Growth experiment."""
import csv

def growth_threshold_reached(path: str, threshold: float) -> float:
    """Return the time point at which the growth threshold is reached.
    
    :param path: The path to the folder of the data files.
    :param threshold: The threshold value.
    
    :return: The average time point.
    """
    time_points = []
    for i in range(160):
        with open(f'{path}/experiment_{i:03d}.csv', 'r') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            found = False
            for j, value in enumerate(next(reader)):
                if value > threshold:
                    time_points.append(j)
                    found = True
                    break
            if not(found):
                time_points.append(10)
    sum = 0
    for time in time_points:
        sum += time
    average = sum/160
    return average