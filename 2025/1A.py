import sys
fin = sys.argv[1]

names, instrs = open(fin).read().split('\n\n')
names = names.split(',')
instrs = instrs.split(',')

pos = 0
for instr in instrs:
    amt = int(instr[1:])
    if instr[0]=='R':
        pos = min(pos+amt, len(names)-1)
    else:
        pos = max(pos-amt, 0)
    print(instr, pos)
print(names[pos])
