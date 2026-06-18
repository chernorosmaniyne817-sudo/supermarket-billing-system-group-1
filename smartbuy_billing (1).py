# ============================================================
#   SmartBuy Supermarket Billing System
#   Course  : IPG101 - Introduction to Programming
#   Project : Supermarket Billing System
# ============================================================

def display_welcome():
    print("=" * 55)
    print("       SMARTBUY SUPERMARKET BILLING SYSTEM")
    print("=" * 55)

def display_receipt(product_names, quantities, unit_prices):
    subtotal = 0

    print("\n" + "=" * 55)
    print("              SMARTBUY SUPERMARKET")
    print("                    RECEIPT")
    print("=" * 55)
    print(f"{'PRODUCT':<20} {'QTY':>5} {'PRICE':>8} {'TOTAL':>10}")
    print("-" * 55)

    for i in range(len(product_names)):
        product_total = quantities[i] * unit_prices[i]
        subtotal += product_total
        print(f"{product_names[i]:<20} {quantities[i]:>5} {unit_prices[i]:>8.2f} {product_total:>10.2f}")

    print("-" * 55)
    print(f"{'Subtotal':<35} {'Le':>5} {subtotal:>8.2f}")

    discount = 0
    if subtotal > 500:
        discount = subtotal * 0.10
        print(f"{'Discount (10%)':<35} {'Le':>5} {discount:>8.2f}")

    total = subtotal - discount
    print("=" * 55)
    print(f"{'TOTAL TO PAY':<35} {'Le':>5} {total:>8.2f}")
    print("=" * 55)

    if discount > 0:
        print("  ** 10% discount applied — total exceeded Le 500 **")

    print()

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a valid number.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("  Please type 'yes' or 'no'.")

def main():
    display_welcome()

    while True:
        # ── New customer ──────────────────────────────────────
        if not get_yes_no("\nServe a new customer? (yes/no): "):
            break

        product_names = []
        quantities    = []
        unit_prices   = []

        print("\n--- Enter product details ---")

        # ── Product entry loop ────────────────────────────────
        while True:
            print()
            name     = input("  Product name     : ").strip()
            if not name:
                print("  Product name cannot be empty.")
                continue

            quantity = int(get_positive_number("  Quantity          : "))
            price    = get_positive_number("  Price per unit (Le): ")

            product_names.append(name)
            quantities.append(quantity)
            unit_prices.append(price)

            if not get_yes_no("\n  Add another product? (yes/no): "):
                break

        # ── Display receipt ───────────────────────────────────
        display_receipt(product_names, quantities, unit_prices)

    # ── Exit ──────────────────────────────────────────────────
    print("=" * 55)
    print("   Thank you for using SmartBuy Billing System!")
    print("                   Goodbye!")
    print("=" * 55)

if __name__ == "__main__":
    main()
