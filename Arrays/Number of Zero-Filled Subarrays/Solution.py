from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarray_zeros = total_subarray_zeros = 0

        for num in nums:
            if num == 0:
                subarray_zeros += 1
                total_subarray_zeros += subarray_zeros
            else:
                subarray_zeros = 0
        return total_subarray_zeros
