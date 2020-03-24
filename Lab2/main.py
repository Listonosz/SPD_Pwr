import os
import heapq

def sortbyR(RPQ):
    RPQ.sort(key = lambda x: x[1])
    return RPQ

def sortbyRQ(RPQ):
    return RPQ.sort(key = lambda x: [x[1],x[3]])

def getRPQtime(RPQ, fullInfo = False):
    S = []
    C = []
    S.append(RPQ[0][1])
    C.append(S[0]+RPQ[0][2])
    Cmax = C[0]+ RPQ[0][3]

    for j in range(len(RPQ)-1):
        k = j + 1
        S.append(max(RPQ[k][1], C[j]))
        C.append(S[k] + RPQ[k][2])
        Cmax = max(Cmax, C[k] + RPQ[k][3])

    if fullInfo: return [Cmax,S]
    else: return Cmax


def loadRPQfromdataDirectory(nazwa):
    file_handler = open(os.getcwd()+'/dataIN/'+nazwa, 'r')
    file_data = file_handler.readlines()
    RPQ = list()
    i = 0
    for line in file_data:
        newline = list(map(int, line.split()))
        newline.insert(0, i)
        i += 1
        if( len(newline) != 4):
            continue
        RPQ.append(newline)
    return RPQ

def loadRPQfromFile(file_handler):
    file_data = file_handler.readlines()
    RPQ = list()
    i = 0
    for line in file_data:
        newline = list(map(int, line.split()))
        newline.insert(0, i)
        i += 1
        if( len(newline) != 4):
            continue
        RPQ.append(newline)
    return RPQ

def getfilesfromDirectory():
    path = os.getcwd()
    fileList = []
    with os.scandir(path+"/dataIN/") as dire:
        for files in dire:
            fileList.append(files.name)
    return fileList

def writetoFile(filename, output):
    outFileName = os.getcwd() + "/dataOUT/" + "OUT" + filename
    fOut = open(outFileName, 'w')
    fOut.write(output)
    fOut.close()

def findRmin(RPQ, getFullRecord=False):
    RPQ_ = RPQ.copy()
    sortbyR(RPQ_)
    if not getFullRecord: return RPQ_[0][1]
    else: return RPQ_[0]
#Return full RQP line, with smallest R

def findQmax(RPQ, getFullRecord=False):
    RPQ_ = RPQ.copy()
    RPQ_.sort(key= lambda x: x[3], reverse=True)
    if not getFullRecord: return RPQ_[0][3]
    else: return RPQ_[0]
#Return full RQP line, with biggest Q

def Schrage(RPQ, fullInfo=False):
    result = []
    result_onlyID = []
    k = 1
    G = []
    N = RPQ.copy()
    t = findRmin(N)
    Cmax = 0
    while ( (len(G) != 0) or (len(N) != 0)):
        while((len(N) != 0) and findRmin(N) <= t):
            cJob = findRmin(N, 1)
            G.append( cJob )
            N.remove( cJob )
        if(len(G) != 0):
            cJob = findQmax(G, 1)
            G.remove( cJob )
            result.insert(k, cJob)
            result_onlyID.insert(k, cJob[3])
            t = t + cJob[2]
            k = k + 1
            Cmax = max(Cmax,t+cJob[3])
        else:
            t = findRmin(N)
    if fullInfo: return [result, Cmax]
    else: return Cmax

def SchragePMTN(RPQ, fullInfo=False):
    Cmax = 0
    Ng = []
    Nn = RPQ.copy()
    t = 0
    l = [0,0,0,9999999]
    while( len(Ng) !=0 or len(Nn) != 0 ):
        while( len(Nn) != 0 and findRmin(Nn) <= t):
            cJob = findRmin(Nn, 1)
            Ng.append(cJob)
            Nn.remove(cJob)
            if cJob[3] > l[3]:
                l[2] = t - cJob[1]
                t = cJob[1]
                if l[2] > 0:
                    Ng.append(l)
        if len(Ng) != 0:
            cJob = findQmax(Ng, 1)
            Ng.remove(cJob)
            l = cJob.copy()
            t = t + cJob[2]
            Cmax = max(Cmax, t+cJob[3])
        else:
            t = findRmin(Nn)
    return Cmax

def SchrageHEAPQ(RPQ):
    result = []
    k = 1
    G = list()
    N = RPQ.copy()
    heapq.heapify(G)
    Cmax = 0
    t = heapq.nsmallest(1, N, key=lambda x: x[1])[0][1]
    while( len(G) != 0 or len(N) != 0):
        while( len(N) != 0  and heapq.nsmallest(1, N, key=lambda x: x[1])[0][1] <= t):
            cJob = heapq.nsmallest(1, N, key=lambda x: x[1])[0]
            heapq.heappush(G, cJob)
            N.remove(cJob)

        if( len(G) != 0 ):
            cJob = heapq.nlargest(1, G, key=lambda x: x[3])[0]
            G.remove(cJob)
            result.append(cJob)
            t = t + cJob[2]
            k = k +1
            Cmax = max(Cmax,t+cJob[3])
        else:
            t = heapq.nsmallest(1, N, key=lambda x: x[1])[0][1]
    return [result, Cmax]

def SchrageHEAPQPMTN(RPQ):
    Cmax = 0
    Ng = []
    Nn = RPQ.copy()
    heapq.heapify(Ng)
    t = 0
    l = [0,0,0,9999999]
    while( len(Ng) !=0 or len(Nn) != 0 ):
        while( len(Nn) != 0 and heapq.nsmallest(1, Nn, key=lambda x: x[1])[0][1]  <=  t ):
            cJob = heapq.nsmallest(1, Nn, key=lambda x: x[1])[0]
            heapq.heappush(Ng, cJob)
            Nn.remove(cJob)
            if cJob[3] > l[3]:
                l[2] = t - cJob[1]
                t = cJob[1]
                if l[2] > 0:
                    heapq.heappush(Ng, l)
        if len(Ng) != 0:
            cJob = heapq.nlargest(1, Ng, key=lambda x: x[3])[0]
            Ng.remove(cJob)
            l = cJob.copy()
            t = t + cJob[2]
            Cmax = max(Cmax, t+cJob[3])
        else:
            t = heapq.nsmallest(1, Nn, key=lambda x: x[1])[0][1]
    return Cmax



def produceOutput(result, Cmax):
    output = "Kolejność: "
    for record in result:
        output += str(record[0]) + " "
    output += "\n"
    output += "czas: " + str(Cmax)
    return output

# filelist = getfilesfromDirectory()
# filelist.sort()
# for i in range(7):
#     RPQ = loadRPQfromFile(filelist[i])
#     print(filelist[i])
#     [schragen, t] = Schrage(RPQ,1)
#     output = produceOutput(schragen, t)
#     writetoFile(filelist[i], output)

test2 = open("in200.txt", 'r')
rrr = loadRPQfromFile(test2)
t_c = SchrageHEAPQPMTN(rrr)
# out = produceOutput(res, t_c)
print(t_c)