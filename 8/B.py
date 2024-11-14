import sys
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
priests = int(open(infile).read().strip())
acolytes = 1111
blocks = 20240000

width = 1
thickness = 1
used = 1
while True:
    width += 2
    thickness = (thickness * priests) % acolytes
    used += width*thickness
    if used > blocks:
        break

print(width * (used - blocks))
