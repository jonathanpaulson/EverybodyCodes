#!/usr/bin/python3 
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()

targets = []
for line in G.split('\n'):
    x,y = line.strip().split()
    x,y = int(x),int(y)
    targets.append((x,y))

sources = [(0,0),(0,1),(0,2)]

ans = 0
for (tx,ty) in targets:
    opts = [] # altitude, score
    for (sx,sy) in sources:
        # note: shot always moves 1 right; meteor always moves one left
        assert (tx-sx)%2==0
        time = (tx-sx)//2
        time_ty = ty-time
        dy = time_ty - sy
        assert dy<time






        for power in range(5):
            # up and over. then shot is going down-right and target is going down-left
            # also can wait for any number of down-right moves
            shot_x = sx+power*2
            shot_y = sy+power
            time = ty - shot_y
            if time < 2*power:
                continue
            time_tx = tx - time
            if shot_x <= time_tx and (time_tx-shot_x)%2==0:
                altitude = shot_y - (time_tx-shot_x)//2
                print(f'{tx=} {ty=} {sx=} {sy=} {power=} {shot_x=} {shot_y=} {time=} {time_tx=} {altitude=}')
                opts.append((-altitude, (sy+1)*power))
    best_altitude, best_power = min(opts)
    print(f'{tx=} {ty=} {best_altitude=} {best_power=}')
    ans += best_power
print(ans)
