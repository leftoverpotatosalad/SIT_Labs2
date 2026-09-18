def get_valid_input():
    stock_q = input("Enter stock quantity (or 'quit' to exit): ")
    if stock_q.lower == "quit":
        return "quit"
    if not stock_q.isdigit():
            print("Error: Please enter a valid integer.")
            return None
    stock_q = int(stock_q)

    if stock_q < 0:
         print("Please enter a vaild postive integer")
         return None

    return stock_q

def process_delivery(current_total, new_value)
    current_total += new_value
    if current_total > 500:
        print("ALERT: Inventory exceeds 500 units!")
        return current_total, True
    return current_total, False

def caculate_tax(amount):
     tax_rate = 0.10 
     tax_amount = amount * tax_rate
     return tax_amount     

    





"""
inventory = 0
stock_q = 0
failed = 0


while True:
    

    if stock_q.lower() == "quit":
        break


    if not stock_q.isdigit():
        print("Error: Please enter a valid integer.")
        failed += 1
        continue

    stock_q = int(stock_q)
    if stock_q < 0: 
        print("Error: Please enter a Postive number")
        failed += 1
        continue

    Inventory += stock_q

    if Inventory > 500:
        print("ALERT: Inventory exceeds 500 units!")
        break

print("\n--- Final Report ---")
print("Total Units Processed:", Inventory)
print("Number of Failed/Rejected Entries:", failed)
"""