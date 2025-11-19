import sys
from collections import deque

D = sys.stdin.read()
X = [1]
after = True
for line in D.splitlines():
    start,end = line.strip().split('-')
    xs = list(range(int(start), int(end)+1))
    if after:
        X.extend(xs)
    else:
        X = list(reversed(xs)) + X
    after = not after
print(len(X), X)
i = 0
while X[i] != 1:
    i += 1
print(i)
i = (i+20252025)%len(X)
print(X[i])
