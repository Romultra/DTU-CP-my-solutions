from unitgrade import Report
import cp
from unitgrade import UTestCase

class Week05Primes(UTestCase):
    def test_prime(self):
        # Run and capture output
        # from cp.unitgrade import say_hello
        import numpy as np

        with self.capture() as c:
            from cp.ex05 import primes

        prime_list = np.array([257,181,2503,4871,43,353,2753,3229,2621,3137,3121,877,293,47,997,3023,7,127,13,463,719,4273,307,3617,1597,2377,1433,3061,991,2437,4813,1609,2339,3343,3001,853,4493,1223])
        non_prime_list = prime_list*2

        check = np.all([primes.is_prime(prime) for prime in prime_list])
        self.assertTrue(check)
        check = np.all([not primes.is_prime(non_prime) for non_prime in non_prime_list])
        self.assertTrue(check)

        prime_list = primes.create_prime_list(2,101)
        self.assertTrue(isinstance(prime_list,list))
        self.assertListEqual(prime_list,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101])



class Week05Indexing(UTestCase):
    def __init__(self, *args, skip_remote_check=False, **kwargs):
        super().__init__(*args, skip_remote_check=skip_remote_check, **kwargs)
        self.lst_1 = [88, 26, 71, 56, 34, 93, 4, 53, 87, 97, 23, 18, 54, 48, 78, 40, 70, 89, 4, 59, 29, 82, 72, 64, 49, 33, 30, 50, 50, 50, 21]
        self.lst_2 = [27, 87, 55, 25, 53, 90, 80, 68, 72, 79, 41, 72, 37, 91, 95, 48, 57, 78, 16, 80, 1, 96, 40, 80, 98, 73, 2, 45, 28, 75, 76]

        self.nested_lst_1 = [[88], [26], [71, 56, 34], [93, 4, 53, 87, 97], [23], [18, 54], [48, 78, 40, 70], [89, 4, 59, 29, 82, 72, 64, 49, 33, 30, 50, 50], [50], [21]]
        self.nested_lst_2 = [[27, 87], [55, 25, 53, 90, 80, 68, 72, 79], [41], [72, 37, 91, 95, 48, 57, 78, 16, 80, 1, 96], [40, 80, 98], [73, 2], [45, 28, 75, 76]]

    def test_add_first_and_last(self):
        # Run and capture output
        # from cp.unitgrade import say_hello

        with self.capture() as c:
            from cp.ex05 import indexing

        
        answer = indexing.add_first_and_last(self.lst_1)
        self.assertEqual(answer,88+21)
        
        answer = indexing.add_first_and_last(self.lst_2)
        self.assertEqual(answer,27+76)

    def test_middle_element(self):
        # Run and capture output
        # from cp.unitgrade import say_hello
        import numpy as np

        with self.capture() as c:
            from cp.ex05 import indexing

        mid_el = indexing.middle_element(self.lst_1)
        self.assertEqual(mid_el,40)
        mid_el = indexing.middle_element(self.lst_2)
        self.assertEqual(mid_el,48)
    

    def test_slice_list_in_percent(self):
        # Run and capture output
        # from cp.unitgrade import say_hello
        import numpy as np

        with self.capture() as c:
            from cp.ex05 import indexing

        sub_list = indexing.slice_list_in_percent(self.lst_1,0.1,0.9)
        self.assertListEqual(sub_list,[56, 34, 93, 4, 53, 87, 97, 23, 18, 54, 48, 78, 40, 70, 89, 4, 59, 29, 82, 72, 64, 49, 33, 30])
        sub_list = indexing.slice_list_in_percent(self.lst_2,0.45,0.55)
        self.assertListEqual(sub_list,[91, 95, 48, 57])


    def test_get_longest_sublist(self):
        # Run and capture output
        # from cp.unitgrade import say_hello
        import numpy as np

        with self.capture() as c:
            from cp.ex05 import indexing

        sub_list = indexing.get_longest_sublist(self.nested_lst_1)
        self.assertListEqual(sub_list,[89, 4, 59, 29, 82, 72, 64, 49, 33, 30, 50, 50])
        sub_list = indexing.get_longest_sublist(self.nested_lst_2)
        self.assertListEqual(sub_list,[72, 37, 91, 95, 48, 57, 78, 16, 80, 1, 96])


class Week05UpdatingLists(UTestCase):
    def test_remove_at(self):
        # Run and capture output
        # from cp.unitgrade import say_hello

        with self.capture() as c:
            from cp.ex05 import updating_lists
    
        in_list = ["one","two","three","four","five","six","seven","eight"]
        out_list = updating_lists.remove_at(in_list,5)
        self.assertListEqual(out_list,["one","two","three","four","five","seven","eight"])
        out_list = updating_lists.remove_at(out_list,0)
        self.assertListEqual(out_list,["two","three","four","five","seven","eight"])

    def remove_value(self):
        # Run and capture output
        # from cp.unitgrade import say_hello

        with self.capture() as c:
            from cp.ex05 import updating_lists

        in_list = ["one","two","three","four","five","six","seven","eight"]
        out_list = updating_lists.remove_value(in_list,5)
        self.assertListEqual(out_list,in_list)
        out_list = updating_lists.remove_value(in_list,"three")
        self.assertListEqual(out_list,["one","two","four","five","six","seven","eight"])

class Week05Tests(Report): 
    title = "Tests for week 05"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week05Primes, 10),
                (Week05Indexing, 10),
                (Week05UpdatingLists, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week05Tests())
