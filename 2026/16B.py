import sys
from collections import defaultdict

def is_contiguous(P):
    return max(P)-min(P)+1 == len(P)

D = sys.stdin.read().strip()
D = D*10
D = list(D)

ans = 0
while True:
    by_color = defaultdict(list)
    for i,c in enumerate(D):
        by_color[c].append(i)
    done = True
    for i,c in enumerate(D):
        if not is_contiguous(by_color[c]):
            i0,i1 = min(by_color[c]), max(by_color[c])+1
            while D[i0]==c:
                i0 += 1
                assert i0<len(D)
            #print(f'{c=} {i0=} {i1=} {by_color[c]=}')
            D[i0:i1] = list(D[i0:i1][::-1])
            ans += i1-i0
            print(f'{i1-i0=} {i0=} {i1=} {D=}')
            done = False
            break
    if done:
        break
print(ans)
