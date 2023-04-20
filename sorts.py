import random
import time

new_mass = [random.randint(0, 100000) for _ in range(10)]
mass1 = new_mass
mass2 = new_mass
mass3 = new_mass
mass4 = new_mass
mass5 = new_mass


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
print(bubble_sort(new_mass))
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
print(selection_sort(mass1))
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
print(insertion_sort(mass2))
print('Время сортировки вставками: ', "%0.10f" % (time.perf_counter() - start))


def quick_sort(array):
    """
    Быстрая сортировка
    """
    if len(array) > 1:
        pivot = array.pop()
        right, equal_lst, left = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                right.append(item)
            else:
                left.append(item)
        return quick_sort(left) + equal_lst + quick_sort(right)
    else:
        return array


quick_sort_mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
start = time.perf_counter()
print(quick_sort(mass3))
print('Время быстрой сортировки: ', "%0.10f" % (time.perf_counter() - start))


def merge_sort(mass):
    """
    Сортировка слиянием
    """
    if len(mass) < 2:
        return mass[:]
    else:
        middle = int(len(mass) / 2)
        left = merge_sort(mass[:middle])
        right = merge_sort(mass[middle:])
        return merge(left, right)


def merge(left, right):
    """
    Сортировка и слияние в один массив
    """
    mass = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mass.append(left[i])
            i += 1
        else:
            mass.append(right[j])
            j += 1
    while i < len(left):
        mass.append(left[i])
        i += 1
    while j < len(right):
        mass.append(right[j])
        j += 1
    return mass


merge_sort_mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
start = time.perf_counter()
print(merge_sort(mass4))
print('Время сортировки слиянием: ', "%0.10f" % (time.perf_counter() - start))


def shell_sort(mass):
    """
    Сортировка Шелла
    """
    n = len(mass)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = mass[i]
            j = i
            while j >= interval and mass[j - interval] > temp:
                mass[j] = mass[j - interval]
                j -= interval
            mass[j] = temp
        interval //= 2
    return mass


start = time.perf_counter()
print(shell_sort(mass5))
print('Время сортировки слиянием: ', "%0.10f" % (time.perf_counter() - start))
