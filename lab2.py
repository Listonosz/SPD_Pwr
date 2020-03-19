import lab1

def getP(job):
    return job[0]

def getQ(job):
    return job[2]

def sortR(RPQ):
    RPQ_ = RPQ.copy()
    RPQ_.sort(key=getP)
    return RPQ_

def sortQ(RPQ):
    RPQ_ = RPQ.copy()
    RPQ_.sort(reverse=True, key=getQ)
    return RPQ_

def findRmin(RPQ, getFullRecord=False):
    RPQ_ = sortR(RPQ)
    return RPQ_[0]
#Return full RQP line, with smallest R

def findQmax(RPQ, getFullRecord=False):
    RPQ_ = sortQ(RPQ)
    return RPQ_[0]
#Return full RQP line, with biggest Q

def Schrage(listofJobs):
    result = []
    k = 1
    G = []
    N = listofJobs.copy()
    t = findRmin(N)[0]
    while ( (len(G) != 0) or (len(N) != 0)):
        while((len(N) != 0) and (findRmin(N)[0] <= t)):
            cJob = findRmin(N)
            G.append( cJob )
            N.remove( cJob )
        if(len(G) != 0):
            cJob = findQmax(G)
            G.remove( cJob )
            result.append( cJob )
            t = t + cJob[1]
            k = k + 1
        else:
            t = findRmin(N)[0]
    
    return [result, t]

spr20 = [16, 10, 18, 7, 5, 19, 8, 6, 2, 13, 11, 4, 12, 1, 3, 17, 20, 15, 9, 14]
spr50 = [4, 42, 36, 33, 1, 48, 37, 28, 43, 24, 49, 38, 10, 14, 27, 41, 46, 22, 11, 7, 15, 30, 9, 20, 23, 25, 6, 29, 32, 34, 31, 40, 17, 50, 19, 35, 2, 26, 45, 18, 3, 16, 21, 12, 44, 39, 47, 8, 5, 13]
time20 = 1309
time50 = 1513

[firstLine_, listofJobs_] = lab1.read_from_file("data20.txt")

[wynik, czas] = Schrage(listofJobs_)
result_vec = []
for listy in wynik:
    result_vec.append(listy[3])

print(result_vec, "Time:", czas)
print(spr20, "Time:", time20)
