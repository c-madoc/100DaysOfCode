import json
import string
import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password(length=12, special_chars=True, digits=True):
    characters = string.ascii_letters

    if special_chars:
        characters += "!@#$%^&*()"

    if digits:
        characters += string.digits

    password = [random.choice(characters) for i in range(length)]

    return ''.join(password)


def generate():
    generated_password = generate_random_password()
    pw_entry.delete(0, END)
    pw_entry.insert(0, string=generated_password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = web_entry.get()

    try:
        with open("saved_passwords.json", "r") as saved_data:
            data = json.load(saved_data)

            email = data[website]['email']
            password = data[website]['password']
    except FileNotFoundError:
        messagebox.showerror("Error",
                             f"Could not find database.")
    except KeyError:
        if len(website) == 0:
            messagebox.showerror("Error",
                                 f"You must specify a website!")
        else:
            messagebox.showerror("Error",
                                 f"Could not find login details for {website}.")
    else:
        messagebox.showinfo("Login Found",
                            f"Login details for: {website}\n\n"
                            f"Email: {email}\n"
                            f"Password: {password}")
    finally:
        web_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def copy_to_clip(password):
    window.clipboard_clear()
    window.clipboard_append(password)


def save():
    website = web_entry.get()
    email = un_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Missing field!", "You cannot leave any fields empty!")

    else:
        try:
            with open("saved_passwords.json", "r") as saved_data:
                # Read the old data
                data = json.load(saved_data)

        except FileNotFoundError:
            # Create a new save file
            with open("saved_passwords.json", "w") as saved_data:
                # Save updated data
                json.dump(new_data, saved_data, indent=4)

        else:
            # Update old data with new data
            data.update(new_data)

            # Write to file
            with open("saved_passwords.json", "w") as saved_data:
                # Save updated data
                json.dump(data, saved_data, indent=4)

            messagebox.showinfo("Password Added!",
                                f"Your login details for {website} were successfully saved.")

        finally:
            # Copy the password to clipboard
            copy_to_clip(password)

            # Delete text fields
            web_entry.delete(0, END)
            pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# LABELS
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

un_label = Label(text="Email/Username:")
un_label.grid(column=0, row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# ENTRIES
web_entry = Entry(width=30)
web_entry.grid(column=1, row=1)
web_entry.focus()

un_entry = Entry(width=43)
un_entry.grid(column=1, row=2, columnspan=2)
un_entry.insert(0, string="email@website.com")

pw_entry = Entry(width=30)
pw_entry.grid(column=1, row=3)

# BUTTONS
check_button = Button(text="Check", width=10, command=search)
check_button.grid(column=2, row=1)

gen_button = Button(text="Generate", width=10, command=generate)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add Entry", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
