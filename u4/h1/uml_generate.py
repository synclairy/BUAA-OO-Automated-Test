from class_model import ModelGenerate
import random


if __name__ == "__main__":
    a = ModelGenerate()
    f = open('stdin.txt', 'w')
    for i in range(30):
        a.make_class()
        a.make_interface()
    while len(ModelGenerate.ls) > 0:
        index = random.randint(0, len(ModelGenerate.ls) - 1)
        tt = ModelGenerate.ls[index]
        del ModelGenerate.ls[index]
        print(tt, file=f)
    print("END_OF_MODEL", file=f)
    print("CLASS_COUNT", file=f)
    for i in range(300):
        print(ModelGenerate.make_cmd(), file=f)