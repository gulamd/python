# compare lists
# ==,is
fruit = ['orange','pear','apple']
fruit1 = ['orange','apple','pear']
fruits = ['banana','apple','kiwi','same']

# print(fruit == fruits) false
#print(fruit == fruit1)   # true
# but if we use 'is'
print(fruit is fruit1) # false

# sice both fruit and fruit1 is different object


# == it will check the value is same or not
# is  --will check the memory place or the same or not