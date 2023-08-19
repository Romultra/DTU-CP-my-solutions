from unitgrade import Report
import cp
from unitgrade import UTestCase


class Week03CompareNumbers(UTestCase):
    def test_compare_numbers(self):
        with self.capture() as c:
            from cp.ex03.compare_numbers import compare_numbers
        result = compare_numbers(5.,3.)
        self.assertEqual(result, 'the first number is greater')
        result = compare_numbers(2.,7.)
        self.assertEqual(result, 'the second number is greater')
        result = compare_numbers(4.,4.)
        self.assertEqual(result, 'the numbers are equal')

class Week03BodyTemperature(UTestCase):
    def test_body_Temperature(self):
        with self.capture() as c:
            from cp.ex03.body_temperature import body_temperature
        result = body_temperature(34.5)
        self.assertEqual(result, 'Hypothermia')
        result = body_temperature(36.9)
        self.assertEqual(result, 'Normal')
        result = body_temperature(37.2)
        self.assertEqual(result, 'Slight fever')
        result = body_temperature(38.5)
        self.assertEqual(result, 'Fever')
        result = body_temperature(40.1)
        self.assertEqual(result, 'Hyperthermia')


class Week03HeartAttack(UTestCase):
    def test_heart_attack(self):
        with self.capture() as c:
            from cp.ex03.heart_attack import heart_attack
        result = heart_attack(30, 45, False)
        self.assertEqual(result, "low")
        result = heart_attack(60, 70, True)
        self.assertEqual(result, "high")
        result = heart_attack(17, 40, True)
        self.assertEqual(result, "low")

class Week03Ackermann(UTestCase):
    def test_ackermann(self):
        with self.capture() as c:
            from cp.ex03.ackermann import ackermann
        result = ackermann(3, 4)
        self.assertEqual(result, 125)
        result = ackermann(2, 5)
        self.assertEqual(result, 13)

class Week03Exponential(UTestCase):
    def test_exponential(self):
        with self.capture() as c:
            from cp.ex03.exponential import exponential
        result = exponential(3, 4)
        self.assertEqual(result, 3**4)
        result = exponential(2, 5)
        self.assertEqual(result, 2**5)
        result = exponential(4, -2)
        self.assertEqual(result, 4**-2)

class Week03BACCalculator(UTestCase):
    def test_BAC_calculator(self):
        with self.capture() as c:
            from cp.ex03.bac_calculator import bac_calculator
        result = bac_calculator(0.028, 80., "male", 2.)
        self.assertEqual(result,0.02147058823529411)
        result = bac_calculator(0.021, 70., "female", 2.)
        self.assertEqual(result,0.020545454545454547)


class AckermannTestCase(UTestCase):

    def test_ackermann(self):
        from cp.ex03.ackermann import ackermann
        self.assertEqual(ackermann(0, 0), 1)
        self.assertEqual(ackermann(0, 1), 2)
        self.assertEqual(ackermann(1, 0), 2)
        self.assertEqual(ackermann(1, 1), 3)
        self.assertEqual(ackermann(1, 2), 4)
        self.assertEqual(ackermann(2, 0), 3)
        self.assertEqual(ackermann(2, 1), 5)
        self.assertEqual(ackermann(2, 2), 7)
        self.assertEqual(ackermann(3, 0), 5)
        self.assertEqual(ackermann(3, 1), 13)
        self.assertEqual(ackermann(3, 2), 29)
        # Add more test cases as needed


class ExponentialTestCase(UTestCase):

    def test_exponential_with_positive_power(self):
        from cp.ex03.exponential import exponential
        self.assertEqual(exponential(2, 0), 1.0)
        self.assertEqual(exponential(2, 1), 2.0)
        self.assertEqual(exponential(2, 2), 4.0)
        self.assertEqual(exponential(3, 3), 27.0)
        self.assertEqual(exponential(5, 4), 625.0)
        # Add more test cases as needed

    def test_exponential_with_negative_power(self):
        from cp.ex03.exponential import exponential
        self.assertEqual(exponential(2, -1), 0.5)
        self.assertEqual(exponential(2, -2), 0.25)
        self.assertAlmostEqual(exponential(3, -3), 0.037037037037)
        self.assertAlmostEqual(exponential(5, -4), 5**(-4) )
        # Add more test cases as needed

    def test_exponential_with_zero_power(self):
        from cp.ex03.exponential import exponential
        self.assertEqual(exponential(2, 0), 1.0)
        self.assertEqual(exponential(3, 0), 1.0)
        self.assertEqual(exponential(5, 0), 1.0)
        # Add more test cases as needed


class HeartAttackTests(UTestCase):

    def test_heart_attack_low(self):
        from cp.ex03.heart_attack import heart_attack
        self.assertEqual(heart_attack(25, 55, False), "low")
        self.assertEqual(heart_attack(16, 45, False), "low")
        self.assertEqual(heart_attack(30, 58, False), "low")

    def test_heart_attack_high(self):
        from cp.ex03.heart_attack import heart_attack
        self.assertEqual(heart_attack(45, 70, True), "high")
        self.assertEqual(heart_attack(11, 70, True), "high")


import unittest.mock
import io
class SolarPanelTests(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_maybe(self, mock_stdout):
        from cp.ex03.solar_panel import solar_panel
        solar_panel(True, False, False, False)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip().lower(), "maybe")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_good_luck(self, mock_stdout):
        from cp.ex03.solar_panel import solar_panel
        solar_panel(True, False, True, True)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip().lower().splitlines(), ["haha", "good luck"])


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_probably_not1(self, mock_stdout):
        from cp.ex03.solar_panel import solar_panel
        solar_panel(True, True, False, False)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip().lower(), "probably not")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_probably_not2(self, mock_stdout):
        from cp.ex03.solar_panel import solar_panel
        solar_panel(False, False, True, True)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip().lower(), "probably not")


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_sure(self, mock_stdout):
        from cp.ex03.solar_panel import solar_panel
        solar_panel(False, False, False, False)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip().lower(), "sure")


class Week03Tests(Report): #40 total.
    title = "Tests for week 03"
    version = 1.0
    url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week03CompareNumbers, 10),
                (Week03BodyTemperature, 10),
                (Week03BACCalculator, 10),
                (AckermannTestCase, 10),
                (ExponentialTestCase, 10),
                (HeartAttackTests, 10),
                (SolarPanelTests, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week03Tests())
