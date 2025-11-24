import tkinter as tk
from tkinter import ttk, messagebox
import random



class BillingApp:
    def __init__(self, master):

        self.root = master
        self.root.title("Basic Retail Billing System (Student Version)")
        self.root.geometry("2000x900")


        self.customerName = tk.StringVar()
        self.billNum = tk.StringVar(value=str(random.randint(1000, 9999)))


        self.item_name_var = tk.StringVar()
        self.item_price_var = tk.DoubleVar(value=0.0)
        self.item_qty_var = tk.IntVar(value=1)


        self.allItems = []
        self.total_var = tk.DoubleVar(value=0.0)


        detailsFrame = ttk.LabelFrame(master, text="Customer Details")
        detailsFrame.pack(padx=10, pady=12, fill="x")

        ttk.Label(detailsFrame, text="Name:").grid(row=0, column=0, padx=4)
        ttk.Entry(detailsFrame, width=26, textvariable=self.customerName).grid(row=0, column=1, padx=3)

        ttk.Label(detailsFrame, text="Bill No:").grid(row=0, column=2, padx=10)
        ttk.Label(detailsFrame, textvariable=self.billNum).grid(row=0, column=3, padx=4)


        itemFrame = ttk.LabelFrame(master, text="Add Item Below")
        itemFrame.pack(padx=10, pady=10, fill="x")

        ttk.Label(itemFrame, text="Item Name:").grid(row=0, column=0, padx=5)
        ttk.Entry(itemFrame, textvariable=self.item_name_var, width=22).grid(row=0, column=1, padx=4)

        ttk.Label(itemFrame, text="Price:").grid(row=0, column=2, padx=6)
        ttk.Entry(itemFrame, textvariable=self.item_price_var, width=9).grid(row=0, column=3)

        ttk.Label(itemFrame, text="Qty:").grid(row=0, column=4, padx=6)
        ttk.Entry(itemFrame, textvariable=self.item_qty_var, width=6).grid(row=0, column=5)


        ttk.Button(itemFrame, text="Add To Bill", command=self.add_item_to_list).grid(row=0, column=6, padx=25)


        self.bill_text = tk.Text(master, width=85, height=17)
        self.bill_text.pack(padx=10, pady=10)


        bottomRow = ttk.Frame(master)
        bottomRow.pack(fill="x", padx=10, pady=10)

        ttk.Label(bottomRow, text="Total: ₹").pack(side="left")
        ttk.Label(bottomRow, textvariable=self.total_var, font=("Arial", 14, "bold")).pack(side="left")

        ttk.Button(bottomRow, text="Generate Bill", command=self.make_final_bill).pack(side="right", padx=20)
        ttk.Button(bottomRow, text="Clear", command=self.clear_everything).pack(side="right")

    def add_item_to_list(self):

        try:
            nm = self.item_name_var.get()
            pr = float(self.item_price_var.get())
            q = int(self.item_qty_var.get())


            if nm == "" or pr <= 0 or q <= 0:
                messagebox.showerror("Error", "Item details look wrong, check again plz.")
                return

            total_for_item = pr * q


            self.allItems.append((nm, pr, q, total_for_item))


            self.update_bill_area()


            self.item_name_var.set("")
            self.item_price_var.set(0.0)
            self.item_qty_var.set(1)

        except Exception as e:

            messagebox.showerror("Problem", f"Something went wrong: {e}")

    def update_bill_area(self):

        self.bill_text.delete("1.0", tk.END)

        # header
        self.bill_text.insert(tk.END, "===============================\n")
        self.bill_text.insert(tk.END, f"Bill No: {self.billNum.get()} | Customer: {self.customerName.get()}\n")
        self.bill_text.insert(tk.END, "===============================\n")
        self.bill_text.insert(tk.END, f"{'Item':<21}{'Price':>9}{'Qty':>6}{'Total':>12}\n")
        self.bill_text.insert(tk.END, "-------------------------------\n")

        total_count = 0
        for a, b, c, d in self.allItems:

            self.bill_text.insert(tk.END, f"{a:<21}₹{b:>8.2f}{c:>6}   ₹{d:>8.2f}\n")
            total_count += d

        self.total_var.set(total_count)

        self.bill_text.insert(tk.END, "-------------------------------\n")
        self.bill_text.insert(tk.END, f"{'GRAND TOTAL:':<30} ₹{total_count:.2f}\n")
        self.bill_text.insert(tk.END, "===============================\n")

    def make_final_bill(self):

        if len(self.allItems) == 0:
            messagebox.showwarning("Uh-oh", "Add something first!")
            return


        messagebox.showinfo("Done!", f"Bill for {self.customerName.get()} completed.\nTotal: ₹{self.total_var.get():.2f}")



    def clear_everything(self):

        self.allItems = []
        self.customerName.set("")
        self.total_var.set(0.0)
        self.billNum.set(str(random.randint(1000, 9999)))
        self.bill_text.delete("1.0", tk.END)

        messagebox.showinfo("Cleared", "Bill cleared successfully!")



if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
