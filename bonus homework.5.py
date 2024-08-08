#Bonus:
#start
import random

len: int = 0
new_word = " "
len = random.randint(5, 20)
print(f"The length of our word is: {len}")

for i in range(1,len+1):
    letters = random.choice(["a","b","c"])
    new_word = new_word + letters

print(f"Therefore:{new_word}",end=" ")
print("")



#end