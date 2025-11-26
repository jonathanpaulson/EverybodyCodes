import sys
import heapq
from collections import deque
from copy import deepcopy

D = sys.stdin.read()

X = [int(x) for x in D.split(',')]

ANS = []
ans = 1
for i,x in enumerate(X):
    for j in range(i):
        if (i+1)%(j+1)==0:
            x -= ANS[j]
    if x>0:
        assert x==1
        ans *= (i+1)
    ANS.append(x)
print(ans)
