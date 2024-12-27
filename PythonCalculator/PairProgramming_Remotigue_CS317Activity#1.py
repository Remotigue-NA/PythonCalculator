import tkinter as tk

#function to update the button
def click_button(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + item)

#function to clear the display
def clear_display():
    display.delete(0, tk.END)

#function to evaluate the expression
def calculate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
    
#function to create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("400x500")

#function to create the dispaly of inputs and results
display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

#funtion for the button layout

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

row = 1
col = 0

#function to create buttons 
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=40, pady=20, font =("Arial", 18), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=40, pady=20, font =("Arial", 18), command=lambda b=button: click_button(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

#function for clearing button
tk.Button(root, text="C", padx=40, pady=20, font =("Arial", 18), command=clear_display).grid(row=row, column=0)

#function to run 
root.mainloop()