import customtkinter as ctk
from tkinter import messagebox

from log_in import log_in
from sign_up import sign_up


# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Modes: "light" or "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Function to handle sign-in action
def on_log_in():
    user = username_entry.get()
    password = password_entry.get()

    log_in(user, password)
    
def on_sign_up():
    user = username_entry.get()
    password = password_entry.get()

    sign_up(user, password)

def clear_window():
    for widget in app.winfo_children():
        widget.destroy()

def display_sign_up():
    # Title Label
    title_label = ctk.CTkLabel(app, text="Sign Up", font=("Arial", 20))
    title_label.pack(pady=20)

    # Username Field
    username_label = ctk.CTkLabel(app, text="Username:")
    username_label.pack(pady=5)

    username_entry = ctk.CTkEntry(app, width=200)
    username_entry.pack(pady=5)

    # Password Field
    password_label = ctk.CTkLabel(app, text="Password:")
    password_label.pack(pady=5)

    password_entry = ctk.CTkEntry(app, width=200, show="*")
    password_entry.pack(pady=5)

    sign_up_button = ctk.CTkButton(app, text="Sign up", command=on_sign_up)
    sign_up_button.pack(pady=20)

    go_back_button = ctk.CTkButton(app, text="Go back", command=display_log_in)
    go_back_button.pack(pady=20)

    

def display_log_in():
    clear_window()
    # Title Label
    title_label = ctk.CTkLabel(app, text="Sign In", font=("Arial", 20))
    title_label.pack(pady=20)

    # Username Field
    username_label = ctk.CTkLabel(app, text="Username:")
    username_label.pack(pady=5)

    username_entry = ctk.CTkEntry(app, width=200)
    username_entry.pack(pady=5)

    # Password Field
    password_label = ctk.CTkLabel(app, text="Password:")
    password_label.pack(pady=5)

    password_entry = ctk.CTkEntry(app, width=200, show="*")
    password_entry.pack(pady=5)

    # Sign-In Button
    log_in_button = ctk.CTkButton(app, text="Log In", command=on_log_in)
    log_in_button.pack(pady=20)

    # Sign-up Button
    sign_up_button = ctk.CTkButton(app, text="No Account? Sign Up", command=switch_to_sign_up)
    sign_up_button.pack(pady=50)

def switch_to_sign_up():
    clear_window()
    display_sign_up()

# Initialize the main application window
app = ctk.CTk()
app.title("CustomTkinter Sign In")
app.geometry("500x300")

# Title Label
title_label = ctk.CTkLabel(app, text="Sign In", font=("Arial", 20))
title_label.pack(pady=20)

# Username Field
username_label = ctk.CTkLabel(app, text="Username:")
username_label.pack(pady=5)

username_entry = ctk.CTkEntry(app, width=200)
username_entry.pack(pady=5)

# Password Field
password_label = ctk.CTkLabel(app, text="Password:")
password_label.pack(pady=5)

password_entry = ctk.CTkEntry(app, width=200, show="*")
password_entry.pack(pady=5)

# Sign-In Button
log_in_button = ctk.CTkButton(app, text="Log In", command=on_log_in)
log_in_button.pack(pady=20)

# Sign-up Button
sign_up_button = ctk.CTkButton(app, text="No Account? Sign Up", command=switch_to_sign_up)
sign_up_button.pack(pady=50)


# Run the application
app.mainloop()
