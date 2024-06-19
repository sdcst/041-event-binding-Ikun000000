import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def minions(event):
    print(event)
    p.playsound("Minions - Stuarts & Dave official teaser trailer(2015) Despicable Me 3.mp3")
    
def dancing(event):
    print(event)
    p.playsound("Dancing Funeral Coffin MeMe - Original Ful Version 1080p.mp3")

def chicken(event):
    print(event)
    p.playsound("Chickens Talking.mp3")
    
def dog(event):
    print(event)
    p.playsound("Beagle Barking.mp3")
    
def cat(event):
    print(event)
    p.playsound("Black cat meowing.mp3")

win = tk.Tk()
win.title()

l1 = tk.Label(win,text="Press any button to play a sound")
l2 = tk.Button(win, text="minions", relief=GROOVE, width=20)
l2.bind("<Button>",minions)
l3 = tk.Button(win, text="dacing",relief=GROOVE,width=20)
l3.bind("<Button>", dancing)
l4 = tk.Button(win, text="chicken",relief=GROOVE,width=20)
l4.bind("<Button>", chicken)
l5 = tk.Button(win, text="dog",relief=GROOVE,width=20)
l5.bind("<Button>", dog)
l6 = tk.Button(win, text="cat",relief=GROOVE,width=20)
l6.bind("<Button>", cat)

l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)


win.mainloop()