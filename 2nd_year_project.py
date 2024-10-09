import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar, DateEntry

# Initialize the main window
root = tk.Tk()
root.title("Airline Ticket Booking System")
root.geometry("400x400")

# Set a beautiful font for the labels and buttons
title_font = ("Arial", 24, "bold")
label_font = ("Arial", 14)
button_font = ("Arial", 16, "bold")

# Labels and entry fields
tk.Label(root, text="Airline Ticket Booking", font=title_font).grid(row=0, column=1, pady=10)

tk.Label(root, text="Name:", font=label_font).grid(row=1, column=0, pady=5, padx=10, sticky="w")
name_entry = tk.Entry(root, font=label_font)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", font=label_font).grid(row=2, column=0, pady=5, padx=10, sticky="w")
phone_entry = tk.Entry(root, font=label_font)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="From:", font=label_font).grid(row=3, column=0, pady=5, padx=10, sticky="w")
from_entry = tk.Entry(root, font=label_font)
from_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="To:", font=label_font).grid(row=4, column=0, pady=5, padx=10, sticky="w")
to_entry = tk.Entry(root, font=label_font)
to_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Class:", font=label_font).grid(row=5, column=0, pady=5, padx=10, sticky="w")
class_var = tk.StringVar(value="Economy")
class_menu = ttk.Combobox(root, textvariable=class_var, font=label_font, state="readonly")
class_menu['values'] = ('Economy', 'Business')
class_menu.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Travel Date:", font=label_font).grid(row=6, column=0, pady=5, padx=10, sticky="w")

# Using DateEntry from tkcalendar for date selection
date_entry = DateEntry(root, width=16, background="darkblue", foreground="white", font=label_font, date_pattern='dd/mm/yyyy')
date_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Passengers:", font=label_font).grid(row=7, column=0, pady=5, padx=10, sticky="w")
passengers_var = tk.StringVar(value="1")
passengers_menu = ttk.Combobox(root, textvariable=passengers_var, font=label_font, state="readonly")
passengers_menu['values'] = ('1', '2', '3', '4')
passengers_menu.grid(row=7, column=1, padx=10, pady=5)

# Function to display a confirmation message
def book_ticket():
    name = name_entry.get()
    phone = phone_entry.get()
    source = from_entry.get()
    destination = to_entry.get()
    travel_class = class_var.get()
    date = date_entry.get()
    passengers = passengers_var.get()

    if not (name and phone and source and destination and travel_class and date):
        messagebox.showwarning("Input Error", "Please fill out all fields.")
    else:
        messagebox.showinfo("Booking Confirmed", f"Ticket booked successfully!\n\n"
                             f"Name: {name}\nPhone: {phone}\nFrom: {source}\nTo: {destination}\n"
                             f"Class: {travel_class}\nTravel Date: {date}\nPassengers: {passengers}")

# Book Button
book_btn = tk.Button(root, text="Book Ticket", command=book_ticket, bg="green", fg="white", font=button_font)
book_btn.grid(row=8, column=1, pady=20)

# Start the tkinter loop
root.mainloop()