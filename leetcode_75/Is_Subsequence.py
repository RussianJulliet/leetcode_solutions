class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for elem_s in s:
            # print('elem_s', elem_s)
            if j == len(t):
                return False
            if elem_s == t[j]:
                j += 1
            else:
                new_str = t[j:]
                # print('new_str', new_str)
                for index in range(len(new_str)):
                    j += 1
                    # print('new_str[index]', new_str[index])
                    if elem_s == new_str[index]:
                        break
                    else:
                        if index == (len(new_str) - 1):
                            # print('new_str[index]', new_str[index])
                            return False
        return True
