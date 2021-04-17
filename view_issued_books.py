from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox

def view_issued_books():
    root = Tk()
    root.title('View Books')
    root.minsize(width=450, height=450)
    root.geometry('600x500')

    try:
        mycon = mysql.connector.connect(host='localhost', user='root', passwd='root', database='library')
        cur = mycon.cursor()

        canvas1 = Canvas(root)
        canvas1.config(bg='#ff6e40')
        canvas1.pack(expand=True, fill=BOTH)

        headingFrame1 = Frame(root, bg="#FFBB00", bd=1)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.18)

        label1 = Label(headingFrame1, text='Books Issued By', bg='black', fg='White', font=('Courier', 15))
        label1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

        label_frame = Frame(root, bg='black')
        label_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.6)
        y = 0.25

        Label(label_frame, text="%-20s%-50s%-40s" % ('Sr No.', 'Name', 'Book Title'),
              bg='black', fg='white').place(relx=0.07, rely=0.1)
        Label(label_frame, text="----------------------------------------------------------------------------",
              bg='black', fg='white').place(relx=0.05, rely=0.2)

        query = 'select * from book_issued'
        cur.execute(query)
        result = cur.fetchall()
        # print( result)

        display_book_query = f'''select title from books inner join book_issued on books.bid = book_issued.bid'''
        cur.execute(display_book_query)
        title = cur.fetchall()
        # print(title[0][0])
        k=1
        j = 0
        for i in result:
            # print(i)
            Label(label_frame, text='%-20s%-40s%-40s' % (k, i[1], title[j][0]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
            j += 1
            k += 1


    except Exception as e:
        print('Error >>>>> view_issued_books >>>>>>>>>', e)
        messagebox.showinfo('Error',"Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)


    root.mainloop()
