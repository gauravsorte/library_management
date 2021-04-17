from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox

def view_books():
    root = Tk()
    root.title('View Books')
    root.minsize(width=400, height=400)
    root.geometry('600x500')
    try:
        mycon = mysql.connector.connect(host='localhost', user='root', passwd='root', database='library')
        cur = mycon.cursor()

        canvas1 = Canvas(root)
        canvas1.config(bg='#ff6e40')
        canvas1.pack(expand=True, fill=BOTH)

        headingFrame1 = Frame(root, bg="#FFBB00", bd=1)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.18)

        label1 = Label(headingFrame1, text='View Books', bg='black', fg='White', font = ('Courier',15))
        label1.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        label_frame = Frame(root, bg='black')
        label_frame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.6)
        y=0.25

        Label(label_frame, text="%-10s%-50s%-30s%-20s" % ('BID', 'Title', 'Author', 'Total_Books'),
              bg='black', fg='white').place(relx=0.07, rely=0.1)
        Label(label_frame, text="----------------------------------------------------------------------------",
              bg='black', fg='white').place(relx=0.05, rely=0.2)

        query = 'select * from books'
        cur.execute(query)
        result = cur.fetchall()


        for i in result:
            # print(i)
            Label(label_frame, text='%-10s%-40s%-30s%-20s' % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
            # print('p1')

    except Exception as e:
        print('error - ', e)
        messagebox.showinfo("Failed to fetch files from database")



    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

# view_books()