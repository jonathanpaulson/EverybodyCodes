def score(data):
    _id, xs = data.split(':')
    xs = [int(x) for x in xs.split(',')]
    SPINE = []
    for x in xs:
        found = False
        for i,(lo,med,hi) in enumerate(SPINE):
            if lo is None and x<med:
                SPINE[i] = (x, med, hi)
                found = True
                break
            if hi is None and x>med:
                SPINE[i] = (lo, med, x)
                found = True
                break
        if not found:
            SPINE.append((None, x, None))

    ans = int(''.join(str(med) for (lo,med,hi) in SPINE))
    return _id, ans

D = {}
while True:
    try:
        S = input()
    except:
        break
    k,v = score(S)
    D[k] = v
print(max(D.values()) - min(D.values()))
