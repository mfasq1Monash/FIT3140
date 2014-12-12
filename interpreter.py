'''
Author: Michael Asquith
Created: 2014.12.08
Last Modified: 2014.12.12

Interpreter for a simple functional programming language.
Access with execute(command)

Based on Peter Norig's Lispy interpreter, http://norvig.com/lispy.html
'''
import math, operator as op
from robotio import RobotIO

Symbol = str

class Procedure(object):
    """A user-defined method"""
    
    def __init__(self, parms, stats, env, inter):
        self.parameters = parms
        self.statements = stats
        self.environment = env
        self.interpreter = inter

    def __call__(self, *args):
        return self.interpreter.evaluate(self.statements, Environment(self.parameters, args, self.environment))

class Environment(dict):

    def __init__(self, parms=(), expressions=(), outer=None):
        """When evaluating, procedures will pass in their parameters"""
        self.update(zip(parms, expressions))
        self.outer = outer
        
    def find(self, variable):
        """Returns the lowest level Environment which has variable"""
        if variable in self:
            return self
        return self.outer.find(variable)
        
    def add_new(self, variable, value):
        """Adds a new definition to the environment. If the variable is already present, raises a KeyAlreadyPresentError"""
        if variable in self:
            raise(VariableAlreadyPresentError)
        self[variable] = value

class Interpreter:

    def __init__(self, newrobotio):
        self.global_environment = self.standard_environment()
        self.robotio = newrobotio

    def interpret(self, code):
        "Interprets and executes code."
        return self.evaluate(self.parse(code))

    def parse(self, code):
        "Read an expression from a string."
        return self.read_from_tokens(self.tokenize(code))

    def tokenize(self, s):
        "Convert a string into a list of tokens."
        return s.replace('(',' ( ').replace(')',' ) ').split()

    def read_from_tokens(self, tokens):
        "Read an expression from a sequence of tokens."
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF while reading')
        token = tokens.pop(0)
        if '(' == token:
            L = []
            while tokens[0] != ')':
                L.append(self.read_from_tokens(tokens))
            tokens.pop(0) # pop off ')'
            return L
        elif ')' == token:
            raise SyntaxError('unexpected )')
        else:
            return self.atom(token)

    def atom(self, token):
        "Numbers become numbers, booleans become booleans, everything else become symbols."
        try:
            return int(token)
        except ValueError:
                if token == 'true':
                    return True
                elif token == 'false':
                    return False
                else:
                    return Symbol(token)


    def standard_environment(self):
        "Creates the base variable environment"
        env = Environment()
        env.update(vars(math))
        env.update({
            '+':op.add, '-':op.sub, '*':op.mul, '/':op.div, '%': op.mod,
            '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq,
            'and':  lambda x,y: x and y,
            'or':   lambda x,y: x or y,
            'not':  lambda x: not x
        })
        
        return env

    def evaluate(self, x, env=None):

        if env == None:
            env = self.global_environment
        
        #If x is a list, must be evaluating a method
        if isinstance(x, list):
            method = x.pop(0)
                    
            if method == 'define':
                try:
                    self.global_environment.add_new(x[0], Procedure(x[1], x[2], env, self))    
                except VariableAlreadyPresentError:
                    raise FunctionAlreadyDefinedError
                    
            elif method == 'if':
                # If statement. [Test, consequences, alternative]
                if self.evaluate(x[0]):
                    return self.evaluate(x[1])
                return self.evaluate(x[2])

            elif method == 'set':
                try:
                    env.add_new(x[0], evaluate(x[1],env))
                except VariableAlreadyPresentError:
                    raise VariableAlreadySetError
                return

            elif method == 'comment':
                return

            elif method == 'move':
                self.robotio.move(self.evaluate(x[1]))
                return

            elif method == 'turn':
                self.robotio.turn(self.evaluate(x[1]))
                return

            else:
                method = self.evaluate(method, self.global_environment)
                args = [self.evaluate(variable, env) for variable in x]
                return method(*args)
            
        elif isinstance(x, Symbol):
                return self.evaluate(env.find(x)[x])

        else:
            return x
