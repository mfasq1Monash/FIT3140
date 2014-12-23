from interpreter import (Interpreter,
                         VariableNotFoundException,
                         VariableAlreadySetException,
                         FunctionAlreadyDefinedException)
from robotio import RobotIO
import unittest

class InterpreterTest(unittest.TestCase):

    def setUp(self):
        self.inter = Interpreter(RobotIO())

    def listSetUp(self):
        self.inter.interpret('(set list (build 4 (build 18 (build 39 []))))')
        self.inter.interpret('(set meta (build list (build 3 [])))')

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
        # boolean AND
        self.assertEqual(self.inter.interpret('(and true true)'),True)
        self.assertEqual(self.inter.interpret('(and true false)'),False)
        self.assertEqual(self.inter.interpret('(and false false)'),False)

    def test_or(self):
        # boolean OR
        self.assertEqual(self.inter.interpret('(or true false)'),True)
        self.assertEqual(self.inter.interpret('(or false false)'),False)
        self.assertEqual(self.inter.interpret('(or true true)'),True)

    def test_not(self):
        # boolean NOT
        self.assertEqual(self.inter.interpret('(not true)'),False)
        self.assertEqual(self.inter.interpret('(not false)'),True)

    def test_if(self):
        # boolean IF
        self.assertEqual(self.inter.interpret('(if true 100 -50)'),100)
        self.assertEqual(self.inter.interpret('(if false 100 -50)'),-50)

    def test_plus(self):
        # integer plus
        self.assertEqual(self.inter.interpret('(+ 16 9)'),25)
        self.assertEqual(self.inter.interpret('(+ -1000 34)'),-966)

    def test_minus(self):
        # integer minus
        self.assertEqual(self.inter.interpret('(- 16 9)'),7)
        self.assertEqual(self.inter.interpret('(- 34 -1000)'),1034)


    def test_multiply(self):
        # integer multiply
        self.assertEqual(self.inter.interpret('(* 16 9)'),144)
        self.assertEqual(self.inter.interpret('(* 34 -1000)'),-34000)

    def test_divide(self):
        # integer divide 
        self.assertEqual(self.inter.interpret('(/ 16 8)'),2)
        self.assertEqual(self.inter.interpret('(/ 1000 35)'),28)

        # divide by zero
        self.assertRaises(ZeroDivisionError,self.inter.interpret,('(/ 2 0)'))

    def test_set(self):
        # setting variable to a number
        self.inter.interpret('(set a 3)')
        self.assertEqual(self.inter.interpret('a'),3)

        # setting variable to a boolean
        self.inter.interpret('(set b true)')
        self.assertEqual(self.inter.interpret('b'),True)

        # attempting to re-set a variable should raise an error
        self.assertRaises(VariableAlreadySetException,
                         self.inter.interpret,'(set b 4)')

    def test_define(self):
        # defining a function without parameters
        self.inter.interpret('(define a () 3)')
        self.assertEqual(self.inter.interpret('(a)'),3)

        # defining a function with a parameter
        self.inter.interpret('(define b x (* x 2))')
        self.assertEqual(10,self.inter.interpret('(b 5)'))

        # defining a function with multiple parameters
        self.inter.interpret('(define defence (banana pointedstick)' +
                             '(* banana pointedstick))')
        self.assertEqual(21, self.inter.interpret('(defence 7 3)'))

        # defining a function which does not use all its parameters
        self.inter.interpret('(define grenade count 5)')
        self.assertEqual(5, self.inter.interpret('(grenade 462)'))

    def test_move(self):
        # robot will move
        self.inter.robotio.move(2)
        temp = self.inter.robotio.getLocationAndFacing()
        self.inter = Interpreter(RobotIO())
        self.inter.interpret('(move 2)')
        self.assertEqual(temp, self.inter.robotio.getLocationAndFacing())

    def test_turn(self):
        # robot will turn
        self.inter.robotio.turn(1)
        temp = self.inter.robotio.getLocationAndFacing()
        self.inter = Interpreter(RobotIO())
        self.inter.interpret('(turn 1)')
        self.assertEqual(temp, self.inter.robotio.getLocationAndFacing())

    def test_detectwall(self):
        # robot will detect wall
        self.assertEqual(4, self.inter.interpret('(detect-wall 5)'))

    def test_detectgoal(self):
        # robot will detect goal
        self.assertEqual(8, self.inter.interpret('(detect-goal 10)'))

    def test_equality(self):
        # integer equality
        self.assertEqual(True, self.inter.interpret('(= 3 3)'))
        self.assertEqual(False, self.inter.interpret('(= 3 4)'))

    def test_inequalities(self):
        # integer less than
        self.assertEqual(True, self.inter.interpret('(< 2 6)'))
        self.assertEqual(False, self.inter.interpret('(< 6 2)'))
        
        # integer greater than
        self.assertEqual(False, self.inter.interpret('(> 2 6)'))
        self.assertEqual(True, self.inter.interpret('(> 6 2)'))

        # integer less than or equal
        self.assertEqual(True, self.inter.interpret('(<= 2 6)'))
        self.assertEqual(False, self.inter.interpret('(<= 6 2)'))
        self.assertEqual(True, self.inter.interpret('(<= 2 2)'))

        # integer greater than or equal
        self.assertEqual(False, self.inter.interpret('(>= 2 6)'))
        self.assertEqual(True, self.inter.interpret('(>= 6 2)'))
        self.assertEqual(True, self.inter.interpret('(>= 2 2)'))

    def test_comment(self):
        # comment should return None
        self.assertEqual(None, self.inter.interpret('(comment (run away!))'))
        
    def test_modulus(self):
        # integer modulus
        self.assertEqual(2, self.inter.interpret('(% 17 5)'))
        self.assertEqual(3, self.inter.interpret('(% 2 -5)'))
        self.assertEqual(4, self.inter.interpret('(% -1 5)'))

        # n modulo 0 is impossible
        self.assertRaises(ZeroDivisionError,self.inter.interpret,('(% 2 0)'))

    def test_build(self):
        # build a list
        self.assertEqual([3], self.inter.interpret('(build 3 [])'))
        self.assertEqual([1,2], self.inter.interpret('(build 1 (build 2 []))'))

        self.listSetUp() # list = [4,18,39]; meta = [list, 3]
        
        self.assertEqual([4,18,39], self.inter.interpret('list'))
        self.assertEqual([[4,18,39],3], self.inter.interpret('meta'))

    def test_head(self):
        # list "head" method
        self.listSetUp()
        
        self.assertEqual(4, self.inter.interpret('(head list)'))
        self.assertEqual([4,18,39], self.inter.interpret('(head meta)'))

        self.inter.interpret('(set list2 (head meta))')
        self.assertEqual(4, self.inter.interpret('(head list2)'))

    def test_tail(self):
        # list "tail" method
        self.listSetUp()
        
        self.assertEqual([18,39], self.inter.interpret('(tail list)'))
        self.assertEqual([3], self.inter.interpret('(tail meta)'))
        self.assertEqual([[4,18,39],3],
                         self.inter.interpret('(build (head meta) (tail meta))'))
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InterpreterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
