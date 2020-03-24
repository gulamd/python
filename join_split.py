#user_info = 'harshit 23'
# split() 
user_info = 'harshit 24'.split()
print(user_info)  # output ['harshit','24'] since it has one space and it splited that
user_info1 = 'harshit,24'.split(',')
print(user_info1)
#name , age = input("Enter you name and age ").split(',')
#print(name)
#print(age)

#join method
# convert list to string
user_info_j = ['harshit','24']
print(','.join(user_info_j))
