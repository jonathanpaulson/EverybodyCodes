import sys
from collections import deque

D = sys.stdin.read()
X = [(1,1,1)]
after = True
total_sz = 1
for line in D.splitlines():
    start,end = line.strip().split('-')
    start,end = int(start),int(end)
    sz = end-start+1
    if after:
        X.append((start,end,sz))
    else:
        X = [(end,start,sz)] + X
    after = not after
    total_sz += sz

i = 0
while X[i] != (1,1,1):
    i += 1
amt = 202520252025
amt = amt % total_sz
#print(f'{amt=} {i=} {X=} {total_sz=}')
while amt >= 0:
    start,end,sz = X[i]
    #print(f'{amt=} {start=} {end=} {sz=} {i=}')
    if amt >= sz:
        amt -= sz
        i = (i+1)%len(X)
    else:
        if start<end:
            xi_list = list(range(start, end+1))
        else:
            xi_list = list(reversed(range(end, start+1)))
        assert len(xi_list) == sz, f'{len(xi_list)=} {sz=} {start=} {end=}'
        assert amt < sz
        print(xi_list[amt])
        break
