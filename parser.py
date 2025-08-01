def parse(tokens):
    tokens = list(tokens)
    index = 0
    ast = []

    def match(expected_type):
        nonlocal index
        if tokens[index][0] == expected_type:
            index += 1
            return tokens[index - 1][1]
        raise SyntaxError(f"Expected {expected_type}, got {tokens[index][0]}")

    while index < len(tokens):
        token_type, _ = tokens[index]

        if token_type == 'LET':
            match('LET')
            var_name = match('IDENTIFIER')
            match('EQUAL')
            left = match('NUMBER') if tokens[index][0] == 'NUMBER' else match('IDENTIFIER')

            op = None
            right = None

            if tokens[index][0] in ('PLUS', 'MINUS', 'MUL'):
                op = tokens[index][1]
                match(tokens[index][0])
                right = match('NUMBER') if tokens[index][0] == 'NUMBER' else match('IDENTIFIER')
                expr = f"{left} {op} {right}"
            else:
                expr = left

            match('SEMICOLON')
            ast.append(('assign', var_name, expr))

        elif token_type == 'PRINT':
            match('PRINT')
            expr = match('IDENTIFIER')
            match('SEMICOLON')
            ast.append(('print', expr))

        else:
            raise SyntaxError(f"Unexpected token: {token_type}")

    return ast
            