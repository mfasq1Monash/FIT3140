from interpreter import Interpreter, VariableNotFoundException
from robotio import RobotIO
import unittest

class InterpreterTest(unittest.TestCase):

    def setUp(self):
        self.inter = Interpreter(RobotIO())

    def test_evaluateBoolean(self):
        # interpreting "True" or "False" should return the boolean
        self.assertEqual(self.inter.interpret('true'), True)
        self.assertEqual(self.inter.interpret('FAlsE'), False)

    def test_evaluateInteger(self):
        # interpreting an integer should return that integer
        self.assertEqual(self.inter.interpret('3'),3)
        self.assertEqual(self.inter.interpret('0'),0)
        self.assertEqual(self.inter.interpret('-500'),-500)
        self.assertRaises(VariableNotFoundException,self.inter.interpret,'3.5')        

    def test_evaluateSymbol(self):
        # interpreting any non-integer/non-boolean should find that in the
        # interpreter's environment
        self.assertEqual(
            self.inter.interpret('pi'),
            self.inter.global_environment['pi'])

    def test_and(self):
        # boolean and
        self.assertEqual(self.inter.interpret('(and true true)'),True)
        self.assertEqual(self.inter.interpret('(and true false)'),False)
        self.assertEqual(self.inter.interpret('(and false false)'),False)
        #self.assertEqual(self.inter.interpret('(and true 3)')
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InterpreterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
