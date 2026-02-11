import sys

def solve(text):
    total = 0

    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue

        best = 0
        n = len(s)

        # Teste toutes les paires (i < j) pour former le plus grand nombre à 2 chiffres
        for i in range(n - 1):
            for j in range(i + 1, n):
                v = (ord(s[i]) - 48) * 10 + (ord(s[j]) - 48)
                if v > best:
                    best = v

        total += best

    return total

data = sys.stdin.read()
print(solve(data))
