# Я воспользовался нейросейтью
# ChatGPT https://chat.openai.com/auth/login
# для решения данной задачи, ради любопытства.
# Все решение полностью написала "она".
# А еще она может целые классы на разных языках описывать.
# Круто, да? ))

import random


def shuffle_list(lst):
    # Копируем список, чтобы не изменять исходный список
    shuffled = lst[:]

    # Перемешиваем список, меняя местами случайные элементы
    for i in range(len(shuffled)):
        j = random.randint(i, len(shuffled) - 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return shuffled


lst = [1, 2, 3, 4, 5]
shuffled = shuffle_list(lst)
print(shuffled)