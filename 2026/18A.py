import sys

D = sys.stdin.read()

ON = set()
x0 = None
x1 = None
y0 = None
y1 = None

for line in D.splitlines():
    x,y = line.split()
    x = int(x.removeprefix('x='))
    y = int(y.removeprefix('y='))
    for yy in range(y):
        ON.add((x,yy))

x0 = min(x for x,_ in ON)
x1 = max(x for x,_ in ON)
y0 = min(y for _,y in ON)
y1 = max(y for _,y in ON)
for x in range(x0,x1+1):
    for y in range(y0,y1+1):
        has_left = any((xx,y) in ON for xx in range(x-100,x))
        has_right = any((xx,y) in ON for xx in range(x,x+100))
        if has_left and has_right and (x,y) not in ON:
            print(f'{x=} {y=}')
            ON.add((x,y))
print(len(ON))


