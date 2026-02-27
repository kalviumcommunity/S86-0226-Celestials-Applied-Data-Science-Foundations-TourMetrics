"""First standalone Python script for basic data analysis.

This script uses small in-memory sample data and prints analysis results.
"""


def main() -> None:
    print("=== TourMetrics: First Python Script ===")

    # Sample monthly visitor counts (small, script-friendly data)
    monthly_visitors = [1200, 1350, 1425, 1600, 1580, 1710]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    print("\nInput data:")
    for month, visitors in zip(months, monthly_visitors):
        print(f"- {month}: {visitors} visitors")

    total_visitors = sum(monthly_visitors)
    average_visitors = total_visitors / len(monthly_visitors)
    highest_visitors = max(monthly_visitors)
    lowest_visitors = min(monthly_visitors)
    growth_from_jan_to_jun = monthly_visitors[-1] - monthly_visitors[0]

    print("\nAnalysis results:")
    print(f"- Total visitors (Jan-Jun): {total_visitors}")
    print(f"- Average visitors per month: {average_visitors:.2f}")
    print(f"- Highest monthly visitors: {highest_visitors}")
    print(f"- Lowest monthly visitors: {lowest_visitors}")
    print(f"- Growth from Jan to Jun: {growth_from_jan_to_jun}")

    print("\nScript executed successfully from top to bottom.")


if __name__ == "__main__":
    main()
