"""Milestone script: passing data into functions and returning results.

This script demonstrates:
- Defining parameters and passing arguments
- Returning values with return
- Reusing returned results in further computation
- Avoiding common mistakes (hardcoding, print-vs-return confusion)
"""


def calculate_total_price(unit_price: float, quantity: int) -> float:
    """Return total price for a given unit price and quantity."""
    return unit_price * quantity


def apply_discount(amount: float, discount_percent: float) -> float:
    """Return discounted amount as a new value."""
    discount_factor = 1 - (discount_percent / 100)
    return amount * discount_factor


def classify_budget(amount: float) -> str:
    """Return a text label for the amount."""
    if amount >= 5000:
        return "High budget"
    if amount >= 2000:
        return "Medium budget"
    return "Low budget"


def safe_divide(numerator: float, denominator: float) -> float | None:
    """Return division result, or None when denominator is zero."""
    if denominator == 0:
        return None
    return numerator / denominator


def format_currency(amount: float) -> str:
    """Return a formatted currency string."""
    return f"₹{amount:,.2f}"


def main() -> None:
    print("=== Passing Data into Functions and Returning Results ===")

    print("\n1) Parameters and arguments")
    unit_price = 249.50
    quantity = 8
    subtotal = calculate_total_price(unit_price, quantity)
    print(f"Unit price: {unit_price}, Quantity: {quantity}")
    print(f"Subtotal (returned value): {format_currency(subtotal)}")

    print("\n2) Returning values from functions")
    discount_percent = 10
    discounted_total = apply_discount(subtotal, discount_percent)
    print(f"Discount: {discount_percent}%")
    print(f"Discounted total (returned value): {format_currency(discounted_total)}")

    print("\n3) Using returned results in further computation")
    service_fee = 99.0
    final_total = discounted_total + service_fee
    budget_label = classify_budget(final_total)
    print(f"Service fee: {format_currency(service_fee)}")
    print(f"Final total: {format_currency(final_total)}")
    print(f"Budget class (returned text): {budget_label}")

    print("\n4) Passing returned values to other functions")
    ratio = safe_divide(final_total, quantity)
    if ratio is None:
        print("Per-item cost cannot be calculated (denominator is zero).")
    else:
        print(f"Per-item cost: {format_currency(ratio)}")

    print("\n5) Avoiding common mistakes")
    print("- No hardcoded values inside core calculation functions")
    print("- Functions return values; printing happens in main")
    print("- `safe_divide` returns None on invalid path instead of crashing")

    print("\nMilestone demo complete.")


if __name__ == "__main__":
    main()
