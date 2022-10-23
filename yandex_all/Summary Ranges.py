class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            rangs_array = []
        elif len(nums) == 1:
            rangs_array = [f"{nums[0]}"]
        else:
            rangs_array =[]
            first = nums[0]
            second = nums[0]
            for i in range(1, len(nums)):
                if ((nums[i] - nums[i-1]) == 1):
                    second = nums[i]
                else: 
                    if first != second:
                        rangs_array.append(f"{first}->{second}")
                    else:
                        rangs_array.append(f"{first}")
                    first = nums[i]
                    second = nums[i]
            if first != second:
                rangs_array.append(f"{first}->{second}")
            else:
                rangs_array.append(f"{first}")
        return rangs_array
