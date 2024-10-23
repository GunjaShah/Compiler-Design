class Interpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, node):
        """
        Evaluates the syntax tree and executes the code.
        """
        if node[0] == 'NUM':
            return node[1]
        elif node[0] == 'VAR':
            var_name = node[1]
            return self.variables.get(var_name, 0)  # Default to 0 if variable is not defined
        elif node[0] == 'ASSIGN':
            var_name = node[1]
            value = self.eval(node[2])
            self.variables[var_name] = value
            return value
        elif node[0] == 'BINOP':
            left = self.eval(node[2])
            right = self.eval(node[3])
            if node[1] == '+':
                return left + right
            elif node[1] == '-':
                return left - right
            elif node[1] == '*':
                return left * right
            elif node[1] == '/':
                return left / right
        elif node[0] == 'IF':
            condition_value = self.eval(node[1])
            if condition_value:
                return self.eval(node[2])
