import random
import limit

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
_id_s = '"_id":"ID_'
_end_s = '"}'
class_parent = "class_parent_id"
interface_parent = "interface_parent_id"


class ModelGenerate:
    class_num = 0
    interface_num = 0
    attribute_num = 0
    operation_num = 0
    generation_num = 0
    realization_num = 0
    parameter_num = 0
    element_num = 0
    ls = []
    c_ids = []
    c2op = []
    f = open('class_model_analysis.txt', 'w')

    @staticmethod
    def er_case():
        i = random.randint(0, 7)
        if i == 0:
            return True
        return False

    @staticmethod
    def _end(s, with_sep):
        if with_sep:
            s = s + separate_s
        else:
            s = s + _end_s
        return s

    @staticmethod
    def _make_parent(pid, with_sep = True):
        s = parent_s + str(pid)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make_visibility(with_sep = True):
        s = visibility_s + ModelGenerate._random_vis()
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make_name(n, with_sep=True):
        s = name_s + str(n)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make_null_name(with_sep=True):
        s = '"name":null'
        if with_sep:
            s = s + ','
        else:
            s = s + '}'
        return s

    @staticmethod
    def _make_direction(n, with_sep=True):
        s = direction_s + str(n)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make__type(n, with_sep=True):
        s = _type_s + str(n)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make_source(n, with_sep=True):
        s = source_s + str(n)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make_target(n, with_sep=True):
        s = target_s + str(n)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _make_type(n, with_sep=True):
        s = type_s + str(n)
        if with_sep:
            s = s + ', '
        else:
            s = s + '}'
        return s

    @staticmethod
    def _make_id(m, with_sep=True):
        s = _id_s + str(m)
        return ModelGenerate._end(s, with_sep)

    @staticmethod
    def _random_vis():
        i = random.randint(0, 3)
        if i < 1:
            return "package"
        elif i < 2:
            return "private"
        elif i < 3:
            return "public"
        else:
            return "protected"

    @staticmethod
    def _random_basic(isin):
        i = 0
        if ModelGenerate.class_num != 0 and random.randint(0, 2) == 0:
            return ref_s + "ID_" + ModelGenerate.c_ids[random.randint(0, len(ModelGenerate.c_ids) - 1)] + _end_s
        elif ModelGenerate.interface_num != 0 and random.randint(0, 1) == 0:
            return ref_s + "ID_Interface_" + str(random.randint(0, ModelGenerate.interface_num - 1)) + _end_s
        if isin:
            i = random.randint(0, 8)
        else:
            i = random.randint(0, 9)
        if i < 1:
            return '"byte"'
        elif i < 2:
            return '"short"'
        elif i < 3:
            return '"int"'
        elif i < 4:
            return '"long"'
        elif i < 5:
            return '"float"'
        elif i < 6:
            return '"double"'
        elif i < 7:
            return '"char"'
        elif i < 8:
            return '"boolean"'
        elif i < 9:
            return '"String"'
        else:
            return '"void"'

    @staticmethod
    def make_class():
        if ModelGenerate.er_case() and ModelGenerate.class_num > 1:
            print("@duplicate", file=ModelGenerate.f)
            index = random.randint(0, ModelGenerate.class_num - 1)
        else:
            index = ModelGenerate.class_num
            ModelGenerate.class_num += 1
            ModelGenerate.c2op.append([])
        mid = "Class_" + str(index) + "_e" + str(limit.Element.total)
        s = "{" + ModelGenerate._make_parent(class_parent) + \
            ModelGenerate._make_visibility() + \
            ModelGenerate._make_name("Class_" + str(index)) + \
            ModelGenerate._make__type("UMLClass") + \
            ModelGenerate._make_id(mid, False)
        ModelGenerate.c_ids.append(mid)
        limit.Element.total += 1
        ModelGenerate.ls.append(s)
        print("Class_" + str(index) + ": ID = " + mid, file=ModelGenerate.f)
        if index > 2 and random.randint(0, 2) == 0:
            iii = random.randint(0, ModelGenerate.class_num - 2)
            ModelGenerate.make_generation(mid, ModelGenerate.c_ids[random.randint(0, len(ModelGenerate.c_ids) - 2)])
        if ModelGenerate.interface_num > 4:
            aaa = []
            t = random.randint(0, ModelGenerate.interface_num - 1)
            times = random.randint(0, 2)
            for i in range(times):
                while t in aaa:
                    t = random.randint(0, ModelGenerate.interface_num - 1)
                aaa.append(t)
                ModelGenerate.make_realization(mid, "Interface_" + str(t))
        for i in range(0, random.randint(0, limit.Element.max_attr)):
            ModelGenerate.make_attribute(mid)
        for i in range(0, random.randint(0, limit.Element.max_op)):
            ModelGenerate.make_operation(index, mid)
        print("", file=ModelGenerate.f)


    @staticmethod
    def make_interface():
        index = ModelGenerate.interface_num
        s = "{" + ModelGenerate._make_parent(interface_parent) + \
            ModelGenerate._make_visibility() + \
            ModelGenerate._make_name("Interface_" + str(index)) + \
            ModelGenerate._make__type("UMLInterface") + \
            ModelGenerate._make_id("Interface_" + str(index), False)
        print("Interface_" + str(index) + ": ID = Interface_" + str(index), file=ModelGenerate.f)
        ModelGenerate.interface_num += 1
        limit.Element.total += 1
        if index > 2 and random.randint(0, 1) == 0:
            ModelGenerate.make_generation("Interface_" + str(index),
                                          "Interface_" + str(random.randint(0, index - 1)))
        for i in range(0, random.randint(0, limit.Element.max_attr)):
            ModelGenerate.make_attribute("Interface_" + str(index))
        for i in range(0, random.randint(0, limit.Element.max_op)):
            if len(ModelGenerate.c2op) > 1:
                ModelGenerate.make_operation(random.randint(0, len(ModelGenerate.c2op)-1), "Interface_" + str(index))
        ModelGenerate.ls.append(s)
        print("", file=ModelGenerate.f)

    @staticmethod
    def make_attribute(pid):
        index = ModelGenerate.attribute_num
        t = ModelGenerate._random_basic(True)
        s = "{" + ModelGenerate._make_parent(pid) + \
            ModelGenerate._make_visibility() + \
            ModelGenerate._make_name("Attribute_" + str(index)) + \
            ModelGenerate._make__type("UMLAttribute") + \
            ModelGenerate._make_id("Attribute_" + str(index) + "_e" + str(limit.Element.total)) + \
            ModelGenerate._make_type(t, False)
        print("    Attribute_" + str(index) + ": " + str(t), file=ModelGenerate.f)
        ModelGenerate.attribute_num += 1
        limit.Element.total += 1
        ModelGenerate.ls.append(s)

    @staticmethod
    def make_operation(ind, total):
        pid = total
        index = 0
        if random.randint(0, 3) != 0:
            index = random.randint(0, ModelGenerate.operation_num)
        else:
            index = ModelGenerate.operation_num
        if random.randint(0, 2) == 0:
            ModelGenerate.operation_num += 1
        mid = "Operation_" + str(index) + "_e" + str(limit.Element.total)
        s = "{" + ModelGenerate._make_parent(pid) + \
            ModelGenerate._make_visibility() + \
            ModelGenerate._make_name("Operation_" + str(index)) + \
            ModelGenerate._make__type("UMLOperation") + \
            ModelGenerate._make_id(mid, False)
        print("    Operation_" + str(index) + ":", file=ModelGenerate.f)
        limit.Element.total += 1
        ModelGenerate.c2op[ind].append(index)
        ModelGenerate.ls.append(s)
        for i in range(random.randint(0, 4)):
            ModelGenerate.make_parameter(mid)
        ModelGenerate.make_parameter(mid, "return")

    @staticmethod
    def make_generation(pid, ppid):
        total = limit.Element.total
        s = "{" + ModelGenerate._make_parent(pid) + \
            ModelGenerate._make_null_name() + \
            ModelGenerate._make__type("UMLGeneralization") + \
            ModelGenerate._make_id(total) + \
            ModelGenerate._make_source("ID_" + str(pid)) + \
            ModelGenerate._make_target("ID_" + str(ppid), False)
        print("    extends " + str(ppid), file=ModelGenerate.f)
        ModelGenerate.generation_num += 1
        limit.Element.total += 1
        ModelGenerate.ls.append(s)

    @staticmethod
    def make_realization(pid, ppid):
        total = limit.Element.total
        s = "{" + ModelGenerate._make_parent(pid) + \
            ModelGenerate._make_null_name() + \
            ModelGenerate._make__type("UMLInterfaceRealization") + \
            ModelGenerate._make_id(total) + \
            ModelGenerate._make_source("ID_" + str(pid)) + \
            ModelGenerate._make_target("ID_" + str(ppid), False)
        print("    implements " + str(ppid), file=ModelGenerate.f)
        ModelGenerate.realization_num += 1
        limit.Element.total += 1
        ModelGenerate.ls.append(s)

    @staticmethod
    def make_parameter(pid, direction="in"):
        total = limit.Element.total
        t = ModelGenerate._random_basic(True)
        s = "{" + ModelGenerate._make_parent(pid) + \
            ModelGenerate._make_null_name() + \
            ModelGenerate._make__type("UMLParameter") + \
            ModelGenerate._make_id(total) + \
            ModelGenerate._make_type(t) + \
            ModelGenerate._make_direction(direction, False)
        print("        " + direction + ":" + str(t), file=ModelGenerate.f)
        ModelGenerate.parameter_num += 1
        limit.Element.total += 1
        ModelGenerate.ls.append(s)

    @staticmethod
    def make_cmd():
        i = random.randint(0, 6)
        index = random.randint(0, ModelGenerate.class_num)
        if i < 1:
            return 'CLASS_SUBCLASS_COUNT Class_' + str(index)
        elif i < 2:
            return 'CLASS_OPERATION_COUNT Class_' + str(index)
        elif i < 3:
            if index >= ModelGenerate.class_num or len(ModelGenerate.c2op[index]) == 0:
                return 'CLASS_OPERATION_VISIBILITY Class_' + str(index) + " SLEEP"
            else:
                r = random.randint(0, len(ModelGenerate.c2op[index]) - 1)
                return 'CLASS_OPERATION_VISIBILITY Class_' + str(index) + " Operation_" +\
                       str(ModelGenerate.c2op[index][r])
        elif i < 4:
            if index >= ModelGenerate.class_num or len(ModelGenerate.c2op[index]) == 0:
                return 'CLASS_OPERATION_COUPLING_DEGREE Class_' + str(index) + " SLEEP"
            else:
                r = random.randint(0, len(ModelGenerate.c2op[index]) - 1)
                return 'CLASS_OPERATION_COUPLING_DEGREE Class_' + str(index) + " Operation_" + str(
                    ModelGenerate.c2op[index][r])
        elif i < 5:
            return 'CLASS_ATTR_COUPLING_DEGREE Class_' + str(index)
        elif i < 6:
            return 'CLASS_IMPLEMENT_INTERFACE_LIST Class_' + str(index)
        else:
            return 'CLASS_DEPTH_OF_INHERITANCE Class_' + str(index)

