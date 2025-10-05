"""Harder example to use pdb for debugging."""

print("Yay, we're starting!")


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists (ascending) into a single sorted list.
    The resulting list should have all the elements of both lists and be sorted
    in ascending order.
    """
    i, j = 0, 0  # i for list1, j for list2
    merged = []

    while (i < len(list1)) and (j < len(list2)):
        # i = 4, j = 2
        # list1[4] does not exit.
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i = i + 1
        else:
            merged.append(list2[j])
            j = j + 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


if __name__ == "__main__":
    list_a = [1, 3, 4, 5]
    list_b = [2, 6, 8, 10, 12, 16]

    result = merge_sorted_lists(list_a, list_b)
    print("Merged list:", result)
