def score(data):
    id_, xs = data.strip().split(':')
    id_ = int(id_)
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

    quality = int(''.join(str(med) for (lo,med,hi) in SPINE))
    assert len(str(quality)) == len(SPINE)
    levels = [int(('' if lo is None else str(lo)) + str(med) + ('' if hi is None else str(hi))) for (lo,med,hi) in SPINE]
    assert len(xs) == sum(len(str(level)) for level in levels)
    key = [quality]
    for level in levels:
        key.append(level)
    key.append(id_)
    return (tuple(key), id_)

SWORDS = []
while True:
    try:
        S = input()
    except:
        break
    SWORDS.append(score(S))
assert len(SWORDS) == 500
SWORDS = sorted(SWORDS, reverse=True)
ans = 0
for i,(_key, k) in enumerate(SWORDS):
    ans += k*(i+1)
    #print(k, len(str(quality)), quality, levels, ans)
print(ans)
