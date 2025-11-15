track = open('track.in').read().strip()
track = track.split('\n')
track_str = ''
for i,row in enumerate(track):
    if i==0:
        track_str += row[1:]
    elif i==len(track)-1:
        track_str += ''.join(reversed(row))
    else:
        track_str += row[-1]
for i,row in enumerate(track):
    if 0<i<len(track)-1:
        track_str += row[0]
track_str += '='
print(track)
print(track_str)

data = open('B.in').read().strip()
T = 10
by_score = {}
for line in data.split('\n'):
    id_, actions = line.split(':')
    actions = actions.split(',')

    score = 0
    power = 10
    i = 0
    for round_ in range(10):
        for c in track_str:
            if c=='=':
                c = actions[i%len(actions)]
            if c=='+':
                power += 1
            elif c=='-':
                power -= 1
            else:
                assert c=='='
            score += power
            i += 1
    by_score[score] = id_

ranks = ''.join([v for k,v in sorted(by_score.items(), reverse=True)])
print(by_score)
print(ranks)
