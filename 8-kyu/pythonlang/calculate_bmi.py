# Calculate BMI [https://www.codewars.com/kata/57a429e253ba3381850000fb/solutions/python]
def bmi(weight, height):
    bmi_value = weight / height**2
    if (bmi_value <= 18.5):
        return 'Underweight'
    elif (bmi_value > 18.5 and bmi_value <= 25.0):
        return 'Normal'
    elif (bmi_value > 25.0 and bmi_value <= 30.0):
        return 'Overweight'
    
    return 'Obese'