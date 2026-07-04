class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[]for _ in range(n+1)]

        for u , v , w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))

        vis = [False]*(n+1)
        q = [1]
        vis[1] = True
        front = 0 
        ans = float('inf')
        while front < len(q):
            node = q[front]
            front += 1

            for nei , wt in adj[node]:
                ans = min(wt, ans)

                if not vis[nei]:
                    vis[nei] = True
                    q.append(nei)
        return ans