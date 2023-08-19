from unitgrade import UTestCase, Report, hide
import math

class TestSineCosineWeek9(UTestCase):
    def test_make_symbol(self):
        from cp.ex09.sinus import make_symbol, Variable
        v = make_symbol('x')
        self.assertIsInstance(v, Variable)



    def test_sine(self):
        from cp.ex09.sinus import make_symbol, sine, Sin
        v = make_symbol('x')
        s = sine(v)
        self.assertIsInstance(s, Sin)
        self.assertEqual(s.arg, v)



    def test_cosine(self):
        from cp.ex09.sinus import make_symbol, cosine, Cos
        v = make_symbol('x')
        c = cosine(v)
        self.assertIsInstance(c, Cos)
        self.assertEqual(c.arg, v)


    def test_format_expression(self):
        from cp.ex09.sinus import make_symbol, sine, cosine, format_expression
        v = make_symbol('x')
        s = sine(v)
        c = cosine(v)
        self.assertEqual(format_expression(v), 'x')
        self.assertEqual(format_expression(s), 'sin(x)')
        self.assertEqual(format_expression(c), 'cos(x)')

        # Test nested expressions
        s2 = sine(c)
        c2 = cosine(s)
        self.assertEqual(format_expression(s2), 'sin(cos(x))')
        self.assertEqual(format_expression(c2), 'cos(sin(x))')


class TestConstant(UTestCase):

    def test_inheritance(self):
        from cp.ex10.symbolic import Constant, Expression
        c = Constant(7)
        self.assertIsInstance(c, Expression)


    def test_print(self):
        from cp.ex10.symbolic import Constant
        self.assertEqual(str(Constant(7)), "7")
        self.assertEqual(str(Constant(0)), "0")
        self.assertEqual(str(Constant(3.14)), "3.14")



    def test_negative_print(self):
        from cp.ex10.symbolic import Constant
        self.assertEqual(str(Constant(-101)), "(-101)")


    def test_evaluate(self):
        from cp.ex10.symbolic import Constant
        c = Constant(7)
        self.assertEqual(c.evaluate({}), 7)
        self.assertEqual(c.evaluate({"z": -10}), 7)



    def test_derivative(self):
        from cp.ex10.symbolic import Constant
        c = Constant(7)
        d = c.differentiate("x")
        self.assertIsInstance(d, Constant)
        self.assertEqual(d.evaluate({}), 0)


class TestVariable(UTestCase):
    def test_inheritance(self):
        from cp.ex10.symbolic import Variable, Expression
        self.assertIsInstance(Variable("x"), Expression)


    def test_print(self):
        from cp.ex10.symbolic import Variable
        self.assertEqual(str(Variable("x")), "x")


    def test_evaluate(self):
        from cp.ex10.symbolic import Variable
        c = Variable("x")
        self.assertEqual(c.evaluate({"x": 7}), 7)


    def test_derivative(self):
        from cp.ex10.symbolic import Variable, Constant
        c = Variable("x")
        d = c.differentiate("x")
        self.assertIsInstance(d, Constant)
        self.assertEqual(str(d), "1")


class TestAddition(UTestCase):
    def test_inheritance(self):
        from cp.ex10.symbolic import Addition, Constant, BinaryOperator
        self.assertIsInstance(Addition(Constant(1), Constant(2)), BinaryOperator)


    def test_print(self):
        from cp.ex10.symbolic import Addition, Variable
        self.assertEqual(str(Addition(Variable("x"), Variable("y"))), "(x + y)")


    def test_evaluate(self):
        from cp.ex10.symbolic import Addition, Constant, Variable
        c = Addition(Variable("x"), Constant(3))
        self.assertEqual(c.evaluate({"x": 7}), 10)



    def test_derivative(self):
        from cp.ex10.symbolic import Addition, Constant, Variable
        c = Addition(Variable("x"), Constant(3))
        d = c.differentiate("x")
        self.assertEqual(str(d), "(1 + 0)")
        self.assertEqual(d.evaluate({}), 1)


    def test_derivative_nested(self):
        from cp.ex10.symbolic import Addition, Constant, Variable
        c = Addition(Variable("x"), Addition(Constant(3), Variable("x")))
        d = c.differentiate("x")
        self.assertEqual(str(d), "(1 + (0 + 1))")


