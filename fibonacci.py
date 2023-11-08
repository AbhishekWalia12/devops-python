
num1 = 0
num2 = 1
print(num1, num2)

for n in range(1, 8):
    new_num = num1 + num2
    num1 = num2
    num2 = new_num
    print(new_num)
