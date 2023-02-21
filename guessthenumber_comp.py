import random
def guess(x):
    num = random.randint(1,x)
    guess = 0
    while guess != num:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess < num:
            print("Sorry, guessed to low")
        elif guess > num:
            print("sorry, guessed too high")
    print("Yey...congratulations you guessed the number correct \n ###Rahulcodes###")
x=int(input("guess number from 1 to :"))
guess(x)

