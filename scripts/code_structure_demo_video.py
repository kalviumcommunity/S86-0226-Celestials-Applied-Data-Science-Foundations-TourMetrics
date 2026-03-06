"""
Code Structure Demo for Video Walkthrough
==========================================
A simplified demonstration of Python code structure best practices.
Perfect for a 2-minute video walkthrough.

Author: Python Learner
Date: March 3, 2026
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
# All imports at the top - easy to see dependencies
from datetime import datetime

print("=" * 50)
print("PYTHON CODE STRUCTURE DEMONSTRATION")
print("=" * 50)


# ==============================================================================
# SECTION 2: CONSTANTS
# ==============================================================================
# Constants in UPPERCASE - configuration in one place
TAX_RATE = 0.08
DISCOUNT_RATE = 0.10
CURRENCY = "$"


# ==============================================================================
# SECTION 3: UTILITY FUNCTIONS
# ==============================================================================
# Small, reusable helper functions

def format_currency(amount):
    """Format number as currency."""
    return f"{CURRENCY}{amount:.2f}"


def print_header(title):
    """Print a formatted header."""
    print(f"\n{title}")
    print("-" * 50)


# ==============================================================================
# SECTION 4: CALCULATION FUNCTIONS
# ==============================================================================
# Business logic functions - focused on one task each

def calculate_tax(amount):
    """Calculate tax on amount."""
    return amount * TAX_RATE


def calculate_discount(amount, threshold=100):
    """Calculate discount if amount meets threshold."""
    if amount >= threshold:
        return amount * DISCOUNT_RATE
    return 0


def calculate_total(subtotal):
    """Calculate final total with discount and tax."""
    discount = calculate_discount(subtotal)
    subtotal_after_discount = subtotal - discount
    tax = calculate_tax(subtotal_after_discount)
    total = subtotal_after_discount + tax
    return total, discount, tax


# ==============================================================================
# SECTION 5: DISPLAY FUNCTIONS
# ==============================================================================
# Functions that handle output

def display_receipt(item, quantity, price):
    """Display formatted receipt."""
    subtotal = price * quantity
    total, discount, tax = calculate_total(subtotal)
    
    print(f"\n  Item: {item}")
    print(f"  Quantity: {quantity}")
    print(f"  Price: {format_currency(price)}")
    print(f"  Subtotal: {format_currency(subtotal)}")
    
    if discount > 0:
        print(f"  Discount: -{format_currency(discount)}")
    
    print(f"  Tax (8%): {format_currency(tax)}")
    print(f"  TOTAL: {format_currency(total)}")


# ==============================================================================
# DEMONSTRATION 1: CODE ORGANIZATION
# ==============================================================================
print_header("1. ORGANIZED CODE STRUCTURE")

print("""
✓ This script is organized into clear sections:
  • Imports at the top
  • Constants for configuration
  • Utility functions (helpers)
  • Calculation functions (business logic)
  • Display functions (output)
  • Main execution at the bottom

✓ Easy to navigate and understand!
""")


# ==============================================================================
# DEMONSTRATION 2: FUNCTION REUSE
# ==============================================================================
print_header("2. FUNCTIONS FOR REUSE")

print("\n❌ BAD - Repetitive code:")
print("   tax1 = 100 * 0.08")
print("   tax2 = 200 * 0.08")
print("   tax3 = 300 * 0.08")

print("\n✓ GOOD - Reusable function:")
print("   tax1 = calculate_tax(100)")
print("   tax2 = calculate_tax(200)")
print("   tax3 = calculate_tax(300)")

print("\n✓ Demonstration:")
amounts = [100, 200, 300]
for amount in amounts:
    tax = calculate_tax(amount)
    print(f"   Amount: {format_currency(amount)} → Tax: {format_currency(tax)}")


# ==============================================================================
# DEMONSTRATION 3: SEPARATION OF CONCERNS
# ==============================================================================
print_header("3. LOGIC SEPARATED FROM EXECUTION")

print("""
✓ Functions defined above (logic):
  • calculate_tax() - computes tax
  • calculate_discount() - computes discount
  • calculate_total() - computes final total
  • display_receipt() - formats output

✓ Main execution below (clean):
  • Just calls the functions
  • Easy to read and understand
  • Testable and maintainable
""")


# ==============================================================================
# DEMONSTRATION 4: PRACTICAL EXAMPLE
# ==============================================================================
print_header("4. PRACTICAL EXAMPLE")

print("\n✓ Processing a sale using structured code:\n")

# Clean, readable execution
display_receipt("Laptop", 1, 999)
display_receipt("Mouse", 3, 25)


# ==============================================================================
# DEMONSTRATION 5: WHY STRUCTURE MATTERS
# ==============================================================================
print_header("5. WHY THIS MATTERS")

print("""
✓ BEFORE (unstructured):
  • Long blocks of repeated code
  • Hard to find what you need
  • Difficult to modify
  • Prone to errors

✓ AFTER (structured):
  • Clear sections and organization
  • Reusable functions
  • Easy to maintain
  • Professional quality

✓ BENEFITS:
  • Saves time debugging
  • Easier collaboration
  • Scalable for larger projects
  • Your future self will thank you!
""")


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================
print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)
print("""
1. ORGANIZE: Group related code into sections
2. REUSE: Extract repeated logic into functions
3. SEPARATE: Define functions, then execute
4. DOCUMENT: Use clear names and docstrings
5. MAINTAIN: Think about future readers

Good structure = Better code!
""")
print("=" * 50)
