from unitgrade import Report
import cp
from unitgrade import UTestCase
from cp.ex02.taylor import evaluate_taylor

class Taylor(UTestCase):
    def test_taylor_x1(self):
        self.assertL2(evaluate_taylor(1))

    def test_taylor_x3(self):
        self.assertL2(evaluate_taylor(3))

class TaylorVariants(UTestCase):

    def test_taylor_variant_1(self):
        from inspect import getmembers, isfunction
        from cp.ex02 import taylor_variant1
        mm = getmembers(taylor_variant1, isfunction)
        if len(mm) == 0:
            raise Exception("You did not define a function in your code")

        name, taylor = mm[0]

        print("Running:")
        print(f"{name}(x)")
        self.assertL2(taylor(1.4))

    def test_taylor_variant_2(self):
        import inspect
        from cp.ex02 import taylor_variant2

        if hasattr(taylor_variant2, 'y'):
            self.assertL2(taylor_variant2.y, 0.41666, tol=1e-4)

        source = inspect.getsource(taylor_variant2)
        lines = source.splitlines()
        for k, l in enumerate(lines):
            if l.strip().replace(" ", "").startswith("x="):
                lines[k] = "x = 9"
        # y  = None
        s = "\n".join(lines)
        # global y
        # locals_ = locals()
        ldict = {}
        exec(s, globals(), ldict)
        # print(y)
        if 'y' not in ldict:
            raise Exception("You failed to define y in your test")
        else:
            y = ldict['y']
            self.assertL2(y)

class Week01Tests(Report): #240 total.
    title = "Tests for week 01"
    pack_imports = [cp]
    individual_imports = []
    questions = [
        (Taylor, 10),
        (TaylorVariants, 10),
                 ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week01Tests())
