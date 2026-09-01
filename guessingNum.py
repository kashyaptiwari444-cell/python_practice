import random
c=0
print("You have 5 chance only. choose in 1 to 20.")
for i in range(0,5):
    num = int(input("Guess number: "))
    rdm = random.randint(1, 20)
    c+=1
    if rdm > num:
        print("Too Low..")
        print(f"You have {5-c} chance more")
    elif rdm < num:
        print("Too High..")
        print(f"You have {5-c} chance more")
    else:
        print("You are win!!")
        print(f"you win in {c} times")
        break
if c == 5:
    print("you loss.. try again")
    print(f"Gussing number is {rdm}")

