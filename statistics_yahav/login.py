from tkinter import *
import datetime


def login():
    def log_in():
        username = username_entry.get()
        password = password_entry.get()
        semel = semel_entry.get()
        year = year_entry.get()

        config_text = """mashov = {"username": '"""
        config_text += username + """', 'password': '"""
        config_text += password + "', 'semel': '"
        config_text += semel + "', 'year': '"
        config_text += year + "'}"
        with open("statistics_yahav/config.py", 'w') as f:
            f.write(config_text)
        root.destroy()

    def skip_login():
        root.destroy()

    root = Tk()
    root.title("Login")
    root.geometry("200x200")

    username_entry = Entry(root)
    username_entry.insert(0, "Username: ")

    password_entry = Entry(root, show="*")
    password_entry.insert(0, "Password: ")

    semel_entry = Entry(root)
    semel_entry.insert(0, "School ID: ")

    year_entry = Entry(root)
    year_entry.insert(0, str(datetime.date.today()).split("-")[0])

    login_button = Button(root, command=log_in, text="Log In")
    skip_login_button = Button(root, command=skip_login, text="Skip Login")
    cancel_button = Button(root, command=quit, text="cancel")

    login_button.grid(row=4, column=0)
    skip_login_button.grid(row=5, column=0)
    cancel_button.grid(row=6, column=0)

    username_entry.grid(row=0, column=0)
    password_entry.grid(row=1, column=0)
    semel_entry.grid(row=2, column=0)
    year_entry.grid(row=3, column=0)

    root.mainloop()
