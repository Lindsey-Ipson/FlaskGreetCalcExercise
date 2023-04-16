from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome. This is the root directory.'

@app.route('/add')
def execute_add():
    """Add a and b parameters"""
    print(request.args)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def execute_sub():
    """Subtract b parameter from a parameter"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def execute_mult():
    """Multiply a and b parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def execute_div():
    """Divide b parameter from a parameter"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)


"""All-in-one version:"""

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def execute_math(operation):
    """Execute math function on a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[operation](a, b)

    return str(result)





