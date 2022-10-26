class Solution:
    def subarraySum(self, nums, k: int) -> int:
        n = len(nums)
        j = cs = count = 0
        for i in range(n):
            print(i, j, cs, count)
            print('cs', cs)
            print('nums[i]', nums[i])
            cs = cs + nums[i]
            print('cs', cs)
            while (abs(cs) > k) & (i > j):
                cs = cs - nums[j]
                j += 1
            if cs == k:
                count += 1
        return count

sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))
