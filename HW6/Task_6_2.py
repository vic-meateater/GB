def find_multiple(user_range: int):
    range_numbers = range(20, user_range + 1)
    multiple_list = [el for el in range_numbers if el % 20 == 0 or el % 21 == 0]
    return multiple_list


user_input = int(input("Введите макс. длину списка: "))
print('in\n' + str(user_input))
print('out')
print(find_multiple(user_input))