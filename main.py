# Created by Anthony Terrano
# Twitch Livestream 5/14/2022

# Imports
from tkinter import *
import customtkinter  # <- import the CustomTkinter module
import socket 

# Set the appearence of Custom Tkinter
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# root stuff
root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
root_tk.geometry("400x480")
# root_tk.iconbitmap('icon.ico') # Put an icon file at root, and it's path here if you want an icon!
root_tk.title("Whats my TCP/IP Info?!")
root_tk.resizable(False, False)

# Constants
y_padding = 20
RED = '#ba1f1c'
HOVRED = '#d62824'

# Widgets
frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

my_text = Text(frame_1, height=16, width=22)
my_text.configure(font =("Courier", 14))
my_text.place(relx=.06, rely=.15)

# Widget Functions
def clear_all():
    my_text.config(state='normal')
    my_text.delete("1.0","end")
    my_text.config(state=DISABLED)


def get_ip_info():
    my_text.config(state='normal')
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    total_text = f'Your Computer Name:\n{hostname}\n\nYour IP Address:\n{IPAddr}'
    my_text.insert(END, total_text)
    my_text.config(state=DISABLED)

# More widgets
button_1 = customtkinter.CTkButton(master=frame_1, command=get_ip_info, text= 'Run')
button_1.grid(pady=y_padding, padx=10, column=0, row=0)

clear_button = customtkinter.CTkButton(master=frame_1, 
                                        command=clear_all, 
                                        fg_color=RED, 
                                        hover_color=HOVRED, 
                                        text='Clear')

clear_button.grid(pady=y_padding, padx=10, column=1, row=0)

# Main loop
root_tk.mainloop()
