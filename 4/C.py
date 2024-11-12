X = [int(x) for x in open('C.in').read().strip().split('\n')]
best = 1e100
for target in X:
    score = 0
    for x in X:
        score += abs(x-target)
    best = min(best, score)
print(best)
