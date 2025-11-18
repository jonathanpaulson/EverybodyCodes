import sys
from collections import deque

D = sys.stdin.read()
X = [int(x) for x in D.splitlines()]

#X = [368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368787, 368788, 368788, 368788, 368788, 368788, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508390, 508391, 508391, 508391, 517580, 517580, 517580, 517580, 517580, 517580, 517580, 517580, 517581]
print(X)

# move right->left, bigger->smaller
# assume already sorted; now want to make equal

for i in range(len(X)-1):
    assert X[i]<=X[i+1]
final = sum(X)//len(X)
assert final * len(X) == sum(X)

ans = 0
for x in X:
    if x<final:
        ans += final-x
print(ans)
assert False



# number of birds, when they start moving
NEED = deque([])
MOVES = [0 for _ in range(len(X))]
for i in range(len(X)-1):
    if X[i]<final:
        NEED.append((i, final-X[i]))
    else:
        extra = X[i]-final
        while extra > 0:
            assert len(NEED) > 0
            ni,namt = NEED.popleft()
            amt = min(namt, extra)
            print(f'MATCH {ni=} {i=} {amt=}')
            for mi in range(ni+1, i+1):
                MOVES[mi] += amt
            if amt == extra:
                NEED.appendleft((ni, namt-amt))
                extra = 0
            else:
                extra -= amt
ans = max(MOVES)
assert ans == 2118594, f'{ans=} 2118594'
