expression = input("Please enter a mathematical expression: ")
equation = expression.split(" ")
print(equation)

i = 0

while i < len(equation):
    if i < len(equation) and (equation[i] == "*" or equation[i] == "/"):
        if equation[i] == "*":
            equation[i] = int(equation[i-1]) * int(equation[i+1])
        else:
            equation[i] = int(equation[i-1]) / int(i+1)
        print(equation)
        equation.pop(i-1)
        equation.pop(i)
    else:
        i += 1

i = 0

while i < len(equation):
    if i < len(equation) and (equation[i] == "+" or equation[i] == "-"):
        if equation[i] == "+":
            equation[i] = int(equation[i-1]) + int(equation[i+1])
        else:
            equation[i] = int(equation[i-1]) - int(equation[i+1])
        equation.pop(i-1)
        equation.pop(i)
    else:
        i += 1

print(equation)
    

