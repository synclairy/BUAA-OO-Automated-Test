import random

ap_w = 3
ar_w = ap_w + 5
qv_w = ar_w + 1
qps_w = qv_w + 1
qci_w = qps_w + 4
qbs_w = qci_w + 4
ag_w = qbs_w + 1
atg_w = ag_w + 1
dfg_w = atg_w + 1
s = dfg_w
p_ids = []
u_ids = []
g_ids = []
names = []


def get2(ori):
    instr = ori
    if re_case():
        for j in range(2):
            if random.randint(0, 1) == 0 and len(p_ids) != 0:
                r = random.randint(1, len(p_ids))
                instr = instr + str(p_ids[r - 1]) + " "
            else:
                r = random.randint(1, len(u_ids))
                instr = instr + str(u_ids[r - 1]) + " "
    elif len(p_ids) < 2:
        return ap_i()
    else:
        for j in range(2):
            r = random.randint(1, len(p_ids))
            instr = instr + str(p_ids[r - 1]) + " "
    return instr


def names_init():
    infile = r'champions.txt'
    with open(infile, encoding='utf-8') as fr:
        for line in fr:
            a = line[0:-1]
            names.append(a)
    for j in range(len(names)):
        u_ids.append(j + 1)


def re_case():
    if random.randint(1, 5) == 1:
        return True
    return False


def gen_instr():
    r = random.randint(1, s) - 1
    if r < ap_w:
        return ap_i()
    elif r < ar_w:
        return ar_i()
    elif r < qv_w:
        return qv_i()
    elif r < qps_w:
        return qps_i()
    elif r < qci_w:
        return qci_i()
    elif r < qbs_w:
        return qbs_i()
    elif r < ag_w:
        return ag_i()
    elif r < atg_w:
        return atg_i()
    else:
        return dfg_i()


def ap_i() -> str:
    instr = "ap "
    if len(p_ids) != 0 and re_case():
        r = random.randint(1, len(p_ids))
        instr = instr + str(p_ids[r-1]) + " err_name 233"
    else:
        r = random.randint(1, len(u_ids))
        instr = instr + str(u_ids[r-1]) + " " + names[r-1] + " " + str(random.randint(0, 200))
        p_ids.append(u_ids[r-1])
        del u_ids[r-1]
        del names[r-1]
    return instr


def ar_i() -> str:
    instr = "ar "
    if re_case():
        for j in range(2):
            if random.randint(0, 1) == 0 and len(p_ids) != 0:
                r = random.randint(1, len(p_ids))
                instr = instr + str(p_ids[r - 1]) + " "
            else:
                r = random.randint(1, len(u_ids))
                instr = instr + str(u_ids[r - 1]) + " "
        instr = instr + "2333"
    elif len(p_ids) < 2:
        return ap_i()
    else:
        for j in range(2):
            r = random.randint(1, len(p_ids))
            instr = instr + str(p_ids[r - 1]) + " "
        instr = instr + str(random.randint(0, 1000))
    return instr


def qv_i() -> str:
    instr = get2("qv ")
    return instr


def qps_i():
    instr = "qps"
    return instr


def qci_i():
    instr = get2("qci ")
    return instr


def qbs_i():
    instr = "qbs"
    return instr


def ag_i():
    instr = "ag "
    if len(g_ids) != 0 and re_case():
        r = random.randint(1, len(g_ids))
        instr = instr + str(g_ids[r-1])
    else:
        r = random.randint(1, 10000)
        while r in g_ids:
            r = random.randint(1, 10000)
        instr = instr + str(r)
        g_ids.append(r)
    return instr


def atg_i():
    instr = "atg "
    if re_case() or len(p_ids) == 0:
        instr = instr + str(u_ids[random.randint(1, len(u_ids)) - 1])
    else:
        instr = instr + str(p_ids[random.randint(1, len(p_ids)) - 1])
    if re_case() or len(g_ids) == 0:
        instr = instr + " " + str(random.randint(1, 10000))
    else:
        instr = instr + " " + str(g_ids[random.randint(1, len(g_ids)) - 1])
    return instr


def dfg_i():
    instr = "dfg "
    if re_case() or len(p_ids) == 0:
        instr = instr + str(u_ids[random.randint(1, len(u_ids)) - 1])
    else:
        instr = instr + str(p_ids[random.randint(1, len(p_ids)) - 1])
    if re_case() or len(g_ids) == 0:
        instr = instr + " " + str(random.randint(1, 10000))
    else:
        instr = instr + " " + str(g_ids[random.randint(1, len(g_ids)) - 1])
    return instr


if __name__ == '__main__':
    f = open('stdin.txt', 'w')
    names_init()
    for i in range(3000):
        print(gen_instr(), file=f)




