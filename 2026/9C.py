import sys
import re
from functools import cache

sys.setrecursionlimit(10**6)
#print(sys.getrecursionlimit())

# how many branches does X split into after T seconds?
@cache
def f(x, t, growth):
    if t<=0:
        return 0
    dt = growth-x
    if t<dt:
        return 0
    return 1 + 2*f(growth//2, t-dt, growth) + f(1,t-dt, growth)

def slowF(x, t, growth):
    segments = [1]
    branches = 0
    for _ in range(t):
        new_segments = []
        for x in segments:
            if x==growth-1:
                branches += 1
                new_segments.extend([growth//2,growth//2,1])
            else:
                new_segments.append(x+1)
        segments = new_segments
    return branches


D = sys.stdin.read()
ans = 0
for line in D.splitlines():
    id_, growth, limit = [int(x) for x in re.findall(r'\d+', line)]

    lo = 0
    hi = 1
    while f(1,hi,growth)+1 < limit:
        hi *= 2
    while lo < hi:
        mid = (lo+hi)//2
        #assert f(1,mid,growth) == slowF(1,mid,growth)
        #print(f'{mid=}')
        if f(1,mid,growth)+1 >= limit:
            hi = mid
        else:
            lo = mid+1
    assert lo==hi
    ans += lo+1
    #print(id_, growth, limit, ans)
print(f.cache_info())
print(ans)

