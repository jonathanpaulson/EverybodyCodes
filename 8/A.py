import sys
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
D = int(open(infile).read().strip())

x = 1
while x*x<D:
    x += 1
print((2*x-1) * (x*x-D))

