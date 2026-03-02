"""
Python Functions Milestone
===========================
This script demonstrates how to define and use functions in Python for clean, modular code.

Topics covered:
1. Defining functions
2. Calling functions
3. Using parameters and arguments
4. Understanding function scope (basics)
5. Best practices for writing functions
"""

print("=" * 60)
print("PYTHON FUNCTIONS MILESTONE")
print("=" * 60)
print()

# ==============================================================================
# 1. DEFINING A FUNCTION
# ==============================================================================
print("1. DEFINING FUNCTIONS - Creating Reusable Code")
print("-" * 60)

# Example 1.1: Simple function with no parameters
def greet():
    """A simple greeting function."""
    print("Hello, welcome to Python functions!")

print("\nExample 1.1: Function with no parameters")
print("Function defined: greet()")
greet()  # Call the function

# Example 1.2: Function with a single parameter
def greet_user(name):
    """Greet a user by name."""
    print(f"Hello, {name}!")

print("\nExample 1.2: Function with one parameter")
print("Function defined: greet_user(name)")
greet_user("Alice")
greet_user("Bob")

# Example 1.3: Function with multiple parameters
def introduce_person(name, age, city):
    """Introduce a person with their details."""
    print(f"{name} is {age} years old and lives in {city}.")

print("\nExample 1.3: Function with multiple parameters")
print("Function defined: introduce_person(name, age, city)")
introduce_person("Charlie", 25, "New York")
introduce_person("Diana", 30, "London")

# Example 1.4: Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

print("\nExample 1.4: Function that returns a value")
print("Function defined: add_numbers(a, b)")
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Example 1.5: Function with default parameter values
def greet_with_title(name, title="Mr./Ms."):
    """Greet someone with an optional title."""
    print(f"Hello, {title} {name}!")

print("\nExample 1.5: Function with default parameters")
print("Function defined: greet_with_title(name, title='Mr./Ms.')")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title

# Example 1.6: Function with docstring
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    area = length * width
    return area

print("\nExample 1.6: Well-documented function")
print("Function defined: calculate_area(length, width)")
print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")

print("\n" + "=" * 60)

# ==============================================================================
# 2. CALLING FUNCTIONS
# ==============================================================================
print("\n2. CALLING FUNCTIONS - Executing Reusable Logic")
print("-" * 60)

# Example 2.1: Basic function call
def welcome_message():
    """Display a welcome message."""
    print("  ✓ Function executed successfully!")

print("\nExample 2.1: Simple function call")
print("Calling welcome_message()...")
welcome_message()

# Example 2.2: Multiple function calls
def count_to_three():
    """Count from 1 to 3."""
    for i in range(1, 4):
        print(f"  Count: {i}")

print("\nExample 2.2: Calling function multiple times")
print("First call:")
count_to_three()
print("Second call:")
count_to_three()

# Example 2.3: Function calling other functions
def format_name(first, last):
    """Format a full name."""
    return f"{first} {last}"

def display_formatted_name(first, last):
    """Display a formatted name."""
    full_name = format_name(first, last)
    print(f"  Formatted name: {full_name}")

print("\nExample 2.3: Functions calling other functions")
print("Calling display_formatted_name('John', 'Doe'):")
display_formatted_name("John", "Doe")

# Example 2.4: Storing function results
def multiply(x, y):
    """Multiply two numbers."""
    return x * y

print("\nExample 2.4: Storing and using function results")
result1 = multiply(5, 4)
result2 = multiply(3, 7)
total = result1 + result2
print(f"  5 × 4 = {result1}")
print(f"  3 × 7 = {result2}")
print(f"  Total: {total}")

# Example 2.5: Function execution order
def first_function():
    """First function in sequence."""
    print("  → First function executed")

def second_function():
    """Second function in sequence."""
    print("  → Second function executed")

def third_function():
    """Third function in sequence."""
    print("  → Third function executed")

print("\nExample 2.5: Observing execution order")
print("Calling functions in sequence:")
first_function()
second_function()
third_function()

print("\n" + "=" * 60)

# ==============================================================================
# 3. USING PARAMETERS AND ARGUMENTS
# ==============================================================================
print("\n3. PARAMETERS AND ARGUMENTS - Making Functions Flexible")
print("-" * 60)

# Example 3.1: Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"  I have a {animal_type} named {pet_name}.")

print("\nExample 3.1: Positional arguments")
print("Function: describe_pet(animal_type, pet_name)")
describe_pet("dog", "Max")
describe_pet("cat", "Whiskers")

# Example 3.2: Keyword arguments
print("\nExample 3.2: Keyword arguments (order doesn't matter)")
describe_pet(pet_name="Buddy", animal_type="dog")
describe_pet(animal_type="parrot", pet_name="Polly")

# Example 3.3: Default parameter values
def make_pizza(size, topping="cheese"):
    """Make a pizza with specified size and topping."""
    print(f"  Making a {size}-inch {topping} pizza.")

