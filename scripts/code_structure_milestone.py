"""
Python Code Structure Milestone
================================
This script demonstrates best practices for structuring Python code for
readability, maintainability, and reuse.

Author: Python Learner
Date: March 3, 2026
Purpose: Demonstrate code organization and structure
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
# Standard library imports come first
import math
from datetime import datetime

# Third-party imports would come next (if any)
# import numpy as np
# import pandas as pd

# Local/custom imports would come last
# from my_module import my_function


# ==============================================================================
# SECTION 2: CONSTANTS AND CONFIGURATION
# ==============================================================================
# Constants in UPPERCASE for easy identification
TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 100
MAX_ITEMS = 50
CURRENCY_SYMBOL = "$"

# Configuration settings
DEFAULT_GREETING = "Welcome"
MIN_AGE = 0
MAX_AGE = 120


# ==============================================================================
# SECTION 3: UTILITY FUNCTIONS (Helpers)
# ==============================================================================
# Small, reusable functions that support main logic

def format_currency(amount):
    """
    Format a number as currency.
    
    Args:
        amount (float): The amount to format
    
    Returns:
        str: Formatted currency string
    """
    return f"{CURRENCY_SYMBOL}{amount:,.2f}"


def format_percentage(decimal):
    """
    Format a decimal as percentage.
    
    Args:
        decimal (float): Decimal value (e.g., 0.15)
    
    Returns:
        str: Formatted percentage string
    """
    return f"{decimal * 100:.1f}%"


def get_timestamp():
    """
    Get current timestamp as formatted string.
    
    Returns:
        str: Current timestamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_header(title):
    """
    Print a formatted section header.
    
    Args:
        title (str): The header title
    """
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def print_subheader(title):
    """
    Print a formatted subsection header.
    
    Args:
        title (str): The subheader title
    """
    print(f"\n{title}")
    print("-" * 60)


# ==============================================================================
# SECTION 4: VALIDATION FUNCTIONS
# ==============================================================================
# Functions that validate data

def validate_age(age):
    """
    Validate if age is within acceptable range.
    
    Args:
        age (int): Age to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    return MIN_AGE <= age <= MAX_AGE


def validate_price(price):
    """
    Validate if price is positive.
    
    Args:
        price (float): Price to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    return price > 0


def validate_email(email):
    """
    Basic email validation.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid format, False otherwise
    """
    return "@" in email and "." in email


# ==============================================================================
# SECTION 5: CALCULATION FUNCTIONS
# ==============================================================================
# Functions that perform calculations

def calculate_tax(amount):
    """
    Calculate tax on given amount.
    
    Args:
        amount (float): Base amount
    
    Returns:
        float: Tax amount
    """
    return amount * TAX_RATE


def calculate_total(subtotal, tax):
    """
    Calculate total including tax.
    
    Args:
        subtotal (float): Subtotal before tax
        tax (float): Tax amount
    
    Returns:
        float: Total amount
    """
    return subtotal + tax


def calculate_discount(amount):
    """
    Calculate discount if applicable.
    
    Args:
        amount (float): Purchase amount
    
    Returns:
        float: Discount amount
    """
    if amount >= DISCOUNT_THRESHOLD:
        return amount * 0.10  # 10% discount
    return 0.0


def calculate_final_price(base_price, quantity):
    """
    Calculate final price with discount and tax.
    
    Args:
        base_price (float): Price per item
        quantity (int): Number of items
    
    Returns:
        dict: Dictionary with price breakdown
    """
    subtotal = base_price * quantity
    discount = calculate_discount(subtotal)
    subtotal_after_discount = subtotal - discount
    tax = calculate_tax(subtotal_after_discount)
    total = calculate_total(subtotal_after_discount, tax)
    
    return {
        'subtotal': subtotal,
        'discount': discount,
        'subtotal_after_discount': subtotal_after_discount,
        'tax': tax,
        'total': total
    }


# ==============================================================================
# SECTION 6: DATA PROCESSING FUNCTIONS
# ==============================================================================
# Functions that process data

def filter_valid_ages(ages):
    """
    Filter list to include only valid ages.
    
    Args:
        ages (list): List of ages to filter
    
    Returns:
        list: Valid ages only
    """
    valid_ages = []
    for age in ages:
        if validate_age(age):
            valid_ages.append(age)
    return valid_ages


