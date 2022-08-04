"""283: move zeroes"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    zero_p = 0
    current_p = 0

    while current_p < len(nums):
        if nums[current_p]:
            if nums[zero_p] == 0:
                nums[zero_p] = nums[current_p]
                nums[current_p] = 0
                zero_p += 1
            else:
                zero_p += 1
        current_p += 1

