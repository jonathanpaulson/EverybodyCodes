import sys
from collections import deque

sys.setrecursionlimit(10**7)

D = sys.stdin.read()
lines = D.splitlines()

G = []
for line in lines:
    G.append(list(line))
R = len(G)
C = len(G[0])
print(R,C)
SHEEP = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 'D':
            sr,sc = r,c
        if G[r][c] == 'S':
            SHEEP.append((r,c))
print(sorted(SHEEP))

print(f'{R**len(SHEEP) * R * C * 2=}')

DRAGON_POS = set()
SHEEP_POS = set()
SHEEP_TURN = set()
KEYS = set()

DS = [(-1,2),(1,2),(-1,-2),(1,-2),
      (-2,1),(2,1),(-2,-1),(2,-1)]

DP = {}
def dp(G, dragon, sheep, sheep_turn):
    # how many ways for the dragon to eat the sheep?
    if len(sheep) == 0:
        return 1
    key = (tuple(dragon), frozenset(sheep), sheep_turn)
    #DRAGON_POS.add(tuple(dragon))
    #assert len(DRAGON_POS) <= R*C
    #SHEEP_POS.add(frozenset(sheep))
    #assert len(SHEEP_POS) <= R**len(SHEEP)
    #SHEEP_TURN.add(sheep_turn)
    #assert len(SHEEP_TURN) <= 2
    #KEYS.add(key)
    #assert len(KEYS) <= (R**len(SHEEP)) * R*C * 2

    if key in DP:
        return DP[key]
    ans = 0
    if sheep_turn:
        found = False
        for (sr,sc) in sheep:
            if sr+1==R:
                found = True
            if sr+1<R and (G[sr+1][sc]=='#' or (sr+1,sc)!=dragon):
                NEW_SHEEP = (sheep - {(sr,sc)}) | {(sr+1,sc)}
                ans += dp(G, dragon, NEW_SHEEP, False)
                found = True
        if not found:
            # sheep skip turn
            ans += dp(G, dragon, sheep, False)
    else:
        for dr,dc in DS:
            new_dragon = (dragon[0]+dr, dragon[1]+dc)
            if 0<=new_dragon[0]<R and 0<=new_dragon[1]<C:
                if G[new_dragon[0]][new_dragon[1]] != '#':
                    new_sheep = sheep - {new_dragon}
                else:
                    new_sheep = sheep
                ans += dp(G, new_dragon, new_sheep, True)
    DP[key] = ans
    if len(DP) % 10000==0:
        print(len(DP))
    return ans

print(dp(G, (sr,sc), set(SHEEP), True))
