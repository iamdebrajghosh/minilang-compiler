from lexer import tokenize
from parser import parse
from codegen import generate

def compile_file(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    tokens = tokenize(code)
    ast = parse(tokens)
    js_code = generate(ast)

    with open(output_file, 'w') as f:
        f.write(js_code)

    print("✅ Compilation successful!")
    print(f"➡️ Output written to: {output_file}")

if __name__ == "__main__":
    compile_file("example.min", "output.js")
