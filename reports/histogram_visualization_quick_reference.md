# Histogram Visualization Quick Reference

**One-Page Cheat Sheet for Creating and Interpreting Histograms**

---

## Quick Definition

**Histogram:** Visual representation of data distribution showing frequency of values across bins.

- **X-axis:** Value ranges (bins)
- **Y-axis:** Frequency (count)
- **Purpose:** See the shape of your data

---

## Basic Syntax

```python
import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Create histogram
plt.hist(df['column_name'].dropna(), bins=10, color='steelblue', 
         edgecolor='black', alpha=0.7)
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.title('Distribution of Column Name')
plt.show()
```

---

## Essential Parameters

| Parameter | Default | Description | Example |
|-----------|---------|-------------|---------|
| `bins` | 10 | Number of intervals | `bins=20` |
| `color` | 'blue' | Bar color | `color='steelblue'` |
| `edgecolor` | 'none' | Border color | `edgecolor='black'` |
| `alpha` | 1.0 | Transparency (0-1) | `alpha=0.7` |
| `range` | Auto | Data range to plot | `range=(0, 100)` |

---

## Distribution Shapes

### Symmetric (Normal)
```
     ▄▄▄
   ▄▄███▄▄
 ▄▄███████▄▄
```
- **Mean ≈ Median**
- **Skewness ≈ 0** (-0.5 to 0.5)
- **Interpretation:** Evenly distributed

### Right-Skewed (Positive)
```
 ▄▄▄
 ███▄
 ████▄▄
 ██████▄▄▄▄
```
- **Mean > Median**
- **Skewness > 0.5**
- **Interpretation:** Most values low, few high

### Left-Skewed (Negative)
```
       ▄▄▄
     ▄▄███
   ▄▄████
 ▄▄██████
```
- **Mean < Median**
- **Skewness < -0.5**
- **Interpretation:** Most values high, few low

---

## Interpretation Checklist

✓ **Center:** Where is the peak? Where are most values?  
✓ **Spread:** How wide is the distribution?  
✓ **Shape:** Symmetric, skewed, or multi-modal?  
✓ **Outliers:** Any isolated bars far from main cluster?  
✓ **Gaps:** Any empty bins suggesting missing ranges?

---

## Skewness Calculation

```python
# Calculate skewness
skewness = df['column_name'].skew()

# Interpret
if abs(skewness) < 0.5:
    print("Symmetric")
elif skewness > 0.5:
    print("Right-Skewed")
else:
    print("Left-Skewed")
```

**Rule of Thumb:**
- `|skewness| < 0.5` → Approximately Symmetric
- `0.5 < skewness < 1` → Moderately Skewed
- `|skewness| > 1` → Highly Skewed

---

## Choosing Bin Size

| Data Size | Recommended Bins | Reasoning |
|-----------|------------------|-----------|
| < 50 | 5-10 | Avoid over-detail |
| 50-500 | 10-20 | Balance detail/clarity |
| 500+ | 20-50 | More data supports detail |

**Quick Formula:** `bins = int(sqrt(n))` where n = number of observations

**Sturges' Rule:** `bins = 1 + log2(n)`

```python
import numpy as np

# Auto-calculate bins
n = len(df['column_name'].dropna())
bins = int(np.sqrt(n))

plt.hist(df['column_name'].dropna(), bins=bins)
```

---

## Comparing Multiple Distributions

```python
# Side-by-side histograms
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].hist(df['col1'].dropna(), bins=10, color='steelblue')
axes[0].set_title('Column 1')

axes[1].hist(df['col2'].dropna(), bins=10, color='forestgreen')
axes[1].set_title('Column 2')

axes[2].hist(df['col3'].dropna(), bins=10, color='coral')
axes[2].set_title('Column 3')

plt.tight_layout()
plt.show()
```

---

## Common Patterns

### Uniform Distribution
```
 ████████████
```
All bins roughly equal → No clear pattern

### Bimodal Distribution
```
 ▄▄▄   ▄▄▄
 ███   ███
```
Two peaks → Two distinct groups

### Exponential Distribution
```
 ████▄▄▄
```
Sharp decline → Rare events data

---

## Outlier Detection

```python
# IQR Method
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Find outliers
outliers = df['column'][(df['column'] < lower) | (df['column'] > upper)]

print(f"Outliers: {len(outliers)}")

# Visualize with bounds
plt.hist(df['column'].dropna(), bins=10)
plt.axvline(lower, color='red', linestyle='--', label='Lower Bound')
plt.axvline(upper, color='red', linestyle='--', label='Upper Bound')
plt.legend()
plt.show()
```

---

## Saving Histograms

```python
# Save to file
plt.hist(df['column_name'].dropna(), bins=10)
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.title('Distribution')
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
plt.show()
```

**Image Formats:**
- `.png` - Best for screen/web (default)
- `.pdf` - Best for print/papers
- `.svg` - Best for editing/vector graphics

---

## Advanced Customization

### Add Mean and Median Lines
```python
plt.hist(df['column'].dropna(), bins=10, alpha=0.7)
plt.axvline(df['column'].mean(), color='red', 
            linestyle='--', label='Mean')
plt.axvline(df['column'].median(), color='green', 
            linestyle='--', label='Median')
plt.legend()
```

