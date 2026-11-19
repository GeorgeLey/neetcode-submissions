class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            I am given a 2D grid and I need to find the number of groups of 1s

            run dfs on every node in the grid that is == to one and increment the count

            this version of dfs will explore the node only if we have not seen it and it is not == 0
            
            after the dfs on that node
        """


        count = 0

        directions = [(-1,0), (1,0), (0, 1), (0, -1)]

        def dfs(curr):
            row, col = curr
            if grid[row][col] == "1":
                grid[row][col] = "0"
                for r, c in directions:
                    nr, nc = row + r, col + c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "0":
                        dfs((nr, nc))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs((i, j))
                    count += 1
        
        return count
        