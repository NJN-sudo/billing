Basic Retail Billing System (Student Version) 

This is a simple desktop application developed in Python using the **Tkinter** library to simulate a basic retail billing system. It allows users to input customer details, add multiple items with price and quantity, calculate the total bill, and generate a printable summary.

Features

Simple GUI:** Easy-to-use graphical user interface created using tkinter and tkinter.ttk.
Customer & Bill Tracking: Input fields for the customer name and a random, automatically generated bill number.
Item Management Easily add items to the bill using name, price, and quantity.
Automatic Calculation:Calculates the price for each item and also the overall total of the entire bill.
Formatted Bill Output: A well-structured receipt is displayed in a dedicated text area.

Explicit: Clear Functionality: Ability to reset the whole transaction for another customer.

 Prerequisites 

This application requires only standard Python libraries, mainly **Tkinter.

Requirements: Python 3.x

How to Run the Application

1. Save the Code: Save the given Python code in a file and name it billing_app.py.

2. Execute from Terminal: Open your terminal or command prompt, go to the location where you have saved the file, and run the script as follows:


python billing_app.py


3.  The GUI Window:A window with the title "Basic Retail Billing System "will open.

Usage Instructions

1. Customer Information

In the Customer Details section at the top:

* Enter the customer's Name. (The Bill No is generated automatically).

2. Adding Items
In the Add Item Below section:
1. Write the Item Name (for example, "Milk").

2. In the Price per unit (for example, 55.50),

3.  Enter the Qty (Quantity, e.g., 2).

4. Click the Add To Bill button.
This will add the item to the running list and automatically update both the bill area and the grand total.

3. Review and Finalize

* At the bottom, the label Total: ₹ shows the current grand total of all added items.

* The large text area displays the formatted receipt, showing individual item totals and the grand total.

* Once the transaction is complete, click Generate Bill. A pop-up will appear confirming the final amount.

4. Create a New Bill
 Click the button Clear to clear the current transaction including the list of items, customer name, and total. A new Bill No will be generated randomly.
 Code Structure Python Class
The application is structured within a single Python class:
 Method / Variable  Description 

init(self, master)  Sets up the main window, all Tkinter widgets (ttk.Entry, ttk.Button, tk.Text), and state variables. 
customerName, billNum, etc. | tk.StringVar/tk.DoubleVar variables associated with GUI inputs. 

self.allItems (list) | Stores item tuples: (name, price, quantity, item_total)

add_item_to_list(self) checks input is valid, calculates an item's total and adds the item to self.allItems, calls update_bill_area

update_bill_area(self) Clears and regenerates the content of the tk.Text widget with formatted header, items and total. 
make_final_bill(self) Displays a confirmation message with the final total. 
clear_everything(self)  Resets all the application data and variables to start a new bill.
  Student Notes / Areas for Improvement This is a simple version, which can be elaborated upon when learning: Data Persistence:Right now, bill data is lost when the app closes. The solution should save bills to a file (e.g., CSV, JSON) or a simple SQLite database. Error Handling:** Enhance the robustness of input validation - for example, preventing non-numeric input for Price/Qty immediately. Item Removal: Add functionality for the selection and removal of an item from the bill list before finalizing. Item Stock: Inventory management to track the availability of the stock.  Tax/Discount: Add fields for applying sales tax or discounts to the grand total.
