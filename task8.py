
with open('input8') as f:
    data = [x.strip().split() for x in f.readlines()]


def run_system(dat):
    system_log = {i: 0 for i in range(len(dat))}
    acc = 0
    icommand = 0
    while True:
        if system_log[icommand] == 0:
            system_log[icommand] = 1
            if dat[icommand][0] == 'acc':
                acc = acc+int(dat[icommand][1])
                icommand += 1
                if icommand >= len(system_log):
                    return acc, icommand, 1
            elif dat[icommand][0] == 'jmp':
                icommand = icommand + int(dat[icommand][1])
                if icommand >= len(system_log):
                    return acc, icommand, 1
            elif dat[icommand][0] == 'nop':
                icommand += 1
                if icommand >= len(system_log):
                    return acc, icommand, 1
        else:
            return acc, icommand, 0


#  part 1
print(run_system(data)[0])

#  part 2


def change_input(input):
    for icommand, command in enumerate(input):
        if command[0] == 'jmp':
            input[icommand][0] = 'nop'
            acc, ic, isend = run_system(input)
            if isend == 1:
                input[icommand][0] = 'jmp'
                return acc, ic, isend
            else:
                input[icommand][0] = 'jmp'
        elif command[0] == 'nop':
            input[icommand][0] = 'jmp'
            acc, ic, isend = run_system(input)
            if isend == 1:
                input[icommand][0] = 'nop'
                return acc, ic, isend
            else:
                input[icommand][0] = 'nop'
    return 0, 0, 0


change_input(data)
