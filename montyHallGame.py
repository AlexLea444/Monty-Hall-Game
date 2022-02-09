import random

def game():
    car = random.randint(1,3)
    guess = input("Which door do you choose?")
    if guess == 'end':
        quit()
    else:
        guess = int(guess)
    goat = 0
    switch = 0
    if guess == 1:
        if car == 1:
            goat = random.randint(2,3)
        if car == 2:
            goat = 3
        if car == 3:
            goat = 2
    elif guess == 2:
        if car == 1:
            goat = 3
        if car == 2:
            goat = random.randint(0,1)
            goat *= 2
            goat += 1
        if car == 3:
            goat = 1
    elif guess == 3:
        if car == 1:
            goat = 2
        if car == 2:
            goat = 1
        if car == 3:
            goat = random.randint(1,2)
    print("There is a goat behind door " + str(goat))
    choice = input("You can now change your answer if you'd like. Which door do you choose?")
    if choice == 'end':
        quit()
    else:
        choice = int(choice)
    if choice == car:
        return 1
    else:
        return 0

tally = 0
total = 0
while True:
    if game() == 1:
        tally += 1
        total += 1
        print('You win! You have played ' + str(total) + ' games. You have won ' + str(tally) + ' games!')
    else:
        total += 1
        print('Better luck next time! You have played ' + str(total) + ' games. You have won ' + str(tally) + ' games!')
