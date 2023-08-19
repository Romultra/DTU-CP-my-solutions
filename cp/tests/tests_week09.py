from unitgrade import Report, UTestCase
import unittest
from unittest.mock import patch
import cp
import io

class TestRectangleArea(UTestCase):
    def test_area(self):
        from cp.ex09.rectangle import area, Rectangle
        r = Rectangle()
        r.width = 10
        r.height = 4
        self.assertEqual(area(r), 40)

class TestMakeARectangle(UTestCase):
    def test_make_a_rectangle(self):

        from cp.ex09.rectangle import make_a_rectangle, Rectangle, Point

        rectangle = make_a_rectangle(0, 0, 4, 5)
        self.assertIsInstance(rectangle, Rectangle)

        rectangle = make_a_rectangle(9, 2, 3, 7)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertIsInstance(rectangle.corner, Point)
        self.assertEqual(rectangle.corner.x, 9)
        self.assertEqual(rectangle.corner.y, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 7)

    def test_rectangle(self):

        from cp.ex09.rectangle import make_a_rectangle, Rectangle, Point, area
        rectangle = make_a_rectangle(5, 3, 1, 1)
        self.assertEqual(area(rectangle), 1)
        rectangle = make_a_rectangle(0, 0, 20, 10)
        self.assertEqual(area(rectangle), 200)


class TestSplitRectangle(UTestCase):
    def setUp(self):
        from cp.ex09.rectangle import make_a_rectangle
        self.rectangle = make_a_rectangle(0, 0, 4, 6)

    def test_split_horizontally(self):
        from cp.ex09.rectangle import split_rectangle
        split = split_rectangle(self.rectangle, True)
        self.assertEqual(len(split), 2)

        left_rectangle = split[0]
        right_rectangle = split[1]

        self.assertEqual(left_rectangle.width, 2)
        self.assertEqual(left_rectangle.height, 6)

        self.assertEqual(right_rectangle.width, 2)
        self.assertEqual(right_rectangle.height, 6)

    def test_split_vertically(self):
        from cp.ex09.rectangle import split_rectangle
        split = split_rectangle(self.rectangle, False)
        self.assertEqual(len(split), 2)

        top_rectangle = split[0]
        bottom_rectangle = split[1]

        self.assertEqual(top_rectangle.width, 4)
        self.assertEqual(top_rectangle.height, 3)

        self.assertEqual(bottom_rectangle.width, 4)
        self.assertEqual(bottom_rectangle.height, 3)


class TestRectangleInception(UTestCase):
    def test_inception_areas(self):
        from cp.ex09.rectangle import make_a_rectangle, rectangle_inception, area

        r = make_a_rectangle(2, 4, 12, 16)
        rs = rectangle_inception(r, 4)
        areas = [area(r_) for r_ in rs]
        self.assertEqual(len(areas), 5)
        self.assertEqual(areas,  [96.0, 48.0, 24.0, 12.0, 12.0])

    def test_inception_location(self):
        from cp.ex09.rectangle import make_a_rectangle, Rectangle, rectangle_inception
        rs = rectangle_inception(make_a_rectangle(2, 4, 12, 16), 4)
        r = rs[-1]
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.corner.x, 11)
        self.assertEqual(r.corner.y, 16)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

class TestMakeVector(UTestCase):
    def test_make_vector(self):
        from cp.ex09.vector import Vector, make_vector

        v1 = make_vector(2,3)
        self.assertIsInstance(v1, Vector, msg="Must return a Vector instance.")
        self.assertEqual(v1.x, 2)
        self.assertEqual(v1.y, 3)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_vector(self, mock_stdout):
        from cp.ex09.vector import make_vector, print_vector

        v1 = make_vector(2, 3)
        print_vector(v1)
        out = mock_stdout.getvalue().strip()
        self.assertEqual(out, "(2, 3)")

class TestVectorOperations(UTestCase):
    def test_dot_product(self):
        from cp.ex09.vector import make_vector, dot
        v1 = make_vector(2,3)
        v2 = make_vector(4,5)
        self.assertEqual(dot(v1, v2), 23)

    def test_scale(self):
        from cp.ex09.vector import make_vector, scale
        v = make_vector(2,3)
        s = 2
        v_scaled = scale(s, v)
        self.assertEqual(v_scaled.x, 4)
        self.assertEqual(v_scaled.y, 6)

    def test_add(self):
        from cp.ex09.vector import make_vector, add
        v1 = make_vector(2,3)
        v2 = make_vector(4,5)
        v_sum = add(v1, v2)
        self.assertEqual(v_sum.x, 6)
        self.assertEqual(v_sum.y, 8)

    def test_subtract(self):
        from cp.ex09.vector import make_vector, sub
        v1 = make_vector(2,3)
        v2 = make_vector(4,5)
        v_sub = sub(v1, v2)
        self.assertEqual(v_sub.x, -2)
        self.assertEqual(v_sub.y, -2)

    def test_hat(self):
        from cp.ex09.vector import make_vector, hat
        v = make_vector(2,3)
        v_hat = hat(v)
        self.assertEqual(v_hat.x, -3)
        self.assertEqual(v_hat.y, 2)


