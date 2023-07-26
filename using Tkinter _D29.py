from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------------------------Save Password------------------------------------------------#


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered:\nEmail:{email}"
                                                      f"\nPassword:{password}\n Is Ok to Save?")
        if is_ok:
            with open("my_file.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------------------------PasswordGenerator--------------------------------------------#
# Password Generator Project
# day 5
def generator_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# -----------------------------------------------CONSTANT---------------------------------------------------#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# --------------------------------------------UI Interface--------------------------------------------------#
window = Tk()
window.title("Password Generator")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)
canvas = Canvas(width=200, height=224)
password_image = PhotoImage(file="D:/logo.png")
canvas.create_image(100, 112, image=password_image)
canvas.grid(column=1, row=0)
# label
website_label = Label(text="Website:", font=("Arial", "14", "bold"))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial", "14", "bold"))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", "14", "bold"))
password_label.grid(column=0, row=3)
# button
generate_password = Button(text="GeneratePassword", command=generator_password)
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", font=("Arial", "14", "bold"), width=30, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
# Entry
password_entry = Entry(width=40)
password_entry.grid(column=1, row=3)
email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sameershaik68168@email.com")
website_entry = Entry(width=60)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
window.mainloop()
