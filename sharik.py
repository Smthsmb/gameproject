import random
from tkinter import *
w = Tk()
w.title ("Поймай шарик")

c = Canvas(w, width=600, height=600,bg='white')
p = Canvas(w, width=600, height=100,bg='green')
c.pack()
p.pack()

colors = ['red','orange','yellow','blue','orange']
count = 0

def ball ():
    c.delete(ALL)
    x = random.randint(10, 580)
    y = random.randint(10,580)
    r = 50
    new_ball = c.create_oval(x,y,x+r,y+r,fill=random.choice(colors),width=0)
    c.tag_bind(new_ball,'<Button-1>',click_on_circle)
    w.after(1500,ball)
    
def click_on_circle(event):
    global count
    count = count + 1
    print(str(count))
    p.delete(ALL)
    p.create_text(80,30, font='Arial 18',text='Попаданий:')
    p.create_text(180,30, font='Arial 20',text=str((count)))
                  
ball()
w.mainloop()
