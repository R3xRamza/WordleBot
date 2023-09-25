from filecmp import clear_cache
import WordleDoc as wd
from collections import Counter
import sys
import random
import operator

print("\n\n")
sys.setrecursionlimit(5000)

allist = wd.Ma + wd.Ta
alllistLen = len(allist)-1
idealWordDict = {}
posWord = wd.Ma[:]
xlis = wd.Ma[:]


wordle = random.choice(wd.Ma)
#print(wordle)

def guesWord(wor,worde):
    worList = []
    checkLet = 0
    for x in range(len(wor)):
        if wor[x] == worde[x]:
            worList.append(tuple((wor[x],2)))
        elif wor[x] in worde:
            worList.append(tuple((wor[x],1)))
        else:
            worList.append(tuple((wor[x],0)))
    return worList

# def getProb(guess):
#     stc = ""
#     h=0
#     for i in xlis:
#         stc += i
#     letterCount = dict(Counter(stc))
#     for i in letterCount.values():
#         h+=i
#     for i,j in letterCount.items():
#         letterCount[i] = (j/h)*100
#     letterCount = dict(sorted(letterCount.items(), key=lambda item: item[1]))
#     return letterCount

def getProbPos(ylis):
    propList = {}
    wordlistList = {}
    x = 0
    for i in ylis:
        wordlistList[x] = list(i)
        x+=1
    for i in range(5):
        stac = ""
        for j in wordlistList.items():
            stac += j[1][i]
        propList[i+1] = dict(sorted(dict(Counter(stac)).items(), key=operator.itemgetter(1),reverse=True))
    return propList
    
def checkword(lis,x,guestWord):
    if x >=0:
        i = lis[x]
        letList = list(i)
        xyv = 0
        for j in guestWord:
            if j[1] == 0 and j[0] in letList:
                if i in xlis:
                    xlis.remove(i)
            if j[1] == 1 and j[0] not in letList:
                if i in xlis:
                    xlis.remove(i)
            if j[1] == 1 and letList[xyv] == j[0]:
                if i in xlis:
                    xlis.remove(i)
            if j[1] == 2 and letList[xyv] != j[0]:
                if i in xlis:
                    xlis.remove(i)
            xyv +=1
        checkword(lis,x-1,guestWord)

def idealWord(posDict):
    bestWordDict = {}
    for i in list(posDict[1].keys())[:7]:
        for j in list(posDict[2].keys())[:7]:
            for k in list(posDict[3].keys())[:7]:
                for l in list(posDict[4].keys())[:7]:
                    for m in list(posDict[5].keys())[:7]:
                        guy = i + j + k + l + m
                        if guy in wd.Ma or guy in wd.Ta:
                            wordScore = posDict[1][i] + posDict[2][j] + posDict[3][k] + posDict[4][l] + posDict[5][m]
                            for x in guy:
                                if guy.count(x)>=2:
                                    wordScore/=2**(1/2)
                            bestWordDict[guy] = int(wordScore)
    bWD = dict(sorted(bestWordDict.items(),key=operator.itemgetter(1),reverse=True))
    return bWD


    
# def bestWordinList(x):
    # if x < alllistLen:
    #     guy = allist[x]
    #     wordScore = 1
    #     for i in guy:
    #         if guy.count(i)>=2:
    #             wordScore/=2
        
    #     #dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    #     bestWordinList(x+1)
        
    # if x == alllistLen:
    #     return idealWordDict
    #     idealWordDict = {}

numofGues = 0

def runWordle(worde):
    global numofGues
    global xlis 
    firsgues = "irate"
    xlis = wd.Ma[:]
    print("\n\n")
    print(worde + "\n")
    print(firsgues)
    gues1 = guesWord(firsgues,worde)
    checkword(posWord,len(posWord)-1,gues1)
    numofGues+=1
    if firsgues != worde:
        secondGues = list(idealWord(getProbPos(xlis)).keys())[0]
        gues2 = guesWord(secondGues,worde)
        print(xlis)
        print(secondGues)
        checkword(posWord,len(posWord)-1,gues2)
        numofGues+=1
        if secondGues != worde:
            thirdGues = list(idealWord(getProbPos(xlis)).keys())[0]
            gues3 = guesWord(thirdGues,worde)
            print(xlis)
            print(thirdGues)
            checkword(posWord,len(posWord)-1,gues3)
            numofGues+=1
            if thirdGues != worde:
                forGues = list(idealWord(getProbPos(xlis)).keys())[0]
                gues4 = guesWord(forGues,worde)
                print(xlis)
                print(forGues)
                checkword(posWord,len(posWord)-1,gues4)
                numofGues+=1
                if forGues != worde:
                    fivGues = list(idealWord(getProbPos(xlis)).keys())[0]
                    gues5 = guesWord(fivGues,worde)
                    print(xlis)
                    print(fivGues)
                    checkword(posWord,len(posWord)-1,gues5)
                    numofGues+=1
                    if fivGues != worde:
                        sixGues = list(idealWord(getProbPos(xlis)).keys())[0]
                        gues6 = guesWord(sixGues,worde)
                        print(xlis)
                        print(sixGues)
                        checkword(posWord,len(posWord)-1,gues6)
                        numofGues+=1



for i in range(3000):
    runWordle(random.choice(wd.Ma))
    print(numofGues/(i+1))

print("\n\n")
