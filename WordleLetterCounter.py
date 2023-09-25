from collections import Counter
import WordleDoc as wd

stc = ""
for i in wd.Ma:
   stc += i

c = Counter(stc)
#print(dict(c))


x=0

letterCount = {'e': 1233, 'a': 979, 'r': 899, 'o': 754, 't': 729, 'l': 719,
               'i': 671, 's': 669, 'n': 575, 'c': 477, 'u': 467, 'y': 425,
               'd': 393, 'h': 389, 'p': 367, 'm': 316, 'g': 311, 'b': 281,
               'f': 230, 'k':210, 'w': 195, 'v': 153, 'z': 40, 'x': 37, 'q': 29, 'j': 27}


for i in letterCount.values():
    x+=i
    
for i,j in letterCount.items():
    letterCount[i] = j/x

#print(letterCount)

n = "shift"

if n in wd.Ta:
   print(n)
