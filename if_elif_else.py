# when u need to check multiple statement
#show ticket pricing 
# 1 to 3 --free
#4 to 10 -- 150

age = input("please input your age : ")
age = int(age)
if age==0 or age < 0:
    print("you cant watch : ")
elif 0<age<=3:
    print("ticket price : free")
elif 3<age<=10:
    print("ticket price : 150 ")
elif 10<age<=60:
    print("ticket price : 250")
else:
    print("ticket price : 200")    