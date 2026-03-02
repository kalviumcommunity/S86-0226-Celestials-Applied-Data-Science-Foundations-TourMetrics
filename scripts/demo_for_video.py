"""
Simple Loops Demo for Video Walkthrough
========================================
Perfect for a 2-minute video demonstration
"""

print("=" * 50)
print("PYTHON LOOPS DEMONSTRATION")
print("=" * 50)

# ==============================================================================
# 1. FOR LOOP EXAMPLE
# ==============================================================================
print("\n1. FOR LOOP - Iterating over a list")
print("-" * 50)

cities = ["New York", "London", "Tokyo", "Paris"]
for city in cities:
    print(f"   Visiting: {city}")

print("\n   → For loops iterate over sequences")
print("   → Automatically handles each item")
print("   → Stops when sequence ends")

# ==============================================================================
# 2. WHILE LOOP EXAMPLE
# ==============================================================================
print("\n2. WHILE LOOP - Condition-based repetition")
print("-" * 50)

count = 1
while count <= 5:
    print(f"   Count: {count}")
    count += 1  # Critical: Update the variable!

print("\n   → While loops run until condition is False")
print("   → Must manually update variables")
print("   → Risk of infinite loop if not careful")

# ==============================================================================
# 3. BREAK - Exit loop early
# ==============================================================================
print("\n3. BREAK - Stop loop when condition met")
print("-" * 50)

for number in range(1, 10):
    if number == 5:
        print(f"   Found {number}! Stopping loop.")
        break
    print(f"   Checking: {number}")

print("\n   → Break exits loop immediately")
print("   → Useful for search operations")

# ==============================================================================
# 4. CONTINUE - Skip iteration
# ==============================================================================
print("\n4. CONTINUE - Skip certain iterations")
print("-" * 50)

print("   Odd numbers only:")
for number in range(1, 8):
    if number % 2 == 0:
        continue  # Skip even numbers
    print(f"   → {number}")

print("\n   → Continue skips to next iteration")
print("   → Useful for filtering data")

# ==============================================================================
# 5. INFINITE LOOP PREVENTION
# ==============================================================================
print("\n5. INFINITE LOOP PREVENTION")
print("-" * 50)

print("\n   ❌ WRONG - Missing update:")
print("   counter = 0")
print("   while counter < 5:")
print("       print(counter)")
print("       # Forgot: counter += 1")
print()
print("   ✓ CORRECT - Variable updated:")
print("   counter = 0")
print("   while counter < 5:")
print("       print(counter)")
print("       counter += 1  # Critical!")

# ==============================================================================
# PRACTICAL EXAMPLE
# ==============================================================================
print("\n6. PRACTICAL EXAMPLE - Data Processing")
print("-" * 50)

temperatures = [18, 25, 30, 22, 35, 28]
hot_days = 0

for temp in temperatures:
    if temp >= 30:
        hot_days += 1
        print(f"   Hot day: {temp}°C")

print(f"\n   Total hot days (≥30°C): {hot_days} out of {len(temperatures)}")

# ==============================================================================
# SUMMARY
# ==============================================================================
print("\n" + "=" * 50)
print("KEY TAKEAWAYS")
print("=" * 50)
print("""
✓ FOR LOOPS: Best for known sequences
✓ WHILE LOOPS: Best for condition-based repetition
✓ BREAK: Exit loop early
✓ CONTINUE: Skip current iteration
✓ ALWAYS: Ensure loops can terminate!
""")
print("=" * 50)
