import sys

D = sys.stdin.read()
TIME = {}
SOLVED = {}
for line in D.splitlines():
    id_, quest, part, time = line.split()
    id_ = int(id_.removeprefix('id='))
    quest = int(quest.removeprefix('quest='))
    part = int(part.removeprefix('part='))
    time = int(time.removeprefix('time='))
    if (quest,part) not in SOLVED:
        SOLVED[(quest,part)] = set()
    SOLVED[(quest,part)].add(id_)
    parts = {1: [1,2,3], 2: [2,3], 3: [3]}[part]
    for part in parts:
        if (quest,part) not in TIME:
            TIME[(quest,part)] = {}
        if id_ not in TIME[(quest,part)]:
            TIME[(quest,part)][id_] = 0
        TIME[(quest,part)][id_] += time
POINTS = {}
for (quest,part),vs in TIME.items():
    vs = {k:v for k,v in vs.items() if k in SOLVED.get((quest,part), set())}
    pts = {1: 50, 2: 100, 3: 150}[part]
    prev_i = 0
    prev_time = None
    print(f'{quest=} {part=} {pts=}')
    for i,(k,v) in enumerate(sorted(vs.items(), key=lambda kv: kv[1])):
        if k not in POINTS:
            POINTS[k] = 0
        if prev_time is not None and v > prev_time:
            pts = pts - (i-prev_i)
            prev_i = i
        if pts>=0:
            POINTS[k] += pts
            print(f'{quest=} {part=} {k=} {v=} {pts=}')
        prev_time = v

print(TIME)
print(POINTS)

ans = 0
prev_score = None
prev_i = 0
place = 1
for i,(k,v) in enumerate(sorted(POINTS.items(), key=lambda kv: -kv[1])):
    if prev_score is not None and v<prev_score:
        place += (i-prev_i)
        prev_i = i
    prev_score = v
    print(place,k,v)
    ans += place*v
print(ans)
