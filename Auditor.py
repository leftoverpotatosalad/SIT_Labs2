inventory = 0
stock_q = 0
failed = 0

while True:
    stock_q = input("Enter stock quantity (or 'quit' to exit): ")

    if stock_q.lower() == "quit":
        break

    if not stock_q.isdigit():
        print("Error: Please enter a valid integer.")
        failed += 1
        continue

    stock_q = int(stock_q)
    inventory += stock_q
