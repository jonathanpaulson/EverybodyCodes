import sys
from collections import deque

D = sys.stdin.read()
X = [1]
after = True
for line in D.splitlines():
    x = int(line.strip())
    if after:
        X.append(x)
    else:
        X = [x] + X
    after = not after
i = 0
while X[i] != 1:
    i += 1
i = (i+2025)%len(X)
print(X[i])
