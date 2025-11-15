#!/usr/bin/python3 
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()

rules = {}
for line in G.split('\n'):
    start, rest = line.split(':')
    rest = rest.split(',')
    rules[start] = rest

have = {'A': 1}
for _ in range(4):
    new_have = defaultdict(int)
    for k,v in have.items():
        for x in rules[k]:
            new_have[x] += v
    have = new_have
print(sum(have.values()))
