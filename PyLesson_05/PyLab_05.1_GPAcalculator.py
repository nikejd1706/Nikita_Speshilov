
GPA = 0;

def calcPoints(lettergrade):

if lettergrade == A:
    return "4.0"
elif lettergrade == B:
    return "3.0"
elif lettergrade == C:
    return "2.0"
elif lettergrade == D:
    return "1.0"
elif lettergrade == F:
    return "0.0"

 
lettergrade1 = input("Please enter your letter grade for math: ")
lettergrade2 = input("Please enter your letter grade for science: ")
lettergrade3 = input("Please enter your letter grade for english: ")
lettergrade4 = input("Please enter your letter grade for history: ")
lettergrade5 = input("Please enter your letter grade for foreign language: ")
lettergrade6 = input("Please enter your letter grade for elective: ")
lettergrade7 = input("Please enter your letter grade for physical education: ")

GPA = (calcPoints(lettergrade1)+calcPoints(lettergrade2)+calcPoints(lettergrade3)+calcPoints(lettergrade4)+lettergrade5+lettergrade6+lettergrade7


print("Your GPA is",GPA)
