import random
def guess(x):
    print(f"Pick a number in your mind between 1 to {x}")
    user=input("Enter ok to start: ")
    while user != "ok":
         user=input("Enter ok to start: ")
    guess = random.randint(1,x)
    i=0
    low = 1
    high = x
    check = 0
    while check != "c":
        i += 1
        check=input(f"Guess={guess}, Enter if high(h) low(l) correct(c): ")
        if check == "h":
            high = guess
            guess = random.randint(low,high)
        elif check == "l":
            low = guess
            guess = random.randint(low,high)
        else:
             print(f"computer guessed the number in {i} guesses")

x = int(input("play guessing game from 1 to: "))
guess(x)
        