class TestMultiplication(UTestCase):
    def test_print(self):
        from cp.ex10.symbolic import Multiplication, Constant, Variable
        self.assertEqual(str(Multiplication(Variable("x"), Constant(3))), "x * 3")



    def test_evaluate(self):
        from cp.ex10.symbolic import Multiplication, Constant, Variable
        self.assertEqual(Multiplication(Variable("x"), Constant(3)).evaluate({"x": 2}), 6)


    def test_derivative(self):
        from cp.ex10.symbolic import Multiplication, Constant, Variable
        c = Multiplication(Variable("x"), Constant(3))
        d = c.differentiate("x")
        self.assertEqual(str(d), "(1 * 3 + x * 0)")
        self.assertEqual(d.evaluate({"x": 10}), 3)



    def test_derivative_nested(self):
        from cp.ex10.symbolic import Multiplication, Constant, Variable, Addition
        c = Multiplication(Variable("x"), Addition(Constant(3), Variable("x")))
        d = c.differentiate("x")
        self.assertEqual(str(d), "(1 * (3 + x) + x * (0 + 1))")


class TestTrigonometricBasic(UTestCase):
    def test_sin_print(self):
        from cp.ex10.symbolic import Variable, Sin
        sin = Sin(Variable("x"))
        self.assertEqual(str(sin), "sin(x)")


    def test_cos_print(self):
        from cp.ex10.symbolic import Constant, Cos
        cos = Cos(Constant(3))
        self.assertEqual(str(cos), "cos(3)")



    def test_sin_evaluate(self):
        from cp.ex10.symbolic import Variable, Sin
        sin = Sin(Variable("x"))
        self.assertAlmostEqual(sin.evaluate({"x": 2}), math.sin(2))


    def test_cos_evaluate(self):
        from cp.ex10.symbolic import Variable, Cos
        self.assertAlmostEqual(Cos(Variable("x")).evaluate({"x": 2}), math.cos(2))



class TestEverything(UTestCase):
    def test_everything(self):
        from cp.ex10.symbolic import Variable, Cos, Multiplication, Sin, Addition, Constant
        x = Variable("x")
        y = Addition( Multiplication(Constant(3), Sin(x)), Cos(x))
        str(y)
        self.assertEqual(str(y),  '(3 * sin(x) + cos(x))')
        self.assertAlmostEqual(y.evaluate({"x": math.pi/2}), 3)
        self.assertEqual(str(y.differentiate("x")), '((0 * sin(x) + 3 * cos(x) * 1) + (-1) * sin(x) * 1)')


class TestTrigonometricDerivative(UTestCase):
    def test_sin(self):
        from cp.ex10.symbolic import Variable, Sin
        x = Variable("x")
        dx = Sin(x).differentiate("x")
        self.assertEqual(str(dx), "cos(x) * 1")

    def test_cos(self):
        from cp.ex10.symbolic import Variable, Cos
        x = Variable("x")
        dx = Cos(x).differentiate("x")
        self.assertEqual(str(dx), "(-1) * sin(x) * 1")

    def test_sin_advanced(self):
        from cp.ex10.symbolic import Variable, Cos, Constant, Multiplication, Addition
        x = Variable("x")
        dx = Multiplication(x, Cos(Addition(x, Constant(3)))).differentiate("x")
        self.assertEqual(str(dx), "(1 * cos((x + 3)) + x * (-1) * sin((x + 3)) * (1 + 0))")


class Project5(Report):
    title = "Project 5"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = [(TestSineCosineWeek9, 20),
                 (TestConstant, 10),
                 (TestVariable, 10),
                 (TestAddition, 10),
                 (TestMultiplication, 10),
                 (TestTrigonometricBasic, 10),
                 (TestTrigonometricDerivative, 10),
                 (TestEverything, 10),
                 ]
    import cp
    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student
    evaluate_report_student(Project5())
