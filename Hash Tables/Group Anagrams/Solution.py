from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            key = "".join(sorted(list(string)))
            hashmap[key].append(string)
        return list(hashmap.values())
