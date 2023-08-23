"""This file contains all the exercises relating to the Minecraft-example 9.3-9.8."""
import matplotlib.pyplot as plt

class Vector:
    """A class that represents a Vector, defined by the endpoint :math:`(x,y)`."""

def make_vector(x : float, y : float) -> Vector:
    """Create a new Vector object with end-points :math:`(x,y)`.

    .. runblock:: pycon

        >>> from cp.ex09.vector import make_vector
        >>> v = make_vector(2,3)
        >>> v.x
        >>> v.y

    :param x: The :math:`x`-position of the vector.
    :param y: The :math:`y`-position of the vector.
    :return: A Vector-object with the given end-point.
    """
    # TODO: 3 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return v

def print_vector(v: Vector):
    """Print a vector object with coordinates (x,y) to the console.

    The output format for a vector with coordinates :math:`x, y` should be simply ``(x, y)`` (on a single line)

    :param v: A vector object instance.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("print(.. format the print statement here .. )")

def dot(v1 : Vector, v2 : Vector) -> float:
    r"""Compute the dot-product of ``v1`` and ``v2``, i.e. :math:`\mathbf{v}_1 \cdot \mathbf{v}_2`.

    :param v1: The first vector,
    :param v2: The second vector,
    :return: The dot product of ``v1`` and ``v2`` (as a ``float``)
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return dot_product

def scale(s : float, v : Vector) -> Vector:
    r"""Scale the vector :math:`\mathbf{v}` by a factor of :math:`s`.

    :param s: A scalar number
    :param v: A vector
    :return: The vector :math:`s \mathbf{v}`.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return w

def add(v1 : Vector, v2 : Vector) -> Vector:
    r"""Add the two vectors ``v1`` and ``v2`` and return the sum as a ``Vector`` object.

    :param v1: The first vector,
    :param v2: The second vector.
    :return: Their sum :math:`\mathbf{v}_1+\mathbf{v}_2`
    """
    vector_sum = make_vector(v1.x + v2.x, v1.y+v2.y)
    return vector_sum

def sub(v1 : Vector, v2 : Vector) -> Vector:
    r"""Subtract the two vectors ``v1`` and ``v2`` and return the difference as a ``Vector`` object.

    :param v1: The first vector,
    :param v2: The second vector.
    :return: Their difference :math:`\mathbf{v}_1-\mathbf{v}_2`
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Remember that x - y = x + (-1) * y.")
    return diff


def hat(v):
    r"""Given a ``Vector`` v1, this function returns a new vector which is orthogonal to v1 ('Tværvektoren' in Danish).

    :param v: A vector :math:`\mathbf{v}`.
    :return: A ``Vector`` that is orthogonal to :math:`\mathbf{v}`, i.e. :math:`\hat{\mathbf{v}}`.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return v_hat

class LineSegment:
    """A class that represents a line segment."""

def make_line_segment(p : Vector, q : Vector) -> LineSegment:
    r"""Construct a ``LineSegment`` connecting the two vectors ``p`` and ``q``.

    Note you have some freedom in terms of how you wish to store ``p`` and ``q`` in the ``LineSegment`` object;
    i.e. you can either store ``p`` and ``q`` directly similar to the ``Vector``, or perhaps do something slightly
    smarter.

    :param p: The vector the line segments begins in
    :param q: The line segment the vector ends in
    :return: A LineSegment class representing the LineSegment.
    """
    # TODO: 3 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return l


def point_on_line(l : LineSegment, t : float) -> Vector:
    r"""Interpolate between the end-points of the LineSegment.

    Given a line segment, the function will interpolate between the end-points using :math:`t \in [0,1]`
    and return a Vector. This can be used to compute any point on the LineSegment and :math:`t=0,1` will
    correspond to the end-points. The order is not important for the following problems.

    :param l: A line defined by the two end-points vectors
    :param t: Weighting of the two end-point in the inerpolation, :math:`t \in [0,1]`.
    :return: A ``Vector`` corresponding to :math:`\mathbf{p} + (\mathbf{q}-\mathbf{p})t`.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return s

def plot_vector(v: Vector):
    """Plot a Vector using matplotlib.

    :param v: Vector to plot.
    """
    plt.plot(v.x, v.y, 'ro')

def plot_line(l : LineSegment):
    r"""Plot a LineSegment using matplotlib.

    :param l: The line segment to plot
    """
    p = point_on_line(l, 0)
    q = point_on_line(l, 1)
    plt.plot([p.x, q.x], [p.y, q.y], 'k-')


class SquareWithPosition:
    """Corresponds to a square located in space. I.e., each corner has an :math:`(x,y)` coordinate."""

def make_square_with_position(x : float,y : float, width : float) -> SquareWithPosition:
    r"""Create a ``SquareWithPosition`` instance with lower-left corner at :math:`(x,y)` and the given ``width``.

    Note: It is up to you how you want to store the information in the SquareWithLocation-class. You can for instance
    choose to store the four corners as ``Vector``-objects, the four sides as ``LineSegment``-objects.

    :param x: :math:`x`-position of the lower-left corner
    :param y: :math:`y`-position of the lower-left corner
    :param width: The side-length of the rectangle
    :return: A ``SquareWithLocation`` object.
    """
    # TODO: 5 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return s


def intersect(l1: LineSegment, l2: LineSegment) -> Vector:
    """Get the intersection between two line segments assuming they intersects.

    :param l1: First line
    :param l2: Second line
    :return: A ``Vector`` representing the point of intersection.
    """
    # TODO: Code has been removed from here.
    raise NotImplementedError("Insert your solution and remove this error.")
    return p

def do_they_intersect(l1 : LineSegment, l2 : LineSegment) -> bool:
    """Determine if two line segments intersects.

    :param l1: First line segment
    :param l2: Second line segment
    :return: ``True`` if the two line segments intersects, otherwise ``False``.
    """
    # TODO: 3 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return is_intersecting


def square_to_lines(sq : SquareWithPosition) -> list:
    """Return a list of ``LineSegment``-objects corresponding to the four sides.

    :param sq: The square
    :return: A list of four sides, ``[l1, l2, l3, l4]``
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return lines

def plot_square(sq: SquareWithPosition):
    """Plot the ``SquareWithLocation`` instance.

    :param sq: The square to plot
    """
    # TODO: 2 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")

def get_intersections(sq : SquareWithPosition, l : LineSegment) -> list:
    """Return a list of ``Vector``-objects corresponding to all intersections between the square and line segment.

    :param sq: A square
    :param l: A line segment
    :return: A list of 0, 1, or 2 ``Vector``-objects corresponding to the intersections.
    """
    # TODO: 1 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")
    return intersections

def plot_intersections(sq : SquareWithPosition, l : LineSegment):
    """Plot all intersections between the square and line.

    :param sq: A square
    :param l: A line segment
    """
    # TODO: 2 lines missing.
    raise NotImplementedError("Insert your solution and remove this error.")

if __name__ == '__main__':
    square = make_square_with_position(1,1,2)
    line = make_line_segment(make_vector(-1, -1), make_vector(2, 4) )
    vec = make_line_segment(make_vector(1, 1), make_vector(3, 1) )
    plot_square(square)
    plot_line(line)
    plot_intersections(square, line)
    plt.show()
