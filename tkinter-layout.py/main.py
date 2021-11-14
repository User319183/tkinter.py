import sys
from tkinter import *
import time

def sathvik():
    toppiece=str("Check out my website at https://sathvik.website")
    configuration.config(text=toppiece)


root  = Tk()
root.geometry("1200x500")
configuration=Label(root,font=("times",50,"bold"),bg="lightblue")
configuration.grid(row=2,column=2,pady=25,padx=100)
sathvik()



top_part = Label(root,text="This is a message!",font="times 24 bold")
top_part.grid(row=0,column=2)


footer=Label(root,text="This code has been created by Sathvik. View the other github repositories created by me at https://github.com/User319183 ", font="times 15 bold")

footer.grid(row=3,column=2)

root.mainloop()
