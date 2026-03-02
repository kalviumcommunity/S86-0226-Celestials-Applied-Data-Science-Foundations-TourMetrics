"""Milestone script: conditional statements for data logic.

This script demonstrates:
- Basic if statement
- if-else branching
- if-elif-else with multiple conditions
- Logical operators: and, or, not

Run this file directly to observe decision paths.
"""


def basic_if_statement(visitor_count: int) -> None:
    print("\n1) Basic if statement")
    print(f"Visitor count = {visitor_count}")

    if visitor_count > 1500:
        print("High traffic detected: staffing alert sent.")

    print("End of basic if example.")


def if_else_branching(ticket_type: str) -> None:
    print("\n2) if-else decision branching")
    print(f"Ticket type = {ticket_type}")

    if ticket_type == "premium":
        print("Access granted to premium lounge.")
    else:
        print("Standard access only.")


def if_elif_else_example(satisfaction_score: int) -> None:
    print("\n3) if-elif-else with multiple conditions")
    print(f"Satisfaction score = {satisfaction_score}")

    if satisfaction_score >= 9:
        print("Rating: Excellent")
    elif satisfaction_score >= 7:
        print("Rating: Good")
    elif satisfaction_score >= 5:
        print("Rating: Average")
    else:
        print("Rating: Needs improvement")


def logical_operators_example(age: int, city: str, has_id: bool) -> None:
    print("\n4) Logical operators (and, or, not)")
    print(f"Age = {age}, City = {city}, Has ID = {has_id}")

    if age >= 18 and has_id:
        print("Entry check (and): Eligible for adult event entry.")
    else:
        print("Entry check (and): Not eligible for adult event entry.")

    if city == "Pune" or city == "Mumbai":
        print("Regional offer (or): Eligible for west-zone promo.")
    else:
        print("Regional offer (or): Not eligible for west-zone promo.")

    if not has_id:
        print("Identity check (not): Verification required at gate.")
    else:
        print("Identity check (not): Verification already complete.")


def main() -> None:
    print("=== Conditional Statements Milestone ===")

    basic_if_statement(visitor_count=1710)
    if_else_branching(ticket_type="standard")
    if_elif_else_example(satisfaction_score=8)
    logical_operators_example(age=20, city="Pune", has_id=True)

    print("\n5) Edge-case checks")
    if_elif_else_example(satisfaction_score=5)
    logical_operators_example(age=17, city="Delhi", has_id=False)

    print("\nMilestone demo complete.")


if __name__ == "__main__":
    main()
