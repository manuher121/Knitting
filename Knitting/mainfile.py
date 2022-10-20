from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Knitting Organizer")
root.resizable(1, 1)
root.iconbitmap("Knit.ico")

imagen = PhotoImage(file="yarn.gif")
labelimage = Label(root, image=imagen, bd=15, bg="violetred4", relief="groove")
labelimage.place(x=0, y=0)

labelmain = Label(root, text="       ManCam Yarn Organizer       ", bg="light pink", fg="hot pink",
                  font=("Ubuntu", 24), bd=10, relief="raised")
labelmain.place(x=850, y=5)

label1 = Label(root, text="Introduce the yarn brand\n", bg="pale violet red", font=("Arial", 20))
label1.place(x=627, y=80)

label2 = Label(root, text="Introduce the yarn line\n", bg="pale violet red", font=("Arial", 20))
label2.place(x=627, y=125)

label3 = Label(root, text="Introduce the yarn size category\n", bg="pale violet red", font=("Arial", 20))
label3.place(x=627, y=170)

label4 = Label(root, text="Introduce the yarn needle size\n", bg="pale violet red", font=("Arial", 20))
label4.place(x=627, y=215)

label5 = Label(root, text="Introduce the yarn color\n", bg="pale violet red",
               font=("Arial", 20))
label5.place(x=627, y=260)

label6 = Label(root, text="Introduce the yarn fiber content\n", bg="pale violet red",
               font=("Arial", 20))
label6.place(x=627, y=305)

label7 = Label(root, text="Introduce the yarn skein weight\n", bg="pale violet red",
               font=("Arial", 20))
label7.place(x=627, y=350)

label8 = Label(root, text="Introduce the yarn skein quantity\n", bg="pale violet red", font=("Arial", 20))
label8.place(x=627, y=395)

label9 = Label(root, text="ID:", bg="pale violet red",
               font=("Arial", 20))
label9.place(x=627, y=440)

label10 = Label(root, text="Weight:", bg="pale violet red",
                font=("Arial", 20))
label10.place(x=760, y=440)

label11 = Label(root, text="Quantity:", bg="pale violet red",
                font=("Arial", 20))
label11.place(x=950, y=440)

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()

entry1 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e1,
               state="normal")
entry1.place(x=1180, y=80)

entry2 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e2,
               state="normal")
entry2.place(x=1180, y=125)

entry3 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e3,
               state="normal")
entry3.place(x=1180, y=170)

entry4 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e4,
               state="normal")
entry4.place(x=1180, y=215)

entry5 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e5,
               state="normal")
entry5.place(x=1180, y=260)

entry6 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e6,
               state="normal")
entry6.place(x=1180, y=305)

entry7 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e7,
               state="normal")
entry7.place(x=1180, y=350)

entry8 = Entry(root, width=20, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e8,
               state="normal")
entry8.place(x=1180, y=395)

entry9 = Entry(root, width=5, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e9,
               state="disabled")
entry9.place(x=670, y=440)

entry10 = Entry(root, width=5, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e10,
                state="disabled")
entry10.place(x=860, y=440)

entry11 = Entry(root, width=5, font=("Arial", 20), bg="pale violet red1", bd=5, relief="ridge", textvariable=e11,
                state="disabled")
entry11.place(x=1065, y=440)


def submit3():
    es9 = entry9.get()
    if len(es9) != 0:
        option = messagebox.askquestion("Delete", "Are you sure you want to delete the yarn?")
        if option:
            conexion = sqlite3.connect("Yarn.db")
            cursor = conexion.cursor()

            cursor.execute("DELETE FROM Yarn WHERE ID={}".format(es9))

            conexion.commit()
            conexion.close()
            messagebox.showinfo("Deleted", "The yarn you selected was removed!")
            erase()
        else:
            messagebox.showwarning("Warning", "The data was not removed!")


    else:
        messagebox.showerror("Error!", "You must fill the ID square, otherwise it will not be deleted!")
    e9.set("")
    entry1.config(state="normal")
    entry2.config(state="normal")
    entry3.config(state="normal")
    entry4.config(state="normal")
    entry5.config(state="normal")
    entry6.config(state="normal")
    entry7.config(state="normal")
    entry8.config(state="normal")
    entry9.config(state="disabled")
    entry10.config(state="disabled")
    entry11.config(state="disabled")
    button1.config(command=submit1)


