# DataFrame Inspection Video Guide

## Video Requirements

- **Duration:** ~2 minutes
- **Format:** Screen capture with clear visibility
- **Content:** Demonstrate head(), info(), describe() methods
- **Goal:** Show why inspection matters before analysis

---

## Video Script & Structure

### Introduction (15 seconds)

**What to say:**
> "Hi! Today I'm demonstrating DataFrame inspection using Pandas. I'll show you the three essential methods every data scientist uses before analyzing data: head(), info(), and describe()."

**What to show:**
- Open Jupyter notebook or Python script
- Show the datasets you'll be using

---

### Section 1: head() Method (30 seconds)

**What to say:**
> "First, head() gives us a quick visual preview. Let me load the employees dataset and use head() to see the first few rows."

**What to do:**
```python
import pandas as pd
df = pd.read_csv('data/raw/employees.csv')
df.head()
```

**What to explain:**
> "We can see 4 columns: Name, Department, Salary, and Years. The data looks clean and properly aligned. head() is perfect for a quick sanity check."

**What to show:**
- Execute the code
- Point to the output
- Highlight column names and sample values

---

### Section 2: info() Method (40 seconds)

**What to say:**
> "Next, info() tells us about the structure. This is where we check data types and missing values."

**What to do:**
```python
df.info()
```

**What to explain:**
> "Look at this output. We have 5 rows and 4 columns. The Non-Null Count column shows all 5 values are present—no missing data. We have 2 object columns for text and 2 int64 columns for numbers. This is crucial because wrong data types cause analysis errors."

**What to show:**
- Execute the code
- Point to:
  - Row count (5 entries)
  - Non-Null Count (all 5)
  - Dtypes (object vs int64)
  - Memory usage

---

### Section 3: describe() Method (30 seconds)

**What to say:**
> "Finally, describe() gives us statistical summaries for numeric columns."

**What to do:**
```python
df.describe()
```

**What to explain:**
> "For Salary, we see the range is $65,000 to $80,000 with an average of $71,600. For Years, the range is 2 to 5 years. No extreme outliers here. This helps us understand the data distribution before we start analyzing."

**What to show:**
- Execute the code
- Point to:
  - Count (5 values)
  - Mean (averages)
  - Min and Max (ranges)
  - No outliers

---

### Section 4: Why It Matters (15 seconds)

**What to say:**
> "Why does this matter? Because most analysis mistakes start with poor inspection. These three methods—head, info, and describe—catch data issues early and save you from incorrect conclusions later."

**What to show:**
- Quick example of messy data (optional)
- Or just emphasize the point verbally

---

### Conclusion (10 seconds)

**What to say:**
> "Always inspect your data before analyzing it. Use head for preview, info for structure, and describe for statistics. Thanks for watching!"

**What to show:**
- Final screen with key takeaways (optional)

---

## Detailed Walkthrough

### Setup Before Recording

1. **Open your environment:**
   - Jupyter Notebook: `notebooks/dataframe_inspection_milestone.ipynb`
   - OR Python script: `scripts/dataframe_inspection_demo.py`
   - OR interactive Python session

2. **Prepare your screen:**
   - Close unnecessary windows
   - Increase font size for visibility
   - Test screen recording software

3. **Have data ready:**
   - Ensure `data/raw/employees.csv` exists
   - Optionally prepare `data/raw/books.csv`

### Recording Tips

1. **Audio:**
   - Speak clearly and at moderate pace
   - Explain what you're doing as you do it
   - Don't rush—2 minutes is enough time

2. **Visual:**
   - Make sure code and output are clearly visible
   - Use zoom if needed
   - Highlight important parts with cursor

3. **Flow:**
   - Follow the script but be natural
   - If you make a mistake, pause and continue
   - Keep it conversational

---

## Code to Execute (In Order)

### Complete Demo Script

