import tkinter as tk

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = "Invalid operator"

        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Hesap Makinesi")

# Num1 Label
num1_label = tk.Label(root, text="Sayı 1")
num1_label.grid(row=0, column=0)

# Num1 Entry
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1)

# Operator Label
operator_label = tk.Label(root, text="İşlem")
operator_label.grid(row=1, column=0)

# Operator Radiobuttons
operator_var = tk.StringVar()
operator_add = tk.Radiobutton(root, text="+", variable=operator_var, value="+")
operator_add.grid(row=1, column=1)

operator_subtract = tk.Radiobutton(root, text="-", variable=operator_var, value="-")
operator_subtract.grid(row=2, column=1)

operator_multiply = tk.Radiobutton(root, text="*", variable=operator_var, value="*")
operator_multiply.grid(row=3, column=1)

operator_divide = tk.Radiobutton(root, text="/", variable=operator_var, value="/")
operator_divide.grid(row=4, column=1)

# Num2 Label
num2_label = tk.Label(root, text="Sayı 2")
num2_label.grid(row=5, column=0)

# Num2 Entry
num2_entry = tk.Entry(root)
num2_entry.grid(row=5, column=1)

# Calculate Button
calculate_button = tk.Button(root, text="Hesapla", command=calculate)
calculate_button.grid(row=6, column=1)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=1)

root.mainloop()
