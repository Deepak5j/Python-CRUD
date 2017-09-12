from Tkinter import *
from ttk import *
import sqlite3
from time import sleep
import ttk
import tkMessageBox

root = Tk()
root.title("Band Data")
root.resizable(width=False, height=False);

mainframe = Frame(root)                                 
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 50, padx = 80)

var = StringVar(root)

# Use dictionary to map names to ages.
choices = {
    "Australia":"1",
    "Bangladesh":"2",
    "France":"4",    
    "Germany":"5",
    "India":"3",
    "":""
    }

option = OptionMenu(mainframe, var, *choices)
var.set('Select Country')

option.grid(row = 1, column =1)

Label(mainframe, text="Country ID").grid(row = 2, column = 1)

age = StringVar()
# Bind age instead of var
age_ent = Entry(mainframe, text=age, width = 15).grid(column = 2, row = 2)

# change_age is called on var change.
def change_age(*args):
    age_ = choices[var.get()]
    age.set(age_)
    show(age_)
    #clear()
    
# trace the change of var
var.trace('w', change_age)
    
def show(x):
    var = StringVar()
    label = Message( root, textvariable=var, relief=RAISED, padx=5, pady=5, takefocus=True,justify=LEFT)
    txt = ""
    conn = sqlite3.connect('wp.db')
    try:
        cursor = conn.execute("SELECT * FROM  radios where id=?",(x))
        exist = cursor.fetchone()
        
        if exist is None:
            #print "Data not found"
            tkMessageBox.showinfo("Message","Data not found")
        else:
            cursor = conn.execute("SELECT * FROM  radios where id=?",(x))
            for row in cursor:
                txt += "ID: " + str(row[0]) + "\n" + "IP: " + str(row[1]) + "\n" + "DSP: " + str(row[2])
            var.set(txt)
            label.pack(side=BOTTOM,anchor=N)
            B = Button(label, text =txt, command = clear)
            B.pack()
    except sqlite3.Error as mess:
      tkMessageBox.showinfo("Message",mess)
def clear():
    list = root.pack_slaves()
    a = ""
    for l in list:
        a=l
    a.destroy()

#frame.destroy()
#frame.pack_forget()
#frame.grid_forget()

root.mainloop()
