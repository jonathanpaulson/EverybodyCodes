import sys
import heapq
from collections import deque
from copy import deepcopy

D = sys.stdin.read()

X = [int(x) for x in D.split(',')]
ans = 0
for x in X:
    ans += 90//x
print(ans)
