user_info = {
    'name' : 'Harshit',
    'age' : 27,
    'fav_movies' : 'love aaj kal',
    'fav_song' : 'tum hi ho'


}

# check if key exit in dict

if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if value exist in dict

if 27 in user_info.values():
    print('present')
else:
    print('not present')
#loop in dicts
for i in user_info:
    print(i)   # print all key
for i in user_info.values():
    print(i)
# values methos
user_info_values = user_info.values()
print(user_info)
print(type(user_info_values))

print('------------------------')
# keys methos
user_info_keys = user_info.keys()
print(user_info)
print(type(user_info_keys))


print('------------------------')

#items methods

user_items = user_info.items()
print(user_items)
print(type(user_items))


print('-----------------------')
for key, value in user_info.items():
    print(f" key is {key} and value is {value}")





