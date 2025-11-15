import sys
import re
fin = sys.argv[1]

def add(x,y):
    return (x[0]+y[0], x[1]+y[1])
def mul(x,y):
    X1,Y1 = x
    X2,Y2 = y
    return (X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2)
def div(x,y):
    return (x[0]//y[0], x[1]//y[1])

data = open(fin).read()
x,y = [int(x) for x in re.findall('\d+', data)]
A = (x,y)
B = (0,0)
for _ in range(3):
    B = mul(B,B)
    B = div(B, (10, 10))
    B = add(B,A)
print(f'[{B[0]},{B[1]}]')
