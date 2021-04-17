from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox

def delete_book():
    book_id = bid_info.get()

    deleteBook = f'''delete from books where bid='{book_id}' '''
    deleteIssue = f'''delete from book_issued where bid='{book_id}' '''

    try:
        cur.execute(deleteBook)
        mycon.commit()

        cur.execute(deleteIssue)
        mycon.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except Exception as e:
        messagebox.showinfo("Please check Book ID")

def delete():

    global root, bid_info, mycon, cur

    root = Tk()
    root.title('Library Delete book')
    root.minsize(width=400, height=400)
    root.geometry('600x500')

    mycon = mysql.connector.connect(host='localhost', user='root', passwd='root', database='library')
    cur = mycon.cursor()

    canvas1 = Canvas()
    canvas1.config(bg='#ff6e40')
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame = Frame(root, bg='#FFBB00', bd=5)
    heading_frame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    heading_label = Label(heading_frame, text='Delete Book', bg='black', fg='White', font = ('Courier',15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Label(root, bg='black')
    label_frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Book id
    label1 = Label(label_frame, text='Enter Book ID :', bg='black', fg='white')
    label1.place(relx=0.05,rely=0.5)

    bid_info = Entry(label_frame)
    bid_info.place(relx=0.3,rely=0.5, relwidth=0.62)

    submit_button = Button(root, text='Submit', bg='#d1ccc0', fg='black', command=delete_book)
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_button = Button(root, text='Quit', bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


    root.mainloop()

# delete()
