# start

movies: list[str] = ['vanilla_sky',"top_gun","scream"]
movies.append("click")
movies.insert(0, 'armagedon')
print(movies)
print(len(movies))

import random

numbers: list[int] = []

for i in range(10):
    rnd: int = random.randint(1, 100)
    numbers.append(rnd)
print(numbers, end="")


import random

bools: list[bool] = []

for i in range(10):
    rnd = random.choice([False, True])
    bools.append(rnd)
print(bools, end="")

#end