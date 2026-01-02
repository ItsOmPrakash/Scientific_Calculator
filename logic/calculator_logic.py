import math

def evaluate_expression(expression):
    try:
        expression = expression.replace("π", str(math.pi))
        return str(eval(expression))
    except:
        return "Error"

def sin(x):
    return round(math.sin(math.radians(x)), 6)

def cos(x):
    return round(math.cos(math.radians(x)), 6)

def tan(x):
    return round(math.tan(math.radians(x)), 6)

def sqrt(x):
    return round(math.sqrt(x), 6)

def log(x):
    return round(math.log10(x), 6)
