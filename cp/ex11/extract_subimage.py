"""Exercise 11.6: Indexing Images."""
import numpy as numpy

def extract_subimage(image: np.ndarray, start_point: tuple, size: tuple) -> np.ndarray:
    """Extract a subimage from an image.

    :param image: Image to extract from.
    :param start_point: Coordinates of the top left corner of the subimage.
    :param size: Size of the subimage.

    :return: Subimage.
    """
    return image[start_point[0]:start_point[0]+size[0],start_point[1]:start_point[1]+size[1]]