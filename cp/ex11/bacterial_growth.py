"""Exercise 11.7-11.8: Bacterial growth."""

import numpy as np 
def load_data() -> np.ndarray:
    """Load data from 160 files into one array. Files are located in cp/ex11/files/experiments.
    
    :return: The data from the files in one array.
    """
    data = np.zeros((160, 12))
    for i in range(160):
        filename = f'cp/ex08/files/experiments/experiment_{i:03}.csv'
        data[i,:] = np.loadtxt(filename, delimiter=',')
    return data

def threshold_exceeded(data : np.ndarray, threshold: float) -> np.ndarray:
    """Return the index at which the threshold is exceeded for each experiment.
    
    :param data: The data to search.
    :param threshold: The threshold to compare against.
    :return: The index at which the threshold is exceeded for each row.
    """
    indexs = np.zeros(160)
    for i in range(160):
        indexs[i] = np.argmax(data[i,:][data[i,:]<=threshold])+1
    return indexs
def get_mean(data : np.ndarray) -> np.ndarray:
    """Calculate the mean of the data.
    
    :param data: The data to calculate the mean of.
    :return: The mean of the data for each time-point.
    """
    
    return data.mean(0)
def get_std(data : np.ndarray) -> np.ndarray:
    """Calculate the standard deviation of the data.
    
    :param data: The data to calculate the standard deviation of.
    :return: The standard deviation of the data for each time-point.
    """
    return data.std(0)
