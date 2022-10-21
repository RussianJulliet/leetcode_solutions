class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sw_p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[sw_p], nums[i] = nums[i], nums[sw_p]
                sw_p += 1
