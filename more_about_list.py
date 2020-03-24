# generates lists with range functions
# somtjing more about pop
#index methos
#pass list to a fucntion
#numbers = list(range(1,11))
#print(numbers)
#pooped_item = numbers.pop()
#print(pooped_item)
#print(numbers.index(1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))