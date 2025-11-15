import math

X = []
while True:
    try:
        S = input()
    except:
        break
    if '|' in S:
        x,y = S.split('|')
        X.append((int(x), int(y)))
    else:
        X.append(int(S))
print(X)

turns = 100
for i in range(1, len(X)):
    from_ = X[i-1]
    if isinstance(from_, tuple):
        from_ = from_[1]
    to_ = X[i]
    if isinstance(to_, tuple):
        to_ = to_[0]
    turns = turns * from_/to_
    print(f'{i=} {from_=} {to_=} {turns=}')
print(math.floor(turns))
