def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
num1 = int(input("Entert first number : "))
num2 = int(input("Entert secound number : "))
num3 = int(input("Entert third number : "))
greatest = greatest(num1,num2,num3)
print(greatest)