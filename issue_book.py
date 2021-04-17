from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox


def issue_book():
    bid = bid_info.get()
    name = name_info.get()

    try:
        query = f'''select total_no_of_books from books where bid='{bid}' '''
        cur.execute(query)
        # mycon.commit()
        result = cur.fetchone()
        if (int(result[0]) > int(0)):
            book_query = f'''update books set total_no_of_books='{int(result[0]) - 1}' where bid = '{bid}' '''
            issued_book_query = f'''insert into book_issued(name, bid) values('{name}','{bid}')'''

            cur.execute(book_query)
            mycon.commit()

            cur.execute(issued_book_query)
            mycon.commit()

            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            messagebox.showinfo('Message', "Book Is Not Available")

    except Exception as e:
        print('error - ', e)

def issue():
    global root, bid_info, mycon, cur, name_info

    root = Tk()
    root.title('Issue Book')
    root.minsize(width=400, height=400)
    root.geometry('600x500')

    mycon = mysql.connector.connect(host='localhost', user='root', passwd='root', database='library')
    cur = mycon.cursor()

    canvas1 = Canvas()
    canvas1.config(bg='#ff6e40')
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame = Frame(root, bg='#FFBB00', bd=5)
    heading_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame, text='Issue A Book', bg='black', fg='White', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Label(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book id
    label1 = Label(label_frame, text='Enter Book ID :', bg='black', fg='white')
    label1.place(relx=0.05,rely=0.2)

    bid_info = Entry(label_frame)
    bid_info.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issed Name
    label2 = Label(label_frame, text='Enter Your Name :', bg='black', fg='white')
    label2.place(relx=0.05, rely=0.4)

    name_info = Entry(label_frame)
    name_info.place(relx=0.3, rely=0.4, relwidth=0.62)

    issue_button = Button(root, text='Issue', bg='#d1ccc0', fg='black', command=issue_book)
    issue_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_button = Button(root, text='Quit', bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()


# issue()