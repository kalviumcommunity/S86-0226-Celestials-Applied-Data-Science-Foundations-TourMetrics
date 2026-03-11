# Summary Statistics Quick Reference

**Purpose:** Compute and interpret basic statistics for DataFrame columns

---

## Essential Statistics

| Statistic | Method | What It Tells You |
|-----------|--------|-------------------|
| **Count** | `.count()` | Number of non-null values |
| **Mean** | `.mean()` | Average value (affected by outliers) |
| **Median** | `.median()` | Middle value (robust to outliers) |
| **Min** | `.min()` | Smallest value |
| **Max** | `.max()` | Largest value |
| **Std** | `.std()` | Standard deviation (measure of spread) |

---

## Quick Formulas

```python
# Select column
column = df['ColumnName']

# Basic statistics
count = column.count()
mean = column.mean()
median = column.median()
std = column.std()
min_val = column.min()
max_val = column.max()

# Derived statistics
range_val = max_val - min_val
cv = (std / mean) * 100  # Coefficient of Variation (%)

# All at once
summary = column.describe()
```

---

## Interpretation Guide

### Mean vs Median
- **Mean ≈ Median:** Symmetric distribution
- **Mean > Median:** Right-skewed (high outliers)
- **Mean < Median:** Left-skewed (low outliers)

### Coefficient of Variation (CV)
- **CV < 15%:** Low variability
- **CV 15-30%:** Moderate variability
- **CV > 30%:** High variability

### Standard Deviation
- **Higher std:** More spread out
- **Lower std:** More clustered near mean
- **Compare:** std relative to mean (use CV)

### Range Analysis
- **Large range:** Diverse values or outliers
- **Small range:** Consistent values
- **Check:** Min/Max for unrealistic values

---

## Common Patterns

### Detecting Outliers
```python
mean_median_diff = abs(mean - median)
if mean_median_diff / mean > 0.10:  # 10% difference
    print("Potential outliers detected")
```

### Comparing Columns
```python
# Compute for multiple columns
stats_df = df[['Column1', 'Column2']].describe()
print(stats_df)

# Compare variability
cv1 = (df['Column1'].std() / df['Column1'].mean()) * 100
cv2 = (df['Column2'].std() / df['Column2'].mean()) * 100
print(f"Column1 CV: {cv1:.1f}%")
print(f"Column2 CV: {cv2:.1f}%")
```

### Checking Data Quality
```python
total_rows = len(df)
non_null = df['Column'].count()
missing = total_rows - non_null
print(f"Missing values: {missing}")
```

---

## One-Line Commands

```python
# Quick summary
df['Price'].describe()

# Multiple columns
df[['Price', 'Stock']].describe()

# Specific statistics
df['Price'].agg(['mean', 'median', 'std', 'min', 'max'])

# Comparison table
df[['Price', 'Stock']].agg(['mean', 'median', 'std'])
```

---

## Interpretation Checklist

When analyzing statistics, always check:

- [ ] **Count:** Any missing values?
- [ ] **Mean vs Median:** Outliers present?
- [ ] **Min/Max:** Values realistic?
- [ ] **Std/CV:** How variable is the data?
- [ ] **Range:** How spread out are values?
- [ ] **Context:** What do these numbers mean for your data?

---

## Common Mistakes

❌ **Don't:**
- Look only at mean (ignores spread)
- Ignore outliers
- Forget to check for missing values
- Compare statistics without context
- Assume correlation from summary stats

✓ **Do:**
- Look at multiple measures together
- Consider mean AND median
- Check data quality (count)
- Understand variability (std, CV)
- Interpret in context of your domain

---

## Example Output

```
STATISTICS FOR: Price
==================================================
Column: Price
Data Type: float64

Basic Statistics:
  Count      : 14
  Mean       : 208.78
  Median     : 84.99
  Std Dev    : 306.20

Range:
  Minimum    : 4.99
  Maximum    : 899.99
  Range      : 895.00

INTERPRETATION:
→ Mean > Median (right-skewed)
→ High CV (146.7%) = high variability
→ No missing values
```

---

## When to Use Each Statistic

| Use Case | Best Statistic |
|----------|----------------|
| Central tendency (general) | Mean |
| Central tendency (outliers) | Median |
| Data completeness | Count |
| Value bounds | Min/Max |
| Variability | Standard Deviation |
| Compare variability | Coefficient of Variation |
| Quick overview | describe() |

---

## Code Template

```python
"""
Summary Statistics Template
"""
import pandas as pd

# Load data
df = pd.read_csv('your_data.csv')

# Select column
column = df['YourColumn']

# Compute statistics
stats = {
    'count': column.count(),
    'mean': column.mean(),
    'median': column.median(),
    'std': column.std(),
    'min': column.min(),
    'max': column.max(),
    'range': column.max() - column.min(),
    'cv': (column.std() / column.mean()) * 100
}

# Display
for stat, value in stats.items():
    print(f"{stat:8} : {value:.2f}")
    
# Quick method
print(column.describe())
```

---

## Video Demonstration Outline

1. **Introduction** (15s): Show DataFrame
2. **Select Column** (15s): Extract numeric column
3. **Compute Stats** (30s): Calculate mean, median, std, min, max
4. **Interpret** (30s): Explain what numbers mean
5. **Compare** (30s): Show comparison with another column

Total: ~2 minutes

---

## Key Takeaways

1. **Summary statistics** provide quantitative data overview
2. **Mean and median** together reveal distribution shape
3. **Standard deviation** measures spread/variability
4. **Always check** for missing values (count vs total rows)
5. **Compare** mean vs median to detect skewness
6. **Use CV** to compare variability across different scales
7. **Interpret** statistics in context, not in isolation

---

## Next Steps

After mastering summary statistics:
- Combine with visualizations
- Learn about percentiles/quartiles
- Study correlation between columns
- Explore groupby statistics
- Detect and handle outliers

---

## Quick Test

Can you answer these?
1. What does it mean if mean > median?
2. How do you measure variability?
3. What's the difference between std and CV?
4. When would median be better than mean?
5. How do you check for missing values?

**Answers:**
1. Right-skewed distribution
2. Standard deviation or coefficient of variation
3. CV is relative (%), std is absolute value
4. When there are outliers present
5. Compare count() to len(df)

---

*Keep this reference handy while working on data analysis!*
