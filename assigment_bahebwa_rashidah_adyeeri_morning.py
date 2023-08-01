import tkinter as tk

class ReceiptApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Receipt Printing Program")

        self.items = []
        self.total = 0

        # Create GUI elements
        self.item_label = tk.Label(self.window, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(self.window)
        self.item_entry.pack()

        self.price_label = tk.Label(self.window, text="Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(self.window)
        self.price_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.receipt_text = tk.Text(self.window)
        self.receipt_text.pack()

        self.print_button = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        price = float(self.price_entry.get())
        self.items.append((item, price))
        self.total += price

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def print_receipt(self):
        self.receipt_text.insert(tk.END, "Receipt\n")
        self.receipt_text.insert(tk.END, "-----------------\n")

        for item, price in self.items:
            self.receipt_text.insert(tk.END, f"{item}: ${price:.2f}\n")

        self.receipt_text.insert(tk.END, "-----------------\n")
        self.receipt_text.insert(tk.END, f"Total: ${self.total:.2f}\n")

    def run(self):
        self.window.mainloop()

# Create an instance of the ReceiptApp class and run the program
app = ReceiptApp()
app.run()
