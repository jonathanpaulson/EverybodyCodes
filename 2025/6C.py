REPEAT = 1000
DISTANCE = 1000

# count number of uppercase letters within 1000 spaces of each lowercase letter

data = input()
print(data, len(data))
ans = 0
for i,c in enumerate(data):
    if 'A'<=c<='Z':
        pass
    else:
        si = 0
        for dpos in range(-DISTANCE, DISTANCE+1):
            if data[(i+dpos+len(data))%len(data)] == c.upper():
                #print(f'{i=} {dpos=}')
                si += REPEAT
                if i+dpos < 0:
                    si -= 1
                if i+dpos >= len(data):
                    si -= 1
        ans += si
        print(f'{i=} {si=}')
print(ans)
