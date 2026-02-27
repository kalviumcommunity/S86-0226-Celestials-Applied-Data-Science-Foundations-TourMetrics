"""Milestone: Understanding Python numeric and string data types.

This script demonstrates:
- Numeric types (int, float) and arithmetic
- String creation and operations
- Safe and unsafe number/string mixing
- Type inspection with type()
"""


def numeric_demo() -> None:
    print("=== 1) Numeric Data Types ===")

    visitors_jan = 1200          # int
    visitors_growth_rate = 0.15  # float

    visitors_feb_estimate = visitors_jan * (1 + visitors_growth_rate)
    total_two_months = visitors_jan + int(visitors_feb_estimate)

    print(f"visitors_jan = {visitors_jan} ({type(visitors_jan).__name__})")
    print(f"visitors_growth_rate = {visitors_growth_rate} ({type(visitors_growth_rate).__name__})")
    print(f"Estimated Feb visitors = {visitors_feb_estimate}")
    print(f"Total Jan + Feb estimate = {total_two_months}")

    print("\nDivision behavior:")
    print(f"5 / 2 = {5 / 2} (float division)")
    print(f"5 // 2 = {5 // 2} (floor division)")

    print("\nBasic precision note:")
    print(f"0.1 + 0.2 = {0.1 + 0.2}")


def string_demo() -> None:
    print("\n=== 2) String Data Types ===")

    destination = "Goa"
    month = "March"
    message = "Tourism Report"

    combined_text = message + " - " + destination + " - " + month

    print(f"destination = {destination} ({type(destination).__name__})")
    print(f"month = {month} ({type(month).__name__})")
    print(f"Combined text: {combined_text}")
    print(f"Uppercase destination: {destination.upper()}")
    print(f"First letter of month: {month[0]}")


def mixing_demo() -> None:
    print("\n=== 3) Mixing Numbers and Strings Safely ===")

    visitors_text = "1500"
    visitors_number = 1500

    print("Unsafe mix example (captured error):")
    try:
        result = "Visitors: " + visitors_number
        print(result)
    except TypeError as error:
        print(f"TypeError -> {error}")

    print("\nSafe conversions:")
    print("Visitors: " + str(visitors_number))

    converted_visitors = int(visitors_text)
    print(f"Converted '{visitors_text}' to number: {converted_visitors} ({type(converted_visitors).__name__})")

    invalid_number_text = "15OO"  # letter O instead of zero
    try:
        int(invalid_number_text)
    except ValueError as error:
        print(f"ValueError converting '{invalid_number_text}' -> {error}")


def type_inspection_demo() -> None:
    print("\n=== 4) Inspecting Data Types ===")

    sample_values = [42, 3.14, "tourism", "2026", True]

    for value in sample_values:
        print(f"Value: {value!r:<10} Type: {type(value).__name__}")

    year_text = "2026"
    if isinstance(year_text, str):
        print("'year_text' is text; convert before arithmetic.")


def main() -> None:
    print("Python Data Types Milestone Script")
    numeric_demo()
    string_demo()
    mixing_demo()
    type_inspection_demo()
    print("\nScript completed successfully.")


if __name__ == "__main__":
    main()
