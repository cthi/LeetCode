class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
            
        islands = 0
        
        N = len(grid)
        M = len(grid[0])
        seen = [[False for i in range(M)] for j in range(N)]
        
        for i in range(N):
            for j in range(M):
                if not seen[i][j] and grid[i][j] == '1':
                    islands += 1
                    self.flood(i + 1, j, N, M, grid, seen)
                    self.flood(i - 1, j, N, M, grid, seen)
                    self.flood(i, j + 1, N, M, grid, seen)
                    self.flood(i, j - 1, N, M, grid, seen)
                    
        return islands
        
    def flood(self, i, j, N, M, grid, seen):
        if i < 0 or i >= N:
            return
        if j < 0 or j >= M:
            return
        
        if grid[i][j] == '0':
            return
        
        if seen[i][j]:
            return
        
        seen[i][j] = True
        
        self.flood(i + 1, j, N, M, grid, seen)
        self.flood(i - 1, j, N, M, grid, seen)
        self.flood(i, j + 1, N, M, grid, seen)
        self.flood(i, j - 1, N, M, grid, seen)
        
