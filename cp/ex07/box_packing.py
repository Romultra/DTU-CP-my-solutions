"""Exercise 7.5: Box packing."""

def box_packing(object : tuple, box : tuple)-> tuple:
    """Return the amount of object sticking in each dimension, or zero if sufficient space.
    
    :param object: Tuple (h,w) the dimensions of the object
    :param box: Tuple (H, W) the dimensions of the box.
    :return: Tuple
    """
    dif_x = object[0] - box[0]
    dif_y = object[1] - box[1]

    if dif_x < 0:
        dif_x = 0
    
    if dif_y < 0:
        dif_y = 0
    
    return(dif_x, dif_y)