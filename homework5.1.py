#start
numbers: list = []
pos_numbers: list = []
neg_numbers: list = []

pos_num = 0
neg_num = 0
zero_num = 0
seven_num = 0

num = 0
count = 0

for i in range(10):
    num = int(input("please enter 10 number:"))
    numbers.append(num)
    if num == -9999:
        break
    elif 1000 < num < -1000:
        continue
    if num < 0:
        neg_num += 1
        neg_numbers.append(num)
    elif num > 0:
        pos_num += 1
        pos_numbers.append(num)
    elif num == 0:
        zero_num += 1
    elif num % 7 == 0:
        seven_num += 1

print(f"the numbers you entered: {numbers}")
print(f"Total positive numbers are: {pos_num}")
print(f"Total negative numbers are: {neg_num}")
print(f"Total seven numbers are: {seven_num}")
print(f"Total zero numbers are: {zero_num}")
print(f"The last positive number is: {pos_numbers[-1]}")
print(f"The last negative number is: {neg_numbers[-1]}")



