items = {
    "milk":80,
    "bread":40,
    "eggs":60,
    "pen":20,
    "notebook":30,
    "shirt":200,
    "pants":300,
}
cart = []
def print_bill():
  total = 0
  for item,qty,price in cart:
    cash = qty*price
    print(item,qty,price)
    total = total + cash
  print("Grand total = ",total)
def add_to_cart(item,qty):
  if item in items:
    price = items[item]
    cart.append((item,qty,price))
    print("Added!!")
while True:
  print("1.Add to cart")
  print("2.Print bill")
  print("3.Show items")
  print("4.Exit")
  ch = input("Enter your choice: ")
  if ch == '1':
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    add_to_cart(item,qty)
  elif ch == '2':
    print_bill()
    print("Thank you")
    break
  elif ch == '3':
    for item,price in items.items():
      print(f"{item}---{price}")
  elif ch == '4':
    print("Thank you!!!")
    break
  else:
    print("Invalid choice")