def submit2():
    es9 = entry9.get()
    es10 = entry10.get()
    es11 = entry11.get()
    if len(es9) and len(es10) and len(es11) != 0:
        option = messagebox.askquestion("Save", "Are you sure you want to add the information?")
        if option:
            conexion = sqlite3.connect("Yarn.db")
            cursor = conexion.cursor()

            cursor.execute("SELECT SkeinWeight FROM Yarn WHERE ID={}".format(es9))
            fetch = cursor.fetchall()
            strfetch = (fetch[0])
            intfetch = (strfetch[0])

            ess10 = float(entry10.get())
            cursor.execute("""
                UPDATE Yarn SET SkeinWeight='{}' WHERE ID={}
            """.format((intfetch + ess10), es9))

            cursor.execute("SELECT SkeinQuantity FROM Yarn WHERE ID={}".format(es9))
            fetch1 = cursor.fetchall()
            strfetch1 = (fetch1[0])
            intfetch1 = (strfetch1[0])

            ess11 = float(entry11.get())
            cursor.execute("""
                            UPDATE Yarn SET SkeinQuantity='{}' WHERE ID={}
                        """.format((intfetch1 + ess11), es9))

            conexion.commit()
            conexion.close()
            messagebox.showinfo("Saved", "The yarn weight was successfully updated!")
            erase()
        else:
            messagebox.showwarning("Warning", "The data was not saved!")


    else:
        messagebox.showerror("Error!", "You must fill both charts,otherwise it will not save your information!")
    e7.set("")
    e8.set("")
    entry1.config(state="normal")
    entry2.config(state="normal")
    entry3.config(state="normal")
    entry4.config(state="normal")
    entry5.config(state="normal")
    entry6.config(state="normal")
    entry7.config(state="normal")
    entry8.config(state="normal")
    entry9.config(state="disabled")
    entry10.config(state="disabled")
    entry11.config(state="disabled")
    button1.config(command=submit1)


