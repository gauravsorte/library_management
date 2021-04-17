from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from add_book import *
from view_books import *
from delete_book import *
from issue_book import *
from return_book import *
from view_issued_books import *

root = Tk()
root.title('Library')
root.minsize(width=400, height=400)
root.geometry('650x550')

same = True
n = 0.9

# Adding a background image
background_image = Image.open('D:/nebula.jpg')
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
    # print('if part ',newImageSizeHeight)
else:
    newImageSizeHeight = int(imageSizeHeight / n)
    # print('else part ',newImageSizeHeight)


background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(325, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n D.Y.Patil Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


add_book_btn = Button(root, text='Add Book Details', bg='black', fg='white', command=add_book)
add_book_btn.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

delete_book_btn = Button(root, text='Delete Book', bg='black', fg='white', command=delete)
delete_book_btn.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

view_book_btn = Button(root, text='View Book List', bg='black', fg='white', command=view_books)
view_book_btn.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

issue_book_btn = Button(root, text='Issue Book', bg='black', fg='white', command=issue)
issue_book_btn.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

view_issued_book_btn = Button(root, text='View Issued Books', bg='black', fg='white', command=view_issued_books)
view_issued_book_btn.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

return_book_btn = Button(root, text='Return Book', bg='black', fg='white', command=return_book_templete)
return_book_btn.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)
# 'D:/nebula.jpg'


root.mainloop()