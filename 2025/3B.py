xs = [int(x) for x in input().split(',')]
xs = sorted(xs)
print(len(xs))

DP = {}
def dp(xs, i, sz, prev):
    if i == len(xs):
        return 0 if sz==20 else 10**18
    key = (i, sz, prev)
    if key in DP:
        return DP[key]
    ans = dp(xs, i+1, sz, prev)
    if prev is None or xs[i]>prev:
        ans = min(ans, xs[i]+dp(xs, i+1, sz+1, xs[i]))
    DP[key] = ans
    return ans

ans = dp(xs, 0, 0, None)
print(ans)
