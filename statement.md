Statement of Purpose: Basic Retail Billing System
Objective

The main goal of this project is to develop a functional, instructive application that will illustrate the use of the **Tkinter** library for creating graphical user interfaces in Python. This is intended to be a practical basic example of a data input, processing, and output application for students to learn from.

Overview of Functionality

The application mimics core retail billing activities, including:

1.  Data Input: Customer names and item details - name, price, quantity.
2. Calculation: Automatically compute individual item totals and a running grand total.
3. Display: Creating a formatted and easily readable text-based receipt or bill summary.

4. Control: Providing controls to finalize the bill or clear all data for a new transaction.

Educational Value

This project emphasizes several key concepts in programming:
GUI Programming: Using the event-driven model of Tkinter.
Data Structures: Lists (`self.allItems`) to store dynamic item data.
Data Binding: Using 'tk.StringVar', 'tk.DoubleVar', and  'tk.IntVar ' to bind Python variables to GUI widgets.

* **String Formatting:** This code uses Python's f-strings and alignment (`<`, `>`) to produce structured output in the bill area. * **Error Handling:** The code performs a basic kind of validation through `try.except` blocks and conditional checks to make sure the data input is accurate. This project will serve as the base from which students can extend further by adding more features such as database integration, advanced validation, and the ability to remove items.
