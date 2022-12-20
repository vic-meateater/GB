num = int(input("~#: "))
die_summe = 0
list_nums = []

for i in range(1, num + 1):
    result = round((1 + 1 / i) ** i, 3)
    list_nums.append(result)
    die_summe += result

print(list_nums)
print(die_summe)
