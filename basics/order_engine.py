"""
Order Processing Engine
----------------------
A mini-project combining Python basics:
- Strings: Clean up messy input data (strip whitespace, normalize IDs)
- Tuples: Stores immutable product catalog entries
- Sets: Fast O(1) checks for restricted or missing items
- Dicts: Track live inventory counts and assemble invoice data
- Lists: Collect ordered items sequentially
"""

# Product Catalog -> (ID, Name, Price)
CATALOG = (
    ("P101", "wireless mouse", 25.00),
    ("P102", "mechanical keyboard", 85.50),
    ("P103", "usb-c hub", 45.00),
    ("P104", "gaming monitor", 250.00)
)

# Stock levels in warehouse
inventory = {
    "P101": 10,
    "P102": 3,
    "P103": 5,
    "P104": 1
}

# Items flagged as invalid/restricted
restricted_skus = {"P999", "P888"}


def clean_sku(raw_item):
    """Normalize input string to uppercase without surrounding spaces."""
    return raw_item.strip().upper()


def find_catalog_price(item_id):
    """Look up product details from the catalog tuple."""
    for pid, name, price in CATALOG:
        if pid == item_id:
            return name.title(), price
    return None, 0.0


def process_cart(customer_name, cart_items):
    formatted_name = customer_name.strip().title()
    purchased_items = []
    failed_skus = set()
    total_bill = 0.0

    print(f"\n--- Processing Order for {formatted_name} ---")

    for raw_sku in cart_items:
        sku = clean_sku(raw_sku)

        # Skip restricted or unlisted products
        if sku in restricted_skus or sku not in inventory:
            failed_skus.add(sku)
            continue

        # Check if item is available in warehouse
        if inventory[sku] > 0:
            item_name, price = find_catalog_price(sku)

            # Deduct stock and add to total
            inventory[sku] -= 1
            total_bill += price
            purchased_items.append((sku, item_name, price))
        else:
            # Out of stock
            failed_skus.add(sku)

    # Return invoice summary dictionary
    return {
        "customer": formatted_name,
        "items": purchased_items,
        "rejected": failed_skus,
        "total": round(total_bill, 2)
    }


def print_receipt(invoice):
    print("\n" + "=" * 35)
    print(f"OFFICIAL RECEIPT: {invoice['customer']}")
    print("=" * 35)

    if not invoice["items"]:
        print("No items were purchased.")
    else:
        for sku, name, price in invoice["items"]:
            print(f" • {name} ({sku}) - ${price:.2f}")

    print("-" * 35)
    print(f"Total Amount Paid: ${invoice['total']:.2f}")

    if invoice["rejected"]:
        print(f"Failed/Skipped SKUs: {', '.join(invoice['rejected'])}")
    print("=" * 35 + "\n")


# Quick test run
if __name__ == "__main__":
    print("Initial Inventory State:", inventory)

    # Test cart with extra spaces, duplicate items, and invalid SKUs
    bhavani_cart = [" p101 ", "P102", "p102", "P102", "P102", "P999"]

    order_summary = process_cart("  bhavani prasad  ", bhavani_cart)
    print_receipt(order_summary)

    print("Updated Inventory State:", inventory)
