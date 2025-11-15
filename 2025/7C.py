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

ANS = set()

def f(name):
    if 7<=len(name)<=11:
        ANS.add(name)
    if len(name)<11:
        for nc in OK.get(name[-1], []):
            f(name+nc)

for ni,name in enumerate(names):
    ok = True
    for i in range(len(name)):
        if i+1<len(name) and name[i+1] not in OK.get(name[i], []):
            ok = False
    if ok:
        f(name)
print(len(ANS))
