import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def minions(event):
    print(event)
    p.playsound("Minions - Stuarts & Dave official teaser trailer(2015) Despicable Me 3.mp3")
    
def Superidol(event):
    print(event)
    p.playsound("Dancing Funeral Coffin MeMe - Original Ful Version 1080p.mp3")

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
l2 = tk.Button(win, text="gegagedigedagedago",width=20)
l2.bind("<Button>", minions)
l3 = tk.Button(win, text="",width=20)
l3.bind("<Button>", )
l4 = tk.Button(win, text="",width=20)
l4.bind("<Button>", )
l5 = tk.Button(win, text="",width=20)
l5.bind("<Button>", )
l6 = tk.Button(win, text="",width=20)
l6.bind("<Button>", Superidol)
l7 = tk.Button(win, text="",width=20)
l7.bind("<Button>", headshot)


win.mainloop()