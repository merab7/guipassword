from tkinter import *
from tkinter import messagebox  # it is not included in asterix because it is not Class or constant
import pandas
from random import choice, randint, shuffle
import pyperclip

# password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# window settings
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)
window.maxsize(width=600, height=400)

# logo

logo_canvas = Canvas()
logo = PhotoImage(file="logo.png")
logo_canvas.config(width=200, height=200)
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(row=0, column=1)

# website
# label
website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
# entry
website_entry = Entry(width=52)

website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# email
# label
email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0)
# entry
email_entry = Entry(width=52)

email_entry.insert(0, "merabtodua1223@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# password
# label
password_label = Label(text="Password :")
password_label.grid(row=3, column=0)
# entry
password_entry = Entry(width=34)
user_password = password_entry.get()
password_entry.grid(row=3, column=1)

# user input dict
saved_dict = {}


def gen_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# save_inputs
def save_inputs(u_email, u_site, u_password):
    global saved_dict
    saved_dict = {
        "email": f"{u_email}",
        "website": f"{u_site}",
        "password": f"{u_password}"
    }


def call_save_inputs():
    user_mail = email_entry.get()
    user_website = website_entry.get()
    getuser_password = password_entry.get()

    if len(user_mail) == 0 or len(getuser_password) == 0 or len(user_mail) == 0:
        messagebox.showinfo(title="!!!", message="Please do not leave eny field empty")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: \n{user_mail} "
                                                                   f"\n{getuser_password}"
                                                                   f"\n Is it okay to save")
        if is_ok:
            save_inputs(user_mail, user_website, getuser_password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            save_data = pandas.DataFrame(saved_dict, index=[0])
            save_data.to_csv(sep="|", path_or_buf="passwords.csv", mode="a", index=False, header=False)
            messagebox.showinfo(message="Password added")


# buttons
# generator
generator_bt = Button(text="Generate Password", command=gen_password)
generator_bt.grid(row=3, column=2)
# add
add_bt = Button(text="Add", width=45, command=call_save_inputs)
add_bt.grid(row=4, column=1, columnspan=2)

window.mainloop()
