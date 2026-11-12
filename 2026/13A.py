import sys
import math

D = sys.stdin.read()
hands,direction,current,move = D.splitlines()
hands = list(map(int, hands.split()[1].split(':')))
direction = direction.split()[1].split(':')
current = list(map(int, current.split()[1].split(':')))
move = list(map(int, move.split()[1].split(':')))

T = max(move)

L = math.lcm(*hands)
N = len(hands)
amt = [0 for _ in range(N)]
for i in range(N):
    assert L%hands[i] == 0
    current[i] *= L//hands[i]
    amt[i] = L//hands[i]


for cw in direction:
    assert cw in ['CW', 'CCW']

# a+(b-a)*t == c+(d-c)*t
# a-c = t*(d-c) - (b-a)*t
# a-c == t*(d-c-b+a)
# t = (a-c)/(d-c-b+a)

# does a->b overlap with c->d
def intervals_overlap(a1,b1,a2,b2):
    den = (b2-a2-b1+a1)
    if den == 0:
        return False
    t = (a1-a2)/den
    return 0<=t<=1
    #if a1>b1:
    #    return intervals_overlap(b1,a1,b2,a2)
    #assert a1<=b1
    #if a1<=a2 and b1>=b2:
    #    return True
    #if a2<=a1 and b2>=b1:
    #    return True
    #return False


ans = 0
for t in range(T):
    old_pos = list(current)
    print(f'{t=} {current=} {ans=}')
    for i in range(len(hands)):
        if t<move[i]:
            current[i] = (current[i] + amt[i]*(1 if direction[i]=='CW' else -1))
    for i in range(N):
        for j in range(i+1, N):
            if intervals_overlap(old_pos[i], current[i], old_pos[j], current[j]) and old_pos[i] != old_pos[j]:
                ans += 1
            if intervals_overlap(old_pos[i]+L, current[i]+L, old_pos[j], current[j]) and old_pos[i] != old_pos[j]:
                ans += 1
            if intervals_overlap(old_pos[i]-L, current[i]-L, old_pos[j], current[j]) and old_pos[i] != old_pos[j]:
                ans += 1
    for i in range(N):
        current[i] = (current[i]+L)%L
print(ans)




#print(hands,direction,current,move)
