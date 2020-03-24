name = input("Enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
print(len(temp))   # to get the stored varialble lenght