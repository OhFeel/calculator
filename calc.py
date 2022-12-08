from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator")
root.configure(bg="black")
root.iconbitmap("assets/calc.ico")
# Create the input and output fields
input_field = Entry(root, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
output_field = Entry(root, width=35, borderwidth=5)
output_field.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

## Define the function for each button
def button_click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))

def button_clear():
    input_field.delete(0, END)

def button_add():
    first_number = input_field.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    input_field.delete(0, END)
def button_subtract():
    first_number = input_field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    input_field.delete(0, END)
def button_multiply():
    first_number = input_field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    input_field.delete(0, END)
def button_divide():
    first_number = input_field.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    input_field.delete(0, END)

def button_equal():
    second_number = input_field.get()
    input_field.delete(0, END)

    if math == "addition":
        input_field.insert(0, f_num + int(second_number))

    elif math == "subtraction":
        input_field.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        input_field.insert(0, f_num * int(second_number))

    elif math == "division":
        input_field.insert(0, f_num / int(second_number))
# Create the buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(1), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_2 = Button(root, text="2", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(2), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_3 = Button(root, text="3", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(3), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_4 = Button(root, text="4", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(4), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_5 = Button(root, text="5", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(5), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_6 = Button(root, text="6", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(6), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_7 = Button(root, text="7", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(7), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_8 = Button(root, text="8", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(8), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_9 = Button(root, text="9", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(9), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_0 = Button(root, text="0", padx=40, pady=20, bg="black", fg="white", command=lambda: button_click(0), relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_add = Button(root, text="+", padx=39, pady=20, bg="black", fg="white", command=button_add, relief=SUNKEN, bd=4
, activebackground="black", activeforeground="white")
button_equal = Button(root, text="=", padx=91, pady=20, bg="black", fg="white", command=button_equal, relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_clear = Button(root, text="Clear", padx=79, pady=20, bg="black", fg="white", command=button_clear, relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_subtract = Button(root, text="-", padx=41, pady=20, bg="black", fg="white", command=button_subtract, relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_multiply = Button(root, text="x", padx=40, pady=20, bg="black", fg="white", command=button_multiply, relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")
button_divide = Button(root, text="/", padx=41, pady=20, bg="black", fg="white", command=button_divide, relief=SUNKEN, bd=4, activebackground="black", activeforeground="white")

# button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
# button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
# button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
# button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
# button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)


# Place the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equal.grid(row=5, column=1, columnspan=2)


# Run the main loop
root.mainloop()
