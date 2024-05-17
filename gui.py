# olly stuff
import tkinter as tk
import time
import random
import sort

print(sort)
root = tk.Tk()
root.configure(bg="white")
root.title = "Sorting"
n = len(sort.items)
root.geometry(f"{n * 14 + 20}x{n * 10 + 50}")

label = tk.Label(root, text="Sorting Algorithm")
label.configure(bg="white", fg="black", border="10", borderwidth="10", )
label.pack(side="top")
print(label.winfo_width())
frames = []
for i in sort.items:
    frame = tk.Frame(root, width=10, height=(i + 1)*10)
    frame.place(x=14 + i * 14, y=-10, relx=0, rely=1.0, anchor="sw")
    frames.append(frame)
random.shuffle(sort.items)
j = 0
for i in sort.items:
    frames[j].place(x=14 + i * 14, y=-10, relx=0, rely=1.0, anchor="sw")
    j += 1

def bogo():
    sort.sort()
    print(sort.items)
    j = 0
    for i in sort.items:
        frames[j].place(x=14 + i * 14, y=-10, relx=0, rely=1.0, anchor="sw")
        j += 1
    if CheckSort(sort.items):
        print("yippe!")
        root.mainloop()
    else:
        root.after(1, bogo)



def CheckSort(arr):
    j = 0
    for i in arr:
        print(i, j)
        if i == j:
            j+= 1
        else:
            return False
    return True

root.after(2000, bogo)
root.mainloop()

