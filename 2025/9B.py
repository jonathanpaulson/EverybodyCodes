import sys

D = sys.stdin.read()
lines = D.splitlines()
PEOPLE = {}
for line in lines:
    k,v = line.split(':')
    PEOPLE[k] = v

ans = 0
for k, v in PEOPLE.items():
    for p1k, p1v in PEOPLE.items():
        for p2k, p2v in PEOPLE.items():
            if len({k,p1k,p2k}) == 3:
                is_ok = True
                for i in range(len(v)):
                    if v[i] != p1v[i] and v[i]!=p2v[i]:
                        is_ok = False
                if is_ok:
                    s1 = 0
                    s2 = 0
                    for i in range(len(v)):
                        if v[i]==p1v[i]:
                            s1 += 1
                        if v[i]==p2v[i]:
                            s2 += 1
                    ans += s1*s2
print(ans//2)
