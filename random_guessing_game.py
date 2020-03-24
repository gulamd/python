winning_number = 43
guess = 1
number = int(input("guess number between 1 and 100 :"))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you won , and you guessed this number {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("guess again :"))
        else: 
            print("too hingh")
            guess += 1
            number = int(input("guess again :"))