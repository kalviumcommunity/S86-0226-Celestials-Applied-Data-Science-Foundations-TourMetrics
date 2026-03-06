# DataFrame Inspection Quick Reference

## The Three Essential Methods

### 1. head() - Visual Preview

**Purpose:** Quick look at first few rows

```python
df.head()      # First 5 rows (default)
df.head(10)    # First 10 rows
df.tail()      # Last 5 rows
```

**What You See:**
- Column names
- Sample values
- Data alignment
- Visual quality check

**When to Use:**
- First look at new data
- Quick sanity check
- Verify data loaded correctly

---

### 2. info() - Structure & Types

**Purpose:** Understand DataFrame structure

```python
df.info()
```

**What You See:**
- Number of rows and columns
- Column names
- Data types (int64, float64, object, etc.)
- Non-null counts (missing value detection)
- Memory usage

**When to Use:**
- Check data types
- Find missing values
- Understand structure
- Memory optimization

---

### 3. describe() - Numeric Summary

**Purpose:** Statistical summary of numeric columns

```python
df.describe()              # Numeric columns only
df.describe(include='all') # All columns
```

**What You See:**
- **count:** Non-null values
- **mean:** Average
- **std:** Standard deviation
- **min:** Minimum value
- **25%:** First quartile
- **50%:** Median
- **75%:** Third quartile
- **max:** Maximum value

**When to Use:**
- Understand numeric distributions
- Detect outliers
- Check data ranges
- Statistical overview

---

## Complete Inspection Workflow

```python
# Step 1: Load data
df = pd.read_csv('data.csv')

# Step 2: Visual preview
print(df.head())

# Step 3: Structure check
df.info()

# Step 4: Numeric summary
print(df.describe())

# Step 5: Missing values
print(df.isnull().sum())
```

---

## Decision Matrix

| Need | Method | Output |
|------|--------|--------|
| See sample data | `head()` | First N rows |
| Check data types | `info()` | Column dtypes |
| Find missing values | `info()` | Non-null counts |
| Get statistics | `describe()` | Mean, std, min, max |
| Check memory | `info()` | Memory usage |
| Detect outliers | `describe()` | Min/max vs mean |

---

## Common Patterns

### Pattern 1: Quick Inspection
```python
df.head()
df.info()
```

### Pattern 2: Full Analysis
```python
df.head()
df.info()
df.describe()
df.isnull().sum()
```

### Pattern 3: Custom Function
```python
def inspect(df):
    print("Shape:", df.shape)
    print("\nPreview:")
    print(df.head())
    print("\nInfo:")
    df.info()
    print("\nStatistics:")
    print(df.describe())
    print("\nMissing:")
    print(df.isnull().sum())
```

---

## What Each Method Reveals

### head() Reveals:
✓ Visual confirmation of data  
✓ Column names  
✓ Sample values  
✗ Cannot count missing values easily  
✗ No statistical summary  

### info() Reveals:
✓ Exact row/column counts  
✓ Data types  
✓ Missing value counts  
✓ Memory usage  
✗ No sample data  
✗ No statistics  

### describe() Reveals:
✓ Statistical summary  
✓ Distribution insights  
✓ Outlier detection  
✓ Data ranges  
✗ Numeric columns only (by default)  
✗ No missing value details  

---

## Best Practices

### Always Do:
✓ Inspect immediately after loading  
✓ Use all three methods together  
✓ Check for missing values  
✓ Verify data types are correct  
✓ Re-inspect after transformations  

### Never Do:
✗ Start analysis without inspection  
✗ Assume data types are correct  
✗ Ignore missing values  
✗ Skip outlier checks  
✗ Trust data blindly  

---

## Common Issues Detected

### Issue 1: Wrong Data Types
```python
df.info()
# Expected: int64, Got: object
# Solution: Convert or clean data
```

### Issue 2: Missing Values
```python
df.info()
# Non-Null Count shows < total rows
# Solution: Handle nulls before analysis
```

### Issue 3: Outliers
```python
df.describe()
# Max >> mean or min << mean
# Solution: Investigate outliers
```

### Issue 4: Unexpected Range
```python
df.describe()
# Age: min=-5, max=200
# Solution: Data validation needed
```

---

## Cheat Sheet

```python
# Load
df = pd.read_csv('file.csv')

# Preview
df.head()           # First 5 rows
df.head(3)          # First 3 rows
df.tail()           # Last 5 rows

# Structure
df.info()           # Full info
df.shape            # (rows, cols)
df.columns          # Column names
df.dtypes           # Data types

# Statistics
df.describe()       # Numeric summary
df.describe(include='all')  # All columns

# Missing Values
df.isnull().sum()   # Count per column
df.isnull().any()   # Boolean per column

# Quick Checks
len(df)             # Number of rows
df.shape[0]         # Number of rows
df.shape[1]         # Number of columns
df.memory_usage()   # Memory per column
```

---

## Example Output Interpretation

### head() Output
```
   Name  Age  Salary
0  John   25   50000
1  Jane   30   60000
```
→ 3 columns, numeric and text data, looks clean

### info() Output
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Name     100 non-null    object
 1   Age      98 non-null     int64 
 2   Salary   100 non-null    int64 
```
→ 100 rows, Age has 2 missing values

### describe() Output
```
              Age        Salary
count       98.00        100.00
mean        32.50      55000.00
std          5.20       8000.00
min         22.00      40000.00
25%         28.00      50000.00
50%         32.00      55000.00
75%         37.00      60000.00
max         45.00      75000.00
```
→ Age: 22-45 (reasonable), Salary: $40K-$75K (no outliers)

---

## Remember

**Inspection is not optional—it's mandatory!**

Every data professional inspects data before analysis. Make it a habit:

1. Load → 2. Inspect → 3. Clean → 4. Analyze

**The 3-Method Rule:**
Always use `head()`, `info()`, and `describe()` together for complete understanding.
