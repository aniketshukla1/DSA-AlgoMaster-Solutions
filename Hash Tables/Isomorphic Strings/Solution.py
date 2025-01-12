class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict_s = dict()
        char_dict_t = dict()

        for idx in range(len(s)):
            if (s[idx] in char_dict_s and char_dict_s[s[idx]] != t[idx]) or (t[idx] in char_dict_t and char_dict_t[t[idx]] != s[idx]):
                return False

            char_dict_s[s[idx]] = t[idx]
            char_dict_t[t[idx]] = s[idx]

        return True
