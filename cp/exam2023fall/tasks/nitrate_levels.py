"""Task 9: nitrate levels."""

def nitrate_levels(filename: str) -> (int, int, int, int, int):
    """Return the number of weekly measurements in each category.

    :param filename: Filename of the data file.
    :return: Number of measurements in each of five categories for nitrate levels. 
    """
    very_low_count = 0
    low_count = 0
    normal_count = 0
    high_count = 0
    very_high_count = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            level = float(line)

            if level <= 4.0:
                very_low_count += 1

            elif level > 4.0 and level <= 9.0:
                low_count += 1

            elif level > 9.0 and level < 40.0:
                normal_count += 1
            
            elif level >= 40.0 and level < 50.0:
                high_count += 1

            elif level >= 50.0:
                very_high_count += 1
    
    return (very_low_count, low_count, normal_count, high_count, very_high_count)

if __name__ == '__main__':
    filename = 'cp/exam2023fall/tasks/files/nitrate_data_A.txt'
    print(nitrate_levels(filename))
