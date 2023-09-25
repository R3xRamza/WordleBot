import re
from collections import Counter
import operator
import WordleDoc as wd

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




wordlist1 = ['goner', 'foyer', 'boxer', 'corer', 'roger', 'poker', 'joker', 'homer', 'lover', 'rover', 'cover','hover', 'mover']
l = []
for i in wd.Ma:
    f = re.match(r"k+.*v+",i)
    if f:
        l.append(i)
print(l)

def formRegex(wordlist):
    reggy = ""
    posDict = getProbPos(wordlist)
    print(posDict.values())
    for i in posDict.values():
        if len(list(i)) == 1:
            reggy += list(i.keys())[0]
        else:
            reggy += "."
    return reggy

x = formRegex(wordlist1)
print(x)
print(re.findall(x,str(wordlist1)))