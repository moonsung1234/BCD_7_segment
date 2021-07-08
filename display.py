
from tkinter import *
import BCDpy

window = Tk()

window.title("BCD 7 segment")
window.geometry("300x400")
window.resizable(False, False)

a = (100, 50, 200, 60)
f = (90, 60, 100, 160)
b = (200, 60, 210, 160)
g = (100, 160, 200, 170)
e = (90, 170, 100, 270)
c = (200, 170, 210, 270) 
d = (100, 270, 200, 280) 

canvas = Canvas(window, width=300, height=400)

canvas.create_rectangle(a, fill="white") # a
canvas.create_rectangle(f, fill="white") # f
canvas.create_rectangle(b, fill="white") # b
canvas.create_rectangle(g, fill="white") # g
canvas.create_rectangle(e, fill="white") # e
canvas.create_rectangle(c, fill="white") # c
canvas.create_rectangle(d, fill="white") # d
canvas.pack()

while True :
    _input = int(input())
    
    _a, _f, _b, _g, _e, _c, _d = BCDpy.getAllSegments(_input)
    list1 = (_a, _f, _b, _g, _e, _c, _d)
    list2 = (a, f, b, g, e, c, d)

    for i in range(len(list1)) :
        if list1[i] == 1 :
            canvas.create_rectangle(list2[i], fill="blue")

        else :
            canvas.create_rectangle(list2[i], fill="white")         

window.mainloop()