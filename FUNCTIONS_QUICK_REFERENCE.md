# Python Functions Quick Reference Guide

## 📘 BASIC SYNTAX

### Defining a Function
```python
def function_name(parameter1, parameter2):
    """Docstring: what the function does."""
    # Function body (indented)
    result = parameter1 + parameter2
    return result
```

### Calling a Function
```python
result = function_name(5, 3)
print(result)  # Output: 8
```

---

## 🔧 FUNCTION TYPES

### 1. No Parameters, No Return
```python
def say_hello():
    print("Hello!")

say_hello()  # Output: Hello!
```

### 2. With Parameters, No Return
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### 3. With Parameters and Return
```python
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8
```

### 4. Multiple Return Values
```python
def get_user():
    name = "Alice"
    age = 25
    return name, age

user_name, user_age = get_user()
```

### 5. Default Parameters
```python
def greet(name, title="Mr./Ms."):
    print(f"Hello, {title} {name}")

greet("Smith")              # Hello, Mr./Ms. Smith
greet("Jones", "Dr.")       # Hello, Dr. Jones
```

---

## 📝 PARAMETERS & ARGUMENTS

### Positional Arguments
Order matters!
```python
def describe(animal, name):
    print(f"{name} is a {animal}")

describe("dog", "Max")      # Max is a dog
describe("Max", "dog")      # dog is a Max ❌ Wrong!
```

### Keyword Arguments
Order doesn't matter!
```python
def describe(animal, name):
    print(f"{name} is a {animal}")

describe(name="Max", animal="dog")  # ✓ Works!
describe(animal="cat", name="Whiskers")  # ✓ Works!
```

### Mixing Positional and Keyword
Positional must come first!
```python
def make_pizza(size, topping, extra):
    print(f"{size}-inch {topping} pizza with {extra}")

# Valid
make_pizza(12, "cheese", extra="olives")

# Invalid
make_pizza(size=12, "cheese", "olives")  # ❌ Error!
```

### Variable Number of Arguments (*args)
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3)           # 6
sum_all(10, 20, 30, 40)    # 100
sum_all(5)                 # 5
```

### Variable Keyword Arguments (**kwargs)
```python
def build_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Complete Parameter Order
```python
def function(pos1, pos2, *args, default="value", **kwargs):
    pass

# Order:
# 1. Positional parameters
# 2. *args (variable positional)
# 3. Default parameters
# 4. **kwargs (variable keyword)
```

---

## 🔍 FUNCTION SCOPE

### Local Variables
Exist only inside the function
```python
def calculate():
    result = 10  # Local variable
    print(result)

calculate()  # Output: 10
print(result)  # ❌ Error: result not defined
```

### Global Variables (Read)
Functions can read global variables
```python
message = "Hello"  # Global

def display():
    print(message)  # Can read global

display()  # Output: Hello
```

### Local Shadows Global
Local variable hides global with same name
```python
count = 10  # Global

def increment():
    count = 5  # Local (shadows global)
    count += 1
    print(count)  # 6

increment()  # Output: 6
print(count)  # Output: 10 (global unchanged)
```

### Modifying Global (Not Recommended)
```python
score = 0

def increase():
    global score  # Declare as global
    score += 10

increase()
print(score)  # 10
```

### Best Practice: Return Values
```python
score = 0

def add_points(current_score, points):
    return current_score + points

score = add_points(score, 10)  # ✓ Better!
```

### Parameters are Local
```python
def double(number):
    number = number * 2
    print(f"Inside: {number}")

x = 5
double(x)       # Inside: 10
print(x)        # 5 (x unchanged)
```

### Mutable Objects (Be Careful!)
```python
# Lists can be modified
def add_item(my_list, item):
    my_list.append(item)  # Modifies original!

items = [1, 2, 3]
add_item(items, 4)
print(items)  # [1, 2, 3, 4] (changed!)

# Better: Return new list
def add_item_safe(my_list, item):
    new_list = my_list.copy()
    new_list.append(item)
    return new_list

items = [1, 2, 3]
new_items = add_item_safe(items, 4)
print(items)      # [1, 2, 3] (unchanged)
print(new_items)  # [1, 2, 3, 4]
```

---

## 📚 DOCSTRINGS

### Simple Docstring
```python
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"
```

### Detailed Docstring
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width
```

### Accessing Docstrings
```python
print(calculate_area.__doc__)
help(calculate_area)
```

---

## ✅ BEST PRACTICES

### 1. Naming Conventions
```python
# ✓ Good - Descriptive, verb-based
def calculate_average(numbers):
    pass

def get_user_input():
    pass

def validate_email(email):
    pass

# ❌ Bad - Unclear
def calc(n):
    pass

def do_stuff():
    pass
```

### 2. Keep Functions Focused
```python
# ✓ Good - One task
def calculate_tax(amount):
    return amount * 0.08

def format_currency(amount):
    return f"${amount:.2f}"

# ❌ Bad - Too many tasks
def calculate_and_format_tax(amount):
    tax = amount * 0.08
    formatted = f"${tax:.2f}"
    print(f"Tax: {formatted}")
    return tax
