import sys
fin = sys.argv[1]

names, instrs = open(fin).read().split('\n\n')
names = names.split(',')
instrs = instrs.split(',')

pos = 0
for instr in instrs:
    amt = int(instr[1:])
    if instr[0]=='R':
        pos = (pos+amt)%len(names)
    else:
        pos = (pos+len(names)-amt)%len(names)
    print(instr, pos)
print(names[pos])
