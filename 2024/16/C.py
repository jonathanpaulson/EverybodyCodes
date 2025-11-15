#!/usr/bin/python3 
import sys
from collections import defaultdict, deque, Counter
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
xs, faces = G.split('\n\n')
xs = [int(x) for x in xs.split(',')]
print(xs)
print(faces)

nc = (len(faces.split('\n')[0]) + 1) // 4
C = [[] for _ in range(nc)]

for line in faces.split('\n'):
    row = []
    for i in range(nc):
        face = line[i*4:i*4+3]
        if face.strip():
            C[i].append(face)

def getScore(C, state):
    score = Counter()
    for i in range(nc):
        face = C[i][state[i]]
        score[face[0]] += 1
        score[face[2]] += 1
    score = sum(max(0, v-2) for v in score.values())
    return score

DP = {}
def dp(left, state, do_min):
    if left==0:
        return 0
    key = (left, tuple(state), do_min)
    if key in DP:
        return DP[key]
    ans = None
    for dstate in [-1, 0, 1]:
        new_state = [(state[i]+dstate+xs[i]+len(C[i]))%len(C[i]) for i in range(nc)]
        new_score = getScore(C, new_state)
        new_state_score = new_score + dp(left-1, new_state, do_min)
        if ans is None:
            ans = new_state_score
        elif do_min and new_state_score < ans:
            ans = new_state_score
        elif (not do_min) and new_state_score > ans:
            ans = new_state_score
    DP[key] = ans
    return ans

state = [0 for _ in range(nc)]
mn = dp(256, state, do_min=True)
mx = dp(256, state, do_min=False)
print(f'{mx} {mn}')
print(len(DP))
