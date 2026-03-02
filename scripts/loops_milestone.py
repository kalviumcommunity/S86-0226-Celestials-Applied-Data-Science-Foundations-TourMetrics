"""
Python Loops Milestone
======================
This script demonstrates for and while loops, loop control, and iteration best practices.

Topics covered:
1. For loops for iteration
2. While loops for condition-based repetition
3. Controlling loop flow (break and continue)
4. Avoiding infinite loops
"""

print("=" * 60)
print("PYTHON LOOPS MILESTONE")
print("=" * 60)
print()

# ==============================================================================
# 1. USING FOR LOOPS FOR ITERATION
# ==============================================================================
print("1. FOR LOOPS - Iterating Over Sequences")
print("-" * 60)

# Example 1.1: Iterate over a range of numbers
print("\nExample 1.1: Iterating over a range of numbers (0 to 4)")
for i in range(5):
    print(f"  Iteration {i}: Value is {i}")

# Example 1.2: Iterate over a range with start and end
print("\nExample 1.2: Iterating from 1 to 5")
for num in range(1, 6):
    print(f"  Number: {num}")

# Example 1.3: Iterate over a range with step
print("\nExample 1.3: Iterating with step of 2 (even numbers)")
for even in range(0, 11, 2):
    print(f"  Even number: {even}")

# Example 1.4: Iterate over a list
print("\nExample 1.4: Iterating over a list of cities")
cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
for city in cities:
    print(f"  City: {city}")

# Example 1.5: Iterate with index using enumerate
print("\nExample 1.5: Iterating with index and value")
languages = ["Python", "JavaScript", "Java", "C++"]
for index, language in enumerate(languages):
    print(f"  Position {index}: {language}")

# Example 1.6: Iterate over a dictionary
print("\nExample 1.6: Iterating over a dictionary")
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
for name, score in student_scores.items():
    print(f"  {name} scored {score}")

# Example 1.7: Nested for loop
print("\nExample 1.7: Nested loops - Multiplication table (first 3 rows)")
for i in range(1, 4):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    print(f"  {i} times table: {row}")

print("\n" + "=" * 60)

# ==============================================================================
# 2. USING WHILE LOOPS FOR CONDITION-BASED REPETITION
# ==============================================================================
print("\n2. WHILE LOOPS - Condition-Based Repetition")
print("-" * 60)

# Example 2.1: Simple while loop with counter
print("\nExample 2.1: Counting from 1 to 5 with while loop")
count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1  # Important: Update the loop variable

# Example 2.2: While loop with user-like condition
print("\nExample 2.2: Processing items until list is empty")
items = ["apple", "banana", "cherry"]
while items:  # Continues while list is not empty
    item = items.pop()
    print(f"  Processing: {item}")
    print(f"    Remaining items: {len(items)}")

# Example 2.3: While loop with accumulation
print("\nExample 2.3: Sum of numbers from 1 to 10")
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"  Sum of 1 to 10: {total}")

# Example 2.4: While loop with input simulation
print("\nExample 2.4: Password attempt simulation")
password = "secret123"
attempts = 0
max_attempts = 3
user_input = ""

while user_input != password and attempts < max_attempts:
    attempts += 1
    # Simulating user input
    if attempts == 1:
        user_input = "wrong"
    elif attempts == 2:
        user_input = "secret123"
    
    print(f"  Attempt {attempts}: {'Correct!' if user_input == password else 'Incorrect'}")
    
    if user_input == password:
        print(f"  Access granted after {attempts} attempt(s)")
        break
    elif attempts >= max_attempts:
        print(f"  Maximum attempts reached. Access denied.")

print("\n" + "=" * 60)

# ==============================================================================
# 3. CONTROLLING LOOP FLOW (break and continue)
# ==============================================================================
print("\n3. LOOP CONTROL - Using break and continue")
print("-" * 60)

# Example 3.1: Using break to exit early
print("\nExample 3.1: Using break - Finding first number divisible by 7")
for num in range(20, 50):
    if num % 7 == 0:
        print(f"  First number divisible by 7: {num}")
        break  # Exit loop immediately

# Example 3.2: Using continue to skip iterations
print("\nExample 3.2: Using continue - Print only odd numbers")
print("  Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"    {num}")

# Example 3.3: Break in while loop
print("\nExample 3.3: Breaking out of while loop when target is found")
numbers = [3, 7, 12, 15, 18, 22, 25]
target = 18
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"  Found {target} at position {index}")
        break
    index += 1
else:
    # This executes if loop completes without break
    print(f"  {target} not found")

# Example 3.4: Continue in while loop
print("\nExample 3.4: Continue in while loop - Skip negative numbers")
values = [5, -3, 8, -1, 12, -7, 20]
index = 0

print("  Processing positive numbers only:")
while index < len(values):
    value = values[index]
    index += 1
    
    if value < 0:
        continue  # Skip negative values
    
    print(f"    Processing: {value}")

# Example 3.5: Practical example - Data filtering
print("\nExample 3.5: Data filtering with loops")
temperatures = [18, 22, 15, 28, 30, 19, 25, 32, 17]
hot_days = []

