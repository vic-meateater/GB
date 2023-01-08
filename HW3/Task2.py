import random


def task_two(user_num):
    list = random.sample(range(1, user_num * 2), user_num)
    list2 = []

    for i in range(len(list)):
        while i < len(list) / 2 < user_num:
            user_num = user_num - 1
            a = list[i] * list[user_num]
            list2.append(a)
            i += 1

    print(list)
    print(list2)


task_two(int(input("Enter number of elements: ")))
