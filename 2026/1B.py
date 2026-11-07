import sys
import math

D = sys.stdin.read()
ans = 0
for x in D.split(','):
    x = int(x)
    extra = 0
    while True:
        # (x+2)^2 - x^2 = x^2+4x+4 - x^2 = 4x+4
        if (x+extra)>=8 and (x+extra)%4==0:
            break
        else:
            extra += 1
    ans += extra
    print(extra)
print(ans)
