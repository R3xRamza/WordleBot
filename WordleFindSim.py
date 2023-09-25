
def findSim(lastDict):
    for x in range(len(lastDict)):
        i = lastDict[x]
        for j in lastDict[x:]:
            if i != j:
                runSimCheck(i,j)

def runSimCheck(x,y):
    

findSim(['goose', 'noose', 'moose', 'whose'])


