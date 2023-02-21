import random

def gameWin(comp, you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        if you=="g":
            return True
    elif comp=="w":
        if you=="s":
            return True
        if you=="g":
            return False
    elif comp=="g":
        if you=="w":
            return True
        if you=="s":
            return False

randNo=random.randint(1,3)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

print("Comp: snake(s), water(w) or Gun(g)?")
you=input("You: snake(s), water(w) or Gun(g)?")
print(f"Computer chose {comp}")
a = gameWin(comp, you)
if a == None:
    print("The game is a tie")
elif a == True:
    print("You Win !")
else:
    print("Computer Win !")



        
