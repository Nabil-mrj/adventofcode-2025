import sys

def solve(text):
    total = 0

    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue

        k = 12
        stack = []
        drop = len(s) - k  # combien on peut supprimer

        for ch in s:
            while drop > 0 and stack and stack[-1] < ch:
                stack.pop()
                drop -= 1
            stack.append(ch)

        if drop > 0:
            stack = stack[:-drop]

        best = int("".join(stack[:k]))
        total += best

    return total

data = sys.stdin.read()
print(solve(data))
