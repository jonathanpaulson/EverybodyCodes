import sys
import re

D = sys.stdin.read()
ans = 0
for line in D.splitlines():
    id_, growth, limit = [int(x) for x in re.findall(r'\d+', line)]

    segments = [1]
    branches = 0
    t = 0
    while True:
        t += 1
        #print(f'{t=} {segments=}')
        if 1+branches >= limit:
            ans += t
            break
        new_segments = []
        for x in segments:
            if x==growth-1:
                branches += 1
                new_segments.extend([growth//2,growth//2,1])
            else:
                new_segments.append(x+1)
        segments = new_segments
    #print(id_, growth, limit)
print(ans)

