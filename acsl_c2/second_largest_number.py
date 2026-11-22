from typing import List


def sort(array: List[int]) -> List[int]:
    return sorted(array, key=lambda x: -x)


def get_num(array: List[int]) -> List[int]:
    array = sort(array)
    j = len(array) - 1
    while j >= 0:
        if array[j] > array[-1]:
            break
        j -= 1
    if j < 0:
        return -1  # error
    array[j], array[-1] = array[-1], array[j]
    return array


input = [1, 3, 4, 7]
res = get_num(input)
print(f"{input} -> {res}")
