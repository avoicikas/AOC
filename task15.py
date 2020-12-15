import collections

data = [0, 13, 16, 17, 1, 10, 6]
nth_number = 2020


def solve(start_seq, nth_number):
    memory = collections.defaultdict(list)
    for idx, element in enumerate(start_seq):
        memory[element].append(idx)
        last_number_spoken = element
    for inext in range(len(memory.keys()), nth_number):
        #  breakpoint()
        if len(memory[last_number_spoken]) == 1:
            last_number_spoken = 0
        else:
            last_number_spoken = memory[last_number_spoken][-1] - \
                memory[last_number_spoken][-2]
        memory[last_number_spoken].append(inext)
    return last_number_spoken


test_data1 = [1, 3, 2]  # 1 at 2020

solve(test_data1, nth_number)

#  part 1

solve(data, nth_number)

#  part 2

solve(data, 30000000)
