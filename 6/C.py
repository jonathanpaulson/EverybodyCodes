from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

data = open('C3.in').read().strip().split('\n')

C = defaultdict(list)
for line in data:
    start, edges = line.split(':')
    edges = edges.split(',')
    for e in edges:
        C[start].append(e)

def getPaths(root):
    if root in ['BUG', 'ANT']:
        return []
    ret = []
    if root == '@':
        return [['@']]
    for c in C[root]:
        for p in getPaths(c):
            ret.append([root] + p)
    return ret

paths = getPaths('RR')
by_length = defaultdict(list)
for path in paths:
    by_length[len(path)].append(path)
for _len, paths in by_length.items():
    if len(paths) == 1:
        print(''.join([c[0] for c in paths[0]]))