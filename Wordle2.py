import random
import tkinter as tk

f = open('WordleDoc.txt', 'r')
wordList = f.read()
f.close()



test = wordList
li = list(test.split(','))

listlen = len(li)
for i in range(listlen):
    x = li[i-1]
    li[i-1] = x[1:6]

## li = word list

wordChose = random.choice(li)

print(wordChose)

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(master=window)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Text(master=frame, width=10,height=5)
        label.pack(padx=5, pady=5)

window.mainloop()




