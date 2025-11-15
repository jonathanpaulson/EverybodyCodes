import sys

D = sys.stdin.read()

xs = [int(x) for x in D.split(',')]
print(xs, len(xs))

ans = 0
for i in range(len(xs)-1):
    x,y = xs[i], xs[i+1]
    if abs(x-y)==16:
        ans += 1
    print(i,x,y, ans)
print(ans)
