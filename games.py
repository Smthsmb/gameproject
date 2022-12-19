from tkinter import *
import os

window=Tk()
window.title('games')
window.geometry('400x400')
window.configure(bg='white')

l=Label(window,text='Welcome!')
l.pack()

def x():
    os.system('hangman1.py')

b=Button(window,text='Hangman',command=x)
b.pack()

def z():
    os.system('sharik.py')

b2=Button(window,text='sharik',command=z)
b2.pack()

window.mainloop()
