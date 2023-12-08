from unitgrade import UTestCase, Report, hide
import cp

class Task1_CompoundInterest(UTestCase):
    def test_compound_interest_1(self):
        from cp.midterm2023fall.tasks.compound_interest import compound_interest
        self.assertAlmostEqual(compound_interest(1500, 0.04, 8), 61.060565888)
    def test_compound_interest_2(self):
        from cp.midterm2023fall.tasks.compound_interest import compound_interest
        self.assertAlmostEqual(compound_interest(100, 0.08, 16), 8.307115127602202)
    def test_compound_interest_3(self):
        from cp.midterm2023fall.tasks.compound_interest import compound_interest
        self.assertAlmostEqual(compound_interest(4500, 0.033, 12), 150.76677936244505)
    def test_compound_interest_4(self):
        from cp.midterm2023fall.tasks.compound_interest import compound_interest
        self.assertAlmostEqual(compound_interest(500, 0.09, 2), 46.01249999999993)
    def test_compound_interest_5(self):
        from cp.midterm2023fall.tasks.compound_interest import compound_interest
        self.assertAlmostEqual(compound_interest(300, 0.05, 3), 15.251388888888812)

class Task2_StockStatus(UTestCase):
    def fix(self, s):
        s = s[0].upper() + s[1:].strip()
        if s[-1] in '.!':
            s = s[:-1]
        return s.replace('  ', ' ').replace('.', '')
    def test_stock_status_1(self):
        from cp.midterm2023fall.tasks.stock_status import stock_status
        self.assertEqual(self.fix(stock_status(4, 7)), 'Only 4 left in stock')
    def test_stock_status_2(self):
        from cp.midterm2023fall.tasks.stock_status import stock_status
        self.assertEqual(self.fix(stock_status(0, 7)), 'Available in 7 days')
    def test_stock_status_3(self):
        from cp.midterm2023fall.tasks.stock_status import stock_status
        self.assertEqual(self.fix(stock_status(0, 0)), 'Out of stock')
    def test_stock_status_4(self):
        from cp.midterm2023fall.tasks.stock_status import stock_status
        self.assertEqual(self.fix(stock_status(-1, 7)), 'Unknown')
    def test_stock_status_5(self):
        from cp.midterm2023fall.tasks.stock_status import stock_status
        self.assertEqual(self.fix(stock_status(-10, -10)), 'Unknown')

class Task3_FirstAlarm(UTestCase):
    def test_first_alarm_1(self):
        from cp.midterm2023fall.tasks.first_alarm import first_alarm
        self.assertEqual(first_alarm([1.52, 1.29, 1.32, 1.18, 1.45, 1.63, 1.81, 1.95, 2.11, 2.09, 1.98, 1.3]), 8)
    def test_first_alarm_2(self):
        from cp.midterm2023fall.tasks.first_alarm import first_alarm
        self.assertEqual(first_alarm([0.26, 0.6, 1.33, 1.85, 2.31, 3.15, 4.08, 4.63, 5.11, 5.15, 5.29, 6.28, 6.52, 6.9, 7.0, 7.44, 8.09, 8.34]), 3)
    def test_first_alarm_3(self):
        from cp.midterm2023fall.tasks.first_alarm import first_alarm
        self.assertEqual(first_alarm([0.19, 0.16, 0.5, 1.21, 2.18, 2.87, 3.31, 4.22, 4.97, 5.23, 5.84, 6.46, 7.0, 7.03, 7.99, 8.21, 8.6, 9.53]), 4)
    def test_first_alarm_4(self):
        from cp.midterm2023fall.tasks.first_alarm import first_alarm
        self.assertEqual(first_alarm([-0.52, -0.31, -0.04, 0.03, 0.21, 0.28, 0.29, 0.47, 0.49, 0.5, 0.55]), -1)
    def test_first_alarm_5(self):
        from cp.midterm2023fall.tasks.first_alarm import first_alarm
        self.assertEqual(first_alarm([-0.37, -0.32, 0.25, 0.35, 0.78, 1.49, 2.06, 2.52, 3.27, 3.87]), 6)

class Task4_TypicalSuccessor(UTestCase):
    def test_typical_successor_1(self):
        from cp.midterm2023fall.tasks.typical_successor import typical_successor
        self.assertEqual(typical_successor('Hello world. This usual salutation usually starts programming.', 'l'), 'l')
    def test_typical_successor_2(self):
        from cp.midterm2023fall.tasks.typical_successor import typical_successor
        self.assertEqual(typical_successor('Once, twice, three times a fool. This is what they think.', 't'), 'h')
    def test_typical_successor_3(self):
        from cp.midterm2023fall.tasks.typical_successor import typical_successor
        self.assertEqual(typical_successor('Once, twice, three times a fool.', 'a'), '')
    def test_typical_successor_4(self):
        from cp.midterm2023fall.tasks.typical_successor import typical_successor
        self.assertEqual(typical_successor('Writing a piece of random text with no inspiration, meaning or purpose.', 'i'), 'n')
    def test_typical_successor_5(self):
        from cp.midterm2023fall.tasks.typical_successor import typical_successor
        self.assertEqual(typical_successor('', 'f'), '')

class Task5_DiceFairness(UTestCase):
    def test_dice_fairness_1(self):
        from cp.midterm2023fall.tasks.dice_fairness import dice_fairness
        self.assertEqual(dice_fairness([4, 2, 4, 4, 5, 6, 1, 2, 3, 4, 2, 3, 5, 5, 4, 4, 3, 2, 1, 4, 6]), (4, 7, 3.5))
    def test_dice_fairness_2(self):
        from cp.midterm2023fall.tasks.dice_fairness import dice_fairness
        self.assertEqual(dice_fairness([3, 3, 3, 5, 3, 4, 3, 3, 1, 3, 1, 2, 4, 4, 3, 1, 5, 4, 2, 5]), (3, 8, 20/6))
    def test_dice_fairness_3(self):
        from cp.midterm2023fall.tasks.dice_fairness import dice_fairness
        self.assertEqual(dice_fairness([2, 1, 2, 1, 3, 1, 4, 2]), (1, 3, 4/3))
    def test_dice_fairness_4(self):
        from cp.midterm2023fall.tasks.dice_fairness import dice_fairness
        self.assertEqual(dice_fairness([5, 2, 2, 3, 2, 2, 2, 1, 1, 2, 1, 3, 1, 5, 2, 2, 3, 2, 5, 1, 6, 
                                      5, 4, 6, 4, 3, 3, 1, 3, 1, 4, 1, 5, 3, 4, 6, 3, 6, 5, 1, 2, 2, 
                                      1, 4, 1, 6, 4, 4, 6, 3, 1, 3, 5, 2, 1, 3, 6, 6, 3, 6]), (1, 13, 10.0))
    def test_dice_fairness_5(self):
        from cp.midterm2023fall.tasks.dice_fairness import dice_fairness
        self.assertEqual(dice_fairness([1]), (1, 1, 1/6))

class Midterm2023Fall(Report):
    title = "Computer Programming: Midterm Fall 2023"
    pack_imports = [cp]
    questions = [(Task1_CompoundInterest, 20),
                 (Task2_StockStatus, 20),
                 (Task3_FirstAlarm, 20),
                 (Task4_TypicalSuccessor, 20),
                 (Task5_DiceFairness, 20)]

if __name__ == "__main__":
    from unitgrade import evaluate_report_student
    evaluate_report_student(Midterm2023Fall())
