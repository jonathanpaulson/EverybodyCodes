names = input().split(',')
input()
OK = {}
while True:
    try:
        rule = input()
    except:
        break
    before, after = rule.split(' > ')
    OK[before] = after.split(',')
print(OK)

ans = 0
for ni,name in enumerate(names):
    ok = True
    for i in range(len(name)):
        if i+1<len(name) and name[i+1] not in OK[name[i]]:
            ok = False
    if ok:
        print(ni+1, name)
        ans += ni+1
print(ans)
