name = input("Enter your name : ")
age = input("Enter your age:")
age = int(age)

if age >= 10 and (name[0]=='a' or name[0] == 'A'):  
    print("you can watch this movie")
else:
    print("you cant watch this movie")
