#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
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
print(' '.join(C[i][(xs[i]*100)%len(C[i])] for i in range(nc)))
