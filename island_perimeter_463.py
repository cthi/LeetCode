class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        M = len(grid[0])
        perimeter = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    if i + 1 > N - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    if j + 1 > M - 1 or grid[i][j + 1] == 0:
                        perimeter += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        perimeter += 1

        return perimeter
