import sys

def solve(text):
    grid = [list(line.rstrip("\n")) for line in text.splitlines() if line.strip()]
    h = len(grid)
    w = len(grid[0]) if h else 0

    total = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != "@":
                continue

            cnt = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
                        cnt += 1

            # Accessible si moins de 4 voisins '@'
            if cnt < 4:
                total += 1

    return total

data = sys.stdin.read()
print(solve(data))
