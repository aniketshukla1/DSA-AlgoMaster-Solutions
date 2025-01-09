from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = nums[0]
        prefix = [1, prefix_product]
        for num in nums[1:-1]:
            prefix_product *= num
            prefix.append(prefix_product)

        suffix_product = 1
        product = []
        for idx in range(len(nums)-1, -1, -1):
            product.append(suffix_product * prefix[idx])
            suffix_product *= nums[idx]

        return product[::-1]
