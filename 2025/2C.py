import sys
import re
fin = sys.argv[1]

def add(x,y):
    X1,Y1 = x
    X2,Y2 = y
    return (X1 + X2, Y1 + Y2)
def mul(x,y):
    X1,Y1 = x
    X2,Y2 = y
    return (X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2)
def div(x,y):
    X1,Y1 = x
    X2,Y2 = y
    return (abs(X1) // abs(X2) * (-1 if X1<0 else 1) * (-1 if X2<0 else 1),
            abs(Y1) // abs(Y2) * (-1 if Y1<0 else 1) * (-1 if Y2<0 else 1))

data = open(fin).read()
x,y = [int(x) for x in re.findall(r'-?\d+', data)]
A = (x,y)

PRINT = (35630,-64870)
ans = 0
for x in range(A[0], A[0]+1001, 1):
    for y in range(A[1], A[1]+1001, 1):
        engrave = True
        R = (0,0)
        for t in range(100):
            R = mul(R, R)
            if (x,y)==PRINT:
                print(f'{t=} {R=}')
            R = div(R, (100000,100000))
            if (x,y)==PRINT:
                print(f'{t=} {R=}')
            R = add(R, (x,y))
            if (x,y)==PRINT:
                print(f'{t=} {R=}')
            #if x==35630 and y==64880:
            #    print(f'{t=} {R=}')
            if R[0]<-1000000 or R[0]>1000000 or R[1]<-1000000 or R[1]>1000000:
                engrave = False
                break
        if engrave:
            ans += 1
print(ans)
