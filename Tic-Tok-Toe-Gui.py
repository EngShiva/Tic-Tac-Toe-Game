from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")
root.resizable(False,False)
root.iconbitmap('ttt_icon.ico')

x_click=True
count=0
winner=False

def btn_click(btn):
    global x_click,count
    if(btn["text"]=="" and x_click==True):
        btn["text"]='X'
        x_click=False
        count+=1
        check_winner('X')
    elif(btn["text"]=="" and x_click==False):
        btn["text"]="O"
        x_click=True
        count+=1
        check_winner('O')
    else:
        messagebox.showerror("Tic Tac Toe Error","You clicked the wrong button!!")

def check_winner(s):
    global winner
    if(b1["text"]==s and b2["text"]==s and b3["text"]==s):
        b1["bg"]='light green';b2["bg"]='light green';b3["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b4["text"]==s and b5["text"]==s and b6["text"]==s):
        b4["bg"]='light green';b5["bg"]='light green';b6["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b7["text"]==s and b8["text"]==s and b9["text"]==s):
        b7["bg"]='light green';b8["bg"]='light green';b9["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b1["text"]==s and b4["text"]==s and b7["text"]==s):
        b1["bg"]='light green';b4["bg"]='light green';b7["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b2["text"]==s and b5["text"]==s and b8["text"]==s):
        b2["bg"]='light green';b5["bg"]='light green';b8["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b3["text"]==s and b6["text"]==s and b9["text"]==s):
        b3["bg"]='light green';b6["bg"]='light green';b9["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(b1["text"]==s and b5["text"]==s and b9["text"]==s):
        b1["bg"]='light green';b5["bg"]='light green';b9["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()

    elif(b3["text"]==s and b5["text"]==s and b7["text"]==s):
        b3["bg"]='light green';b5["bg"]='light green';b7["bg"]='light green'
        winner=True
        s='Congratulation '+s+', You Won'
        messagebox.showinfo("Tic Tac Toe Winner",s)
        Restart_Game()
        
    elif(count==9 and winner==False):
        messagebox.showinfo("Tic Tac Toe Winner","uffs, No One Wins...")
        Restart_Game()

def Restart_Game():
    global x_click,count,winner
    count=0;x_click=True;winner=False
    b1["text"]="";b1["bg"]="yellow"
    b2["text"]="";b2["bg"]="yellow"
    b3["text"]="";b3["bg"]="yellow"
    b4["text"]="";b4["bg"]="yellow"
    b5["text"]="";b5["bg"]="yellow"
    b6["text"]="";b6["bg"]="yellow"
    b7["text"]="";b7["bg"]="yellow"
    b8["text"]="";b8["bg"]="yellow"
    b9["text"]="";b9["bg"]="yellow"

#Frames
f1=Frame(root,bg='purple')
f2=Frame(root,bg='purple')
f3=Frame(root,bg='purple')

#Buttons
b1=Button(f1,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b1))
b2=Button(f1,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b2))
b3=Button(f1,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b3))

b4=Button(f2,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b4))
b5=Button(f2,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b5))
b6=Button(f2,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b6))

b7=Button(f3,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b7))
b8=Button(f3,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b8))
b9=Button(f3,text="",bd=10,font=("verdana",60),height=1,width=3,bg='yellow',command= lambda: btn_click(b9))

b1.pack(side=LEFT,padx=10,pady=10)
b2.pack(side=LEFT,padx=10,pady=10)
b3.pack(side=LEFT,padx=10,pady=10)

b4.pack(side=LEFT,padx=10,pady=10)
b5.pack(side=LEFT,padx=10,pady=10)
b6.pack(side=LEFT,padx=10,pady=10)

b7.pack(side=LEFT,padx=10,pady=10)
b8.pack(side=LEFT,padx=10,pady=10)
b9.pack(side=LEFT,padx=10,pady=10)

f1.pack()
f2.pack()
f3.pack()

root.mainloop()

'''#Labels and Entries
Player1=Label(text="Player1").grid(row=0,column=0)
Player2=Label(text="Player2").grid(row=1,column=0)
E_Player1=Entry(root,bd=5).grid(row=0,column=1)
E_Player2=Entry(root,bd=5).grid(row=1,column=1)'''

'''b=[[0,0,0 ],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(text="",font=("verdana",60),height=1,width=3,bg='red')
        print(b[)
        b[i][j].configure(command= lambda: btn_click(b[i][j]))
        b[i][j].grid(row=i,column=j)'''


