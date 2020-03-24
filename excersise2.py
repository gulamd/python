#num1 = input("enter first number: ")
#num2 = input("enter secound number : ")
#num3 = input("Enter third number : ")
# (int(num1) + int(num2) + int(num3)) /3
#print(f"avaregae of three number: {(int(num1) + int(num2) + int(num3)) /3}")
# provide the input at one line 
num1, num2, num3 = input("enter three numbers comma seperated: ").split(",")    # here we can either comma or other thing as well like space 
print(f"average of the three numbers : {(int(num1) + int(num2) + int(num3)) / 3}")