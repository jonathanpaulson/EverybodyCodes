#!/usr/bin/python3 
import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
G = open(infile).read().strip()

targets = []
for line in G.split('\n'):
    x,y = line.strip().split()
    x,y = int(x),int(y)
    targets.append((x,y))

sources = [(0,0),(0,1),(0,2)]

ans = 0
for ti,(tx,ty) in enumerate(targets):
    opts = [] # altitude, score
    new_txs = [tx] #if (tx%2==0) else [tx-1, tx+1]
    for tx in new_txs:
        for i,(sx,sy) in enumerate(sources):
            for wait in range(tx+1):
                wait_tx = tx - wait
                wait_ty = ty - wait
                if wait_tx % 2 != 0:
                    continue
                time = wait_tx/2
                assert sx==0
                # note: shot always moves 1 right; meteor always moves one left
                time_ty = wait_ty-time
                dy = time_ty - sy
                if time_ty < 0:
                    continue

                if dy <= time:
                    for power in [math.floor(dy), math.ceil(dy), (time+dy)//3]:
                        if power < 0:
                            continue
                        shot_dy = min(power,time) - (time-2*power if time>2*power else 0)
                        if shot_dy == dy:
                            assert sy==i
                            score = (i+1)*power
                            #print(f'{tx=} {ty=} {time=} {dy=} {power=} {(time+dy)/3=} {score=}')
                            opts.append((-time_ty, score))

    if len(opts) == 0:
        print(f'BAD {time=}')
    else:
        best_altitude, best_power = min(opts)
        print(f'{ti=} {tx=} {ty=} {best_power=}')
        #print(f'{ti=} {best_power=}')
        ans += best_power
print(ans)
