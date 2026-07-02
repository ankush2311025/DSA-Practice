class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m , n = len(grid), len(grid[0])
        start_hl = health - grid[0][0]
        if start_hl <= 0:
            return False
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[-1]*n for _ in range(m)]
        visited[0][0] = start_hl

        q = []
        q.append((0,0, start_hl))
        front = 0

        while front < len(q):
            r , c , curr_hl = q[front]
            front += 1

            if r == m-1 and c == n-1:
                return True

            for dr , dc in direc:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n :
                    new_hl = curr_hl - grid[nr][nc]

                    if new_hl <= 0 :
                        continue
                    if new_hl > visited[nr][nc]:
                        visited[nr][nc] = new_hl
                        q.append((nr, nc, new_hl))
        return False