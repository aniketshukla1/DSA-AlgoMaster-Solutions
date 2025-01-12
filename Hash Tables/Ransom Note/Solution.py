from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars_dict = defaultdict(int)

        for char in magazine:
            chars_dict[char] += 1

        for char in ransomNote:
            chars_dict[char] -= 1
            if chars_dict[char] < 0:
                return False
        return True
