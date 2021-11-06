with open('input6') as f:
    data = f.read().strip('\n')

groups = []
for group in data.split('\n\n'):
    groups.append(group.split('\n'))


def get_group_unique(group):
    answers = [n for m in group for n in list(m)]
    return set(answers)


def get_united_votes(group):
    if len(group) == 1:
        answer = set(group[0])
    else:
        unique_per_person = [set(x) for x in group]
        answer = unique_per_person[0].intersection(*unique_per_person[1:])
    return answer


#  task a
print(sum([len(get_group_unique(x)) for x in groups]))

#  task b
print(sum([len(get_united_votes(x)) for x in groups]))
