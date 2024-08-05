
#start

floors = int(input("enter number:"))

for i in range(1, floors + 1):
    print(" " * (floors -i), end=" ")
    print("*" * (i * 2 - 1))

#end