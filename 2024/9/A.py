import sys
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
D = open(infile).read().strip()

DP = {}
def f(n):
    if n < 0:
        return 10**9
    if n==0:
        return 0
    if n in DP:
        return DP[n]
    O = [1, 3, 5, 10]
    ans = 10**9
    for o in O:
        ans = min(ans, 1 + f(n-o))
    DP[n] = ans
    return ans

ans = 0
for line in D.split('\n'):
    x = int(line.strip())
    ans += f(x)
print(ans)
