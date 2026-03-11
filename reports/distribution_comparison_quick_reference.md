# Distribution Comparison Quick Reference

**Purpose:** Compare distributions across multiple DataFrame columns

---

## Why Compare Distributions?

**Core Principle:** Never analyze columns in isolation - context comes from comparison.

**What Comparison Reveals:**
- Which columns are more/less variable
- Which have higher/lower averages
- Patterns across multiple variables
- Columns that behave differently

---

## Quick Comparison Workflow

```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Select columns to compare
columns = ['Column1', 'Column2']

# 1. Quick statistics
print(df[columns].describe())

# 2. Compare central tendency
for col in columns:
    print(f"{col}: Mean={df[col].mean():.2f}, Median={df[col].median():.2f}")

# 3. Compare variability
for col in columns:
    cv = (df[col].std() / df[col].mean()) * 100
    print(f"{col} CV: {cv:.1f}%")

# 4. Create comparison table
summary = df[columns].agg(['mean', 'median', 'std', 'min', 'max'])
print(summary)
```

---

## What to Compare

| Dimension | Metrics | What It Reveals |
|-----------|---------|-----------------|
| **Central Tendency** | Mean, Median | Average levels, skewness |
| **Spread** | Std, Range | Absolute variability |
| **Relative Variability** | CV (%) | Scale-independent comparison |
| **Shape** | Mean vs Median | Distribution symmetry |
| **Extremes** | Min, Max | Value boundaries |

---

## Interpretation Guide

### Central Tendency Comparison

**Mean vs Median Patterns:**
| Pattern | Meaning | Interpretation |
|---------|---------|----------------|
| Mean ≈ Median | Symmetric | No strong skew |
| Mean > Median | Right-skewed | High values pull average up |
| Mean < Median | Left-skewed | Low values pull average down |

**When ALL columns show same pattern:**
- Consistent distribution shapes
- May indicate systematic behavior
- Look for common drivers

**When columns show DIFFERENT patterns:**
- Independent distributions
- Different underlying processes
- Analyze separately

### Variability Comparison

**Coefficient of Variation (CV):**
```python
cv = (std / mean) * 100
```

| CV Level | Classification | Meaning |
|----------|---------------|---------|
| < 15% | Low variability | Consistent values |
| 15-30% | Moderate variability | Typical spread |
| > 30% | High variability | Diverse values |

**Comparing CVs:**
- **Similar CVs:** Related variability patterns
- **Different CVs:** Independent behaviors
- **Use CV** when columns have different scales

---

## Common Patterns

### Pattern 1: Similar Distributions
```
Price:  Mean=208, Median=85,  CV=147%
Stock:  Mean=48,  Median=28,  CV=106%
```
✓ Both right-skewed (mean > median)
✓ Both highly variable (CV > 100%)
→ Consistent patterns suggest related behaviors

### Pattern 2: Different Distributions
```
Age:     Mean=35,  Median=35,  CV=20%
Income:  Mean=75K, Median=55K, CV=85%
```
✓ Age symmetric, Income right-skewed
✓ Age low variability, Income high variability
→ Different patterns suggest independent behaviors

---

## One-Line Comparisons

```python
# Quick describe for multiple columns
df[['Col1', 'Col2', 'Col3']].describe()

# Compare means
df[['Col1', 'Col2']].mean()

#Compare medians
df[['Col1', 'Col2']].median()

# Compare std
df[['Col1', 'Col2']].std()

# Compare all at once
df[['Col1', 'Col2']].agg(['mean', 'median', 'std', 'min', 'max'])

# Calculate CV for all columns
for col in ['Col1', 'Col2']:
    cv = (df[col].std() / df[col].mean()) * 100
    print(f"{col}: {cv:.1f}%")
```

---

## Creating Comparison Tables

### Method 1: Manual Table
```python
columns = ['Price', 'Stock']

print(f"{'Measure':<15} {'Price':>12} {'Stock':>12}")
print("-" * 41)
print(f"{'Mean':<15} {df['Price'].mean():>12.2f} {df['Stock'].mean():>12.2f}")
print(f"{'Median':<15} {df['Price'].median():>12.2f} {df['Stock'].median():>12.2f}")
print(f"{'Std Dev':<15} {df['Price'].std():>12.2f} {df['Stock'].std():>12.2f}")
```

### Method 2: Using Pandas
```python
# Transpose for better comparison
df[['Price', 'Stock']].describe().T

# Custom aggregation
df[['Price', 'Stock']].agg({
    'Price': ['mean', 'median', 'std'],
    'Stock': ['mean', 'median', 'std']
})
```

---

## Analysis Checklist

When comparing distributions:

- [ ] **Compute statistics** for all columns
- [ ] **Compare central tendency** (mean, median)
- [ ] **Compare spread** (std, range, CV)
- [ ] **Check for skewness** (mean vs median)
- [ ] **Identify patterns** (similar or different?)
- [ ] **Look for anomalies** (extreme values, unusual patterns)
- [ ] **Interpret in context** (what do patterns mean?)
- [ ] **Ask questions** (why are they different/similar?)

---

## Common Mistakes to Avoid

