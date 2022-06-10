
import encodings


if __name__ == '__main__':
    infile1 = r'stdout1.txt'
    infile2 = r'stdout2.txt'
    ls1 = []
    ls2 = []
    with open(infile1, encoding='utf-8', errors='ignore') as fr:
        for line in fr:
            ls1.append(line[0:-1])

    with open(infile2, encoding='utf-8', errors='ignore') as fr:
        for line in fr:
            ls2.append(line[0:-1])

    lmax = max(len(ls1), len(ls2))
    lmin = min(len(ls1), len(ls2))
    correct = True
    for i in range(lmin):
        if ls2[i] != ls1[i]:
            print("Error in line", i + 1)
            print(ls1[i])
            print(ls2[i])
            correct = False
            break
    if lmax != lmin:
        print("stdout1 has", len(ls1), "lines, stdout2 has", len(ls2), "lines.")
        correct = False
    if correct:
        print("The same answer")
    else:
        print("Different answer")