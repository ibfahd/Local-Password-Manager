from tkinter import *
import random

BG_COLOR = "#d2e69c"
LBL_FONT = ("Century Gothic", 10, "bold")

form = Tk()
form.title("My Local Password Manager")

# set the window form dimension
window_width = 600
window_height = 400

# get the screen dimension
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
form.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

form.config(bg=BG_COLOR, padx=20, pady=20)
form.resizable(False, False)
form.iconbitmap("./assets/lock.ico")

# configure the grid
form.columnconfigure(0, weight=1)
form.columnconfigure(1, weight=2)
form.columnconfigure(2, weight=1)
form.rowconfigure(0, weight=5)
form.rowconfigure(1, weight=1)
form.rowconfigure(2, weight=1)
form.rowconfigure(3, weight=1)
form.rowconfigure(4, weight=1)

logo = PhotoImage(file="./assets/shield.png", master=form)
logo_image = Canvas(form, height=200, width=200, highlightthickness=0, bg=BG_COLOR)
logo_image.grid(column=0, row=0, columnspan=3, sticky=N)
logo_image.create_image(100,100,image=logo)

# website
website_label = Label(form, text="Website:", bg=BG_COLOR, font=LBL_FONT)
website_label.grid(column=0, row=1, sticky=E)

website_entry = Entry(form)
website_entry.grid(column=1, row=1, sticky=EW, columnspan=2)

# username
username_label = Label(form, text="Username:", bg=BG_COLOR, font=LBL_FONT)
username_label.grid(column=0, row=2, sticky=E)

username_entry = Entry(form)
username_entry.grid(column=1, row=2, sticky=EW, columnspan=2)

# password
password_label = Label(form, text="Password:", bg=BG_COLOR, font=LBL_FONT)
password_label.grid(column=0, row=3, sticky=E)

password_entry = Entry(form)
password_entry.grid(column=1, row=3, sticky=EW)

# generate
def generate():
    password_entry.delete(0,END)
    c = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','&','#','{','(','[','-','|','@',')',']','=','+','}','$','£','%','!','?']
    for i in range(0, 16):
        password_entry.insert(END,random.choice(c))
    form.clipboard_clear()
    form.clipboard_append(password_entry.get())

gen_button = Button(form, text="Generate", command=generate)
gen_button.grid(column=2, row=3, sticky=EW, padx=10, pady=10)

# add
def save():
    f = open("passwords.txt","a+")
    f.write("website:" + website_entry.get() + " / username:" + username_entry.get() + " / password:" + password_entry.get() +"\n")
    f.close()
    website_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    
add_button = Button(form, text="ADD", command=save)
add_button.grid(column=2, row=4, sticky=EW, padx=10, pady=10)



form.mainloop()