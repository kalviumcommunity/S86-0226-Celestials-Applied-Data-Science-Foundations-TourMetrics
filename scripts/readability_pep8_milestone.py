"""Milestone script: readable variable names and comments (PEP 8 basics).

This script focuses on code readability practices:
- Descriptive variable names in snake_case
- Basic constant naming style
- Useful comments that explain intent (the why)
- Avoiding noisy or redundant comments
"""

MAX_ALLOWED_DISCOUNT_PERCENT = 25


def calculate_discounted_price(original_price: float, discount_percent: float) -> float:
    """Return final price after applying a capped discount percentage."""
    # Cap discount to protect pricing rules from invalid or excessive values.
    capped_discount_percent = min(discount_percent, MAX_ALLOWED_DISCOUNT_PERCENT)
    discount_amount = original_price * (capped_discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price


def build_summary_line(city_name: str, monthly_visitors: int, ticket_revenue_inr: float) -> str:
    """Return a readable summary string for reporting."""
    average_revenue_per_visitor = ticket_revenue_inr / monthly_visitors
    summary_line = (
        f"{city_name}: {monthly_visitors} visitors, "
        f"₹{ticket_revenue_inr:,.2f} revenue, "
        f"₹{average_revenue_per_visitor:,.2f} per visitor"
    )
    return summary_line


def main() -> None:
    print("=== Readable Variable Names and Comments (PEP 8 Basics) ===")

    print("\n1) Readable variable names")
    city_name = "Pune"
    monthly_visitor_count = 2400
    monthly_ticket_revenue_inr = 612000.0
    city_summary_line = build_summary_line(
        city_name=city_name,
        monthly_visitors=monthly_visitor_count,
        ticket_revenue_inr=monthly_ticket_revenue_inr,
    )
    print(city_summary_line)

    print("\n2) Basic PEP 8 naming conventions")
    original_ticket_price = 1500.0
    requested_discount_percent = 30.0
    final_ticket_price = calculate_discounted_price(
        original_price=original_ticket_price,
        discount_percent=requested_discount_percent,
    )
    print(f"Original price: ₹{original_ticket_price:,.2f}")
    print(f"Requested discount: {requested_discount_percent}%")
    print(f"Applied max discount constant: {MAX_ALLOWED_DISCOUNT_PERCENT}%")
    print(f"Final price: ₹{final_ticket_price:,.2f}")

    print("\n3) Useful comments only where needed")
    # The cap in calculate_discounted_price is a business-rule safeguard.
    print("Comments explain intent in non-obvious places, not every line.")

    print("\n4) Avoiding readability mistakes")
    print("- Avoid vague names like x, tmp, val")
    print("- Avoid commented-out code")
    print("- Keep comments aligned with current behavior")
    print("- Prefer clear naming so fewer comments are needed")

    print("\nMilestone demo complete.")


if __name__ == "__main__":
    main()
