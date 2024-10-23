import re

# Define token patterns for the lexer
token_specification = [
    ('NUMBER',    r'\d+'),           # Integer
    ('ASSIGN',    r'='),             # Assignment operator
    ('END',       r';'),             # Statement terminator
    ('ID',        r'[A-Za-z]+'),     # Identifiers (variable names)
    ('OP',        r'[+\-*/]'),       # Arithmetic operators
    ('IF',        r'if'),            # If statement
    ('THEN',      r'then'),          # Then keyword
    ('EQ',        r'=='),            # Equality comparison
    ('NE',        r'!='),            # Not equal comparison
    ('LT',        r'<'),             # Less than
    ('GT',        r'>'),             # Greater than
    ('LE',        r'<='),            # Less than or equal
    ('GE',        r'>='),            # Greater than or equal
    ('LPAREN',    r'\('),            # Left parenthesis
    ('RPAREN',    r'\)'),            # Right parenthesis
    ('SKIP',      r'[ \t]+'),        # Skip spaces and tabs
    ('MISMATCH',  r'.'),             # Any other character
]

# Build the lexer by compiling the regular expression
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

def lex(code):
    """
    Lexer: Tokenizes the source code based on the defined token patterns.
    """
    tokens = []
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value)  # Convert number strings to integers
        elif kind == 'ID':
            pass  # Keep identifiers as they are
        elif kind == 'SKIP':
            continue  # Skip whitespace
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    return tokens
