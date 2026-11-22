nums = [7, 4, 5, 1, 2, 3, 8, 6, 2]


def sort_nums(nums):
    """
    nums is a list of integers
    change it so that it is sorted from smallest to biggest
    """
    for i in range(len(nums)):
        # find the position of the smallest number starting
        # at position i
        current_num = nums[i]
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < current_num:
                # j is the position of the smallest number
                # we have seen after i
                smallest_idx = j
                current_num = nums[j]
        if smallest_idx != i:
            # swap nums[i] and nums[smallest_idx]
            x = nums[i]
            nums[i] = nums[smallest_idx]
            nums[smallest_idx] = x
        print(f"smallest_idx = {smallest_idx} nums = {nums}")
    return nums


new_list = sort_nums(nums)
print(f"{nums} --> {sort_nums}")
