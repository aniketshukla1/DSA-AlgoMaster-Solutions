from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(int)
        for idx in range(len(nums)):
            if nums[idx] in hashmap:
                if abs(idx - hashmap[nums[idx]]) <= k:
                    return True
            hashmap[nums[idx]] = idx
        return False
