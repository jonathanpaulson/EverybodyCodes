X = [int(x) for x in open('A.in').read().strip().split('\n')]
ans = 0
m = min(X)
for x in X:
    ans += x-m
print(ans)
