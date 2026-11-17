import sys
from collections import defaultdict, deque

def is_contiguous(P):
    return max(P)-min(P)+1 == len(P)

def cost_and_newD(color, D):
    P = []
    for i, c in enumerate(D):
        if c==color:
            P.append(i)

    lo = min(P)
    hi = max(P)+1
    # "sort" D[lo:hi]. report cost and new string
    # first break D[lo:hi] into groups of contiguous "c" and non-c.
    # assert c is first group and remove first group.
    # then pay len(D), first (non-c) group to end reversed (and remove), and last (c) group to front reversed (and remove it)
    # then pay len(D), first (c) group to front (and remove), last (non-c) group to end (not-reversed) (and remove it)
    NEW = list(D)
    for i in range(lo,hi):
        NEW[i] = '?'
    end_pos = hi-1
    front_pos = lo

    GROUPS = deque([])
    GROUP = []
    for i in range(lo,hi):
        if len(GROUP) == 0 or (D[i]==color)==(GROUP[-1]==color):
            GROUP.append(D[i])
        else:
            GROUPS.append(GROUP)
            GROUP = [D[i]]
    if GROUP:
        GROUPS.append(GROUP)
        GROUP = []
    assert GROUPS[0][0] == color
    pay = sum([len(GROUP) for GROUP in GROUPS])
    assert pay == hi-lo, f'{pay=} {hi-lo+1=}'

    pay -= len(GROUPS[0])
    for ch in GROUPS[0]:
        assert NEW[front_pos] == '?'
        NEW[front_pos] = ch
        front_pos += 1
    GROUPS.popleft()

    #print(f'{color=} {P=} {D=} {GROUPS=}')
    ans = 0
    do_last = True
    while len(GROUPS)>0:
        #print(f'{pay=}')
        ans += pay
        if do_last:
            assert GROUPS[0][0]!=color
            assert GROUPS[-1][0]==color
            for ch in GROUPS[0]:
                assert NEW[end_pos] == '?'
                NEW[end_pos] = ch
                end_pos -= 1
            pay -= len(GROUPS[0])
            GROUPS.popleft()
            for ch in GROUPS[-1]:
                assert NEW[front_pos] == '?'
                NEW[front_pos] = ch
                front_pos += 1
            pay -= len(GROUPS[-1])
            GROUPS.pop()
        else:
            assert GROUPS[-1][0]!=color
            assert GROUPS[0][0]==color
            for ch in GROUPS[0]:
                assert NEW[front_pos] == '?'
                NEW[front_pos] = ch
                front_pos += 1
            pay -= len(GROUPS[0])
            GROUPS.popleft()
            for ch in reversed(GROUPS[-1]):
                assert NEW[end_pos] == '?'
                NEW[end_pos] = ch
                end_pos -= 1
            pay -= len(GROUPS[-1])
            GROUPS.pop()
        do_last = not do_last
    for ch in NEW:
        assert ch != '?'
    for i in range(lo, lo+len(P)):
        assert NEW[i] == color, f'{i=} {NEW[i]=} {color=}'
    #for i in range(len(D)):
        #assert NEW[i] == ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'G', 'G', 'Y', 'B', 'Y', 'G', 'Y', 'Y', 'G', 'Y', 'B', 'Y', 'G', 'G', 'Y', 'B', 'Y', 'G', 'Y', 'Y', 'G', 'Y', 'B', 'Y', 'G', 'G', 'Y', 'B', 'Y', 'G', 'Y', 'Y', 'G', 'Y', 'B', 'Y', 'G', 'G', 'Y', 'B', 'Y', 'G', 'Y', 'Y', 'G', 'Y', 'B', 'Y', 'G', 'G', 'Y', 'B', 'Y', 'G', 'Y', 'Y', 'G', 'Y', 'B', 'Y'][i], f'{i=} {NEW[i]=}'
    return ans, NEW




D = sys.stdin.read().strip()
D = D*100
D = list(D)

#print(len(set(D)))

#assert False, len(D)

# process 1 color at a time. we should be able to quickly compute from positions total number of flips to sort that color (?)
# only 4 colors!
# suppose list of positions is [G1,G2,...,Gn]
# first we remove G1 from the front for free. Then pay and remove Gn. Then pay and remove G2. etc.
# ultimately all color moves to front. What about the other colors/positions in the middle?
# Suppose the intervening groups are [X1,...,Xn-1]. X1 goes to the end (reversed) then we recurse on [X{n-1}, ..., X2]

# RARBR
# RRBRA
# RRRBA

# RABCRDRER
# RRERDRCBA
# RRRDRECBA
# RRRRDECBA

# RABRCDREFRGHR
# RRHGRFERDCRBA
# RRRCDREFRGHBA
# RRRRFERDCGHBA
# RRRRREFDCGHBA

assert cost_and_newD('R', list('RABRCDREFRGHR'))[1] == list('RRRRREFDCGHBA'), f"{cost_and_newD('R', 'RABRCDREFRGHR')[1]=}"

ans = 0
changed_color = None
while True:
    print('while')
    by_color = defaultdict(list)
    for i,c in enumerate(D):
        by_color[c].append(i)
    done = True
    for color in by_color:
        if not is_contiguous(by_color[color]):
            c_cost, D = cost_and_newD(color, D)
            #print(f'{c=}')
            ans += c_cost
            done = False
            break
    if done:
        break
print(ans)
