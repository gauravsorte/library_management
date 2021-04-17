from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox

def register_book():
    bid = bid_Info.get()
    title = title_Info.get()
    author = author_Info.get()
    total_books = total_books_Info.get()

    insertBooks = f'''insert into books values ('{bid}','{title}','{author}','{total_books}')'''

    try:
        cur.execute(insertBooks)
    except Exception as e:
        print('error', e)
        messagebox.showinfo("Error", "Can't add data into Database")
    else:
        mycon.commit()
        messagebox.showinfo('Success', "Book added successfully")

def add_book():
    global bid_Info, title_Info, author_Info, total_books_Info, root, mycon, cur

    root = Tk()
    root.title('Add Book')
    root.minsize(width=400, height=400)
    root.geometry('600x500')
    try:
        mycon = mysql.connector.connect(host='localhost' , user='root',passwd='root',database='library')
        cur = mycon.cursor()


        canvas1 = Canvas(root)
        canvas1.config(bg='#ff6e40')
        canvas1.pack(expand=True, fill=BOTH)

        heading_frame = Frame(root, bg='#ffbb00', bd=5)
        heading_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        heading_label = Label(heading_frame, text='Add Books', bg='black', fg='white', font=('Courier',15))
        heading_label.place(relx=0,rely=0, relwidth=1, relheight=1)

        label_frame = Frame(root, bg='black')
        label_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

        # book Id
        label1 = Label(label_frame, text='Book ID :', bg='black', fg='white')
        label1.place(relx=0.05, rely=0.2, relheight=0.08)

        bid_Info = Entry(label_frame)
        bid_Info.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

        # title
        label2 = Label(label_frame, text='Title :', bg='black', fg='white')
        label2.place(relx=0.05, rely=0.35, relheight=0.08)

        title_Info = Entry(label_frame)
        title_Info.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

        #author
        label3 = Label(label_frame, text='Author :', bg='black', fg='white')
        label3.place(relx=0.05, rely=0.50, relheight=0.08)

        author_Info = Entry(label_frame)
        author_Info.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

        # Total Number Of Books
        label4 = Label(label_frame, text='Total No.Of Books :', bg='black', fg='white')
        label4.place(relx=0.05, rely=0.65, relheight=0.08)

        total_books_Info = Entry(label_frame)
        total_books_Info.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

        #Submit Button
        submit_button = Button(root, text='Submit', bg='#d1ccc0', fg='black',command=register_book)
        submit_button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

        quit_button = Button(root, text='Quit', bg='#f7f1e3', fg='black', command=root.destroy)
        quit_button.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)



    except Exception as e:
        print('error - ', e)



    root.mainloop()

# add_book()