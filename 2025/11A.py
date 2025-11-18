import sys
from collections import deque

D = sys.stdin.read()
XS = [int(x) for x in D.splitlines()]

first = True
t = 0
while True:
    t += 1
    if first:
        found = False
        for i in range(len(XS)):
            if i+1<len(XS) and XS[i+1]<XS[i]:
                XS[i+1] += 1
                XS[i] -= 1
                found = True
        if not found:
            first = False
    if not first:
        for i in range(len(XS)):
            if i+1<len(XS) and XS[i+1]>XS[i]:
                XS[i+1] -= 1
                XS[i] += 1
    if all(x==XS[0] for x in XS):
        print(t)
        break

ans = 0
for i,x in enumerate(XS):
    ans += (i+1)*x
print(ans)


