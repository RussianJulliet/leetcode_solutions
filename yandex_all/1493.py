# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == sum(nums):
            return len(nums) - 1
        else:
            df = [[0] * len(nums), [0] * len(nums)]
            for i, elem in enumerate(nums):
                if i == 0:
                    if nums[0] == 0:
                        df[0][0] = 0
                        df[1][0] = 0
                    else:
                        df[0][0] = 1
                        df[1][0] = 1   
                else:
                    if elem == 1:
                        df[0][i] = df[0][i-1] + 1
                        df[1][i] = df[1][i-1] + 1
                    else:
                        df[0][i] = 0
                        df[1][i] = df[0][i-1]
            # print(nums)
            # print(df[0])
            # print(df[1])
            answer = max(df[1])
            return answer


sol = Solution()
print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))
