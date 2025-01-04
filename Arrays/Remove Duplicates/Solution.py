from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_idx = 0
        for idx in range(1, len(nums)):
            if nums[unique_idx] != nums[idx]:
                unique_idx += 1
                nums[unique_idx] = nums[idx]
        return unique_idx + 1
