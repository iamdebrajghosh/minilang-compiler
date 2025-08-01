def generate(ast):
    output = []
    for node in ast:
        if node[0] == 'assign':
            output.append(f"let {node[1]} = {node[2]};")
        elif node[0] == 'print':
            output.append(f"console.log({node[1]});")
    return '\n'.join(output)
