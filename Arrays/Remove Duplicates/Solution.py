from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_element_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[unique_element_idx]:
                unique_element_idx += 1
                nums[idx], nums[unique_element_idx] = nums[unique_element_idx], nums[idx]
            else:
                continue
        return unique_element_idx + 1
