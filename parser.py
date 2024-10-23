class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, token_type):
        """
        Consumes a token if it matches the expected type, otherwise raises an error.
        """
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type:
            self.pos += 1
        else:
            raise Exception(f"Expected {token_type}, got {self.tokens[self.pos]}")

    def parse_assignment(self):
        """
        Parses assignment statements: ID = expression;
        """
        var_name = self.tokens[self.pos][1]  # Get variable name
        self.eat('ID')
        self.eat('ASSIGN')
        expr = self.parse_expression()
        return ('ASSIGN', var_name, expr)

    def parse_expression(self):
        """
        Parses expressions with operators, e.g., x + y or 5 * (2 + 3).
        """
        left = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'OP':
            op = self.tokens[self.pos][1]
            self.eat('OP')
            right = self.parse_term()
            left = ('BINOP', op, left, right)
        return left

    def parse_term(self):
        """
        Parses individual terms, such as numbers, variables, or parenthesized expressions.
        """
        if self.tokens[self.pos][0] == 'NUMBER':
            value = self.tokens[self.pos][1]
            self.eat('NUMBER')
            return ('NUM', value)
        elif self.tokens[self.pos][0] == 'ID':
            var_name = self.tokens[self.pos][1]
            self.eat('ID')
            return ('VAR', var_name)
        elif self.tokens[self.pos][0] == 'LPAREN':
            self.eat('LPAREN')
            expr = self.parse_expression()
            self.eat('RPAREN')
            return expr

    def parse_if_statement(self):
        """
        Parses if statements: if condition then statement;
        """
        self.eat('IF')
        condition = self.parse_expression()
        self.eat('THEN')
        statement = self.parse()
        return ('IF', condition, statement)

    def parse(self):
        """
        Parses the overall structure of the program.
        """
        if self.tokens[self.pos][0] == 'ID':
            return self.parse_assignment()
        elif self.tokens[self.pos][0] == 'IF':
            return self.parse_if_statement()
