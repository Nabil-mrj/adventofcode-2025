import sys

def solve(text):
    total = 0
    ranges = text.strip().split(",")

    for r in ranges:
        a, b = map(int, r.split("-"))
        la = len(str(a))
        lb = len(str(b))

        # On ne génère que des nombres de longueur paire
        for L in range(la, lb + 1):
            if L % 2 != 0:
                continue

            k = L // 2
            start = 10 ** (k - 1)
            end = 10 ** k

            for x in range(start, end):
                s = int(str(x) * 2)
                if s < a:
                    continue
                if s > b:
                    break
                total += s

    return total

data = sys.stdin.read()
print(solve(data))
