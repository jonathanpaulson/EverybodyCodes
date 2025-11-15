import sys
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
#priests = int(open(infile).read().strip())
priests = 901172
acolytes = 10
blocks = 202400000000
#blocks = 202400000

#priests = 2
#acolytes = 5
#blocks = 160

width = 1
thickness = 1
used = 1
layer = 1

slow = False

COLUMNS = [1]

COUNTS = [0 for _ in range(acolytes)]
COUNTS[1] += 1
while True:
    layer += 1
    width += 2
    thickness = (thickness * priests) % acolytes + acolytes
    NEW_COUNTS = [0 for _ in range(acolytes)]
    for x,c in enumerate(COUNTS):
        NEW_COUNTS[(x+thickness)%acolytes] += c
    NEW_COUNTS[thickness%acolytes] += 2
    COUNTS = NEW_COUNTS
    assert sum(COUNTS) == width

    used += thickness*width

    if slow:
        COLUMNS = [thickness] + [x+thickness for x in COLUMNS] + [thickness]
        assert used == sum(COLUMNS), f'{used=} {sum(COLUMNS)=}'

    removed = 0
    for x,c in enumerate(COUNTS):
        if x==(thickness%acolytes):
            assert c>=2
            c -= 2
        removed += ((priests * width * x) % acolytes) * c
        #print(f'{x=} {c=} {removed=}')
    if slow:
        slow_removed = 0
        for c in COLUMNS[1:-1]:
            c_removed = (priests * width * c) % acolytes
            assert c_removed <= c
            slow_removed += c_removed
        assert slow_removed == removed, f'{width=} {removed=} {slow_removed=} {COLUMNS=} {COUNTS=}'

    if layer == 4096:
        print(f'layer={(width+1)//2} {width=} {thickness=} {used=} {removed=} {used-removed=} {used-removed-blocks=} {COUNTS=}')
    if used - removed > blocks:
        print(used-removed-blocks)
        break

# 310147. length correct; first digit correct.
