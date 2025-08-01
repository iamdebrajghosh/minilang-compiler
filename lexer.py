import re

token_specification = [
    ('LET',       r'let'),
    ('PRINT',     r'print'),
    ('NUMBER',    r'\d+'),
    ('IDENTIFIER',r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('EQUAL',     r'='),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('MUL',       r'\*'),
    ('SEMICOLON', r';'),
    ('SKIP',      r'[ \t]+'),
    ('NEWLINE',   r'\n'),
]

token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)

def tokenize(code):
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind not in ('SKIP', 'NEWLINE'):
            yield (kind, value)
