# Python Loops Quick Reference Guide

## 🔄 FOR LOOPS

### Basic Syntax
```python
for variable in sequence:
    # code block
```

### Common Patterns

#### 1. Range Iteration
```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step=2)
    print(i)
```

#### 2. List Iteration
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### 3. Enumerate (Index + Value)
```python
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")
# Output: 0: a, 1: b, 2: c
```

#### 4. Dictionary Iteration
```python
scores = {"Alice": 85, "Bob": 92}

for key in scores:
    print(key)              # Alice, Bob

for value in scores.values():
    print(value)            # 85, 92

for key, value in scores.items():
    print(f"{key}: {value}")  # Alice: 85, Bob: 92
```

---

## ⭕ WHILE LOOPS

### Basic Syntax
```python
while condition:
    # code block
    # MUST update variables!
```

### Common Patterns

#### 1. Counter-Based
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Critical: update!
```

#### 2. Condition-Based
```python
items = [1, 2, 3]
while items:  # While list not empty
    item = items.pop()
    print(item)
```

#### 3. Input/Event Loop
```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter command: ")
    # process input
```

#### 4. Safe Pattern with Max Iterations
```python
iterations = 0
max_iter = 100

while condition and iterations < max_iter:
    # do work
    iterations += 1

if iterations >= max_iter:
    print("Safety limit reached")
```

---

## 🎮 LOOP CONTROL

### BREAK - Exit Loop Early
```python
for num in range(1, 100):
    if num == 10:
        break  # Stop immediately
    print(num)
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
```

**Use Cases:**
- Found what you're looking for
- Error condition met
- Resource limit reached

### CONTINUE - Skip Iteration
```python
for num in range(1, 6):
    if num == 3:
        continue  # Skip this iteration
    print(num)
# Output: 1, 2, 4, 5
```

**Use Cases:**
- Skip invalid data
- Filter items
- Skip special cases

### ELSE Clause (Optional)
```python
for num in range(1, 5):
    if num == 10:
        break
else:
    print("Loop completed normally")
# Runs if no break occurred
```

---

## ⚠️ INFINITE LOOPS

### Common Causes

#### 1. Forgot to Update Variable
```python
# ❌ WRONG
count = 0
while count < 5:
    print(count)
    # Missing: count += 1

# ✓ CORRECT
count = 0
while count < 5:
    print(count)
    count += 1
```

#### 2. Condition Never False
```python
# ❌ WRONG
while True:
    print("Forever!")
    # No break statement

# ✓ CORRECT
while True:
    print("Processing...")
    if should_stop:
        break
```

#### 3. Logic Error
```python
# ❌ WRONG
x = 10
while x > 0:
    print(x)
    x += 1  # Should be x -= 1

# ✓ CORRECT
x = 10
while x > 0:
    print(x)
    x -= 1
```

### Prevention Strategies
```python
# Strategy 1: Max iterations
iterations = 0
while condition and iterations < 1000:
    # work
    iterations += 1

# Strategy 2: Break on specific condition
while True:
    result = process()
    if result == "done":
        break

# Strategy 3: Timeout/timer (advanced)
import time
start = time.time()
while (time.time() - start) < 10:  # 10 second limit
    # work
```

---

## 🆚 FOR vs WHILE

| Aspect | FOR | WHILE |
|--------|-----|-------|
| **Best For** | Known sequences | Unknown iterations |
| **Syntax** | Cleaner | More verbose |
| **Updates** | Automatic | Manual |
| **Control** | Implicit | Explicit |
| **Use When** | Iterating collections | Waiting for condition |

### Choose FOR When:
- Iterating over lists, ranges, or sequences
- Number of iterations known
- Want cleaner, more Pythonic code

### Choose WHILE When:
- Iterations depend on runtime condition
- Waiting for user input or events
- Complex stopping conditions

---

## 💡 BEST PRACTICES

### ✅ DO:
```python
# Use descriptive variable names
for student in students:
    print(student)

# Keep loops simple
for item in items:
    if item.is_valid():
        process(item)

# Use enumerate when you need index
for i, value in enumerate(values):
    print(f"{i}: {value}")

# Update variables in while loops
count = 0
while count < 10:
    print(count)
    count += 1
```

### ❌ DON'T:
```python
# Don't use meaningless names
for x in y:  # What are x and y?
    print(x)

# Don't nest too deeply
for i in range(10):
    for j in range(10):
        for k in range(10):  # Hard to read
            # ...

# Don't modify list while iterating
items = [1, 2, 3, 4]
for item in items:
    items.remove(item)  # Causes issues!

# Don't forget to update while loop variable
while count < 10:
    print(count)
    # Missing: count += 1
```

---

## 📊 PRACTICAL EXAMPLES

### Data Validation
```python
valid_data = []
for value in raw_data:
    if value < 0:
        continue
    valid_data.append(value)
```

### Calculate Running Total
```python
total = 0
for price in prices:
    total += price
print(f"Total: ${total}")
```

### Find First Match
```python
for item in items:
    if item.matches(criteria):
        print(f"Found: {item}")
        break
```

### Process Until Complete
```python
while not task.is_complete():
    task.do_work()
    task.update_progress()
```

### Filter Data
```python
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
```

### Batch Processing
```python
batch_size = 10
index = 0
while index < len(data):
    batch = data[index:index + batch_size]
    process_batch(batch)
    index += batch_size
```

---

## 🎯 QUICK DECISION TREE

```
Need to repeat code?
│
├─ Know exact number of times? → FOR loop
│  └─ Iterating sequence? → for item in sequence:
│  └─ Need index too? → for i, item in enumerate(sequence):
│  └─ Just count? → for i in range(n):
│
└─ Depends on condition? → WHILE loop
   └─ Simple counter? → while count < max:
   └─ Wait for event? → while not done:
   └─ Process until empty? → while items:

Need to exit early? → Use BREAK
Want to skip some? → Use CONTINUE
```

---

## 🔧 DEBUGGING TIPS

### Loop Not Running?
```python
# Check initial condition
print(f"Starting value: {count}")
print(f"Condition: {count < 10}")
```

### Loop Running Too Many Times?
```python
# Add iteration counter
iterations = 0
for item in items:
    iterations += 1
    print(f"Iteration: {iterations}")
```

### Infinite Loop?
```python
# Add safety exit
safety = 0
while condition and safety < 1000:
    # work
    safety += 1
    if safety >= 1000:
        print("SAFETY EXIT!")
```

### Variable Not Updating?
```python
# Print variable each iteration
while count < 10:
    print(f"Before: {count}")
    count += 1
    print(f"After: {count}")
```

---

## 📝 CHEAT SHEET SUMMARY

| **Action** | **Syntax** | **Example** |
|------------|------------|-------------|
| Iterate list | `for x in list:` | `for city in cities:` |
| Iterate range | `for i in range(n):` | `for i in range(10):` |
| With index | `for i, x in enumerate(list):` | `for i, val in enumerate(data):` |
| While loop | `while condition:` | `while count < 10:` |
| Exit early | `break` | `if found: break` |
| Skip iteration | `continue` | `if invalid: continue` |
| Loop + else | `for/while: ... else:` | Runs if no break |

---

## 🎓 REMEMBER

1. **FOR** = Known sequences, automatic handling
2. **WHILE** = Conditions, manual updates
3. **BREAK** = Exit immediately
4. **CONTINUE** = Skip to next
5. **ALWAYS** = Ensure termination!

---

**Print this page and keep it handy while coding! 📌**
