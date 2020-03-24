user_info = {
    'name' : 'Harshit',
    'age' : 27,
    'fav_movies' : 'love aaj kal',
    'fav_song' : 'tum hi ho'
}

# how to add data
user_info['fav_food'] = ['cheicken' , 'briyani']
print(user_info)

# pop method
#popped_item = user_info.pop('fav_food')
#print(f"popped item is {popped_item}")

#popitem method --it will remove key and value ramdanly

popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))