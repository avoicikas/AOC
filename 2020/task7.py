import re

with open('input7') as f:
    data = f.read().split('\n')


def findbags(word):
    for line in data:
        if word in line:
            newword = (re.findall(r'(.*) bags contain', line))[0]
            if newword != word:
                bag.append(newword)
                findbags(newword)
    return bag


#  part a

word = 'shiny gold'
bag = []
print(len(set(findbags(word))))

#  part b

# 126
testdata = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.',
]


def findbagscount(word, data, bag_count):
    for line in data:
        if line.startswith(word):
            num = re.findall(r'(\d)', line)
            newword = re.findall(r'(\w+ \w+) bag', line)[1:]
            for idxelement, element in enumerate(num):
                bag_count += int(element)
                for _ in range(int(element)):
                    bag_count = findbagscount(
                        newword[idxelement], data, bag_count)
            return bag_count


findbagscount('shiny gold', testdata, 0)

print(findbagscount('shiny gold', data, 0))

# better to form dictionary first and then loop over it

#  better solution

import networkx as nx

with open('input7') as f:
    data = [x.strip().split() for x in f.readlines()]

dictionary = {}
for w in data:
    parent = w[0] + w[1]
    i = 4
    contains = []
    while i < len(w) and w[i] != 'no':
        count = int(w[i])
        child = w[i+1] + w[i+2]
        contains.append((count, child))
        i += 4
    rules[parent] = contains

# Part one
G = nx.DiGraph()
for parent, contains in rules.items():
    for _, child in contains:
        G.add_edge(child, parent)

print(len(nx.predecessor(G, 'shinygold')) - 1)


# Part two
def num_bags(color):
    return 1 + sum(count * num_bags(child) for count, child in rules[color])


print(num_bags('shinygold') - 1)
