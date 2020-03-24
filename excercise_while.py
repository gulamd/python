#exercise one of three
#sum of n natural numbers
# ask a user for natural numer (n)
# print total from 1 to n
num = input(" type any natual number: ")
num = int(num)
i = 1
total =  0

while i<= num:
    total = total + i
    i = i + 1
print(total)