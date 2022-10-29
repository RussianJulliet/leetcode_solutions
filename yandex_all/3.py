class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_letter = {}
        start, end, max_len = 0, 0, 0
        for i, elem in enumerate(s):
            if (elem not in dict_letter.keys()) or (dict_letter[elem] == 0):
                dict_letter[elem] = 1
                end += 1
            elif s[start] == elem:
                end += 1
                start += 1
            else:
                end += 1
                while s[start] != elem:
                    dict_letter[s[start]] = 0
                    start += 1
                start += 1
            max_len = max(end - start, max_len)
        return max_len
