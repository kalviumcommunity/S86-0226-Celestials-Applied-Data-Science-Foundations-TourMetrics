# DataFrame Selection Milestone - Quick Reference Guide

## 📚 Overview

This milestone focuses on selecting rows and columns using indexing and slicing in Pandas DataFrames. Mastering these techniques is essential for accurate data extraction and analysis.

---

## 📊 Selection Methods Summary

### 1. Column Selection

| Code | Result Type | Description |
|------|-------------|-------------|
| `df['column']` | Series | Single column |
| `df[['col1', 'col2']]` | DataFrame | Multiple columns |
| `df.column` | Series | Dot notation (use with caution) |

**Examples:**
```python
# Single column
cities = df['City']

# Multiple columns
subset = df[['City', 'Attendance', 'Revenue']]

# Reorder columns
reordered = df[['Revenue', 'City', 'Attendance']]
```

---

### 2. Row Selection by Position (.iloc)

**Position-based indexing using integers (0-based)**

| Code | Description |
|------|-------------|
| `df.iloc[0]` | First row |
| `df.iloc[0:3]` | Rows 0, 1, 2 (excludes 3) |
| `df.iloc[[0, 2, 5]]` | Specific rows |
| `df.iloc[-1]` | Last row |
| `df.iloc[:3]` | First 3 rows |
| `df.iloc[-3:]` | Last 3 rows |
| `df.iloc[::2]` | Every 2nd row |

**Examples:**
```python
# First row
first_row = df.iloc[0]

# Rows 1-3 (excludes 4)
middle_rows = df.iloc[1:4]

# Last 3 rows
last_three = df.iloc[-3:]

# Specific rows
selected = df.iloc[[0, 3, 7]]
```

**Key Points:**
- ✅ Uses integer positions (0-based)
- ✅ Slicing is EXCLUSIVE of end index
- ✅ Negative indexing works
- ✅ Returns Series for single row, DataFrame for multiple

---

### 3. Row Selection by Label (.loc)

**Label-based indexing using index values**

| Code | Description |
|------|-------------|
| `df.loc[0]` | Row with label 0 |
| `df.loc[0:3]` | Rows 0, 1, 2, **3** (inclusive!) |
| `df.loc[['A', 'B']]` | Rows with labels 'A', 'B' |
| `df.loc['T001':'T005']` | Label range (inclusive) |

**Examples:**
```python
# Create labeled index
df_labeled = df.set_index('TourID')

# Single row by label
tour = df_labeled.loc['T003']

# Multiple rows by label
tours = df_labeled.loc[['T001', 'T004', 'T007']]

# Slice by label (INCLUSIVE!)
range_tours = df_labeled.loc['T002':'T005']  # Includes T005!
```

**Key Points:**
- ✅ Uses index labels (not positions)
- ✅ Slicing is INCLUSIVE of both start and end
- ✅ Works with any index type (strings, dates, numbers)
- ✅ More explicit and readable

---

### 4. Combined Row and Column Selection

**Format:** `df.iloc[rows, columns]` or `df.loc[rows, columns]`

**Using .iloc (position-based):**
```python
# Specific rows and columns by position
df.iloc[0:3, 1:4]        # Rows 0-2, columns 1-3

# Specific rows, all columns
df.iloc[0:3, :]          # First 3 rows, all columns

# All rows, specific columns
df.iloc[:, [1, 2, 4]]    # All rows, columns 1, 2, 4

# Single value
value = df.iloc[2, 3]    # Row 2, column 3
```

**Using .loc (label-based):**
```python
# Specific rows and columns by label
df_labeled.loc['T002':'T004', ['City', 'Revenue']]

# Specific rows, all columns
df_labeled.loc['T001':'T003', :]

# All rows, specific columns
df_labeled.loc[:, ['City', 'Revenue', 'Rating']]

# Single value
value = df_labeled.loc['T005', 'Revenue']
```

**Key Points:**
- ✅ Use `:` to select all rows or all columns
- ✅ Combine with filtering for powerful selections
- ✅ Always verify results after selection

---

## ⚠️ Common Mistakes to Avoid

### 1. Confusing .loc and .iloc

```python
# ❌ Mistake: Assuming they're the same
df.iloc[0:2]  # Gets rows 0, 1 (excludes 2)
df.loc[0:2]   # Gets rows 0, 1, 2 (includes 2)

# ✅ Remember: .iloc is exclusive, .loc is inclusive
```

### 2. Single vs Double Brackets

```python
# ❌ Wrong: Single brackets for multiple columns
df['City', 'Revenue']  # ERROR!

# ✅ Correct: Double brackets for multiple columns
df[['City', 'Revenue']]
```

### 3. Chained Indexing

```python
# ❌ Problematic: May not work as expected
df[df['Attendance'] > 10000]['Revenue'] = 999999

# ✅ Better: Use .loc for safe assignment
df.loc[df['Attendance'] > 10000, 'Revenue'] = 999999
```

---

## 🎯 When to Use Each Method

