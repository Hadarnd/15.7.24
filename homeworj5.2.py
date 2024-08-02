#start

sum = 0
sum: int = int(input("numnber:"))

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
    if num == rnd:
        print(f"BINGO!!")
        break

    if num > rnd:
        print(f"number is too big")
    if num < rnd:
        print(f"number is too small")

    print(f"Numbers of tring:{count}")
    choice = input("Would you like to continue the game? (yes/ no):")
    if choice.casefold() == no:
        break










#end    if not i % 7:
        continue
    sum += 1
    print(i);

print(sum)




#end
