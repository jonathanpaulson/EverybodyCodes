data = open('A.in').read().strip()
T = 10
by_score = {}
for line in data.split('\n'):
    id_, actions = line.split(':')
    actions = actions.split(',')

    score = 0
    power = 10
    for t in range(T):
        c = actions[t%len(actions)]
        if c=='+':
            power += 1
        elif c=='-':
            power -= 1
        else:
            assert c=='='
        score += power
    by_score[score] = id_

ranks = ''.join([v for k,v in sorted(by_score.items(), reverse=True)])
print(ranks)
