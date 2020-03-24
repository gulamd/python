def is_palindrom(word):
    return word == word[::-1]
name = input("Enter your name : ")
print(is_palindrom(name))
