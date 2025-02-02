from tkinter import *
from tkinter import messagebox

def fun():
    pwd = e.get()
    if(len(pwd)==0):
        messagebox.showinfo("Warning", "Empty password is not accepted")
    print(pwd)
    f = open("D:\Drowsiness detection\ptext.txt", "w")
    f.write(pwd)
    f.close()

frame = Tk()
frame.geometry('450x400')
frame.title("Encryption Password")

l = Label(text="Enter password for encryption").place(x=145,y=75)
e = Entry(frame,show='*',font=('Arial', 14))
e.pack(padx=112.5,pady=120)
b = Button(frame,text="Submit",bg="light blue",height=1,width=10,command=fun).place(x=177.5,y=165)


frame.mainloop()
