from lexer import lex
from parser import Parser
from interpreter import Interpreter

# Sample code to interpret
code = """
x = 5;
if x == 5 then y = 10;
"""

# Lexical analysis: Tokenize the input code
tokens = lex(code)
print("Tokens:", tokens)

# Parsing: Build an abstract syntax tree (AST)
parser = Parser(tokens)
ast = parser.parse()
print("AST:", ast)

# Interpretation: Evaluate the AST
interpreter = Interpreter()
interpreter.eval(ast)

# Output the final state of variables
print("Final Variables:", interpreter.variables)
