"""The Rectangle-exercises 9.1-9.2."""
import matplotlib.pyplot as plt

class Point:
    """A class that represents a Point. See Section 15.1."""

class Rectangle:
    """A class that represents a Rectangle. See Section 15.3."""

def area(rectangle : Rectangle) -> float: 
    """Compute the area of a Rectangle-object.

    :param rectangle: A rectangle-object. Recall it has properties such as ``rectangle.width`` and ``rectangle.height``.
    :return: The area of the rectangle.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Compute the area here. Try to use the debugger if you are stuck.")
    return a

def make_a_rectangle(x, y, width, height): 
    """Create and return a new Rectangle-object. Look at Section 15.3 to see what fields it must possess.

    :param x: The x-position of the lower-left corner.
    :param y: The y-position of the lower-left corner.
    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: A new Rectangle object.
    """
    # TODO: 6 lines missing.
    raise NotImplementedError("Create and return a Rectangle object here.")
    return rect

def split_rectangle(rectangle : Rectangle, horizontally : bool) -> list: 
    """Split the rectangle object into two. Either horizontally or vertically.

    For instance, if ``horizontally=True`` this function should return a list such as
    ``[left_rectangle, right_rectangle]``.

    :param rectangle: A rectangle-object.
    :param horizontally: If ``True`` the Rectangle is split horizontally otherwise vertically.
    :return: A list with two Rectangle-objects.
    """
    # TODO: 5 lines missing.
    raise NotImplementedError("Implement function body")
    return split

def plot_rectangle(rectangle: Rectangle): 
    """Plot the rectangle using matplotlib.

    :param rectangle: The Rectangle to plot.
    """
    # TODO: 5 lines missing.
    raise NotImplementedError("Implement function body")

def rectangle_inception(rectangle, n): 
    r"""Recursively generate a list of n+1 rectangles by applying split_rectangle n times.

    Note that the list should contain n+1 non-overlapping rectangles with the same total area as the original rectangle.
    The function should begin with a horizontal split.

    :param rectangle: The initial rectangle to split.
    :param n: How many recursive splits to apply
    :return: A list of n+1 Rectangle-instances of the form ``[left, right_top, ...]``
    """
    # TODO: 3 lines missing.
    raise NotImplementedError("Implement function body")
    return rectangles


if __name__ == "__main__":
    rectangles = rectangle_inception(make_a_rectangle(0, 0, 10, 10), 10)
    for r in rectangles:
        plot_rectangle(r)
    # Optionally: Let's save the rectangle for later:
    from cp import savepdf
    savepdf("rectangles.pdf") # Save your pretty rectangles for later.
    plt.show()
