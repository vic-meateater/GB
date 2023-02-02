def find_biggest_prev_elem(list_nums: list):
    result = [list_nums[i] for i in range(1, len(list_nums)) if list_nums[i] > list_nums[i - 1]]
    return result


user_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
print('in\n' + str(len(user_list)))
print('out')
print(user_list)
print(find_biggest_prev_elem(user_list))