### Don'ts ✗
- ❌ Comparing raw values without considering scale
- ❌ Looking only at mean (ignoring spread)
- ❌ Analyzing columns in isolation
- ❌ Ignoring distribution shape (skewness)
- ❌ Assuming causation from correlation
- ❌ Comparing incompatible types (categorical vs numeric)

### Do's ✓
- ✅ Use CV for different scales
- ✅ Look at mean AND median AND std
- ✅ Compare multiple measures together
- ✅ Check distribution shape
- ✅ Interpret patterns in context
- ✅ Ask why patterns exist

---

## Quick Decision Tree

```
Start here: Do I have multiple numeric columns?
    ↓
  YES → Compute describe() for all columns
    ↓
Compare central tendency:
    Are means and medians similar across columns?
    ↓
    YES → Similar averages
    NO  → Different averages (investigate why)
    ↓
Compare variability:
    Are CV values similar across columns?
    ↓
    YES → Similar spread patterns
    NO  → Different spread patterns (investigate why)
    ↓
Compare shapes:
    Are all columns similarly skewed?
    ↓
    YES → Consistent distributions
    NO  → Different distributions (analyze separately)
    ↓
Result: Understand how columns relate and differ
```

---

## Interpretation Templates

### When Columns Are Similar
```
"Price and Stock show similar distribution patterns:
 • Both are right-skewed (mean > median)
 • Both have high variability (CV > 100%)
 • This suggests related behaviors or common drivers"
```

### When Columns Are Different
```
"Price and Age show very different distributions:
 • Price is right-skewed (mean > median), Age is symmetric
 • Price has high variability (CV=147%), Age has low (CV=20%)
 • This suggests independent variables with different drivers"
```

### When One Is Unusual
```
"Stock shows unusual distribution compared to other columns:
 • Extremely high CV (200%) vs others (30-50%)
 • May indicate data quality issues or outliers
 • Requires further investigation"
```

---

## Video Demonstration Outline

**2-Minute Structure:**
1. **Intro (15s):** Show data, state comparison goal
2. **Statistics (30s):** Compute and display for both columns
3. **Central Tendency (30s):** Compare means/medians, discuss skew
4. **Spread (30s):** Compare CV and range, interpret variability
5. **Conclusion (30s):** Summarize similarities/differences, emphasize comparison

---

## Code Template

```python
"""
Distribution Comparison Template
"""
import pandas as pd

# Load data
df = pd.read_csv('your_data.csv')

# Select columns
columns = ['Column1', 'Column2']

print("=" * 50)
print("DISTRIBUTION COMPARISON")
print("=" * 50)

# 1. Basic statistics
print("\n1. Basic Statistics:")
print(df[columns].describe())

# 2. Central tendency comparison
print("\n2. Central Tendency:")
print(f"{'Column':<15} {'Mean':>12} {'Median':>12}")
print("-" * 41)
for col in columns:
    print(f"{col:<15} {df[col].mean():>12.2f} {df[col].median():>12.2f}")

# 3. Variability comparison
print("\n3. Variability:")
print(f"{'Column':<15} {'Std':>12} {'CV (%)':>12}")
print("-" * 41)
for col in columns:
    std = df[col].std()
    cv = (std / df[col].mean()) * 100
    print(f"{col:<15} {std:>12.2f} {cv:>12.1f}")

# 4. Interpretation
print("\n4. Interpretation:")
for col in columns:
    mean = df[col].mean()
    median = df[col].median()
    
    if mean > median * 1.05:
        skew = "right-skewed"
    elif mean < median * 0.95:
        skew = "left-skewed"
    else:
        skew = "symmetric"
    
    cv = (df[col].std() / mean) * 100
    
    if cv < 15:
        var = "low variability"
    elif cv < 30:
        var = "moderate variability"
    else:
        var = "high variability"
    
    print(f"{col}: {skew}, {var}")

print("\n" + "=" * 50)
```

---

## Key Formulas

```python
# Mean
mean = df['column'].mean()

# Median
median = df['column'].median()

# Standard Deviation
std = df['column'].std()

# Range
range_val = df['column'].max() - df['column'].min()

# Coefficient of Variation (CV)
cv = (std / mean) * 100

# Skewness indicator
if mean > median:
    skew = "right-skewed"
elif mean < median:
    skew = "left-skewed"
else:
    skew = "symmetric"
```

---

## Success Criteria

Your comparison should include:
- ✓ Statistics for multiple columns
- ✓ Central tendency comparison
- ✓ Spread/variability comparison
- ✓ Pattern identification
- ✓ Interpretation in context
- ✓ Emphasis on comparative thinking

---

## Key Takeaways

1. **Never analyze in isolation** - Always compare
2. **Use CV for different scales** - Makes comparison fair
3. **Look at mean AND median** - Reveals skewness
4. **Check variability** - Spread matters as much as average
5. **Similar patterns** → May be related
6. **Different patterns** → Independent behaviors
7. **Comparison drives insights** - Context is everything

---

## Next Steps

After mastering this:
- Compare 3+ columns simultaneously
- Add visualization (histograms, box plots)
- Learn correlation analysis
- Practice groupby comparisons
- Explore distribution testing

---

*Keep this reference handy when comparing distributions!*
