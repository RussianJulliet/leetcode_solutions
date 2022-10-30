class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        def dfc_islends(i, j):
            if (i < 0) or (j < 0) or (i == m) or (j == n) or (grid[i][j] == "0"):
                return
            grid[i][j] = "0"
            dfc_islends(i+1, j)
            dfc_islends(i-1, j)
            dfc_islends(i, j+1)
            dfc_islends(i, j-1)
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfc_islends(i, j)
        return count
