
height , weight, bmi =12,32,23.2
def inputData ():
    height = int (input ('Enter height please: '))
    weight = int (input ('Enter weight please: '))

def calculateBMI():
    bmi = weight / (height ** 2)
    return bmi 

def interpret_bmi():
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return"Obesity"