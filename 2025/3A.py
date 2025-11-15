xs = [int(x) for x in input().split(',')]
xs = sorted(xs)
print(len(xs))

DP = {}
def dp(xs, i, prev):
    if i == len(xs):
        return 0
    key = (i, prev)
    if key in DP:
        return DP[key]
    ans = dp(xs, i+1, prev)
    if prev is None or xs[i]>prev:
        ans = max(ans, xs[i]+dp(xs, i+1, xs[i]))
    DP[key] = ans
    return ans

ans = dp(xs, 0, None)
print(ans)
