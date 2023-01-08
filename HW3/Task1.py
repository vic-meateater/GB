import random


def sum_of_odd_index(user_num):
    list_nums = random.sample(range(1, user_num * 2), user_num)
    print(list_nums)
    summ = 0
    for i in range(0, len(list_nums), 2):
        summ += list_nums[i]
    return summ


print(sum_of_odd_index(int(input("Enter number of elements: "))))
