#start

import random
count = 0
yes = 0
no = 0
for i in range(1):
    rnd: int = random.randint(1, 101)
    print("The random number is:", end=" ")
    print(rnd, end=" ")
    print()

while True:
    num: int = int(input("Welcome to a loto game please choose a number:"))

    count += 1
    if num > rnd:
        print(f"number is too big")
    if num < rnd:
        print(f"number is too small")
    if num == rnd:
        print(f"BINGO!!")
        print(f"Numbers of tring:{count}")
        choice = input(f"Would you like to continue the game? (yes/no){yes} {no}")
        if choice.casefold() == no:
            break

        count += 1
        break

#end
