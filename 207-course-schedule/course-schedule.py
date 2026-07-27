class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        vis = [False]*numCourses
        pathVis = [False] * numCourses
        stack = []
        def dfs(node):
            vis[node] = True
            pathVis[node] = True
            for neigh in adj[node]:
                if not vis[neigh]:
                    if dfs(neigh):
                        return True
                elif pathVis[neigh]:
                    return True
            pathVis[node] = False
            return False
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False
        return True
                