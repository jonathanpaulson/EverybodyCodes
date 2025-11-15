import math

X = []
while True:
    try:
        S = input()
    except:
        break
    X.append(int(S))
print(X)

turns = 2025
#for i in range(1, len(X)-1):
#    turns = X[i-1]/X[i]*turns
print(math.floor(turns * X[0]/X[-1]))
