# Реализуйте алгоритм задания случайных чисел без использования встройного генератора певдослучайных чисел.

import time


def my_random(max: int):
    a = time.time()
    tempo = round(a) % max
    return tempo


print(my_random(10))
