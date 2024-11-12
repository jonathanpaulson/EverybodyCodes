D = open('1_2.in').read().strip()
ans = 0
i = 0
while i < len(D):
    c1 = D[i]
    c2 = D[i+1]
    i += 2
    if c1 != 'x' and c2 != 'x':
        ans += 2
    ans += {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}[c1]
    ans += {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}[c2]
print(ans)
