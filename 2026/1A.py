import sys
import math

D = sys.stdin.read()
ans = 0
for x in D.split(','):
    x = int(x)
    extra = 0
    while True:
        irt = int(math.sqrt(x+extra))
        if irt*irt == x+extra:
            break
        else:
            extra += 1
    ans += extra
    print(extra)
print(ans)
