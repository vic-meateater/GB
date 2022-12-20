num = int(input("~#: "))
sum_dig = 1

for i in range(num):
    sum_dig *= i + 1
    print(sum_dig, end=", ")