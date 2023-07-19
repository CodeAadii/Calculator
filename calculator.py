from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

def button_click(number):
    current = entry_var.get()
    entry_var.set(current + str(number))

def button_clear():
    entry_var.set("")

def button_equal():
    expression = entry.get()
    if expression.strip() == "":
        messagebox.showerror("Error", "No blank spaces allowed")
        return
    if expression.isalpha():
        messagebox.showerror("Error", "Integers only")
        return
    try:
        result = eval(expression)
        entry_var.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except Exception as e:
        messagebox.showerror("Error","Invalid Input")

def button_backspace():
    current = entry_var.get()
    entry_var.set(current[:-1])

root = tk.Tk()
root.title("Calculator")
root.geometry("535x580")
path = "bla.jpg"
img = ImageTk.PhotoImage(Image.open(path))
root.iconbitmap("calci.ico")

label = tk.Label(root, image=img)
label.place(x=0, y=0)

entry_var = tk.StringVar()
entry = Entry(root, font=("arial 30 bold"), borderwidth=10, textvariable=entry_var)
entry.grid(row=0, column=1, columnspan=4, padx=36, pady=15)

button_1 = Button(root, text="1", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=19, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click("+"))
button_sub = Button(root, text="-", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click("-"))
button_mul = Button(root, text="*", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click("*"))
button_div = Button(root, text="/", padx=20, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click("/"))
button_equal = Button(root, text="=", padx=19, pady=20, font=("bold"), borderwidth=5, command=button_equal)

button_allclear = Button(root, text="C", padx=19, pady=20, font=("bold"), borderwidth=5, command=button_clear)
button_percent = Button(root, text="%", padx=19, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click("%"))
button_backspace = Button(root, text="<x", padx=18, pady=20, font=("bold"), borderwidth=5, command=button_backspace)
button_dot = Button(root, text=".", padx=15, pady=8, font=("bold 22"), borderwidth=5, command=lambda: button_click("."))
button_doublezero = Button(root, text="00", padx=17, pady=20, font=("bold"), borderwidth=5, command=lambda: button_click("00"))

button_1.grid(row=2, column=1, padx=20, pady=4)
button_2.grid(row=2, column=2, padx=20, pady=4)
button_3.grid(row=2, column=3, padx=20, pady=4)
button_sub.grid(row=2, column=4, padx=20, pady=4)

button_4.grid(row=3, column=1, padx=10, pady=4)
button_5.grid(row=3, column=2, padx=4, pady=4)
button_6.grid(row=3, column=3, padx=4, pady=4)
button_mul.grid(row=3, column=4, padx=4, pady=4)

button_7.grid(row=4, column=1, padx=10, pady=4)
button_8.grid(row=4, column=2, padx=4, pady=4)
button_9.grid(row=4, column=3, padx=4, pady=4)
button_div.grid(row=4, column=4, padx=4, pady=4)

button_0.grid(row=5, column=2, padx=4, pady=4)
button_equal.grid(row=5, column=4, padx=4, pady=4)
button_dot.grid(row=5, column=3, padx=4, pady=4)
button_doublezero.grid(row=5, column=1, padx=10, pady=4)

button_add.grid(row=1, column=4, padx=4, pady=4)
button_allclear.grid(row=1, column=1, padx=10, pady=4)
button_percent.grid(row=1, column=2, padx=4, pady=4)
button_backspace.grid(row=1, column=3, padx=4, pady=4)

root.mainloop()
