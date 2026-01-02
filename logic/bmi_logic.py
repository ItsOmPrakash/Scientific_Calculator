def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except:
        return None
