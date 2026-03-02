"""
Simple Functions Demo for Video Walkthrough
============================================
Perfect for a 2-minute video demonstration
"""

print("=" * 50)
print("PYTHON FUNCTIONS DEMONSTRATION")
print("=" * 50)

# ==============================================================================
# 1. DEFINING A FUNCTION
# ==============================================================================
print("\n1. DEFINING A FUNCTION")
print("-" * 50)

def greet(name):
    """Greet a person by name."""
    print(f"   Hello, {name}! Welcome to Python functions.")

print("\nFunction defined: greet(name)")
print("This function takes a name and prints a greeting.")

# ==============================================================================
# 2. CALLING THE FUNCTION
# ==============================================================================
print("\n2. CALLING THE FUNCTION")
print("-" * 50)

print("\nCalling greet('Alice'):")
greet("Alice")

print("\nCalling greet('Bob'):")
greet("Bob")

print("\n→ The function is reused without rewriting code!")

# ==============================================================================
# 3. FUNCTION WITH PARAMETERS
# ==============================================================================
print("\n3. FUNCTION WITH MULTIPLE PARAMETERS")
print("-" * 50)

def calculate_area(length, width):
    """Calculate and return the area of a rectangle."""
    area = length * width
    return area

print("\nFunction defined: calculate_area(length, width)")
print("This function takes two numbers and returns their product.")

result1 = calculate_area(5, 3)
result2 = calculate_area(10, 4)

print(f"\nArea of 5×3 rectangle: {result1}")
print(f"Area of 10×4 rectangle: {result2}")

print("\n→ Functions can return values for later use!")

# ==============================================================================
# 4. PASSING ARGUMENTS
# ==============================================================================
print("\n4. DIFFERENT WAYS TO PASS ARGUMENTS")
print("-" * 50)

def introduce(name, age, city):
    """Introduce a person with their details."""
    print(f"   {name} is {age} years old and lives in {city}.")

print("\nFunction defined: introduce(name, age, city)")

print("\nPositional arguments:")
introduce("Charlie", 25, "New York")

print("\nKeyword arguments:")
introduce(city="London", name="Diana", age=30)

print("\n→ Arguments can be passed by position or by name!")

# ==============================================================================
# 5. FUNCTION SCOPE
# ==============================================================================
print("\n5. UNDERSTANDING FUNCTION SCOPE")
print("-" * 50)

# Global variable
total_score = 0

def add_points(points):
    """Add points and return new score."""
    new_score = total_score + points
    return new_score

print(f"\nGlobal variable: total_score = {total_score}")
print("\nFunction defined: add_points(points)")
print("This function takes current score and adds points.")

print("\nCalling add_points(10):")
total_score = add_points(10)
print(f"Updated total_score: {total_score}")

print("\nCalling add_points(5):")
total_score = add_points(5)
print(f"Updated total_score: {total_score}")

print("\n→ Functions return values; we update variables explicitly!")

# ==============================================================================
# 6. PRACTICAL EXAMPLE
# ==============================================================================
print("\n6. PRACTICAL EXAMPLE - Temperature Converter")
print("-" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("\nTwo conversion functions defined.")
print("\nConverting temperatures:")

temp1 = 25
temp1_f = celsius_to_fahrenheit(temp1)
print(f"   {temp1}°C = {temp1_f}°F")

temp2 = 77
temp2_c = fahrenheit_to_celsius(temp2)
print(f"   {temp2}°F = {temp2_c:.1f}°C")

print("\n→ Functions make code reusable and organized!")

# ==============================================================================
# 7. FUNCTION EXECUTION FLOW
# ==============================================================================
print("\n7. FUNCTION EXECUTION FLOW")
print("-" * 50)

def step_one():
    """First step in process."""
    print("   → Step 1: Initialize")

def step_two():
    """Second step in process."""
    print("   → Step 2: Process data")

def step_three():
    """Third step in process."""
    print("   → Step 3: Complete")

def run_workflow():
    """Run complete workflow."""
    print("   Starting workflow...")
    step_one()
    step_two()
    step_three()
    print("   Workflow complete!")

print("\nCalling run_workflow():")
run_workflow()

print("\n→ Functions can call other functions!")

# ==============================================================================
# SUMMARY
# ==============================================================================
print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)
print("""
✓ DEFINE: Use 'def' keyword to create functions
✓ CALL: Use function name with () to execute
✓ PARAMETERS: Functions accept input values
✓ RETURN: Functions can return results
✓ SCOPE: Variables inside functions are local
✓ REUSABLE: Write once, use many times!

Functions make code:
  • Organized
  • Reusable
  • Easier to test
  • Easier to maintain
""")
print("=" * 50)
