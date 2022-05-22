import random

ap_w = 1
ar_w = ap_w + 1
qv_w = ar_w + 1
qps_w = qv_w + 1
qci_w = qps_w + 1
qbs_w = qci_w + 1
ag_w = qbs_w + 1
atg_w = ag_w + 1
dfg_w = atg_w + 1
qgps_w = dfg_w + 1
qgvs_w = qgps_w + 1
qgav_w = qgvs_w + 1
am_w = qgav_w + 1
sm_w = am_w + 1
qsv_w = sm_w + 1
qrm_w = qsv_w + 1
qlc_w = qrm_w + 1
arem_w = qlc_w + 1
anm_w = arem_w + 1
cn_w = anm_w + 1
aem_w = cn_w + 1
sei_w = aem_w + 1
qp_w = sei_w + 1
dce_w = qp_w + 1
qm_w = dce_w + 1
sim_w = qm_w + 1
s = sim_w
p_ids = []
u_ids = []
m_ids = []
g_ids = []
em_ids = []
ap_n = 0
ap_max = 2500
qci_n = 0
qci_max = 100
ag_n = 0
ag_max = 20
qlc_n = 0
qlc_max = 20
sim_n = 0
sim_max = 500

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


def uids_init():
    for j in range(10000):
        u_ids.append(j + 1)


def name_gen(nid):
    return "P_" + str(nid)


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
    elif r < dfg_w:
        return dfg_i()
    elif r < qgps_w:
        return qgps_i()
    elif r < qgvs_w:
        return qgvs_i()
    elif r < qgav_w:
        return qgav_i()
    elif r < am_w:
        return am_i()
    elif r < sm_w:
        return sm_i()
    elif r < qsv_w:
        return qsv_i()
    elif r < qrm_w:
        return qrm_i()
    elif r < qlc_w:
        return qlc_i()
    elif r < arem_w:
        return arem_i()
    elif r < anm_w:
        return anm_i()
    elif r < cn_w:
        return cn_i()
    elif r < aem_w:
        return aem_i()
    elif r < sei_w:
        return sei_i()
    elif r < qp_w:
        return qp_i()
    elif r < dce_w:
        return dce_i()
    elif r < qm_w:
        return qm_i()
    else:
        return sim_i()


def ap_i() -> str:
    global ap_n
    instr = "ap "
    if ap_n == ap_max:
        return gen_instr()
    ap_n = ap_n + 1
    if len(p_ids) != 0 and re_case():
        r = random.randint(1, len(p_ids))
        instr = instr + str(p_ids[r-1]) + " errName 23"
    else:
        r = random.randint(1, len(u_ids))
        instr = instr + str(u_ids[r-1]) + " " + name_gen(r-1) + " " + str(random.randint(0, 200))
        p_ids.append(u_ids[r-1])
        del u_ids[r-1]
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
        instr = instr + "233"
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
    global qci_n
    if qci_n == qci_max:
        return gen_instr()
    qci_n = qci_n + 1
    instr = get2("qci ")
    return instr


def qbs_i():
    instr = "qbs"
    return instr


def ag_i():
    instr = "ag "
    global ag_n
    if ag_n == ag_max:
        return gen_instr()
    ag_n = ag_n + 1
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


def get_g(method):
    if len(g_ids) == 0 or re_case():
        r = random.randint(1, 10000)
        while r in g_ids:
            r = random.randint(1, 10000)
        return method + str(r)
    elif len(g_ids) == 0:
        return ag_i();
    else:
        r = random.randint(1, len(g_ids))
        return method + str(g_ids[r-1])


def qgps_i():
    return get_g("qgps ")


def qgvs_i():
    return get_g("qgvs ")


def qgav_i():
    return get_g("qgav ")


def am_i():
    instr = "am "
    if len(m_ids) != 0 and re_case():
        r = random.randint(1, len(m_ids))
        instr = instr + str(m_ids[r-1]) + " " +  str(random.randint(-1000, 1000)) + " " +  \
            str(random.randint(0, 1)) + " " + str(random.randint(-1000, 1000)) \
                 + " " + str(random.randint(-1000, 1000))
    else:
        r = random.randint(1, 10000)
        while r in m_ids:
            r = random.randint(1, 10000)
        instr = instr + str(r) + " " + str(random.randint(-1000, 1000))
        if len(p_ids) < 1:
            return ap_i()
        if len(g_ids) < 1:
            return ag_i()
        if random.randint(0, 1) == 0:
            instr = instr + " 0 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
                + " " + str(p_ids[random.randint(1, len(p_ids))-1])
        else:
            instr = instr + " 1 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
                + " " + str(g_ids[random.randint(1, len(g_ids))-1])
        m_ids.append(r)
    return instr


def sm_i():
    instr = "sm "
    if len(m_ids) == 0 or re_case():
        r = random.randint(1, 10000)
        while r in m_ids:
            r = random.randint(1, 10000)
        return instr + str(r)
    elif len(m_ids) == 0:
        return am_i();
    else:
        r = random.randint(1, len(m_ids))
        return instr + str(m_ids[r-1])


