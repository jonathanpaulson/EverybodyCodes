from collections import Counter

xs = [int(x) for x in input().split(',')]
xs = sorted(xs)
print(len(xs))

VS = []
for x in xs:
    found = False
    for i,v in enumerate(VS):
        if x > v:
            VS[i] = x
            found = True
            break
    if not found:
        VS.append(x)
print(len(VS))
print(max(Counter(xs).values()))
