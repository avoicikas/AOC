from itertools import combinations

test_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95,
             102, 117, 150, 182, 127, 219, 299, 277, 309, 576]


with open('input9') as f:
    data = [int(x) for x in f.readlines()]


def find_mistake(dat, pream):
    for idx, element in enumerate(dat):
        if element not in [sum(x) for x in combinations(pream, 2)]:
            return idx, element, 0
        pream = pream[1:] + [element]
    return 0, 0, 1


testnumber = find_mistake(test_data[5:], test_data[:5])
testnumber

#  part 1

number = find_mistake(data[25:], data[:25])[1]

print(number)

# part 2


def find_contiguous_set(data, number):
    for idx in range(len(data)):
        for idy in range(idx+1, len(data)):
            if sum(data[idx:idy]) == number:
                return data[idx:idy]
    return 0


cl = find_contiguous_set(test_data, testnumber[1])
print(sum([max(cl), min(cl)]))

cl = find_contiguous_set(data, number)
print(sum([max(cl), min(cl)]))