```

### 3. Use Return Values
```python
# ✓ Good
def add_points(score, points):
    return score + points

score = 0
score = add_points(score, 10)

# ❌ Bad - Modifying globals
score = 0

def add_points(points):
    global score
    score += points
```

### 4. Add Docstrings
```python
# ✓ Good
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# ❌ Bad - No documentation
def c_to_f(c):
    return (c * 9/5) + 32
```

### 5. Keep It Short
```python
# ✓ Good - Short and focused
def is_valid_age(age):
    return 0 <= age <= 120

# ❌ Bad - Too long (simplified example)
# If your function is more than 20-30 lines,
# consider breaking it into smaller functions
```

---

## 🎯 COMMON PATTERNS

### Data Validation
```python
def validate_email(email):
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True
```

### Data Transformation
```python
def clean_text(text):
    return text.strip().lower()

def to_uppercase(text):
    return text.upper()
```

### Calculation
```python
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

### Filtering
```python
def filter_positive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result
```

### Formatting
```python
def format_phone(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

def format_currency(amount):
    return f"${amount:,.2f}"
```

### Pipeline Functions
```python
def process_data(raw_value):
    cleaned = clean_text(raw_value)
    validated = validate_data(cleaned)
    if validated:
        return format_output(cleaned)
    return None
```

---

## ⚠️ COMMON MISTAKES

### 1. Forgetting Parentheses
```python
# ❌ Wrong
result = add  # Returns function object, doesn't call it

# ✓ Correct
result = add(5, 3)  # Calls the function
```

### 2. Wrong Argument Order
```python
def divide(a, b):
    return a / b

# ❌ Wrong
divide(2, 10)  # Returns 0.2

# ✓ Correct
divide(10, 2)  # Returns 5.0
```

### 3. Modifying Mutable Defaults
```python
# ❌ Wrong - Default is mutable
def add_item(item, items=[]):
    items.append(item)
    return items

# ✓ Correct
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 4. Not Returning Values
```python
# ❌ Wrong
def add(a, b):
    result = a + b
    # Forgot return!

result = add(5, 3)  # result is None

# ✓ Correct
def add(a, b):
    return a + b
```

### 5. Too Many Parameters
```python
# ❌ Bad - Hard to use
def create_user(name, email, age, city, state, zip, phone, address):
    pass

# ✓ Better - Use dictionary or object
def create_user(user_data):
    pass
```

---

## 🔄 QUICK DECISION TREE

```
Do you need to repeat code?
│
├─ Same logic multiple times? → Create a function
│
├─ Need to pass different values? → Use parameters
│
├─ Need result elsewhere? → Use return
│
├─ Complex logic? → Break into smaller functions
│
└─ Simple one-time task? → Maybe don't need function
```

---

## 📊 FUNCTION CHECKLIST

When creating a function, ask:

- [ ] Does it have a clear, descriptive name?
- [ ] Does it do ONE thing well?
- [ ] Are parameters clearly named?
- [ ] Does it have a docstring?
- [ ] Does it return a value (if needed)?
- [ ] Is it short enough (< 30 lines)?
- [ ] Does it avoid modifying globals?
- [ ] Can it be tested easily?

---

## 💡 REMEMBER

| Concept | Key Point |
|---------|-----------|
| **Define** | Use `def` keyword |
| **Call** | Use parentheses `()` |
| **Parameters** | Variables in definition |
| **Arguments** | Values when calling |
| **Return** | Send value back |
| **Scope** | Local variables stay local |
| **Docstring** | Document what it does |
| **Focus** | One function, one task |

---

## 🎓 FUNCTION TEMPLATE

```python
def function_name(required_param, optional_param="default"):
    """
    Brief description of what function does.
    
    Parameters:
        required_param (type): Description
        optional_param (type): Description (default: "default")
    
    Returns:
        type: Description of return value
    """
    # Validate input (if needed)
    if not is_valid(required_param):
        return None
    
    # Process data
    result = do_something(required_param, optional_param)
    
    # Return result
    return result
```

---

## 🚀 QUICK EXAMPLES

### Before Functions (Repetitive):
```python
print("Welcome, Alice!")
print("Welcome, Bob!")
print("Welcome, Charlie!")

total1 = 100 * 0.08
total2 = 200 * 0.08
total3 = 150 * 0.08
```

### After Functions (Clean):
```python
def welcome(name):
    print(f"Welcome, {name}!")

def calculate_tax(amount):
    return amount * 0.08

welcome("Alice")
welcome("Bob")
welcome("Charlie")

tax1 = calculate_tax(100)
tax2 = calculate_tax(200)
tax3 = calculate_tax(150)
```

---

**Print this page for quick reference! 📌**

---

## Summary: Function Essentials

```python
# DEFINE
def function_name(parameters):
    """What it does."""
    return result

# CALL
result = function_name(arguments)

# KEY POINTS
# - Use clear names
# - Keep focused
# - Return values
# - Document with docstrings
# - Test with different inputs
```

**Functions = Reusable, Organized, Maintainable Code! 🎯**
