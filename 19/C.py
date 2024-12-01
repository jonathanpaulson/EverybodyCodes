#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
from copy import deepcopy
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()

msg, G = G.split('\n\n')
G = G.split('\n')
R = len(G)
C = len(G[0])
G_START = [[G[r][c] for c in range(C)] for r in range(R)]

def getPermutation():
    G = [[(r,c) for c in range(C)] for r in range(R)]
    START = deepcopy(G)
    #print('\n'.join(''.join(row) for row in G))
    mi = 0
    for r in range(R):
        for c in range(C):
            if r>0 and r<R-1 and c>0 and c<C-1:
                ch = msg[mi]
                mi = (mi+1)%len(msg)

                M = {(-1,-1): (-1,0),
                     (-1,0): (-1,1),
                     (-1, 1): (0, 1),
                     (0, 1): (1, 1),
                     (1, 1): (1, 0),
                     (1, 0): (1, -1),
                     (1, -1): (0, -1),
                     (0, -1): (-1, -1)}
                OLD = {(dr,dc): G[r+dr][c+dc] for dr,dc in M.keys()}
                if ch=='L':
                    for (fr,fc),(sr,sc) in M.items():
                        G[r+fr][c+fc] = OLD[(sr,sc)]
                elif ch=='R':
                    for (sr,sc),(fr,fc) in M.items():
                        #print(f'{r+fr=} {c+fc=} {r+sr=} {
                        G[r+fr][c+fc] = OLD[(sr,sc)]
    RET = {}
    for r in range(R):
        for c in range(C):
            RET[(r,c)] = G[r][c]
    return RET

def permutationMultiply(P, Q):
    C = {}
    for k in P.keys():
        C[k] = P[Q[k]]
    return C

def permutationPower(P, N):
    if N==1:
        return P
    elif N%2==0:
        return permutationPower(permutationMultiply(P,P),N//2)
    else:
        return permutationMultiply(P, permutationPower(P, N-1))

P = getPermutation()
N = 1048576000
#N = 100
#N = 1
# apply P N times
P2 = permutationPower(P, N)

def applyPermutation(P, G):
    G2 = [['?' for _ in range(C)] for r in range(R)]
    for r in range(R):
        row = []
        for c in range(C):
            pr,pc = P[(r,c)]
            #G2[pr][pc] = G[r][c]
            G2[r][c] = G[pr][pc]
    return G2
G2 = applyPermutation(P2, G)

print('\n'.join(''.join(row) for row in G2))
