# in keyword in sets and for loop
s = {'a','b','c','d'}

# in keyword
if 'a' in s:
    print("present")
else:
    print("Not present")


# FOR LOOP
for i in s:
    print(i)

# set maths
s1 = {1,2,3,4}
s2 = {3,4,5,6}
#union use |
union_set = s1 | s2
print(union_set)
# intersection

inter_set = s1 & s2
print(inter_set)