"""
📌 MINI-PROJECT: E-Commerce Smart Order & Inventory Engine
🚀 REPO: python-dsa-journey / basics / 06_order_engine.py
🎯 GOAL: Integrate core Python primitives (Lists, Sets, Tuples, Dicts, Strings)
        and Functions into a clean, modular order processing pipeline.

Complexity Overview:
- Time Complexity: O(N) per batch process where N is total items ordered
- Space Complexity: O(U + P) for tracking unique users and inventory state
"""

from typing import Dict, List, Set, Tuple, Any

# ==============================================================================
# 1. INITIAL SYSTEM STATE (Tuples, Dicts, Sets)
# ==============================================================================

# Catalog of Products: Tuple of (product_id, name, unit_price)
CATALOG: Tuple[Tuple[str, str, float], ...] = (
    ("P101", "wireless mouse", 25.00),
    ("P102", "mechanical keyboard", 85.50),
    ("P103", "usb-c hub", 45.00),
    ("P104", "gaming monitor", 250.00),
)

# Inventory Stock: Dict tracking { product_id: quantity_in_stock }
INVENTORY: Dict[str, int] = {
    "P101": 10,
    "P102": 3,
    "P103": 5,
    "P104": 1,
}

# Restricted / Out-of-service IDs: Set for fast O(1) membership checks
RESTRICTED_ITEMS: Set[str] = {"P999", "P888"}


# ==============================================================================
# 2. HELPER UTILITIES (String Parsing & Set Validations)
# ==============================================================================

def normalize_sku(sku: str) -> str:
    """Standardizes product IDs by stripping spaces and forcing uppercase."""
    return sku.strip().upper()


def extract_unique_requested_items(cart_requests: List[str]) -> Set[str]:
    """Uses Set conversion to quickly find unique item SKUs in a cart."""
    return {normalize_sku(item) for item in cart_requests}


# ==============================================================================
# 3. CORE ORDER PIPELINE (Functions + Dict Updates + Tuple Lookup)
# ==============================================================================

def get_product_details(product_id: str) -> Tuple[str, float]:
    """Searches product catalog and returns (name, price) if found."""
    for pid, name, price in CATALOG:
        if pid == product_id:
            return name.title(), price
    return "Unknown Item", 0.0


def process_customer_order(
        customer_name: str, raw_cart: List[str]
) -> Dict[str, Any]:
    """
    Processes a customer's raw cart list against live inventory and catalog.
    Updates stock, filters invalid items, and generates an invoice payload.
    """
    clean_name = customer_name.strip().title()
    processed_items: List[Dict[str, Any]] = []
    rejected_skus: Set[str] = set()
    total_cost = 0.0

    for raw_sku in raw_cart:
        sku = normalize_sku(raw_sku)

        # 1. Guard check against restricted/invalid SKUs using Set
        if sku in RESTRICTED_ITEMS or sku not in INVENTORY:
            rejected_skus.add(sku)
            continue

        # 2. Check stock availability using Dict lookup
        if INVENTORY[sku] > 0:
            name, unit_price = get_product_details(sku)

            # Deduct inventory count
            INVENTORY[sku] -= 1
            total_cost += unit_price

            # Log fulfilled line item
            processed_items.append({
                "sku": sku,
                "item_name": name,
                "price": unit_price
            })
        else:
            # Out of stock
            rejected_skus.add(sku)

    # Return structured invoice payload as a Dictionary
    return {
        "customer": clean_name,
        "fulfilled_items": processed_items,
        "rejected_items": rejected_skus,
        "total_amount": round(total_cost, 2),
    }


def format_order_receipt(invoice: Dict[str, Any]) -> str:
    """Formats invoice dictionary into a professional string output."""
    lines = [
        f"\n{'=' * 40}",
        f"       RECEIPT FOR: {invoice['customer']}",
        f"{'=' * 40}",
    ]

    if not invoice["fulfilled_items"]:
        lines.append("No items could be fulfilled.")
    else:
        lines.append("Items Purchased:")
        for item in invoice["fulfilled_items"]:
            lines.append(f"  - {item['item_name']} ({item['sku']}): ${item['price']:.2f}")

    lines.append(f"\nTotal Paid: ${invoice['total_amount']:.2f}")

    if invoice["rejected_items"]:
        rejected_str = ", ".join(invoice["rejected_items"])
        lines.append(f"Unavailable/Rejected SKUs: [{rejected_str}]")

    lines.append(f"{'=' * 40}\n")
    return "\n".join(lines)


# ==============================================================================
# DRIVER EXECUTION / TESTING
# ==============================================================================
if __name__ == "__main__":
    print("--- LIVE INVENTORY BEFORE ORDERS ---")
    print("Stock:", INVENTORY)

    # Customer Cart contain duplicates, mixed casing, and invalid SKUs
    cart_batch_1 = [" p101 ", "P102", "p102", "P102", "P102", "P999"]

