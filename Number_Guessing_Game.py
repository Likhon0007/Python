
import random
s=random.randint(1,100)
attempts=0




while True:
    a=int(input("enter your number :"))
    attempts=attempts+1

    if attempts > 6:
            print(f"Limited Attempts {attempts} Gameover!")
            break
    elif a > s:
        print("Guess a smaller number")
    elif a < s:
        print("Guess a bigger number")

    else:
        print(f"You attempts { attempts} To find the number { s}" )
        break


