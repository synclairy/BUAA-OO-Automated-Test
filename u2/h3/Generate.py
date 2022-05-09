import random


def add_floor(eid, time):
    m = random.randint(1, 31)
    if m % 2 == 0:
        m = m + 1
    return "[" + format(time, '.1f') + "]ADD-floor-" + str(eid) + "-" + str(random.randint(1, 10)) \
           + "-" + str(random.randint(2, 4) * 2) + "-" + format(random.randint(1, 3) * 0.2, '.1f') + \
           "-" + str(m)


def add_building(eid, time):
    return "[" + format(time, '.1f') + "]ADD-building-" + str(eid) + "-" + str(random.choice('ABCDE')) + "-"\
           + str(random.randint(2, 4) * 2) + "-" + format(random.randint(1, 3) * 0.2, '.1f')


def add_person(pid, time):
    l1 = str(random.randint(1, 10))
    l2 = str(random.randint(1, 10))
    while l1 == l2:
        l2 = str(random.randint(1, 10))
    return "[" + format(time, '.1f') + "]" + str(pid) + "-FROM-" + str(random.choice('ABCDE')) + "-" \
            + l1 + "-TO-" + str(random.choice('ABCDE')) + "-" \
            + l2


if __name__ == '__main__':
    e = 6
    p = 0
    t = 1
    f = open('stdin.txt', 'w')
    for i in range(50):
        r = random.randint(1, 15)
        if r == 1:
            e = e + 1
            t = t + random.uniform(0.2, 1.1)
            print(add_building(e, t), file=f)
        elif r == 2:
            e = e + 1
            t = t + random.uniform(0.2, 1.1)
            print(add_floor(e, t), file=f)
        else:
            p = p + 1
            t = t + random.uniform(0.2, 1.1)
            print(add_person(p, t), file=f)


