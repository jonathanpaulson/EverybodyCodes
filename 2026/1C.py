import sys
import math

D = sys.stdin.read()
ans = 0
for x in D.split(','):
    x = int(x)
    extra = 0
    while True:
        irt = math.isqrt(x+extra+1)
        if (x+extra+1)%2==1 and irt*irt == x+extra+1:
            break
        else:
            extra += 1
    ans += extra
    print(extra)
print(ans)
