import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Calculator')
root.geometry("400x400")
# label = tk.Label(root,text="0",font=("Arial",24),bg="black",fg='white', width=71, anchor="e")
label = tk.Label(root, text="Akash Kumar Singh", font=("Algerian",26), bg="black", fg='white', anchor="e")
label.grid(column=0, row=0, columnspan=5, sticky='NSEW')
for i in range(4):
    root.columnconfigure(i,weight=1)
root.rowconfigure(10,weight=1)

btn_1 = tk.Button(root,text="1",font=("Algerian",24),bg="black",fg="white")
btn_1.grid(column=0,row=1,columnspan=1,rowspan=1,sticky="NSEW")
btn_2 = tk.Button(root,text="2",font=("Algerian",24),bg="black",fg="white")
btn_2.grid(column=1,row=1,columnspan=1,rowspan=1,sticky="NSEW")
btn_3 = tk.Button(root,text="3",font=("Algerian",24),bg="black",fg="white")
btn_3.grid(column=2,row=1,columnspan=1,rowspan=1,sticky="NSEW")
btn_d = tk.Button(root,text="/",font=("Algerian",24),bg="black",fg="white")
btn_d.grid(column=3,row=1,columnspan=1,rowspan=1,sticky="NSEW")
# label.pack()
root.mainloop()