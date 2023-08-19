from unitgrade import Report
import cp
from unitgrade import UTestCase

class Week11DotProducta(UTestCase):
    def test_dot_product_a(self):
        with self.capture() as c:
            from cp.ex11.dot_product import dot_product_a
        result = dot_product_a([1,2,3,4,5],[3,4,5,6,7])
        self.assertEqual(result, 85.)
        result = dot_product_a([2,3,7,8,1,12,5,2,9],[8,4,3,4,5,6,7,17,2])
        self.assertEqual(result, 245.) 

import numpy as np
class Week11DotProductb(UTestCase):
    def test_dot_product_b(self):
        with self.capture() as c:
            from cp.ex11.dot_product import dot_product_b
        result = dot_product_b(np.array([1,2,3,4,5]),np.array([3,4,5,6,7]))
        self.assertEqual(result, 85.)
        result = dot_product_b(np.array([2,3,7,8,1,12,5,2,9]),np.array([8,4,3,4,5,6,7, 17,2]))
        self.assertEqual(result, 245.)   

import numpy as np
class Week11BMICalc(UTestCase):
    def test_calc_bmi(self):
        with self.capture() as c:
            from cp.ex11.BMI_analysis import calc_bmi
        data = np.array([[1, 1.65, 63.4], 
                         [2, 1.70, 87.1],
                         [3, 1.82, 93.7],
                         [4, 1.62, 105],
                         [5, 1.97, 61.3], 
                         [6, 1.62, 78],
                         [7, 1.73, 99.6],
                         [8, 1.77, 81],
                         [9, 1.77, 110.7],
                         [10, 1.60, 55.2]])

        result = calc_bmi(data)
        
        expected_result = np.array([[1.0, 1.65, 63.4, 23.29, 'Normal weight'],
                                    [2.0, 1.70, 87.1, 30.14, 'Obese'],
                                    [3.0, 1.82, 93.7, 28.29, 'Overweight'],
                                    [4.0, 1.62, 105.0, 40.01, 'Obese'],
                                    [5.0, 1.97, 61.3, 15.8, 'Underweight'],
                                    [6.0, 1.62, 78.0, 29.72, 'Overweight'],
                                    [7.0, 1.73, 99.6, 33.28, 'Obese'],
                                    [8.0, 1.77, 81.0, 25.85, 'Overweight'],
                                    [9.0, 1.77, 110.7, 35.33, 'Obese'],
                                    [10.0, 1.60, 55.2, 21.56, 'Normal weight']])

        # Check each element of the arrays individually
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i][j], expected_result[i][j])

class Week11StableMeasurements(UTestCase):
    def test_stable_measurements(self):
        with self.capture() as c:
            from cp.ex11.Stable_measurements import stable_measurements
        result = stable_measurements(np.array([4.3, 5.7, 5.1, 6.4, 7.9, 12.8]))
        self.assertEqual(result.tolist(), [6.4, 7.9, 12.8])
        result = stable_measurements(np.array([4.3, 5.7, 5.1, 8, 7.9, 12.8]))
        self.assertEqual(result.tolist(),[])   
        result = stable_measurements(np.array([8, 7.9, 12.8, 14, 17.5, 18.1]))
        self.assertEqual(result.tolist(),[12.8, 14, 17.5, 18.1])

class Week11Tests(Report): #30 total.
    title = "Tests for week 11"
    version = 0.1
    url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week11DotProducta, 10),
                (Week11DotProductb, 10),
                (Week11BMICalc, 10),
                (Week11StableMeasurements, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week11Tests())
