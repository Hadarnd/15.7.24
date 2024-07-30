#start

sum = 0
sum: int = int(input("numnber:"))

for i in range(1,101):
    if not i % 7:
        continue
    sum += 1
    print(i);

print(sum)




#end