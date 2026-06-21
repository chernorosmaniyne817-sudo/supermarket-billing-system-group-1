# Supermarket Billing System 🛒

## Project Description
The SmartBuy Supermarket Billing System is a Python-based command-line application developed to automate the billing process at SmartBuy Supermarket. It replaces the manual, error-prone process of calculating customer bills by hand, allowing cashiers to quickly enter product details and automatically generate accurate, well-formatted receipts.

This project was developed as part of the IPG101 — Introduction to Programming course at Limkokwing University of Creative Technology, Sierra Leone.

---

## Features
- Accept multiple products per customer (name, quantity, unit price)
- Automatically calculate total price per product and overall bill
- Apply a 10% discount when the total purchase exceeds Le 500
- Display a clean, formatted receipt for each customer
- Process multiple customers continuously without restarting the program
- Input validation to prevent errors from invalid entries

---

## How the Program Works
1. The cashier is welcomed and asked whether to serve a new customer
2. For each customer, the cashier enters each product's name, quantity, and price per unit
3. The system calculates the total for each item and adds it to the overall bill
4. Once all items are entered, the system checks if a 10% discount applies (total > Le 500)
5. A formatted receipt is printed showing all items, subtotal, discount (if any), and final amount
6. The cashier can then process the next customer or exit the program

---

## How to Run the Program

### Requirements
- Python 3.x installed on your computer
- Download Python at: https://www.python.org/downloads/

### Steps
1. Download or clone this repository
2. Open a terminal or command prompt
3. Navigate to the folder containing `smartbuy_billing.py`
4. Run the following command:

```bash
python smartbuy_billing.py
```

5. Follow the on-screen prompts to enter customer and product details

---

## Programming Concepts Used
| Concept | Usage |
|---|---|
| Variables | Store product names, quantities, prices, totals |
| Arithmetic Operators | Calculate product totals and discounts |
| Decision Structures (if/else) | Check if discount applies |
| Loops (while/for) | Customer loop, product loop, receipt printing |
| Arrays (Lists) | Store multiple product details |
| Input / Output | Collect cashier input and display receipt |

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
Developed by: [Your Name]
Course: IPG101 — Introduction to Programming
Institution: Limkokwing University of Creative Technology, Sierra Leone
