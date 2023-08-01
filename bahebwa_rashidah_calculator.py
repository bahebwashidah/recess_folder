import tkinter as tk

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = entry_operator.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, str(result))

    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Error")

# Create the GUI window
window = tk.Tk()
window.title("Bahebwa Rashidah Adyeeri Calculator")

# Create input fields
entry_num1 = tk.Entry(window, width=10)
entry_num1.grid(row=0, column=0)

entry_operator = tk.Entry(window, width=5)
entry_operator.grid(row=0, column=1)

entry_num2 = tk.Entry(window, width=10)
entry_num2.grid(row=0, column=2)

# Create calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=0, column=3)

# Create result field
entry_result = tk.Entry(window, width=15)
entry_result.grid(row=0, column=4)

# Run the GUI window
window.mainloop()
