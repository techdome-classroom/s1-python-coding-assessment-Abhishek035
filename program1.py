class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
    
        if not grid or not grid[0]:
                return 0

        def dfs(r, c):
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 'L':
                        return

                grid[r][c] = 'W'

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

        island_count = 0

        for r in range(len(grid)):
                for c in range(len(grid[0])):
                        if grid[r][c] == 'L':
                        island_count += 1
                        dfs(r, c)

        return island_count
