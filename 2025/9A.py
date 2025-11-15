import sys

D = sys.stdin.read()
lines = D.splitlines()
PEOPLE = {}
for line in lines:
    k,v = line.split(':')
    PEOPLE[k] = v

for k, v in PEOPLE.items():
    is_child = True
    for i,vi in enumerate(v):
        is_ok = False
        for k2,v2 in PEOPLE.items():
            if k!=k2 and v2[i]==vi:
                is_ok = True
        if not is_ok:
            is_child = False
    if is_child:
        ans = 1
        for k2,v2 in PEOPLE.items():
            if k!=k2:
                score = 0
                for i in range(len(v)):
                    if v[i]==v2[i]:
                        score += 1
                ans *= score
        print(ans)
