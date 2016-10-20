bmi = 0
condition = ""

def calcBMI(height, weight):
    global bmi, condition
    bmi = (weight*703)/(height**2)
    if bmi < 18.5:
        condition = "underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        condition =  "normal"
    elif bmi >= 25 and bmi <= 29.9:
        condition = "overweight"
    elif bmi >=30 and bmi <= 34.9:
        condition = "obese"
    elif bmi >= 35 and bmi <= 39.9:
        condition = "very obese"
    else:
        condition = "morbidly obese"


height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

calcBMI(height, weight)
print("Your bmi is",bmi)
print("You are", condition)
      
