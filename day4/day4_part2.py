import sys
from collections import deque

def solve(text):
    grid = [list(line.rstrip("\n")) for line in text.splitlines() if line.strip()]
    h = len(grid)
    w = len(grid[0]) if h else 0

    dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if not (dr == 0 and dc == 0)]

    def adj_count(r, c):
        # Nombre de '@' adjacents
        cnt = 0
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
                cnt += 1
        return cnt

    q = deque()
    inq = [[False] * w for _ in range(h)]

    # Tous les @ en file
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@":
                q.append((r, c))
                inq[r][c] = True

    removed = 0

    while q:
        r, c = q.popleft()
        inq[r][c] = False

        if grid[r][c] != "@":
            continue

        # Retrait si < 4 voisins
        if adj_count(r, c) < 4:
            grid[r][c] = "."
            removed += 1

            for dr, dc in dirs:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
                    if not inq[rr][cc]:
                        q.append((rr, cc))
                        inq[rr][cc] = True

    return removed

data = sys.stdin.read()
print(solve(data))
