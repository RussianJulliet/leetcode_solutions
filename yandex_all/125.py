class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for elem in s:
            if elem.isalnum():
                new_s += elem
        i = 0
        j = len(new_s) - 1
        # print(new_s)
        for i in range(len(new_s) // 2):
            # print(new_s[i])
            # print(new_s[j])
            if new_s[i] == new_s[j]:
                j -= 1
            else: 
                return False
        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
