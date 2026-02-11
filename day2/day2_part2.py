import sys

def ceil_div(a, b):
    return -(-a // b)

def sum_arith(lo, hi):
    if lo > hi:
        return 0
    n = hi - lo + 1
    return (lo + hi) * n // 2

def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return sorted(ds)

def mobius(n):
    # μ(n): 0 si carré divise n, sinon (-1)^(nb de facteurs premiers distincts)
    x = n
    p = 2
    cnt = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            cnt += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        cnt += 1
    return -1 if (cnt % 2 == 1) else 1

def rep_factor(block_len, reps):
    # 1 + 10^block_len + 10^(2*block_len) + ... (reps termes)
    f = 0
    step = 10 ** block_len
    p = 1
    for _ in range(reps):
        f += p
        p *= step
    return f

def sum_primitive_len(d, lo, hi):
    # Somme des entiers à d chiffres dont la période minimale est exactement d, dans [lo,hi]
    lo = max(lo, 10 ** (d - 1))
    hi = min(hi, 10 ** d - 1)
    if lo > hi:
        return 0

    total = 0
    for t in divisors(d):  # t = longueur de période
        reps = d // t
        mu = mobius(reps)
        if mu == 0:
            continue

        f = rep_factor(t, reps)  # x = y * f
        ylo = ceil_div(lo, f)
        yhi = hi // f

        ylo = max(ylo, 10 ** (t - 1))
        yhi = min(yhi, 10 ** t - 1)
        if ylo > yhi:
            continue

        total += mu * f * sum_arith(ylo, yhi)

    return total

def solve(text):
    text = text.strip()
    if not text:
        return 0

    total = 0
    ranges = [r for r in text.split(",") if r]

    for r in ranges:
        a, b = map(int, r.split("-"))
        la, lb = len(str(a)), len(str(b))

        for L in range(la, lb + 1):
            A = max(a, 10 ** (L - 1))
            B = min(b, 10 ** L - 1)
            if A > B:
                continue

            for p in divisors(L):
                if p == L:
                    continue  # au moins 2 répétitions
                reps = L // p
                f = rep_factor(p, reps)  # N = block * f

                blo = ceil_div(A, f)
                bhi = B // f
                if blo > bhi:
                    continue

                sblocks = sum_primitive_len(p, blo, bhi)
                total += f * sblocks

    return total

data = sys.stdin.read()
print(solve(data))
