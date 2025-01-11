from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        good_pairs = 0
        for key in hashmap:
            if hashmap[key] > 1:
                good_pairs += (hashmap[key] * (hashmap[key]-1)) // 2
        return good_pairs
