# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
from typing import List

class Solution():
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        current_sum = 0
        for i, elem in enumerate(nums):
            if current_sum == (total - current_sum - elem):
                return i
            current_sum += elem
        return -1

# nums = list(map(int, input().split()))
nums = [1, 7, 3, 6, 5, 6]
sol = Solution()
print(sol.pivotIndex(nums))
