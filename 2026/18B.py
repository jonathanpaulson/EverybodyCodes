import sys
import heapq

D = sys.stdin.read()

ON = set()
x0 = None
x1 = None
y0 = None
y1 = None

for line in D.splitlines():
    x,y,width = line.split()
    x = int(x.removeprefix('x='))
    y = int(y.removeprefix('y='))
    width = int(width.removeprefix('width='))
    for xx in range(x,x+width):
        for yy in range(y):
            ON.add((xx,yy))


x0 = min(x for x,_ in ON)
x1 = max(x for x,_ in ON)
y0 = min(y for _,y in ON)
y1 = max(y for _,y in ON)
HEIGHT = {x: 0 for x in range(x0,x1+1)}
for x in range(x0,x1+1):
    for y in range(y0,y1+1):
        if (x,y) in ON:
            HEIGHT[x] = max(HEIGHT[x], y)

H = [y for x,y in HEIGHT.items()]
maxh = max(H)

height_so_far = 0
for x in range(x0,x1+1):
    for y in range(y0,y1+1):
        has_left = height_so_far >= y #any((xx,y) in ON for xx in range(x-1000,x))
        has_right = maxh is not None and maxh>=y
        if has_left and has_right and (x,y) not in ON:
            #print(f'{x=} {y=}')
            ON.add((x,y))
    height_so_far = max(height_so_far, HEIGHT[x])
    H = [y for xx,y in HEIGHT.items() if xx>x]
    maxh = max(H) if len(H)>0 else None
print(len(ON))


