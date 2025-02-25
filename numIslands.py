#T(N)= O(N)
#S(N)= O(N)

class Solution:
    vi={}
    
    def dfs(self,grid, x, y, co,m,n):
        #Base Case
        
        if x>=0 and x<m and y>=0 and y<n:
            
            if grid[x][y]=="1":
                grid[x][y]="2"
                self.vi[(x,y)]=co
            else:
                return
        else:
            return
        
        
        #Logic
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in dirs:
            a=i[0]+x
            b=i[1]+y
            self.dfs(grid,a,b,co,m,n)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        q=deque()
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    q.append((i,j))
        co=0
        self.vi={}
        
        while q:
            te=q.popleft()
            if grid[te[0]][te[1]]=="1":
                co+=1
                self.dfs(grid,te[0],te[1],co,m,n)
        return co
                
                    
            
        