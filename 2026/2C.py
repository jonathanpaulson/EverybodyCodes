import sys
from functools import cmp_to_key

D = sys.stdin.read()
ans = 0
for line in D.splitlines():
    V = set()
    LT = set()
    GT = set()
    for cmp in line.split():
        if '<' in cmp:
            a,b = cmp.split('<')
            V.add(a)
            V.add(b)
            LT.add((a,b))
            GT.add((b,a))
        else:
            a,b = cmp.split('>')
            V.add(a)
            V.add(b)
            LT.add((b,a))
            GT.add((a,b))

    for k in V:
        for a in V:
            for b in V:
                if (a,k) in LT and (k,b) in LT:
                    LT.add((a,b))
                if (a,k) in GT and (k,b) in GT:
                    GT.add((a,b))

    def compare(a,b):
        if (a,b) in LT:
            return 1
        elif a==b:
            return 0
        elif (a,b) in GT:
            return -1
        else:
            assert False, f'{a=} {b=}'

    V = sorted(V, key=cmp_to_key(compare))
    score = int(''.join(V))
    ans += score
print(ans)
