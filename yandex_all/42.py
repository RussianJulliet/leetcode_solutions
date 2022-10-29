class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        maxleft, maxright = [0] * n, [0] * n
        
        for i in range(1, n):
            maxleft[i] = max(maxleft[i-1], height[i-1])
            
        for j in range(n-2, -1, -1):
            maxright[j] = max(maxright[j+1], height[j+1])
            
        for ind in range(n):
            water = min(maxright[ind], maxleft[ind])
            if (water - height[ind]) > 0:
                ans += water - height[ind]
        return ans
