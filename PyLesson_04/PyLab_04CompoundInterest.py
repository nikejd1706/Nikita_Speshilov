def payment(p,r,n,t):
    return (p+(p*((1+r/n)**(n*t)))/(t*12));

P = float(input("Please enter the principal:"))
R = float(input("Please enter the interest rate:"))
N = float(input("Please enter the number of times the loan is compounded each year:"))
T = float(input("Please enter the life of the loan in years:"))
print("Your total payment is%8.2f"%payment(P,R,N,T),)
          


          

    
