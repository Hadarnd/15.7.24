#start


while True:
    star = int(input("enter number:"))
    if star % 2 != 0:
        print("odd number, therefore:")
        break

for i in range(star):

    spaces = " " * (star - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


#end
