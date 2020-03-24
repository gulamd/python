def grt(a,b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secound number: "))
greater = grt(num1,num2)
print(greater)