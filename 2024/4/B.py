X = [int(x) for x in open('B.in').read().strip().split('\n')]
ans = 0
m = min(X)
for x in X:
    ans += x-m
print(ans)
