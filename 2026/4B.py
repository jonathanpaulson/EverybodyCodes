import sys

D = sys.stdin.read()
TIME = {}
for line in D.splitlines():
    id_, quest, part, time = line.split()
    id_ = int(id_.removeprefix('id='))
    time = int(time.removeprefix('time='))
    if id_ not in TIME:
        TIME[id_] = []
    TIME[id_].append(time)
print(TIME)

ans = 0
for i,(k,v) in enumerate(sorted(TIME.items(), key=lambda kv: (-len(kv[1]), sum(kv[1])))):
    print(i,k,v)
    ans += (i+1)*sum(v)
print(ans)