print("\nExample 3.3: Default parameter values")
make_pizza(12)  # Uses default topping
make_pizza(16, "pepperoni")  # Custom topping
make_pizza(10, "veggie")

# Example 3.4: Multiple return values
def get_user_info():
    """Return multiple values as a tuple."""
    name = "Alice"
    age = 28
    city = "Boston"
    return name, age, city

print("\nExample 3.4: Functions returning multiple values")
user_name, user_age, user_city = get_user_info()
print(f"  Name: {user_name}")
print(f"  Age: {user_age}")
print(f"  City: {user_city}")

# Example 3.5: Arbitrary number of arguments (*args)
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = sum(numbers)
    return total

print("\nExample 3.5: Variable number of arguments")
print(f"  sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"  sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}")
print(f"  sum_all(5) = {sum_all(5)}")

# Example 3.6: Keyword arguments dictionary (**kwargs)
def build_profile(**user_info):
    """Build a user profile from keyword arguments."""
    print("  User Profile:")
    for key, value in user_info.items():
        print(f"    {key}: {value}")

print("\nExample 3.6: Arbitrary keyword arguments")
build_profile(name="Charlie", age=25, city="Seattle", job="Developer")

# Example 3.7: Mixing argument types
def order_summary(item, quantity, *extras, discount=0, **details):
    """Demonstrate mixing different argument types."""
    print(f"  Item: {item}")
    print(f"  Quantity: {quantity}")
    if extras:
        print(f"  Extras: {', '.join(extras)}")
    print(f"  Discount: {discount}%")
    if details:
        print(f"  Additional details: {details}")

print("\nExample 3.7: Mixing argument types")
order_summary("Laptop", 1, "Mouse", "Keyboard", discount=10, color="Silver")

print("\n" + "=" * 60)

# ==============================================================================
# 4. UNDERSTANDING FUNCTION SCOPE (BASICS)
# ==============================================================================
print("\n4. FUNCTION SCOPE - Variable Visibility and Lifetime")
print("-" * 60)

# Example 4.1: Local variables
def calculate_distance():
    """Demonstrate local variable scope."""
    distance = 100  # Local variable
    print(f"  Inside function: distance = {distance}")

print("\nExample 4.1: Local variables")
calculate_distance()
print("  Local variable 'distance' is not accessible outside the function")

# Example 4.2: Global variables (read)
global_message = "I am a global variable"

def display_message():
    """Access global variable (read-only)."""
    print(f"  Function can read global: '{global_message}'")

print("\nExample 4.2: Reading global variables")
display_message()

# Example 4.3: Local vs Global with same name
counter = 10  # Global counter

def increment_counter():
    """Demonstrate local variable shadowing global."""
    counter = 5  # Local counter (shadows global)
    counter += 1
    print(f"  Inside function: counter = {counter}")

print("\nExample 4.3: Local variable shadows global")
print(f"Before function call: counter = {counter}")
increment_counter()
print(f"After function call: counter = {counter} (unchanged)")

# Example 4.4: Modifying global variables (using global keyword)
score = 0

def increase_score(points):
    """Modify global variable using global keyword."""
    global score
    score += points
    print(f"  Score increased by {points}. New score: {score}")

print("\nExample 4.4: Modifying global variables")
print(f"Initial score: {score}")
increase_score(10)
increase_score(5)
print(f"Final score: {score}")

# Example 4.5: Best practice - Return values instead of modifying globals
def calculate_new_score(current_score, points):
    """Better approach: return new value instead of modifying global."""
    new_score = current_score + points
    return new_score

print("\nExample 4.5: Better practice - Return values")
game_score = 0
print(f"Initial game score: {game_score}")
game_score = calculate_new_score(game_score, 15)
print(f"After earning 15 points: {game_score}")
game_score = calculate_new_score(game_score, 25)
print(f"After earning 25 points: {game_score}")

# Example 4.6: Parameters create local copies
def modify_value(number):
    """Parameters create local copies."""
    print(f"  Inside function before: {number}")
    number = number * 2
    print(f"  Inside function after: {number}")

print("\nExample 4.6: Parameters are local")
original_num = 10
print(f"Before function call: {original_num}")
modify_value(original_num)
print(f"After function call: {original_num} (unchanged)")

# Example 4.7: Mutable objects (lists) - careful!
def add_item(item_list, item):
    """Add item to list - mutates the original."""
    item_list.append(item)
    print(f"  Added '{item}' to list")

print("\nExample 4.7: Mutable objects (lists)")
shopping_list = ["milk", "bread"]
print(f"Before: {shopping_list}")
add_item(shopping_list, "eggs")
print(f"After: {shopping_list} (list was modified)")

# Better approach - return new list
def add_item_safe(item_list, item):
    """Return new list instead of modifying original."""
    new_list = item_list.copy()
    new_list.append(item)
    return new_list

