class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.adj = [None]*numCourses
        for i in range(0, numCourses):
            self.adj[i] = []
        
        for p in prerequisites:
            self.adj[p[0]].append(p[1])
            
        self.visited = [0]*numCourses
        
        for i in range(0, numCourses):
            if self.visited[i] == 0 and not self.dfs(i):
                return False
            
        return True
    
    def dfs(self, v):
        if self.visited[v] == 1:
            return False
        self.visited[v] = 1
        
        for a in self.adj[v]:
            if not self.dfs(a):
                return False
        self.visited[v] = 2
        
        return True