import random
from threading import stack_size
ls = []
separate_s = '",'
parent_s = '"_parent":"ID_'
visibility_s = '"visibility":"'
name_s = '"name":"'
direction_s = '"direction":"'
_type_s = '"_type":"'
type_s = '"type":'
ref_s = '{"$ref":"'
source_s = '"source":"'
target_s = '"target":"'
guard_s = '"guard":null,'
expression_s = '"expression": null,'
_id_s = '"_id":"ID_'
_end_s = '"}'
value_s = '"value": null}'
class_parent = "class_parent_id"
interface_parent = "interface_parent_id"
state_num = 0
final_num = 0
tran_num = 0
event_num = 0
ids = []
f = open('stdin.txt', 'w')
f1 = open('analysis.txt', 'w')


def make_parent(pid, with_sep = True):
    s = parent_s + str(pid)
    return end(s, with_sep)


def make_name(n, with_sep=True):
    s = name_s + str(n)
    return end(s, with_sep)


def make_visibility(with_sep = True):
    s = visibility_s + 'public'
    return end(s, with_sep)


def make__type(n, with_sep=True):
    s = _type_s + str(n)
    return end(s, with_sep)


def make_id(m, with_sep=True):
    s = _id_s + str(m)
    return end(s, with_sep)


def end(s, with_sep):
    if with_sep:
        s = s + separate_s
    else:
        s = s + _end_s
    return s


def make_null_name(with_sep=True):
    s = '"name":null'
    if with_sep:
        s = s + ','
    else:
        s = s + '}'
    return s

def make_source(n, with_sep=True):
    s = source_s + str(n)
    return end(s, with_sep)


def make_target(n, with_sep=True):
    s = target_s + str(n)
    return end(s, with_sep)


def make_state():
    global state_num
    index = state_num
    state_num = state_num + 1
    s = "{" + make_parent('Region') + \
        make_visibility() + \
        make_name('State' + str(index)) + \
        make__type("UMLState") + \
        make_id('State' + str(index), False)
    ids.append('ID_State' + str(index))
    print(s, file=f)


def make_final():
    global final_num
    index = final_num
    final_num = final_num + 1
    s = "{" + make_parent('Region') + \
        make_visibility() + \
        make_null_name() + \
        make__type("UMLFinalState") + \
        make_id('FinalState' + str(index), False)
    ids.append('ID_FinalState' + str(index))
    print(s, file=f)
    print('Final: FinalState' + str(index), file=f1)


def make_transition():
    global tran_num
    index = tran_num
    tran_num = tran_num + 1
    id1 = ids[random.randint(0, len(ids) - 1)]
    while 'Final' in id1:
        id1 = ids[random.randint(0, len(ids) - 1)]
    if random.randint(0, 4) == 0:
        id1 = "ID_InitialState"
    id2 = ids[random.randint(0, len(ids) - 1)]
    while 'Init' in id2:
        id2 = ids[random.randint(0, len(ids) - 1)]
    s = "{" + make_parent('Region') + \
        make_visibility() + \
        guard_s + \
        make_null_name() + \
        make__type("UMLTransition") + \
        make_id('Transition' + str(index)) + \
        make_source(id1) + \
        make_target(id2, False)
    for i in range(random.randint(0, random.randint(1, 2))):
        make_event('Transition' + str(index))
    print(s, file=f)

    print('edge: ' + polish(id1) + ' ---> ' + polish(id2), file=f1)

def polish(s):
    if 'ID_State' in s:
        return s.replace('ID_State', 'S_')
    elif 'ID_FinalState' in s:
        return s.replace('ID_FinalState', 'Final_')
    else:
        return s.replace('ID_InitialState', 'Init')


def make_event(pid):
    global event_num
    index = event_num
    event_num = event_num + 1
    s = "{" + make_parent(pid) + \
        expression_s + \
        make_visibility() + \
        make_name('Event' + str(index)) + \
        make__type("UMLEvent") + \
        make_id('Event' + str(index)) + \
        value_s
    print(s, file=f)


def make_cmd(n):
    print('END_OF_MODEL', file=f)
    print('STATE_COUNT StateMachine1', file=f)
    for i in range(n):
        id1 = 'State' + str(random.randint(0, state_num + 2))
        id2 = 'State' + str(random.randint(0, state_num + 2))
        if random.randint(0, 2) == 1:
            print('TRANSITION_TRIGGER StateMachine1 ' + id1 + ' ' + id2, file=f)
        else:
            print('STATE_IS_CRITICAL_POINT StateMachine1 ' + id1, file=f)



if __name__ == '__main__':
    ls.append('{"_parent":"AAAAAAFF+h6SjaM2Hec=","name":"StateMachine1","_type":"UMLStateMachine","_id":"ID_StateMachine"}')
    ls.append('{"_parent":"ID_StateMachine","visibility":"public","name":null,"_type":"UMLRegion","_id":"ID_Region"}')
    ls.append('{"_parent":"ID_Region","visibility":"public","name":null,"_type":"UMLPseudostate","_id":"ID_InitialState"}')
    print('Init: InitialState', file=f1)
    ids.append('ID_InitialState')
    for l in ls:
        print(l, file=f)
    n = random.randint(1, 30)
    for i in range(n):
        make_state()
    for i in range(random.randint(1, 6)):
        make_final()
    for i in range(random.randint(0, 2 * n)):
        make_transition()
    make_cmd(50)

