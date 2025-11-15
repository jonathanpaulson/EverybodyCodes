D = open('1.in').read().strip()
ans = 0
for c in D:
    ans += {'A': 0, 'B': 1, 'C': 3}[c]
print(ans)
