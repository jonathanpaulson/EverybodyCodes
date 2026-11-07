import sys
import heapq
from collections import deque
from copy import deepcopy

SCORE = {}
THICKNESS = {}
D = sys.stdin.read()
rows = D.split('\n\n')
for row in rows:
    lines = row.splitlines()
    words = lines[0].split()
    id_ = int(words[1])
    thickness = int(words[-1][:-1])
    THICKNESS[id_] = thickness
    SCORE[id_] = 0
    for line in lines[1:]:
        words = line.split()
        if words[1]=='free':
            SCORE[id_] += 1
        else:
            child_id = int(words[4])
            child_thickness = int(words[-1])
            SCORE[id_] += SCORE[child_id]*child_thickness
    if SCORE[id_] < THICKNESS[id_]:
        SCORE[id_] = 0
    print(id_, SCORE[id_])