for temp in temperatures:
    if temp < 20:
        continue  # Skip cool days
    if temp > 30:
        print(f"  Alert: Extremely hot day at {temp}°C")
        hot_days.append(temp)
        continue
    hot_days.append(temp)

print(f"  Hot days (≥20°C): {hot_days}")

print("\n" + "=" * 60)

# ==============================================================================
# 4. AVOIDING INFINITE LOOPS
# ==============================================================================
print("\n4. INFINITE LOOP PREVENTION")
print("-" * 60)

print("\nExample 4.1: CORRECT - Loop variable is updated")
counter = 0
max_iterations = 5
while counter < max_iterations:
    print(f"  Iteration: {counter}")
    counter += 1  # ✓ Counter is incremented

print("\nExample 4.2: Common infinite loop causes (COMMENTED OUT)")
print("  # WRONG: Forgetting to update loop variable")
print("  # counter = 0")
print("  # while counter < 5:")
print("  #     print(counter)")
print("  #     # Missing: counter += 1")
print()
print("  # WRONG: Condition never becomes False")
print("  # while True:")
print("  #     print('This runs forever')")
print("  #     # Missing: break statement or changing condition")

print("\nExample 4.3: Safe pattern with maximum iterations")
iterations = 0
max_iterations = 10
value = 1

while value < 1000 and iterations < max_iterations:
    value *= 2
    iterations += 1
    print(f"  Iteration {iterations}: value = {value}")

if iterations >= max_iterations:
    print(f"  ⚠ Stopped after {max_iterations} iterations (safety limit)")
else:
    print(f"  ✓ Completed in {iterations} iterations")

print("\nExample 4.4: Using break as safety mechanism")
search_value = 15
numbers_list = [3, 7, 11, 15, 19, 23, 27]
found = False
max_checks = 100
checks = 0

while not found:
    checks += 1
    
    # Safety check to prevent infinite loop
    if checks > max_checks:
        print(f"  ⚠ Safety exit: Exceeded {max_checks} checks")
        break
    
    if checks - 1 < len(numbers_list):
        if numbers_list[checks - 1] == search_value:
            print(f"  ✓ Found {search_value} after {checks} check(s)")
            found = True
    else:
        print(f"  Value {search_value} not found in list")
        break

print("\n" + "=" * 60)

# ==============================================================================
# 5. PRACTICAL DATA PROCESSING EXAMPLES
# ==============================================================================
print("\n5. PRACTICAL EXAMPLES - Real-World Scenarios")
print("-" * 60)

# Example 5.1: Data validation
print("\nExample 5.1: Data validation loop")
raw_data = [25, -5, 30, 0, 15, -10, 20, 35]
valid_data = []

for value in raw_data:
    if value < 0:
        print(f"  ⚠ Skipping invalid value: {value}")
        continue
    valid_data.append(value)

print(f"  Valid data points: {valid_data}")
print(f"  Total valid: {len(valid_data)}/{len(raw_data)}")

# Example 5.2: Calculating statistics
print("\nExample 5.2: Calculating running average")
sales = [100, 150, 200, 175, 225]
total = 0

for day, sale in enumerate(sales, start=1):
    total += sale
    average = total / day
    print(f"  Day {day}: Sale=${sale}, Running Average=${average:.2f}")

# Example 5.3: Data transformation
print("\nExample 5.3: Converting temperatures (Celsius to Fahrenheit)")
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = []

for celsius in celsius_temps:
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_temps.append(fahrenheit)
    print(f"  {celsius}°C = {fahrenheit}°F")

# Example 5.4: Finding patterns
print("\nExample 5.4: Finding consecutive increases")
stock_prices = [100, 105, 103, 108, 112, 115, 110]
increases = 0

for i in range(1, len(stock_prices)):
    if stock_prices[i] > stock_prices[i-1]:
        increases += 1
        print(f"  Day {i}: Price increased from ${stock_prices[i-1]} to ${stock_prices[i]}")

print(f"  Total days with price increases: {increases}")

print("\n" + "=" * 60)

# ==============================================================================
# SUMMARY
# ==============================================================================
print("\nSUMMARY - Key Takeaways")
print("-" * 60)
print("""
✓ FOR LOOPS:
  - Use when you know the number of iterations
  - Ideal for iterating over sequences (lists, ranges, strings)
  - Cleaner syntax for most iteration tasks

✓ WHILE LOOPS:
  - Use when iterations depend on a condition
  - Ideal for unknown number of repetitions
  - Requires manual variable updates

✓ LOOP CONTROL:
  - break: Exit loop immediately
  - continue: Skip to next iteration
  - Keep control flow simple and readable

✓ INFINITE LOOP PREVENTION:
  - Always update loop variables
  - Ensure conditions can become False
  - Use safety limits (max iterations)
  - Test with small examples first

✓ BEST PRACTICES:
  - Choose the right loop type for the task
  - Keep loops simple and readable
  - Avoid deeply nested loops when possible
  - Always ensure loops can terminate
""")

print("=" * 60)
print("MILESTONE COMPLETED")
print("=" * 60)
