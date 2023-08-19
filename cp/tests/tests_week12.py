from unitgrade import Report
import cp
from unitgrade import UTestCase
from cp.ex02.taylor import evaluate_taylor

class HelloWorld(UTestCase):
    def test_say_hello(self):
        from cp.ex00 import say_hello
        evaluate_taylor(2)
        self.assertEqual(0,0)

class Week12Tests(Report): #240 total.
    title = "Tests for week 12"
    version = 0.1
    url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (HelloWorld, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week12Tests())
