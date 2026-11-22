from typing import List


def maxArea(height: List[int]) -> int:
    if not height:
        return 0
    left = 0
    right = len(height) - 1
    max_vol = 0
    while left < right:
        cvol = (right - left) * min(height[left], height[right])
        print(f"{left} to {right} cvol = {cvol}")
        if cvol > max_vol:
            max_vol = cvol
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_vol


height = [1, 10, 6, 2, 11, 4, 8, 3, 7]
expected = 49
output = maxArea(height)
print(f"{output} vs {expected}")

height = [1, 1]
expected = 1
output = maxArea(height)
print(f"{output} vs {expected}")
