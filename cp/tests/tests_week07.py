from unitgrade import Report
import cp
from unitgrade import UTestCase
from cp.ex02.taylor import evaluate_taylor

class HelloWorld2(UTestCase):
    def test_say_hello(self):
        from cp.ex00 import say_hello
        evaluate_taylor(1)
        self.assertEqual(0,0)



class Week07Tests(Report): #240 total.
    title = "Tests for week 07"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (HelloWorld2, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week07Tests())