def create_db():
    conexion = sqlite3.connect("Yarn.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            CREATE TABLE Yarn(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Brand VARCHAR(100) NOT NULL,
                YarnLine VARCHAR(100) NOT NULL,
                SizeCategory VARCHAR(100) NOT NULL,
                NeedleSize FLOAT NOT NULL,
                Color VARCHAR(100) NOT NULL,
                FiberContent VARCHAR(100) NOT NULL,
                SkeinWeight FLOAT NOT NULL,
                SkeinQuantity FLOAT NOT NULL
            )
        """)
    except sqlite3.OperationalError:
        pass
    conexion.commit()
    conexion.close()


def add_id():
    entry1.config(state="disabled")
    entry2.config(state="disabled")
    entry3.config(state="disabled")
    entry4.config(state="disabled")
    entry5.config(state="disabled")
    entry6.config(state="disabled")
    entry7.config(state="disabled")
    entry8.config(state="disabled")
    entry9.config(state="normal")
    entry10.config(state="normal")
    entry11.config(state="normal")
    button1.config(command=submit2)


def erase():
    e1.set("")
    e2.set("")
    e3.set("")
    e4.set("")
    e5.set("")
    e6.set("")
    e7.set("")
    e8.set("")
    e9.set("")
    e10.set("")
    e11.set("")


def erase2():
    e4.set("")
    e7.set("")
    e8.set("")


def submit1():
    create_db()
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()
    e7 = entry7.get()
    e8 = entry8.get()

    if len(e1) and len(e2) and len(e3) and len(e4) and len(e5) and len(e6) and len(e7) and len(e8) != 0:
        try:
            ei4 = float(entry4.get())
            ei7 = float(entry7.get())
            ei8 = float(entry8.get())
        except ValueError:
            messagebox.showwarning("Warning", "Needle size, skein weight and skein quantity must be numbers!")
            erase2()
            return
        result = messagebox.askquestion("Save", "Are you sure you want to add the information?")
        print(result)
        if result == 'yes':
            conexion = sqlite3.connect("Yarn.db")
            cursor = conexion.cursor()

            cursor.execute(
                "INSERT INTO Yarn VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}')".format(e1.capitalize(),
                                                                                               e2.capitalize(),
                                                                                               e3.capitalize(), ei4,
                                                                                               e5.capitalize(),
                                                                                               e6.capitalize(), ei7,
                                                                                               ei8))

            conexion.commit()
            conexion.close()
            messagebox.showinfo("Saved", "The yarn was successfully saved!")
            erase()
        else:
            messagebox.showwarning("Warning", "The data was not saved!")
    else:
        messagebox.showerror("Error!", "You must fill all the charts,otherwise it will not save your information!\nIf "
                                       "you do not know a parameter, just add '0'")


def data():
    root = Tk()
    root.title("Knitting DataBase")
    root.resizable(1, 1)
    root.iconbitmap("Knit.ico")

    conexion = sqlite3.connect("Yarn.db")
    cursor = conexion.cursor()
    label1 = Label(root,text="Current Yarn in the database", bg="pale violet red", font=("Arial", 15)).pack(anchor='nw')

    sub = cursor.execute("SELECT * FROM Yarn").fetchall()
    for a in sub:
        label2 = Label(root, text=(
            "ID=>", a[0], "-BRAND=>", a[1], "-YARNLINE=>", a[2], "-SIZECATEGORY=>", a[3], "-NEEDLESIZE=>", a[4],"mm",
            "-COLOR=>",
            a[5], "-FIBERCONTENT=>", a[6], "-SKEINWEIGHT=>", a[7],"grams", "-SKEINQUANTITY=>", a[8]), bg="pale violet red",
                       font=("Arial", 10)).pack(
            anchor='nw')
        label3 = Label(root, text="", bg="pale violet red").pack(anchor='nw')

    conexion.commit()
    conexion.close()

    root.config(bg="pale violet red", bd=15, relief="ridge", width=1500, height=623)

    root.mainloop()


def eraseid():
    entry1.config(state="disabled")
    entry2.config(state="disabled")
    entry3.config(state="disabled")
    entry4.config(state="disabled")
    entry5.config(state="disabled")
    entry6.config(state="disabled")
    entry7.config(state="disabled")
    entry8.config(state="disabled")
    entry9.config(state="normal")
    entry10.config(state="disabled")
    entry11.config(state="disabled")
    button1.config(command=submit3)


def exit1():
    root.quit()
    root.quit()
    root.quit()


button1 = Button(root, text="Submit", bg="HotPink3", font=("Arial", 20), command=submit1)
button1.place(x=880, y=490)

button2 = Button(root, text="Clear data", bg="HotPink3", font=("Arial", 20), command=erase)
button2.place(x=1000, y=490)

button3 = Button(root, text="Add from ID", bg="HotPink3", font=("Arial", 20), command=add_id)
button3.place(x=700, y=490)

button4 = Button(root, text="Show Current Data", bg="HotPink3", font=("Ariel", 20), command=data)
button4.place(x=1160, y=490)

button5 = Button(root, text="Erase from ID", bg="HotPink3", font=("Ariel", 20), command=eraseid)
button5.place(x=920, y=550)

button6 = Button(root, text="Exit",bg="HotPink3", font=("Ariel", 20), command=exit1)
button6.place(x=1120, y=550)
root.config(bg="pale violet red", width=1500, height=623)

root.mainloop()
