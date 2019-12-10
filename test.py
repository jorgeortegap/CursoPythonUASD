from tkinter import *
import sqlite3

conn = sqlite3.connect('phonebook.db')  # establish connection
c = conn.cursor()  # create cursor

c.execute(  # create a table if one does not exist
    '''CREATE TABLE IF NOT EXISTS PHONEBOOK
		( PHONE INT PRIMARY KEY, \
		  NAME TEXT \
		  )'''
)
conn.commit()


tk = Tk()
tk.title("Phonebook Application")


def main():
    label = Label(tk, text="Select an option from the menu above.")
    label.pack()

    f = Frame(tk, width=200, height=200)
    f.pack()

    close_button = Button(tk, text="Close", command=tk.quit)
    close_button.pack()

    menubar = Menu(tk)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add New Entry", command=lambda: addEntry(f))
    filemenu.add_command(label="Lookup Entry", command=lambda: listEntry(f))
    filemenu.add_command(label="List All Entries",
                         command=lambda: listEntries(f))
    filemenu.add_command(label="Quit", command=tk.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    tk.config(menu=menubar)

    tk.mainloop()


def addEntry(frame):
    clearFrame(frame)
    label = Label(frame, text="Name")
    label.pack()
    name = Entry(frame)
    name.pack()

    label2 = Label(frame, text="Phone Number")
    label2.pack()
    phone = Entry(frame)
    phone.pack()

    b = Button(frame, text="Add Entry",
               command=lambda: addEntryProcess(name.get(), phone.get()))
    b.pack()


def listEntry(frame):
    clearFrame(frame)
    label = Label(frame, text="Enter a number to lookup: ")
    label.pack()
    phone = Entry(frame)
    phone.pack()
    b = Button(frame, text="Look up", command=lambda: lookupEntry(phone.get()))
    b.pack()

# list all entries in database


def listEntries(frame):
    clearFrame(frame)
    c.execute('SELECT * FROM Phonebook')
    allData = c.fetchall()
    print(allData)

# insert entry into database


def addEntryProcess(name, phone):
    c.execute("INSERT INTO PHONEBOOK (PHONE, NAME) VALUES(" +
              phone + ", '" + name + "')")
    conn.commit()
    print("\n(%s,%s) has been added to the phonebook!\n" % (phone, name))

# lookup an entry


def lookupEntry(phone):
    c.execute(' SELECT * FROM Phonebook WHERE phone = ' + phone)
    lookUp = c.fetchall()
    print(lookUp)


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


if __name__ == "__main__":
    main()

conn.close()
