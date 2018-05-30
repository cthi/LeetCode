class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = [0 for i in range(len(grid))]
        left = [0 for i in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                top[i] = max(top[i], grid[i][j])
                left[j] = max(left[j], grid[i][j])

        return sum(
            min(top[i], left[j]) - grid[i][j]
            for i in range(len(grid))
            for j in range(len(grid[0]))
        )
