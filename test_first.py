from sorts import quick_sort, bubble_sort, selection_sort, insertion_sort

mass = [1, 13, 6, 9, 8, 0, 123, 2, 3, 235, 6, 234, -2, 32423, 87, 43, 12, 213, 123, 1231]
result = [-2, 0, 1, 2, 3, 6, 6, 8, 9, 12, 13, 43, 87, 123, 123, 213, 234, 235, 1231, 32423]


def test_quick_sort():
    assert quick_sort(mass) == result


def test_bubble_sort():
    assert bubble_sort(mass) == result


def test_selection_sort():
    assert selection_sort(mass) == result


def test_insertion_sort():
    assert insertion_sort(mass) == result
