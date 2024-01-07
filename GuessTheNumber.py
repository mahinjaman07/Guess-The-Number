import random

randomNumber = random.randrange(100);

userGues = int(input("Guess the number out of 100 :"))
if randomNumber > userGues:
    print("Your Gues The Number Is To Low");
    print(f"Correct Number is {randomNumber}")
elif randomNumber < userGues:
    print("Your Gues The Number Is So High");
    print(f"Correct Number is {randomNumber}")

else:
    print("Congratulations..! You Gues The Correct Number");