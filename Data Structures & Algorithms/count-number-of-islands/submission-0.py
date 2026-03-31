class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set() # (r, c)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc) not in visited and grid[nr][nc] == '1':
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    visited.add((r, c))
                    bfs(r, c)
        return res