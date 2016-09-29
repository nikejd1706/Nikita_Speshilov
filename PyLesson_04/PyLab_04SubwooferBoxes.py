def volume(H,L,W):
    return(H*L*W/1728)

H = float(input("Please enter the height of the subwoofer in cubic inches:"))
L = float(input("Please enter the length of the subwoofer in cubic inches:"))
W = float(input("Please enter the width of the subwoofer in cubic inches:"))
print("The subwoofer volume is%8.2F"%volume(H,L,W),"cubic feet.")
            



