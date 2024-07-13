from tkinter import *
import random
import string


def generator():
    passwordField.delete(0, END)
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_character = string.punctuation

    all = small_alphabets + capital_alphabets + special_character + numbers

    password_length = int(length_Box.get())

    password = ''.join(random.sample(all, password_length))
    passwordField.insert(0, password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(passwordField.get())


root = Tk()
root.config(bg='#f0b3ff')
choice = IntVar()
Font = ('arial', 13, 'bold')

passwordLabel = Label(root, text='Password Generator', font=('Helvetica', 20, 'bold'), bg='#03cffc', fg='black')
passwordLabel.grid(pady=10)

weakradiobutton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradiobutton.grid(pady=5)

mediumradiobutton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradiobutton.grid(pady=5)

strongradiobutton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradiobutton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='#03cffc', fg='black')
lengthLabel.grid()

length_Box = Spinbox(root, from_=5, to_=18, width=6, font=Font)
length_Box.grid()

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=30, bd=2)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font, command=copy_to_clipboard)
copyButton.grid(pady=5)

root.mainloop()


_?b"gMI7G