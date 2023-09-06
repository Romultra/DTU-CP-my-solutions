import string
from unitgrade import hide
from cp import minput
from unittest.mock import patch
import io
import unittest
from unitgrade import UTestCase, Report
import math


class TestNormalWeight(UTestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_normal_weight_01(self, mock_stdout):
        from cp.ex02.normal_weight import normal_weight

        normal_weight(1.47)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Normal weight is between 40 and 54 kg.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_normal_weight_02(self, mock_stdout):
        from cp.ex02.normal_weight import normal_weight

        normal_weight(1.96)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Normal weight is between 72 and 96 kg.")




class TestSurvivalTemperature(UTestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_survival_temperature_01(self, mock_stdout):
        from cp.ex02.survival_temperature import survival_temperature

        survival_temperature(186,0.15)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Survival temperature is -5.0 degrees.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_survival_temperature_02(self, mock_stdout):
        from cp.ex02.survival_temperature import survival_temperature

        survival_temperature(356,0.33)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Survival temperature is -7.0 degrees.")




class TestUnitConversion(UTestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_unit_conversion_01(self, mock_stdout):
        from cp.ex02.unit_conversion import unit_conversion

        unit_conversion(4, 3)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "4 ft 3 in is equal to 130 cm.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_unit_conversion_02(self, mock_stdout):
        from cp.ex02.unit_conversion import unit_conversion

        unit_conversion(7, 2)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "7 ft 2 in is equal to 218 cm.")




class TestHadlock(UTestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_hadlock_01(self, mock_stdout):
        from cp.ex02.hadlock import hadlock

        hadlock(35, 36, 12)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "The estimated fetal weight is 5820.8 g.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_hadlock_02(self, mock_stdout):
        from cp.ex02.hadlock import hadlock

        hadlock(28.6, 29.6, 6.3)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "The estimated fetal weight is 2070.0 g.")




class Project1(Report):
    title = "Project 1"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = [
        (TestNormalWeight, 25),
        (TestSurvivalTemperature, 25),
        (TestUnitConversion, 25),
        (TestHadlock, 25),
    ]
    import cp

    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Project1())
