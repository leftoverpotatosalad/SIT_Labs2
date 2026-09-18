def get_valid_input():
    stock_q = input("Enter stock quantity (or 'quit' to exit): ")

    if stock_q.lower() == "quit":
        return "quit"

    if not stock_q.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    stock_q = int(stock_q)

    if stock_q < 0:
        print("Please enter a valid positive integer.")
        return None

    return stock_q


def process_delivery(current_total, new_value):
    current_total += new_value

    if current_total > 500:
        print("ALERT: Inventory exceeds 500 units!")
        return current_total, True

    return current_total, False


def calculate_tax(amount):
    tax_rate = 0.10
    tax_amount = amount * tax_rate
    return tax_amount


def generate_report(total_units, failed_entries):
    print("\n--- Final Report ---")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_entries)


def main():
    inventory = 0
    failed = 0

    while True:
        stock_q = get_valid_input()

        if stock_q == "quit":
            break

        if stock_q is None:
            failed += 1
            continue

        inventory, alert = process_delivery(inventory, stock_q)

        tax = calculate_tax(stock_q)
        print("Tax for this delivery:", tax)

        if alert:
            break

    generate_report(inventory, failed)


main()