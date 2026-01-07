from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    letter = [random.choice(letters) for _ in range(nr_letters)]
    symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter + number + symbol

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)



    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
windows =Tk()
windows.title("My Password Generator")
windows.config(padx= 50, pady= 50)
canvas = Canvas(width= 200, height= 200)
logo_image = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row=0, column= 1)
new_file = " "
website_label = Label(text= "website:", font=("Courier", 16))
website_label.grid(row= 1, column= 0)

website_entry = Entry(width= 21)
website_entry.grid(row= 1, column= 1,  sticky='EW')
website_entry.focus()



email_label = Label(text= "Email/Username:", font=("Courier", 16))
email_label.grid(row= 2, column= 0)


email_entry = Entry(width= 35)
email_entry.grid(row= 2, column= 1, columnspan= 2, sticky='EW')
email_entry.insert(0, "kelanikhad@gmail.com")


password_label = Label(text= "Password:", font=("Courier", 16))
password_label.grid(row= 3, column= 0)

password_entry = Entry(width= 21)
password_entry.grid(row= 3, column=1, sticky='EW')


generate_button = Button(text= "Generate Password", command= generate_password)
generate_button.grid(row= 3, column=2, sticky='EW')

def save_file():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    is_ok = messagebox.askokcancel(title= "website", message= f" these are your details: {email_entry}, {password_entry}, do you want to save")
    details = {
        website:{
            "email": email,
            "password": password
        }
    }

    if is_ok :
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(message="you've left some field empty")
        else:
            try:
                with open("password_details.json", "r") as f:
                    # reading datafile
                    data =  json.load(f)
                    #updating data file

            except FileNotFoundError:
                with open("password_details.json", "w") as f:
                    json.dump( details, f, indent=4)
            else:
                data.update(details)
                with open("password_details.json", "w") as f:
                    json.dump( details, f, indent=4)

            finally:
                    password_entry.delete(0, END)
                    website_entry.delete(0, END)
                    website_entry.focus()

search_button = Button(text="Search", width=13, command= "search_password")
search_button.grid(row=1, column=2)
add_button = Button(text="Add", width=36, command= save_file)
add_button.grid(row = 4, column=1, columnspan=2)
def save_password():
    website = website_entry.get()
    try:
        with open("password_details.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "error", message="no data file found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title= "website", message= f"Email:{email} \n Password:{password}")
            else:
                messagebox.showinfo(title= "error", message= f"no details for {website} exists")
windows.mainloop()

