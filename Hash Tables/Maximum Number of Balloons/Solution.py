from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_hashmap = defaultdict(int)
        balloon_hashmap = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        for char in text:
            if char in "balon":
                char_hashmap[char] += 1
        ratio_map = defaultdict(int)
        for key in balloon_hashmap:
            ratio_map[key] = char_hashmap[key] // balloon_hashmap[key]

        total = float("inf")
        for key in ratio_map:
            total = min(total, ratio_map[key])
        return total
