def unique_sequence(list_in: list):
    print(list_in)
    list_out = []
    for i in list_in:
        if i not in list_out:
            list_out.append(i)
    return list_out


user_list = [2, 5, 8, 9, 8, 5, 11]
print(unique_sequence(user_list))
