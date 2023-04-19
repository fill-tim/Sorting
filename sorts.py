import time


def bubble_sort(mass):
    """
    Сортировка пузырьком
    """
    for i in range(len(mass) - 1):
        for j in range(len(mass) - 1):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]

    return mass


bubble_sort_mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
start = time.perf_counter()
print(bubble_sort(bubble_sort_mass))
print('Время сортировки пузырьком: ', "%0.10f" % (time.perf_counter() - start))


def selection_sort(mass):
    """
    Сортировка выбором
    """
    for i in range(len(mass) - 1):
        small_num_index = i
        for j in range(i + 1, len(mass)):
            if mass[j] < mass[small_num_index]:
                small_num_index = j
        mass[i], mass[small_num_index] = mass[small_num_index], mass[i]

    return mass


selection_sort_mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
start = time.perf_counter()
print(selection_sort(selection_sort_mass))
print('Время сортировки выбором: ', "%0.10f" % (time.perf_counter() - start))


def insertion_sort(mass):
    """
    Сортировка вставками
    """
    for i in range(1, len(mass)):
        j = i - 1
        while j >= 0 and mass[j + 1] < mass[j]:
            mass[j + 1], mass[j] = mass[j], mass[j + 1]
            j -= 1

    return mass


insertion_sort_mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
start = time.perf_counter()
print(insertion_sort(insertion_sort_mass))
print('Время сортировки вставками: ', "%0.10f" % (time.perf_counter() - start))


def quick_sort(mass):
    """
    Быстрая сортировка
    """
    if len(mass) > 1:
        num = mass[0]
        left_mass = [left for left in mass if left < num]
        center_mass = [center for center in mass if center == num]
        right_mass = [right for right in mass if right > num]
        mass = quick_sort(left_mass) + center_mass + quick_sort(right_mass)

    return mass


quick_sort_mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
start = time.perf_counter()
print(quick_sort(quick_sort_mass))
print('Время быстрой сортировки: ', "%0.10f" % (time.perf_counter() - start))


