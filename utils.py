import random

def randomC(colors):
    return random.choice(colors)

def randomA(animals):
    return random.choice(animals)

def random_group_name(colors, animals):
    return randomC(colors) + " " + randomA(animals)

def random_groups(people, num):
    if num < 1:
        return []
    random.shuffle(people)
    idx = 0
    groups = [[] for x in range(num)]
    
    for person in people:
        groups[idx].append(person)
        idx += 1
        idx %= num

    return groups


def random_names(groups):
    n_groups = len(groups)
    random_namesga = []
    if n_groups < 1:
	    return []
    while n_groups >= 1:
        random_namesga.append(random_group_name(colors, animals))
        n_groups = n_groups - 1
    return random_namesga