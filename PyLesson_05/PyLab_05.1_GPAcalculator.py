
GPA = 0;

def calcPoints():
    global lettergrade1, lettergrade2, lettergrade3, lettergrade4, lettergrade5, lettergrade6, lettergrade7

if lettergrade1 == A:
    return "4.0"
elif lettergrade1 == B:
    return "3.0"
elif lettergrade1 == C:
    return "2.0"
elif lettergrade1 == D:
    return "1.0"
elif lettergrade1 == F:
    return "0.0"
if lettergrade2 == A:
    return "4.0"
elif lettergrade2 == B:
    return "3.0"
elif lettergrade2 == C:
    return "2.0"
elif lettergrade2 == D:
    return "1.0"
elif lettergrade2 == F:
    return "0.0"
if lettergrade3 == A:
    return "4.0"
elif lettergrade3 == B:
    return "3.0"
elif lettergrade3 == C:
    return "2.0"
elif lettergrade3 == D:
    return "1.0"
elif lettergrade3 == F:
    return "0.0"
 
lettergrade1 = input("Please enter your letter grade for math: ")
lettergrade2 = input("Please enter your letter grade for science: ")
lettergrade3 = input("Please enter your letter grade for english: ")
lettergrade4 = input("Please enter your letter grade for history: ")
lettergrade5 = input("Please enter your letter grade for foreign language: ")
lettergrade6 = input("Please enter your letter grade for elective: ")
lettergrade7 = input("Please enter your letter grade for physical education: ")

GPA = (lettergrade1+lettergrade2+lettergrade3+lettergrade4+lettergrade5+lettergrade6+lettergrade7)/7


print("Your GPA is",GPA)
