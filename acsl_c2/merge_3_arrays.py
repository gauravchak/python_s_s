from typing import List


def merge3(arr1, arr2, arr3) -> List[int]:
    i = 0
    j = 0
    k = 0
    retval = []
    while (i < len(arr1)) or (j < len(arr2)) or (k < len(arr3)):
        idx = -1
        cmin = 0
        if i < len(arr1):
            cmin = arr1[i]
            idx = 1
        if (j < len(arr2)) and ((idx < 1) or (arr2[j] < cmin)):
            cmin = arr2[j]
            idx = 2
        if (k < len(arr3)) and ((idx < 1) or (arr3[k] < cmin)):
            cmin = arr3[k]
            idx = 3
        if idx == 1:
            retval.append(arr1[i])
            i += 1
        elif idx == 2:
            retval.append(arr2[j])
            j += 1
        else:
            retval.append(arr3[k])
            k += 1
    return retval


# arr1 = [1, 4, 7]
# arr2 = [2, 5, 8]
# arr3 = [3, 6, 9]
arr1 = [-100, -10, -1, -1, 0, 0, 0, 1, 1, 5]
arr2 = [-90, -2, 0, 0, 0, 3, 5, 5]
arr3 = [-20, -1, 0, 0, 1, 4, 4]
res = merge3(arr1, arr2, arr3)
print(res)
