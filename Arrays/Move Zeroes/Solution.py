from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_element = 0
        for idx, _ in enumerate(len(nums)):
            if nums[idx] != 0:
                nums[non_zero_element] = nums[idx]
                non_zero_element += 1

        for i in range(non_zero_element, len(nums)):
            nums[i] = 0
