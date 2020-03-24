# what are dictionaries?
# UNORDERED COLLECTIONS OF DATA IN KEY: VALUE PAIR

#user = {'name' : 'harshit' , 'age': 24}
#print(user)

#2nd method
user1 = dict(name = 'harshit', age = 24)
print(user1)
print(type(user1))

#how to access data
#note-there is not index bcz of unordered collections of data. we use key
print(user1['name'])

# how to add data n dict\
user_info = {}
user_info['name'] = 'gulam'
user_info['age'] = 25
print(user_info)