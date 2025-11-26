import sys
import heapq
from collections import deque
from copy import deepcopy

D = sys.stdin.read()

X = [int(x) for x in D.split(',')]

ANS = set()
for i,x in enumerate(X):
    for j in range(i):
        if (i+1)%(j+1)==0 and j+1 in ANS:
            x -= 1
    if x>0:
        assert x==1
        ANS.add(i+1)
print(sorted(ANS))

blocks = 202520252025000
lo = 0
hi = 10**30
while lo<hi:
    m = (lo+hi+1)//2
    required = 0
    for x in ANS:
        required += (m//x)
    if required<=blocks:
        lo = m
    else:
        hi = m-1
print(lo)
