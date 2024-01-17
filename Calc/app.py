from flask import Flask, request, jsonify
from operations import add, sub, mult, div

app = Flask(__name__)

# Routes for basic arithmetic operations

@app.route("/add")
def do_add():
    """Add a and b parameters."""
    a, b = get_operands()
    result = add(a, b)
    return jsonify(result=result)

@app.route("/sub")
def do_sub():
    """Subtract a and b parameters."""
    a, b = get_operands()
    result = sub(a, b)
    return jsonify(result=result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""
    a, b = get_operands()
    result = mult(a, b)
    return jsonify(result=result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""
    a, b = get_operands()
    try:
        result = div(a, b)
        return jsonify(result=result)
    except ZeroDivisionError:
        return jsonify(error="Cannot divide by zero"), 400

# Route for generic math operation

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""
    a, b = get_operands()
    try:
        result = operators[oper](a, b)
        return jsonify(result=result)
    except KeyError:
        return jsonify(error="Invalid operator"), 400

def get_operands():
    """Helper function to extract 'a' and 'b' parameters from the request."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return a, b

if __name__ == '__main__':
    app.run(debug=True)