print("\nBetter approach - return new list:")
original_list = ["apple", "banana"]
print(f"Original: {original_list}")
new_list = add_item_safe(original_list, "cherry")
print(f"Original after function: {original_list} (unchanged)")
print(f"New list: {new_list}")

print("\n" + "=" * 60)

# ==============================================================================
# 5. PRACTICAL EXAMPLES - Real-World Function Usage
# ==============================================================================
print("\n5. PRACTICAL EXAMPLES - Functions in Action")
print("-" * 60)

# Example 5.1: Data validation function
def validate_age(age):
    """Validate if age is reasonable."""
    if age < 0 or age > 120:
        return False
    return True

print("\nExample 5.1: Data validation")
test_ages = [25, -5, 150, 30, 0]
for age in test_ages:
    is_valid = validate_age(age)
    status = "✓ Valid" if is_valid else "✗ Invalid"
    print(f"  Age {age}: {status}")

# Example 5.2: Temperature conversion
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("\nExample 5.2: Temperature conversion functions")
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"  {temp_c}°C = {temp_f}°F")

temp_f2 = 68
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"  {temp_f2}°F = {temp_c2:.1f}°C")

# Example 5.3: Calculate statistics
def calculate_average(numbers):
    """Calculate average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    """Find maximum value in list."""
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    """Find minimum value in list."""
    if not numbers:
        return None
    return min(numbers)

print("\nExample 5.3: Statistical functions")
scores = [85, 92, 78, 90, 88]
print(f"  Scores: {scores}")
print(f"  Average: {calculate_average(scores):.1f}")
print(f"  Maximum: {find_maximum(scores)}")
print(f"  Minimum: {find_minimum(scores)}")

# Example 5.4: String formatting
def format_currency(amount):
    """Format number as currency."""
    return f"${amount:,.2f}"

def format_percentage(decimal):
    """Format decimal as percentage."""
    return f"{decimal * 100:.1f}%"

print("\nExample 5.4: Formatting functions")
print(f"  Amount: {format_currency(1234.5)}")
print(f"  Amount: {format_currency(999999.99)}")
print(f"  Rate: {format_percentage(0.15)}")
print(f"  Rate: {format_percentage(0.875)}")

# Example 5.5: Data filtering
def filter_positive_numbers(numbers):
    """Return only positive numbers from list."""
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return positive

def filter_even_numbers(numbers):
    """Return only even numbers from list."""
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even

print("\nExample 5.5: Data filtering functions")
data = [5, -3, 8, -1, 12, -7, 20, 0]
print(f"  Original data: {data}")
print(f"  Positive only: {filter_positive_numbers(data)}")
print(f"  Even numbers only: {filter_even_numbers(data)}")

# Example 5.6: Processing pipeline
def clean_data(value):
    """Remove whitespace and convert to lowercase."""
    return value.strip().lower()

def validate_data(value):
    """Check if data is not empty."""
    return len(value) > 0

def process_data(raw_value):
    """Complete data processing pipeline."""
    cleaned = clean_data(raw_value)
    if validate_data(cleaned):
        return cleaned
    return None

print("\nExample 5.6: Data processing pipeline")
raw_inputs = ["  Hello  ", "World", "  ", "Python  "]
print("Processing inputs:")
for raw in raw_inputs:
    processed = process_data(raw)
    if processed:
        print(f"  '{raw}' → '{processed}'")
    else:
        print(f"  '{raw}' → Invalid (empty)")

print("\n" + "=" * 60)

# ==============================================================================
# SUMMARY AND BEST PRACTICES
# ==============================================================================
print("\nSUMMARY - Key Takeaways")
print("-" * 60)
print("""
✓ DEFINING FUNCTIONS:
  - Use 'def' keyword followed by function name
  - Include parameters in parentheses
  - Add docstrings to describe purpose
  - Keep functions focused on one task

✓ CALLING FUNCTIONS:
  - Use function name followed by parentheses
  - Pass required arguments in correct order
  - Store return values when needed
  - Functions can call other functions

✓ PARAMETERS AND ARGUMENTS:
  - Positional arguments: order matters
  - Keyword arguments: order doesn't matter
  - Default values: make parameters optional
  - *args: accept variable number of arguments
  - **kwargs: accept variable keyword arguments

✓ FUNCTION SCOPE:
  - Local variables: exist only inside function
  - Global variables: accessible but avoid modifying
  - Parameters create local copies
  - Return values instead of modifying globals
  - Be careful with mutable objects (lists, dicts)

✓ BEST PRACTICES:
  - Use clear, descriptive function names
  - Write focused, single-purpose functions
  - Add docstrings for documentation
  - Return values don't modify globals
  - Test functions with different inputs
  - Keep functions short and readable
""")

print("=" * 60)
print("MILESTONE COMPLETED")
print("=" * 60)
