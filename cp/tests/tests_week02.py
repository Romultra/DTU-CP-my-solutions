import io
import unittest.mock
from unitgrade import Report
import cp
from unitgrade import UTestCase


class Week02FullName(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_full_name(self, mock_stdout):
        from cp.ex02.full_name import full_name
        full_name('Donald', 'Duck')
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Donald Duck")


class Week02NextThousand(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_next_thousand_01(self, mock_stdout):
        from cp.ex02.next_thousand import next_thousand
        next_thousand(123998)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "124000")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_next_thousand_02(self, mock_stdout):
        from cp.ex02.next_thousand import next_thousand
        next_thousand(-123998)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "-123000")


class Week02NameLength(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_name_length(self, mock_stdout):
        from cp.ex02.name_length import name_length
        name_length('Anita')
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Your name consists of 5 characters.")


class Week02WindChill(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wind_chill_01(self, mock_stdout):
        from cp.ex02.wind_chill import wind_chill
        wind_chill(8, 12.8)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Temperature: 8 degrees feels like 6 degrees.")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wind_chill_02(self, mock_stdout):
        from cp.ex02.wind_chill import wind_chill
        wind_chill(8, 25.8)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Temperature: 8 degrees feels like 4 degrees.")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wind_chill_03(self, mock_stdout):
        from cp.ex02.wind_chill import wind_chill
        wind_chill(-2, 12.8)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Temperature: -2 degrees feels like -6 degrees.")


class Week02NormalWeight(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_weight(self, mock_stdout):
        from cp.ex02.normal_weight import normal_weight
        normal_weight(1.73)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Normal weight is between 56 and 74 kg.")


class Week02SurvivalTemperature(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_survival_temperature(self, mock_stdout):
        from cp.ex02.survival_temperature import survival_temperature
        survival_temperature(200, 0.1)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "Survival temperature is -27.5 degrees.")


class Week02UnitConversion(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_unit_conversion(self, mock_stdout):
        from cp.ex02.unit_conversion import unit_conversion
        unit_conversion(7, 5)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "7 ft 5 in is equal to 226 cm.")

class Week02Hadlock(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hadlock(self, mock_stdout):
        from cp.ex02.hadlock import hadlock
        hadlock(31.1, 30.2, 8.3)
        out = mock_stdout.getvalue()
        self.assertEqual(out.strip(), "The estimated fetal weight is 2990.7 g.")

class Week02Tests(Report): #240 total.
    title = "Tests for week 02"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week02FullName, 10),
                (Week02NextThousand, 10),
                (Week02NameLength, 10),
                (Week02WindChill, 10),
                (Week02NormalWeight, 10),
                (Week02SurvivalTemperature, 10),
                (Week02UnitConversion, 10),
                (Week02Hadlock, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week02Tests())
