import math

X = []
while True:
    try:
        S = input()
    except:
        break
    X.append(int(S))
print(X)

#for i in range(1, len(X)-1):
#    turns = X[i-1]/X[i]*turns

#T * X[0]/X[-1] == 10000000000000
print(math.ceil(10000000000000 * X[-1]/X[0]))