def calculate_statistics(numbers):
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        dict: Dictionary with statistics
    """
    if not numbers:
        return {
            'count': 0,
            'sum': 0,
            'average': 0,
            'min': None,
            'max': None
        }
    
    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }


def process_sale(item_name, price, quantity):
    """
    Process a sale transaction.
    
    Args:
        item_name (str): Name of item
        price (float): Price per item
        quantity (int): Quantity sold
    
    Returns:
        dict: Transaction details
    """
    if not validate_price(price):
        return {'error': 'Invalid price'}
    
    if quantity <= 0:
        return {'error': 'Invalid quantity'}
    
    price_details = calculate_final_price(price, quantity)
    
    return {
        'item': item_name,
        'quantity': quantity,
        'unit_price': price,
        'subtotal': price_details['subtotal'],
        'discount': price_details['discount'],
        'tax': price_details['tax'],
        'total': price_details['total'],
        'timestamp': get_timestamp()
    }


# ==============================================================================
# SECTION 7: DISPLAY/OUTPUT FUNCTIONS
# ==============================================================================
# Functions that handle output formatting

def display_welcome():
    """Display welcome message."""
    print_header("CODE STRUCTURE MILESTONE")
    print("Demonstrating Best Practices for Python Code Organization")
    print(f"Timestamp: {get_timestamp()}")


def display_transaction(transaction):
    """
    Display formatted transaction details.
    
    Args:
        transaction (dict): Transaction details
    """
    if 'error' in transaction:
        print(f"  ✗ Error: {transaction['error']}")
        return
    
    print(f"\n  Item: {transaction['item']}")
    print(f"  Quantity: {transaction['quantity']}")
    print(f"  Unit Price: {format_currency(transaction['unit_price'])}")
    print(f"  Subtotal: {format_currency(transaction['subtotal'])}")
    
    if transaction['discount'] > 0:
        print(f"  Discount: -{format_currency(transaction['discount'])}")
    
    print(f"  Tax ({format_percentage(TAX_RATE)}): {format_currency(transaction['tax'])}")
    print(f"  Total: {format_currency(transaction['total'])}")
    print(f"  Time: {transaction['timestamp']}")


def display_statistics(stats, label="Statistics"):
    """
    Display formatted statistics.
    
    Args:
        stats (dict): Statistics dictionary
        label (str): Label for the statistics
    """
    print(f"\n  {label}:")
    print(f"    Count: {stats['count']}")
    print(f"    Sum: {stats['sum']}")
    print(f"    Average: {stats['average']:.2f}")
    print(f"    Min: {stats['min']}")
    print(f"    Max: {stats['max']}")


# ==============================================================================
# SECTION 8: DEMONSTRATION FUNCTIONS
# ==============================================================================
# Functions that demonstrate concepts

def demonstrate_code_sections():
    """Demonstrate organized code sections."""
    print_header("1. ORGANIZING CODE INTO SECTIONS")
    
    print("\n✓ This script is organized into clear sections:")
    print("  1. Imports - All dependencies at the top")
    print("  2. Constants - Configuration values")
    print("  3. Utility Functions - Small helper functions")
    print("  4. Validation Functions - Data validation")
    print("  5. Calculation Functions - Business logic")
    print("  6. Data Processing - Data transformation")
    print("  7. Display Functions - Output formatting")
    print("  8. Main Execution - Program entry point")
    
    print("\n✓ Benefits:")
    print("  • Easy to find specific functionality")
    print("  • Logical top-to-bottom flow")
    print("  • Clear separation of concerns")
    print("  • Easier to maintain and debug")


def demonstrate_function_reuse():
    """Demonstrate using functions for reuse."""
    print_header("2. USING FUNCTIONS FOR REUSE")
    
    print("\n✓ Without Functions (Repetitive):")
    print("  amount1 = 100 * 0.08")
    print("  amount2 = 200 * 0.08")
    print("  amount3 = 150 * 0.08")
    
    print("\n✓ With Functions (Reusable):")
    print("  tax1 = calculate_tax(100)")
    print("  tax2 = calculate_tax(200)")
    print("  tax3 = calculate_tax(150)")
    
    print("\n✓ Demonstrating reuse:")
    amounts = [100, 200, 150, 50, 300]
    for amount in amounts:
        tax = calculate_tax(amount)
        print(f"  Amount: {format_currency(amount)} → Tax: {format_currency(tax)}")
    
    print("\n✓ Benefits:")
    print("  • Write once, use many times")
    print("  • Easy to update (change in one place)")
    print("  • Reduces errors from copying code")
    print("  • More readable and maintainable")


def demonstrate_logic_separation():
    """Demonstrate separating logic from execution."""
    print_header("3. SEPARATING LOGIC FROM EXECUTION")
    
    print("\n✓ Logic Functions (Defined Earlier):")
    print("  • validate_price() - Checks if price is valid")
    print("  • calculate_tax() - Computes tax")
    print("  • calculate_total() - Computes total")
    print("  • process_sale() - Combines all logic")
    
    print("\n✓ Execution (Clean and Simple):")
    print("  transaction = process_sale('Laptop', 999, 1)")
    print("  display_transaction(transaction)")
    
    print("\n✓ Example execution:")
    transaction = process_sale("Laptop", 999, 1)
    display_transaction(transaction)
    
    print("\n✓ Benefits:")
    print("  • Functions can be tested independently")
    print("  • Logic is reusable in different contexts")
    print("  • Main execution code stays clean")
    print("  • Easier to understand program flow")


def demonstrate_readable_code():
    """Demonstrate readable, maintainable code."""
    print_header("4. WRITING READABLE, MAINTAINABLE CODE")
    
    print("\n✓ Clear Naming:")
    print("  • calculate_tax() - says what it does")
    print("  • format_currency() - obvious purpose")
    print("  • validate_age() - self-documenting")
    
    print("\n✓ Proper Spacing:")
    print("  • Blank lines between sections")
    print("  • Consistent indentation")
    print("  • Grouped related code")
    
    print("\n✓ Documentation:")
    print("  • Docstrings for all functions")
    print("  • Clear parameter descriptions")
    print("  • Return value documentation")
    
    print("\n✓ Example of readable code structure:")
    print("""
    def calculate_final_price(base_price, quantity):
        # Step 1: Calculate subtotal
        subtotal = base_price * quantity
        
        # Step 2: Apply discount if eligible
        discount = calculate_discount(subtotal)
        subtotal_after_discount = subtotal - discount
        
        # Step 3: Calculate tax
        tax = calculate_tax(subtotal_after_discount)
        
        # Step 4: Calculate total
        total = calculate_total(subtotal_after_discount, tax)
        
        return total
    """)
    
    print("\n✓ Benefits:")
    print("  • Others can understand your code")
    print("  • You can understand it months later")
    print("  • Easier to find and fix bugs")
    print("  • Facilitates team collaboration")


def demonstrate_practical_example():
    """Demonstrate practical application."""
    print_header("5. PRACTICAL EXAMPLE - Processing Multiple Sales")
    
    # Sample sales data
    sales = [
        ("Laptop", 999.99, 1),
        ("Mouse", 25.00, 2),
        ("Keyboard", 75.00, 1),
        ("Monitor", 299.99, 2),
        ("USB Cable", 15.00, 5)
    ]
    
    print("\n✓ Processing sales transactions:")
    print("  Using well-structured, reusable functions\n")
    
    all_totals = []
    
    for item_name, price, quantity in sales:
        transaction = process_sale(item_name, price, quantity)
        display_transaction(transaction)
        
        if 'total' in transaction:
            all_totals.append(transaction['total'])
    
    # Calculate and display statistics
    if all_totals:
        stats = calculate_statistics(all_totals)
        print_subheader("Sales Summary")
        display_statistics(stats, "Transaction Totals")
        
        print(f"\n  Grand Total: {format_currency(stats['sum'])}")
        print(f"  Average Transaction: {format_currency(stats['average'])}")


# ==============================================================================
# SECTION 9: MAIN EXECUTION
# ==============================================================================
# Main program entry point - keeps execution logic clean and organized

def main():
    """
    Main program execution.
    
    This function orchestrates the program flow by calling other functions
    in a logical order. Keeping main() clean makes the program easy to follow.
    """
    # Display welcome
    display_welcome()
    
    # Run demonstrations
    demonstrate_code_sections()
    demonstrate_function_reuse()
    demonstrate_logic_separation()
    demonstrate_readable_code()
    demonstrate_practical_example()
    
    # Final summary
    print_header("SUMMARY - KEY TAKEAWAYS")
    print("""
✓ ORGANIZE CODE INTO SECTIONS:
  • Imports at top
  • Constants/config next
  • Functions grouped by purpose
  • Main execution at bottom

✓ USE FUNCTIONS FOR REUSE:
  • Identify repeated logic
  • Extract into functions
  • Call functions instead of copying
  • Easy to maintain and update

✓ SEPARATE LOGIC FROM EXECUTION:
  • Define functions first
  • Keep main execution clean
  • Logic is testable and reusable
  • Clear program flow

✓ WRITE READABLE CODE:
  • Use clear names
  • Add docstrings
  • Maintain consistent style
  • Think about future readers

Good structure makes code:
  • Easier to understand
  • Easier to maintain
  • Easier to debug
  • Easier to extend
  • Better for collaboration
    """)
    
    print("=" * 60)
    print("MILESTONE COMPLETED")
    print("=" * 60)


# ==============================================================================
# PROGRAM ENTRY POINT
# ==============================================================================
# This is the standard way to make a script both importable and executable

if __name__ == "__main__":
    # This block only runs when script is executed directly
    # Not when imported as a module
    main()
