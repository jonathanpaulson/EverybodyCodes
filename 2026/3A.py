import sys

D = sys.stdin.read()
ans = 0
for line in D.splitlines():
    a,b = line.split()
    a = a.removeprefix('ISO-')
    #a,b = int(a),int(b)
    assert len(a) == len(b)
    score = 0
    for i in range(len(a)):
        xi = int(b[i])*int(a[i])**(len(a)-1-i)
        score += xi
    print(score)
    ans += score
print(ans)
