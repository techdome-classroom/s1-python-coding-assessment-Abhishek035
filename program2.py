def decode_message( s: str, p: str) -> bool:

        if not grid or not grid[0]:
                return 0

        def dfs(r, c):
        # If out of bounds or at water, return
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 'L':
                        return
        # Mark the current cell as visited
                grid[r][c] = 'W'

        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

        island_count = 0

        for r in range(len(grid)):
                for c in range(len(grid[0])):
                        if grid[r][c] == 'L':  # Found a new island
                        island_count += 1
                        dfs(r, c)  # Mark all connected land as visited

        return island_count


  
        return False