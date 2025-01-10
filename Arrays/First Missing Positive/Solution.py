from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for idx in range(len(nums)):
            if nums[idx] < 0:
                nums[idx] = 0

        for idx in range(len(nums)):
            val = abs(nums[idx])
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1)

        for idx in range(1, len(nums)+1):
            if nums[idx - 1] >= 0:
                return idx

        return len(nums) + 1