| Scenario | Method | Example |
|----------|--------|---------|
| Quick column access | `df['column']` | `df['City']` |
| Multiple columns | `df[['col1', 'col2']]` | `df[['City', 'Revenue']]` |
| First/last N rows | `.iloc[:n]` or `.iloc[-n:]` | `df.iloc[:5]` |
| Specific positions | `.iloc[[0, 2, 5]]` | `df.iloc[[0, 3, 7]]` |
| Specific labels | `.loc[['A', 'B']]` | `df.loc[['T001', 'T005']]` |
| Label ranges | `.loc['A':'D']` | `df.loc['T001':'T005']` |
| Row + column combo | `.iloc[rows, cols]` | `df.iloc[0:3, 1:4]` |

---

## 💡 Practical Examples

### Example 1: Get Top Performers
```python
# Get top 3 cities by revenue
df_sorted = df.sort_values('Revenue', ascending=False)
top3 = df_sorted[['City', 'Revenue', 'Rating']].iloc[:3]
```

### Example 2: Extract Specific Range
```python
# Get middle tours (rows 2-5)
middle = df[['City', 'Attendance']].iloc[2:6]
```

### Example 3: Filter and Select
```python
# Revenue for specific cities
cities = ['New York', 'Los Angeles', 'Chicago']
result = df.loc[df['City'].isin(cities), ['City', 'Revenue']]
```

### Example 4: Custom Index Selection
```python
# Set TourID as index
df_indexed = df.set_index('TourID')

# Select specific tours
tours = df_indexed.loc[['T002', 'T005', 'T007'], ['City', 'Revenue']]
```

---

## 📹 Video Recording Guide (2 Minutes)

### Structure Your Video:

**Introduction (15 seconds)**
- State your name
- Topic: "DataFrame Selection - Indexing and Slicing"
- Show the dataset overview

**Section 1: Column Selection (20 seconds)**
```python
# Demonstrate
df['City']                          # Single column
df[['City', 'Attendance', 'Revenue']]  # Multiple columns
```
- Explain: Single brackets = Series, Double brackets = DataFrame

**Section 2: Row Selection by Position (25 seconds)**
```python
# Demonstrate
df.iloc[0]       # First row
df.iloc[0:3]     # First 3 rows
df.iloc[-2:]     # Last 2 rows
```
- Explain: .iloc uses positions, slicing excludes end

**Section 3: Row Selection by Label (25 seconds)**
```python
# Demonstrate
df_labeled = df.set_index('TourID')
df_labeled.loc['T003']           # Single tour
df_labeled.loc['T002':'T005']    # Range (inclusive!)
```
- Explain: .loc uses labels, slicing includes end

**Section 4: Combined Selection (25 seconds)**
```python
# Demonstrate
df.iloc[0:3, 1:4]                          # Position-based
df_labeled.loc['T001':'T003', ['City', 'Revenue']]  # Label-based
```
- Explain: Format is [rows, columns]

**Conclusion (10 seconds)**
- Summary: "Use .iloc for positions, .loc for labels"
- When to use each method
- Importance of accurate data selection

### Recording Tips:
✅ Ensure screen is clearly visible
✅ Zoom in on code and output
✅ Speak clearly and at moderate pace
✅ Show results after each selection
✅ Keep it under 2 minutes
✅ Test audio and video quality before final recording

---

## 🎓 Knowledge Check

Before recording your video, ensure you can:
- [ ] Select single and multiple columns
- [ ] Use .iloc to select rows by position
- [ ] Use .loc to select rows by label
- [ ] Combine row and column selection
- [ ] Explain when to use each method
- [ ] Demonstrate slicing behavior differences
- [ ] Show practical examples

---

## 📝 Files Created for This Milestone

1. **Script:** `scripts/dataframe_selection_milestone.py`
   - Comprehensive demonstration script
   - Run with: `python scripts/dataframe_selection_milestone.py`

2. **Notebook:** `notebooks/dataframe_selection_milestone.ipynb`
   - Interactive Jupyter notebook
   - Practice exercises included
   - Ideal for video recording

3. **Reference:** `reports/dataframe_selection_quick_reference.md` (this file)
   - Quick lookup guide
   - Video recording tips

---

## 🚀 Next Steps

1. ✅ Run the Python script to see all demonstrations
2. ✅ Practice in the Jupyter notebook
3. ✅ Complete the practice exercises
4. ✅ Plan your video structure
5. ✅ Record your 2-minute video
6. ✅ Submit your work according to course guidelines

---

## 📊 Key Takeaways

| Concept | Remember |
|---------|----------|
| **Column Selection** | Single brackets = Series, Double brackets = DataFrame |
| **.iloc** | Position-based, 0-indexed, EXCLUSIVE slicing |
| **.loc** | Label-based, INCLUSIVE slicing |
| **Combined** | Format: [rows, columns], use : for all |
| **Best Practice** | Be explicit, verify results, avoid chaining |

---

**Remember:** Accurate data selection is the foundation of reliable analysis. Take your time to understand each method and practice regularly!

Good luck with your milestone! 🎉
