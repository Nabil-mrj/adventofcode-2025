import sys

def solve(text):
    # Position initiale 
    pos = 50
    hits = 0

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        n = int(line[1:])

        if direction == "R":
            # On cherche k tel que (pos + k) % 100 == 0
            k0 = (-pos) % 100
        elif direction == "L":
            # On cherche k tel que (pos - k) % 100 == 0
            k0 = pos % 100
        else:
            continue

        if k0 == 0:
            k0 = 100

        if k0 <= n:
            hits += 1 + (n - k0) // 100

        # Position finale 
        if direction == "R":
            pos = (pos + n) % 100
        elif direction == "L":
            pos = (pos - n) % 100

    return hits

data = sys.stdin.read()
print(solve(data))
