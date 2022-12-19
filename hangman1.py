from tkinter import *
from string import ascii_uppercase
import random
import tkinter.messagebox
print('Welcome to Hangman')
print('It is a region of Kyrgyzstan')


window=Tk()
window.title("Hangman")


word_list=["BISHKEK","OSH","JALAL-ABAD","TALAS","BATKEN","NARYN","ISSYK-KUL"]


photos = [PhotoImage(file="hangman2/hang0.png"),PhotoImage(file="hangman2/hang1.png"),PhotoImage(file="hangman2/hang2.png"),
          PhotoImage(file="hangman2/hang3.png"),PhotoImage(file="hangman2/hang4.png"),PhotoImage(file="hangman2/hang5.png"),
          PhotoImage(file="hangman2/hang6.png"),PhotoImage(file="hangman2/hang7.png"),PhotoImage(file="hangman2/hang8.png"),
          PhotoImage(file="hangman2/hang9.png"),PhotoImage(file="hangman2/hang10.png"),PhotoImage(file="hangman2/hang11.png")]



def newGame():
    global the_word_withSpaces
    global number0fGuesses
    number0fGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global number0fGuesses
    if number0fGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    tkinter.messagebox.showinfo("Hangman","You guessed it!")
                    newGame()
        else:
            number0fGuesses+=1
            imgLabel.config(image=photos[number0fGuesses])
            if number0fGuesses==11:
                tkinter.messagebox.showwarning("Hangman","Game Over")
                  
            
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord,font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

n=0
for c in ascii_uppercase:
    Button(window,text=c, command=lambda c=c: guess(c),font=("Helvetica 18"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(),font=("Helvetica 10 bold")).grid(row=3, column=8, sticky='NSWE')
    
newGame()
window.mainloop()
