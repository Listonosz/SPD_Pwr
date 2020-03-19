import glob, os
import operator
import time

def sortR(listT):
    return sorted(listT, key=operator.itemgetter(0))

def sortQ(listT):
    return sorted(listT, key=operator.itemgetter(2))

def sortRQ(listT):
    return sorted(listT, key=operator.itemgetter(0, 2))


def c_max(listT, n):
    S = []
    C = []
    S.append(listT[0][0])
    C.append(S[0] + listT[0][1])
    wynik = C[0] + listT[0][2]

    for j in range(int(n) - 1):
        k = j + 1
        # print(k)
        S.append(max(listT[k][0], C[j]))
        C.append(S[k] + listT[k][1])
        wynik = max(wynik, C[k] + listT[k][2])
    return wynik

def read_from_file(nazwa):

    f = open(nazwa,"r")
    first = (' '.join(f.readline().split())).split(" ") # reduces spaces for first line and make list
    listRQP = []

    # Based on data from first line
    for i in range( int(first[0]) ):
        # reduce spaces
        a = ' '.join(f.readline().split())
        # deletes \n on the end
        a = a.replace("\n", "")
        #  make list
        a = a.split(" ")
        # ads index to list
        a.append(i+1)
        # make list of int and appends
        listRQP.append(list(map(int, a)))
    return [first, listRQP]

def foo(nazwa):

    [first, listRQP] = read_from_file(nazwa)

    # ------------------- sort -----------------------

    listRQP_sortedR = sortR(listRQP.copy())
    listRQP_sortedRQ = sortRQ(listRQP.copy())

    c_max_v = c_max(listRQP, first[0])
    c_max_v1 = c_max(listRQP_sortedR, first[0])
    c_max_v2 = c_max(listRQP_sortedRQ, first[0])

    # ------------------ Write To File -----------------------
    print(nazwa, c_max_v, c_max_v1, c_max_v2)

    fw = open("output_" + nazwa, "w+")

    fw.write(str(c_max_v ) + " " + str(c_max_v1) + " " + str(c_max_v2) + "\n")
    for i in listRQP:
        fw.write(str(i[3]) + " ")
    fw.write("\n")

    for i in listRQP_sortedR:
        fw.write(str(i[3]) + " ")
    fw.write("\n")

    f = open(nazwa,"r")
    first = (' '.join(f.readline().split())).split(" ") # reduces spaces for first line and make list
    listRQP = []

    # Based on data from first line
    for i in range( int(first[0]) ):
        # reduce spaces
        a = ' '.join(f.readline().split())
        # deletes \n on the end
        a = a.replace("\n", "")
        #  make list
        a = a.split(" ")
        # ads index to list
        a.append(i+1)
        # make list of int and appends
        listRQP.append(list(map(int, a)))

    fw.close()
    f.close()