def get_p(method):
    if len(p_ids) == 0 or re_case():
        r = random.randint(1, 10000)
        while r in p_ids:
            r = random.randint(1, 10000)
        return method + str(r)
    elif len(p_ids) == 0:
        return ap_i();
    else:
        r = random.randint(1, len(p_ids))
        return method + str(p_ids[r-1])


def qsv_i():
    return get_p("qsv ")


def qrm_i():
    return get_p("qrm ")


def qlc_i():
    global qlc_n
    if qlc_n == qlc_max:
        return gen_instr()
    qlc_n = qlc_n + 1
    return get_p("qlc ")


def arem_i():
    instr = "arem "
    if len(m_ids) != 0 and re_case():
        r = random.randint(1, len(m_ids))
        instr = instr + str(m_ids[r-1]) + " " +  str(random.randint(0, 200)) + " " +  \
            str(random.randint(0, 1)) + " " + str(random.randint(0, 200)) \
                 + " " + str(random.randint(0, 200))
    else:
        r = random.randint(1, 10000)
        while r in m_ids:
            r = random.randint(1, 10000)
        instr = instr + str(r) + " " + str(random.randint(0, 200))
        if len(p_ids) < 1:
            return ap_i()
        if len(g_ids) < 1:
            return ag_i()
        if random.randint(0, 1) == 0:
            instr = instr + " 0 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
                + " " + str(p_ids[random.randint(1, len(p_ids))-1])
        else:
            instr = instr + " 1 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
                + " " + str(g_ids[random.randint(1, len(g_ids))-1])
        m_ids.append(r)
    return instr


def anm_i():
    instr = "anm "
    if len(m_ids) != 0 and re_case():
        r = random.randint(1, len(m_ids))
        instr = instr + str(m_ids[r-1]) + " n_" +  str(r) + " " +  \
            str(random.randint(0, 1)) + " " + str(random.randint(0, 1000)) \
                 + " " + str(random.randint(0, 1000))
    else:
        r = random.randint(1, 10000)
        while r in m_ids:
            r = random.randint(1, 10000)
        instr = instr + str(r) + " n_" +  str(r)
        if len(p_ids) < 1:
            return ap_i()
        if len(g_ids) < 1:
            return ag_i()
        if random.randint(0, 1) == 0:
            instr = instr + " 0 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
                + " " + str(p_ids[random.randint(1, len(p_ids))-1])
        else:
            instr = instr + " 1 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
                + " " + str(g_ids[random.randint(1, len(g_ids))-1])
        m_ids.append(r)
    return instr


def cn_i():
    return get_p("cn ")


def qm_i():
    return get_p("qm ")


def aem_i():
    instr = "aem "
    ri = 0
    if len(m_ids) != 0 and re_case():
        r = random.randint(1, len(m_ids))
        instr = instr + str(m_ids[r-1]) + " "
    else:
        ri = random.randint(1, 10000)
        while ri in m_ids:
            ri = random.randint(1, 10000)
        instr = instr + str(ri) + " "
        if len(p_ids) < 1:
            return ap_i()
        if len(g_ids) < 1:
            return ag_i()
    if len(em_ids) != 0 and re_case():
        r = random.randint(1, 10000)
        while r in em_ids:
            r = random.randint(1, 10000)
        instr = instr + str(r)
    else:
        if len(em_ids) == 0:
            return sei_i()
        r = random.randint(1, len(em_ids))
        instr = instr + str(em_ids[r-1])
        if len(p_ids) < 1:
            return ap_i()
        if len(g_ids) < 1:
            return ag_i()
        m_ids.append(ri)
    if random.randint(0, 1) == 0:
        instr = instr + " 0 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
            + " " + str(p_ids[random.randint(1, len(p_ids))-1])
    else:
        instr = instr + " 1 " + str(p_ids[random.randint(1, len(p_ids))-1]) \
            + " " + str(g_ids[random.randint(1, len(g_ids))-1])
    return instr


def sim_i():
    global sim_n
    instr = "sim "
    if sim_n == sim_max:
        return gen_instr()
    sim_n = sim_n + 1
    instr = "sim "
    if len(m_ids) == 0 or re_case():
        r = random.randint(1, 10000)
        while r in m_ids:
            r = random.randint(1, 10000)
        return instr + str(r)
    elif len(m_ids) == 0:
        return am_i();
    else:
        r = random.randint(1, len(m_ids))
        return instr + str(m_ids[r-1])


def sei_i():
    instr = "sei "
    if len(em_ids) != 0 and re_case():
        r = random.randint(1, len(em_ids))
        instr = instr + str(em_ids[r-1])
    else:
        r = random.randint(1, 10000)
        while r in em_ids:
            r = random.randint(1, 10000)
        em_ids.append(r)
        instr = instr + str(r)
    return instr


def qp_i():
    instr = "qp "
    if len(em_ids) != 0 and re_case():
        r = random.randint(1, 10000)
        while r in em_ids:
            r = random.randint(1, 10000)
        instr = instr + str(r)
    else:
        if len(em_ids) == 0:
            return sei_i()
        r = random.randint(1, len(em_ids))
        instr = instr + str(em_ids[r-1])
    return instr


def dce_i():
    instr = "dce " + str(random.randint(0, 5))
    return instr

if __name__ == '__main__':
    f = open('stdin.txt', 'w')
    uids_init()
    for i in range(5000):
        print(gen_instr(), file=f)