```python
# Import pandas
import pandas as pd

# Load dataset
print("Loading employees dataset...")
df = pd.read_csv('data/raw/employees.csv')

# 1. HEAD - Visual Preview
print("\n1. HEAD() - Visual Preview")
print("="*50)
print(df.head())
print("\n→ Shows first 5 rows, column names, sample values")

# 2. INFO - Structure & Types
print("\n2. INFO() - Structure & Types")
print("="*50)
df.info()
print("\n→ Shows data types, null counts, memory usage")

# 3. DESCRIBE - Numeric Summary
print("\n3. DESCRIBE() - Numeric Summary")
print("="*50)
print(df.describe())
print("\n→ Shows statistics: mean, min, max, quartiles")

# Summary
print("\n" + "="*50)
print("ALWAYS inspect data before analysis!")
print("Use: head() + info() + describe()")
print("="*50)
```

---

## Alternative: Jupyter Notebook Demo

If using Jupyter, execute cells in this order:

**Cell 1: Import and Load**
```python
import pandas as pd
df = pd.read_csv('data/raw/employees.csv')
```

**Cell 2: head()**
```python
# Visual preview
df.head()
```

**Cell 3: info()**
```python
# Structure and types
df.info()
```

**Cell 4: describe()**
```python
# Numeric summary
df.describe()
```

**Cell 5: Explain**
```python
print("Key Takeaway:")
print("Always use all three methods together!")
print("- head(): Visual preview")
print("- info(): Structure & missing values")
print("- describe(): Numeric statistics")
```

---

## What to Emphasize

### For head()
- "Quick visual check"
- "See column names and sample values"
- "Verify data loaded correctly"

### For info()
- "Check data types—very important!"
- "Non-Null Count reveals missing values"
- "All 5 values present—no missing data"

### For describe()
- "Statistical summary of numeric columns"
- "Check ranges and averages"
- "Detect outliers by comparing min/max to mean"

---

## Common Mistakes to Avoid

### Don't:
- Rush through the explanation
- Skip explaining what the output means
- Use datasets with too many columns (hard to see)
- Forget to explain WHY inspection matters
- Make the video too long (keep it ~2 minutes)

### Do:
- Speak clearly and confidently
- Point to specific parts of the output
- Explain the practical value
- Keep it concise and focused
- Show enthusiasm for the topic

---

## Example Narration (Full Script)

> "Hi everyone! Today I'm demonstrating DataFrame inspection in Pandas—the three methods you must use before any data analysis.
>
> Let me start by loading the employees dataset. [Execute load code]
>
> First method: head(). [Execute df.head()] This shows the first 5 rows. We can see our columns: Name, Department, Salary, and Years. The data looks clean and properly aligned. This is our quick visual sanity check.
>
> Second method: info(). [Execute df.info()] This is crucial. Look at the output: we have 5 rows and 4 columns. The Non-Null Count shows all 5 values are present in each column—no missing data. We have 2 object columns for text data and 2 int64 columns for numeric data. Checking data types here prevents analysis errors later.
>
> Third method: describe(). [Execute df.describe()] This gives us statistics for numeric columns. Salary ranges from 65,000 to 80,000 with an average of 71,600. Years ranges from 2 to 5 with an average of 3.4. No extreme outliers detected. This helps us understand the distribution.
>
> Why does this matter? Most analysis mistakes start with poor inspection. These three methods catch data issues early—wrong types, missing values, outliers—before they ruin your analysis.
>
> Remember: always inspect your data. Use head for preview, info for structure, and describe for statistics. Make it a habit, and your analysis will be reliable. Thanks for watching!"

---

## Checklist Before Submitting

- [ ] Video is approximately 2 minutes
- [ ] Screen is clearly visible
- [ ] Audio is clear and understandable
- [ ] Demonstrated head() method
- [ ] Demonstrated info() method
- [ ] Demonstrated describe() method
- [ ] Explained why inspection matters
- [ ] Showed actual code execution
- [ ] Explained the output of each method
- [ ] Kept it concise and focused

---

## Submission

After recording:
1. Review the video to ensure quality
2. Upload to required platform
3. Submit the video link as instructed
4. Include this milestone report if required

---

**Good luck with your video! You've got this!** 🎥
