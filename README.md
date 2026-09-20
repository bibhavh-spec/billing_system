# Billing System (Python)

A simple command-line billing program built with Python. The user can view items, add them to a cart, and print a bill with the grand total.

## Features

- View available items and prices
- Add items to the cart with a quantity
- Print a bill with the total for each item and the grand total
- Shows a message if an item is not available

## Concepts Used

- Dictionary (items and prices)
- List of tuples (the cart)
- Functions
- Loops and conditions

## How to Run

1. Install Python 3 on your computer
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run:

```
python billing.py
```

## Sample Output

```
1. Show items
2. Add to cart
3. Print bill
4. Exit
Enter your choice: 2
Item name: rice
Quantity: 2
Added!

Enter your choice: 3
rice 2 60 120
Grand Total: 120
```

## Known Limitations

- Item names must be typed in lowercase
- Entering text instead of a number for quantity will crash the program

## Future Improvements

- Handle wrong input without crashing
- Add discounts
- Remove items from the cart
- Track stock quantity
- Save bills to a file

## Author

[Bibhav Shrestha]
