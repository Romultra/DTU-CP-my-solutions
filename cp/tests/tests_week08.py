from unitgrade import Report
import cp
from unitgrade import UTestCase
from cp.ex02.taylor import evaluate_taylor
from cp.ex02.fibonacci import fibonacci_number

class HelloWorld2(UTestCase):
    def test_say_hello(self):
        from cp.ex00 import say_hello
        evaluate_taylor(1)
        self.assertEqual(0,0)


class Week08Tests(Report):
    title = "Tests for week 08"
    version = 0.1
    url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [(HelloWorld2, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week08Tests())
