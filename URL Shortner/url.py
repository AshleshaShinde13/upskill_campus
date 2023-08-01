import pyshorteners
from tkinter import *

win = Tk()
win.geometry("500x370")
win.configure(bg="light blue")

#button functioning
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.insert(END,s)

#label for entering user url
Label(win, text="Enter your URL", font= "impack 16 ", bg= "black", fg= "white").pack(fill="x")

#enter box
entry1= Entry(win, font="12", bd=3, width=50)
entry1.pack(pady=40)

#button
Button(win, text="Click me", font="impack 12", bg="blue", fg="white", width="15", command=short).pack()

#entry
entry2= Entry(win, font="impack 16 bold", bg="light blue", width = 24, bd=0)
entry2.pack(pady=30)
mainloop()