from flask import Flask, request, jsonify
from flask_cors import CORS
from lexer import tokenize
from parser import parse
from codegen import generate

app = Flask(__name__)
CORS(app)  # Allow React frontend to access

@app.route("/compile", methods=["POST"])
def compile_code():
    try:
        code = request.json["code"]
        tokens = tokenize(code)
        ast = parse(tokens)
        js_code = generate(ast)
        return jsonify({"js_code": js_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
