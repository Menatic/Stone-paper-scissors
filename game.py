import random
P = input("What's your choice ? - Stone, Paper, Scissors.")
choices = ["Stone", "Paper", "Scissors"]
C = random.choice(choices)
print(f"\nP chose {P}, C chose {C}.\n")
if (P == C):
    print("No one wins")
elif (P == "Stone"):
    if (C == "Scissors"):
        print("P is the winner")
    else:
        print("C is the winner")
elif (P == "Paper"):
    if (C == "Stone"):
        print("P is the winner")
    else:
        print("C is the winner")
elif (P == "Scissors"):
    if (C == "Paper"):
        print("P is the winner")
    else:
        print("C is the winner")