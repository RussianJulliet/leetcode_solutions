class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        s1_dict = {}
        for letter in range(l1):
            s1_dict[s1[letter]] = s1_dict.get(s1[letter], 1) + 1
            # if s1[letter] in s1_dict.keys():
            #     s1_dict[s1[letter]] += 1
            # else:
            #     s1_dict[s1[letter]] = 1
                
        for i in range(l2 - l1 + 1):
            start, end = i, i + l1
            curr_dict = {}
            for j in range(start, end):
                curr_dict[s2[j]] = curr_dict.get(s2[j], 1) + 1
            #     if s2[j] in curr_dict.keys():
            #         curr_dict[s2[j]] += 1
            #     else:
            #         curr_dict[s2[j]] = 1
            if curr_dict == s1_dict:
                return True
        return False
