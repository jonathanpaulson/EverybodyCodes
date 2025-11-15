import sys
fin = sys.argv[1]

names, instrs = open(fin).read().split('\n\n')
names = names.split(',')
instrs = instrs.split(',')

for instr in instrs:
    amt = int(instr[1:]) % len(names)
    print(instr, len(names))
    if instr[0]=='R':
        swap_idx = amt
    else:
        swap_idx = len(names)-amt
    names[0],names[swap_idx] = names[swap_idx],names[0]
print(names[0])
