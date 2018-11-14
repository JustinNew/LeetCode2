# 200. Number of Islands

# Facebook Tag

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])

        visited = [[0 for i in range(n)] for j in range(m)]

        def dfs(ni, nj):

            visited[ni][nj] = -1
            if ni - 1 >= 0 and grid[ni - 1][nj] == '1' and visited[ni - 1][nj] == 0:
                dfs(ni - 1, nj)
            if ni + 1 < m and grid[ni + 1][nj] == '1' and visited[ni + 1][nj] == 0:
                dfs(ni + 1, nj)
            if nj - 1 >= 0 and grid[ni][nj - 1] == '1' and visited[ni][nj - 1] == 0:
                dfs(ni, nj - 1)
            if nj + 1 < n and grid[ni][nj + 1] == '1' and visited[ni][nj + 1] == 0:
                dfs(ni, nj + 1)

            visited[ni][nj] = 1
            return

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count