### Overlay Multiple Histograms
```python
plt.hist(df['col1'].dropna(), bins=10, alpha=0.5, label='Group 1')
plt.hist(df['col2'].dropna(), bins=10, alpha=0.5, label='Group 2')
plt.legend()
```

### Cumulative Histogram
```python
plt.hist(df['column'].dropna(), bins=10, cumulative=True)
plt.title('Cumulative Distribution')
```

### Log Scale (for wide ranges)
```python
plt.hist(df['column'].dropna(), bins=10)
plt.yscale('log')  # Log scale on y-axis
```

---

## Common Mistakes

### ❌ Don't Do This
```python
# Missing .dropna() - includes NaN values
plt.hist(df['column'], bins=10)

# No labels - unclear what's shown
plt.hist(df['column'].dropna(), bins=10)
plt.show()

# Using histogram for categorical data
plt.hist(df['category_column'].dropna(), bins=10)
```

### ✅ Do This Instead
```python
# Remove missing values
plt.hist(df['column'].dropna(), bins=10)

# Always label axes
plt.hist(df['column'].dropna(), bins=10)
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.title('Distribution of Column Name')
plt.show()

# Use bar chart for categorical data
df['category_column'].value_counts().plot(kind='bar')
```

---

## Histogram vs Other Plots

| Plot Type | Best For | Example |
|-----------|----------|---------|
| **Histogram** | Distribution of continuous data | Age, salary, temperature |
| **Bar Chart** | Comparing categories | Product types, regions |
| **Box Plot** | Outliers and quartiles | Identifying extreme values |
| **Density Plot** | Smooth distribution curve | Probability distributions |
| **Scatter Plot** | Relationship between two variables | Height vs weight |

---

## Quick Workflow

1. **Load data:** `df = pd.read_csv('data.csv')`
2. **Check data type:** `df.info()`
3. **Basic stats:** `df['column'].describe()`
4. **Create histogram:** `plt.hist(df['column'].dropna(), bins=10)`
5. **Interpret shape:** Calculate skewness
6. **Check outliers:** Use IQR method
7. **Compare columns:** Side-by-side histograms
8. **Save plot:** `plt.savefig('histogram.png')`

---

## Statistical Insights from Shape

| Shape | Mean vs Median | Common In | Implication |
|-------|----------------|-----------|-------------|
| **Symmetric** | Mean ≈ Median | Natural phenomena | Use mean and std dev |
| **Right-Skewed** | Mean > Median | Income, prices | Consider median, may need log transform |
| **Left-Skewed** | Mean < Median | Scores, ratings | Consider median, ceiling effect |
| **Bimodal** | Varies | Mixed populations | Analyze groups separately |

---

## One-Line Histogram

```python
# Minimal working example
df['column_name'].hist(bins=10)
```

**Note:** This uses pandas' built-in method, but matplotlib gives more control.

---

## Keyboard Shortcuts (Jupyter)

- **Run cell:** `Shift + Enter`
- **Add cell below:** `B`
- **Add cell above:** `A`
- **Delete cell:** `D + D`
- **Save notebook:** `Ctrl/Cmd + S`

---

## Essential Imports

```python
import pandas as pd                # Data manipulation
import numpy as np                 # Numerical operations
import matplotlib.pyplot as plt    # Plotting
```

---

## Quick Debugging

### Problem: Histogram is empty
**Solution:** Check for missing values, use `.dropna()`

### Problem: All values in one bin
**Solution:** Data range too small, increase bins or check data type

### Problem: Can't see bars clearly
**Solution:** Add `edgecolor='black'` and reduce `alpha=0.7`

### Problem: X-axis labels overlap
**Solution:** Rotate labels with `plt.xticks(rotation=45)`

### Problem: Too many bars, looks noisy
**Solution:** Reduce number of bins (try 5-10)

---

## Remember

> **"Numbers describe the data. Histograms let you SEE the data."**

Always visualize before you analyze.

---

## Quick Commands Reference

```python
# Statistics
df['col'].mean()          # Average
df['col'].median()        # Middle value
df['col'].std()           # Standard deviation
df['col'].skew()          # Skewness (-∞ to +∞)
df['col'].min()           # Minimum
df['col'].max()           # Maximum
df['col'].count()         # Non-null count

# Percentiles
df['col'].quantile(0.25)  # Q1 (25th percentile)
df['col'].quantile(0.50)  # Q2 (50th percentile / median)
df['col'].quantile(0.75)  # Q3 (75th percentile)

# Summary
df['col'].describe()      # All statistics at once
```

---

## Pro Tips

💡 **Always check data types first** - Histograms only work with numeric data  
💡 **Remove missing values** - Use `.dropna()` to avoid errors  
💡 **Start with 10 bins** - Then adjust based on what you see  
💡 **Compare mean vs median** - Quick check for skewness  
💡 **Look for gaps** - May indicate missing categories or outliers  
💡 **Use color meaningfully** - Different colors for different groups  
💡 **Save your plots** - Document your analysis with images  

---

**Bookmark this page for quick reference during your analysis!**
