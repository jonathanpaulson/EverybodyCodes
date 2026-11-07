import sys
from functools import cmp_to_key

D = sys.stdin.read()
ans = 0
for line in D.splitlines():
    V = set()
    LT = set()
    for cmp in line.split():
        if '<' in cmp:
            a,b = cmp.split('<')
            V.add(a)
            V.add(b)
            LT.add((a,b))
        else:
            a,b = cmp.split('>')
            V.add(a)
            V.add(b)
            LT.add((b,a))

    def compare(a,b):
        if (a,b) in LT:
            return 1
        elif a==b:
            return 0
        else:
            return -1

    V = sorted(V, key=cmp_to_key(compare))
    score = int(''.join(V))
    ans += score
print(ans)