class TestLineSegmentMethods(UTestCase):
    def test_make_line_segment(self):
        from cp.ex09.vector import make_vector, make_line_segment, LineSegment
        p = make_vector(1, 2)
        q = make_vector(3, 4)
        l = make_line_segment(p, q)
        self.assertIsInstance(l, LineSegment)


    def test_point_on_line(self):
        from cp.ex09.vector import make_vector, make_line_segment, Vector, point_on_line
        p = make_vector(1, 2)
        q = make_vector(3, 4)
        l = make_line_segment(p, q)
        self.assertIsInstance(point_on_line(l, 0), Vector)
        self.assertEqual(point_on_line(l, 0).x, p.x)
        self.assertEqual(point_on_line(l, 0).y, p.y)

        self.assertEqual(point_on_line(l, 1).x, q.x)
        self.assertEqual(point_on_line(l, 1).y, q.y)

    def test_point_on_line_midpoint(self):
        from cp.ex09.vector import make_vector, make_line_segment, point_on_line
        p = make_vector(1, 2)
        q = make_vector(3, 4)
        l = make_line_segment(p, q)
        self.assertEqual(point_on_line(l, .5).x, (p.x+q.x)/2)
        self.assertEqual(point_on_line(l, .5).y, (p.y+q.y)/2)

class SquareWithLocationTests(UTestCase):
    def test_make_square(self):
        from cp.ex09.vector import SquareWithPosition, make_square_with_position
        sq = make_square_with_position(1, 2, 3)
        self.assertIsInstance(sq, SquareWithPosition)

    def test_square_to_lines(self):
        from cp.ex09.vector import make_square_with_position, square_to_lines, LineSegment, point_on_line
        sq = make_square_with_position(1, 2, 3)
        lines = square_to_lines(sq)
        self.assertIsInstance(lines, list, msg="Must return a list")
        self.assertEqual(len(lines), 4, msg="Must return 4 lines")
        for l in lines:
            self.assertIsInstance(l, LineSegment, msg="Must return 4 line segments")
        tpl = lambda v: (v.x, v.y)
        lmd = lambda l: tuple( set( (tpl(point_on_line(l, 0) ), tpl(point_on_line(l, 1) )) ) )
        l2 = list( set( [lmd(l) for l in lines] ) )
        self.assertEqual(l2[0], ((4,5), (1, 5)), msg="Problem with first line. It should connect points (4,5) -- (1, 5)")
        self.assertEqual(l2[1], ((1, 2), (4, 2)))
        self.assertEqual(l2[2], ((1, 2), (1, 5)))
        self.assertEqual(l2[3], ((4, 5), (4, 2)))

class TestIntersection(UTestCase):
    def test_do_they_intersect(self):
        from cp.ex09.vector import make_vector, make_line_segment, do_they_intersect
        l1 = make_line_segment(make_vector(1, 1), make_vector(4, 1))
        l2 = make_line_segment(make_vector(2, -2), make_vector(2, 3))

        self.assertTrue( do_they_intersect(l1, l2), msg="These lines should intersect")
        self.assertTrue( do_they_intersect(l2, l1), msg="Reverse order; lines should still intersect")

        l3 = make_line_segment(make_vector(2, -2), make_vector(-1, 3))

        self.assertFalse(do_they_intersect(l1, l3), msg="These lines should not intersect")
        self.assertFalse(do_they_intersect(l3, l1), msg="Reverse order; lines should still not intersect")

    def test_intersect(self):
        from cp.ex09.vector import make_vector, make_line_segment, intersect
        l1 = make_line_segment(make_vector(1, 1), make_vector(4, 1))
        l2 = make_line_segment(make_vector(2, -2), make_vector(2, 3))
        isect = intersect(l1, l2)
        self.assertAlmostEqual(isect.x,2)
        self.assertAlmostEqual(isect.y, 1)

class GetAllIntersections(UTestCase):
    def test_get_intersections_none(self):
        from cp.ex09.vector import make_line_segment
        from cp.ex09.vector import make_vector, make_square_with_position, get_intersections
        sq = make_square_with_position(1, 1, 6)
        l = make_line_segment(make_vector(-1, 2), make_vector(0, 0.5))
        intersections = get_intersections(sq, l)
        self.assertIsInstance(intersections, list)
        self.assertEqual(len(intersections), 0)

    def test_get_intersections_one(self):
        from cp.ex09.vector import make_vector, make_square_with_position, get_intersections, make_line_segment
        sq = make_square_with_position(1, 1, 6)
        l = make_line_segment(make_vector(-1, 2), make_vector(4, 3))
        intersections = get_intersections(sq, l)
        self.assertEqual(len(intersections), 1)
        self.assertAlmostEqual(intersections[0].x, 1)
        self.assertAlmostEqual(intersections[0].y, 2.4)

    def test_get_intersections_two(self):
        from cp.ex09.vector import make_line_segment, make_vector, make_square_with_position, get_intersections
        sq = make_square_with_position(1, 1, 6)
        l = make_line_segment(make_vector(-1, 2), make_vector(9, 4))
        ls = get_intersections(sq, l)
        self.assertEqual(len(ls), 2)
        ls = list(set([(ls[0].x, ls[0].y), (ls[1].x, ls[1].y)]))

        self.assertAlmostEqual(ls[0][0], 1, msg="testing x-coordinate of first point")
        self.assertAlmostEqual(ls[0][1], 2.4, msg="testing y-coordinate of first point")

        self.assertAlmostEqual(ls[1][0], 7, msg="testing x-coordinate of second point")
        self.assertAlmostEqual(ls[1][1], 3.6, msg="testing y-coordinate of second point")

class Week09Tests(Report):
    title = "Tests for week 09"
    version = 1.0
    url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
        (TestRectangleArea, 10),
        (TestMakeARectangle, 10),
        (TestSplitRectangle,10),
        (TestRectangleInception, 10),
        (TestMakeVector, 10),
        (TestVectorOperations, 10),
        (TestLineSegmentMethods, 10),
        (TestIntersection, 10),
        (GetAllIntersections, 10),
        ]
    

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week09Tests())
