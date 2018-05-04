class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        def flood_fill(x, y, N, M, seen, grid):
            if x < 0 or y < 0 or x > N - 1 or y > M - 1 or seen[x][y]:
                return 0

            seen[x][y] = True
            
            if grid[x][y] == 1:
                size = 1
                
                for i, j in dirs:
                    size += flood_fill(x + i, y + j, N, M, seen, grid)
          
                return size
            else:
                return 0
                            
        N = len(grid)
        M = len(grid[0])
        seen = [[False for j in range(M)] for i in range(N)]
        
        return max(flood_fill(x, y, N, M, seen, grid) for x in range(N) for  y in range(M))
