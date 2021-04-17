from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox

def return_book():
    bid = bid_info.get()
    name = name_info.get()

    query = f'''select * from book_issued where bid='{bid}' and name = '{name}' '''
    try:
        cur.execute(query)
        result = cur.fetchone()
        if result:
            return_query = f'''delete from book_issued where bid='{bid}' and name = '{name}' '''
            cur.execute(return_query)
            mycon.commit()


            books_query = f'''select total_no_of_books from books where bid='{bid}' '''
            cur.execute(books_query)
            total_books = cur.fetchone()


            update_query = f'''update books set total_no_of_books='{str(int(total_books[0])+1)}' where bid='{bid}' '''
            cur.execute(update_query)
            mycon.commit()

            messagebox.showinfo('Success', "Book Returned Successfully")
            root.destroy()
        else:
            messagebox.showinfo('Error','No Books Issued By This Name')

    except Exception as e:
        print('Error >>>>>>> ', e)

def return_book_templete():
    global root, bid_info, mycon, cur, name_info

    root = Tk()
    root.title('Library Delete book')
    root.minsize(width=400, height=400)
    root.geometry('600x500')
    try:
        mycon = mysql.connector.connect(host='localhost', user='root', passwd='root', database='library')
        cur = mycon.cursor()
    except:
        print('Error in connecting Database >>>>>> Return Book File')

    canvas1 = Canvas()
    canvas1.config(bg='#ff6e40')
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame = Frame(root, bg='#FFBB00', bd=5)
    heading_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame, text='Return Book', bg='black', fg='White', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Label(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book Id
    label1 = Label(label_frame, text='Enter Book ID :', bg='black', fg='white')
    label1.place(relx=0.05, rely=0.4)

    bid_info = Entry(label_frame)
    bid_info.place(relx=0.3, rely=0.4, relwidth=0.62)


    # Issed Name
    label2 = Label(label_frame, text='Enter Your Name :', bg='black', fg='white')
    label2.place(relx=0.05, rely=0.55)

    name_info = Entry(label_frame)
    name_info.place(relx=0.3, rely=0.55, relwidth=0.62)


    return_button = Button(root, text='Return', bg='#d1ccc0', fg='black', command=return_book)
    return_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_button = Button(root, text='Quit', bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


    root.mainloop()

# return_book_templete()