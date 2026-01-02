def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"
