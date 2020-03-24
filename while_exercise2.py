str = input("Enter the number: ")
strl = len(str)
i = 0
cal = 0
while i < strl:
    cal =  cal + int(str[i])
    i = i + 1

print(cal)