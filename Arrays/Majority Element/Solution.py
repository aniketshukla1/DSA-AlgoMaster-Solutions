from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = 1
        majority_element = nums[0]

        for num in nums[1:]:
            if num == majority_element:
                majority_count += 1
            else:
                if majority_count <= 0:
                    majority_count = 1
                    majority_element = num
                else:
                    majority_count -= 1
        return majority_element
