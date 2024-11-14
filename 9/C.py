import sys
sys.setrecursionlimit(10**7)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
D = open(infile).read().strip()

# F[N] is the cheapest way to make N using elements from O.

F = []
F.append(0)
O = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
for x in range(1, 10**7):
    fx = 10**9
    for o in O:
        if x-o>=0:
            fx = min(fx, 1+F[x-o])
    F.append(fx)

DP = {}
def f(n):
    return F[n]
    #if n < 0:
    #    return 10**9
    #if n==0:
    #    return 0
    #if n in DP:
    #    return DP[n]
    #ans = 10**9
    #for o in O:
    #    ans = min(ans, 1 + f(n-o))
    #DP[n] = ans
    #return ans

def g(n):
    mid = n//2
    ans = 1e9
    for x in range(mid-200, mid+200):
        y = n-x
        if abs(x-y)<=100:
            score = f(x) + f(y)
            if score < ans:
                ans = score
    return ans


ans = 0
for line in D.split('\n'):
    x = int(line.strip())
    ans += g(x)
print(ans)
