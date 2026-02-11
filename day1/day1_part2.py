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

        # Comptage des passages par 0 pendant la rotation
        if direction == "R":
            # (pos + k) % 100 == 0
            k0 = (-pos) % 100
        elif direction == "L":
            # (pos - k) % 100 == 0
            k0 = pos % 100
        else:
            continue

        # k = 0 correspond à "aucun click", on l'ignore
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
