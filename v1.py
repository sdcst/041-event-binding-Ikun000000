import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def minions(event):
    print(event)
    p.playsound("Minions - Stuarts & Dave official teaser trailer(2015) Despicable Me 3.mp3")
    
def Superidol(event):
    print(event)
    p.playsound("")

def fbi(event):
    print(event)
    p.playsound("")
    
def scream(event):
    print(event)
    p.playsound("")
    
def jesus(event):
    print(event)
    p.playsound("")

def headshot(event):
    print(event)
    p.playsound("")

win = tk.Tk()
win.title()

l1 = tk.Label(win,text="Press any button to play a sound")
l2 = tk.Button(win, text="gegagedigedagedago", relief=GROOVE, width=20)
l2.bind("<Button>", minions)
l3 = tk.Button(win, text="",relief=GROOVE,width=20)
l3.bind("<Button>", )
l4 = tk.Button(win, text="",relief=GROOVE,width=20)
l4.bind("<Button>", )
l5 = tk.Button(win, text="",relief=GROOVE,width=20)
l5.bind("<Button>", )
l6 = tk.Button(win, text="",relief=GROOVE,width=20)
l6.bind("<Button>", Superidol)
l7 = tk.Button(win, text="",relief=GROOVE,width=20)
l7.bind("<Button>", headshot)

l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)
l7.grid(row=3, column=3)


win.mainloop()