import sqlite3
from Tkinter import *
import tkMessageBox

def show():
   conn = sqlite3.connect('wp.db')
   flag = 0
   try:
      cursor = conn.execute("SELECT * FROM  radios;")
      exist = cursor.fetchone()
      txt = ""
      if exist is None:
        #print "Data not found"
        tkMessageBox.showinfo("Message","Data not found")
      else:
         cursor = conn.execute("SELECT * FROM  radios;")
         #print "_______________________________________";
         #print "Table contents";
         for row in cursor:
            #print "ID = ", row[0]
            #print "IP = ", row[1]
            #print "DSP = ", row[2], "\n"
            txt += "ID: " + str(row[0]) + "\n" + "IP: " + str(row[1]) + "\n" + "DSP: " + str(row[2]) + "\n\n"
         #print "_______________________________________";
         flag = 1
   except sqlite3.Error as mess:
      #print mess
      tkMessageBox.showinfo("Message",mess)
   if flag == 1:
      root = Tk()
      root.title("Table Data")
      S = Scrollbar(root)
      T = Text(root, height=30, width=30)
      S.pack(side=RIGHT, fill=Y)
      T.pack(side=LEFT, fill=Y)
      S.config(command=T.yview)
      T.config(yscrollcommand=S.set)
      quote = txt
      T.insert(END, quote)
      mainloop(  )
   
'''
   master = Tk()
   whatever_you_do = txt
   msg = Message(master, text = whatever_you_do)
   msg.config(bg='lightgreen', font=('times', 10, 'italic'))
   msg.pack( )
   mainloop( )
'''


fields = 'ID', 'IP', 'DSP'
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def add(entries):
   try:
      conn = sqlite3.connect('wp.db')
      data = []
      for entry in entries:
         text  = entry[1].get()
         data.append(text)
      cursor = conn.execute('insert into radios values (?,?,?)', (data[0],data[1],data[2]))
      conn.commit()
      #print "data added successfuly"
      tkMessageBox.showinfo("Message","data added successfuly")
   except sqlite3.IntegrityError as mess:
      #print mess
      tkMessageBox.showinfo("Message",mess)
   except sqlite3.Error as mess:
      #print mess
      tkMessageBox.showinfo("Message",mess)
      
def create():
   try:
      conn = sqlite3.connect('wp.db')
      cursor = conn.execute('''CREATE TABLE radios
                           (id INTEGER PRIMARY KEY NOT NULL,
                           ip VARCHAR(50),
                           dsp INT)''')
      #print "Table created successuly"
      tkMessageBox.showinfo("Message","Table created successuly")
   except sqlite3.Error as mess:
      #print mess
      tkMessageBox.showinfo("Message",mess)
                  
if __name__ == '__main__':
   root = Tk()
   root.resizable(width=False, height=False);
   root.title("Radio DataBse")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   
   b1 = Button(root, text='Show Data', command=show)
   b1.pack(side=LEFT, padx=15, pady=15)
   
   b2 = Button(root, text='Add Data', command=(lambda e=ents: add(e)))   
   b2.pack(side=LEFT, padx=15, pady=15)

   b3 = Button(root, text='Create Table', command=create)   
   b3.pack(side=LEFT, padx=15, pady=15)
   
   
   b4 = Button(root, text='Quit Interface', command=root.destroy)   
   b4.pack(side=LEFT, padx=15, pady=15)
   root.mainloop()

#   b1 = Button(root, text='Show Data', command=(lambda e=ents: fetch(e)))
#   b1.pack(side=LEFT, padx=5, pady=5)
   
