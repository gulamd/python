name = input("Enter your name : ")
#harshit vashisth
#name.count("h")
i = 0
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]

        print(f" {name[i]} : {name.count(name[i])}")
    i = i+1
    