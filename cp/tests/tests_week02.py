from unitgrade import Report
import cp
from unitgrade import UTestCase
from cp.ex02.taylor import evaluate_taylor
from cp.ex02.fibonacci import fibonacci_number


class Fibonacci(UTestCase):
    def test_fibonacci_x0(self):
        self.assertEqual(fibonacci_number(0), 0, msg="The start of the sequence is wrong -- remember that x_0 = 0!")

    def test_fibonacci_x1(self):
        self.assertEqual(fibonacci_number(0), 0, msg="The start of the sequence is wrong -- remember that x_1 = 1!")

    def test_fibonacci_x2(self):
        self.assertEqual(fibonacci_number(6), 8, msg="The first recursive step is not quite right -- remember that x_2 = x_1 + x_0")

    def test_fibonacci_x6(self):
        self.assertEqual(fibonacci_number(6), 8, msg="There is a problem in your recursion. You did not compute x_6 correctly.")

    def test_fibonacci_x23(self):
        # Test a large value. I cache the result so I don't have to enter it manually.
        self.assertEqualC(fibonacci_number(23), 28657)

    def test_fibonacci_x_many(self):
        # Caching works for arbitrary calls. This test all the values up to 20.
        for k in range(20):
            self.assertEqualC(fibonacci_number(k))




class Week02Tests(Report): #240 total.
    title = "Tests for week 02"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Fibonacci, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week02Tests())
