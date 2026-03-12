# Boxplot Visualization Quick Reference

## What is a Boxplot?

A **boxplot** (box-and-whisker plot) is a standardized way of displaying the distribution of data based on five key statistics:

```
    Maximum (upper whisker)
         │
    ┌────┴────┐
    │   Q3    │  ← 75th percentile
    │─────────│  ← Median (Q2, 50th percentile)
    │   Q1    │  ← 25th percentile
    └────┬────┘
         │
    Minimum (lower whisker)
```

## Key Components

| Component | Description | Calculation |
|-----------|-------------|-------------|
| **Q1** | First Quartile (25th percentile) | 25% of data below this value |
| **Median (Q2)** | Middle value (50th percentile) | 50% of data below this value |
| **Q3** | Third Quartile (75th percentile) | 75% of data below this value |
| **IQR** | Interquartile Range | Q3 - Q1 |
| **Lower Whisker** | Minimum within 1.5×IQR from Q1 | Q1 - 1.5×IQR |
| **Upper Whisker** | Maximum within 1.5×IQR from Q3 | Q3 + 1.5×IQR |
| **Outliers** | Points beyond whiskers | < Lower Whisker OR > Upper Whisker |

## Creating Boxplots

### Single Column Boxplot

```python
import matplotlib.pyplot as plt

# Basic boxplot
plt.boxplot(df['column_name'].dropna())
plt.ylabel('Column Name')
plt.title('Distribution of Column')
plt.show()
```

### Enhanced Boxplot with Mean

```python
fig, ax = plt.subplots(figsize=(8, 6))

bp = ax.boxplot(df['column'].dropna(), 
                vert=True,
                patch_artist=True,
                showmeans=True,  # Show mean as diamond
                meanprops=dict(marker='D', markerfacecolor='red', markersize=8))

bp['boxes'][0].set_facecolor('steelblue')
bp['boxes'][0].set_alpha(0.7)
plt.show()
```

### Multiple Columns Comparison

```python
# Method 1: Separate subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for idx, col in enumerate(['col1', 'col2', 'col3']):
    axes[idx].boxplot(df[col].dropna())
    axes[idx].set_title(col)
plt.show()

# Method 2: Side-by-side on same plot
plt.boxplot([df['col1'], df['col2'], df['col3']], 
            labels=['Col1', 'Col2', 'Col3'])
plt.show()
```

### Horizontal Boxplot

```python
plt.boxplot(df['column'].dropna(), vert=False)
plt.xlabel('Values')
plt.show()
```

## Identifying Outliers

### Visual Identification
```python
bp = plt.boxplot(df['column'].dropna(), 
                 showfliers=True,  # Show outliers
                 flierprops=dict(marker='o', markerfacecolor='red', 
                                markersize=10, alpha=0.7))
plt.show()
```

### Programmatic Outlier Detection
```python
# Calculate bounds
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = df[(df['column'] < lower_bound) | (df['column'] > upper_bound)]
print(f"Number of outliers: {len(outliers)}")
```

## Interpretation Guide

### Box Width (IQR)
- **Wide box** → High variability in middle 50% of data
- **Narrow box** → Low variability in middle 50% of data

### Median Position
- **Median in center** → Symmetric distribution
- **Median near Q1** → Right-skewed (positive skew)
- **Median near Q3** → Left-skewed (negative skew)

### Whisker Length
- **Long whiskers** → Wide overall range
- **Short whiskers** → Compact data range
- **Asymmetric whiskers** → Skewed distribution

### Outliers
- **Few outliers** → Mostly typical values
- **Many outliers** → High variability or data quality issues
- **One-sided outliers** → Skewed distribution

## Boxplot vs Histogram

| Feature | Boxplot | Histogram |
|---------|---------|-----------|
| **Shows quartiles** | ✅ Clear | ❌ Not directly |
| **Shows outliers** | ✅ Individual points | ⚠️ May be hidden in bins |
| **Shows shape** | ⚠️ Limited | ✅ Detailed |
| **Compare columns** | ✅ Excellent | ⚠️ Harder |
| **Compact** | ✅ Very | ❌ Needs more space |

**Best Practice**: Use both together for complete understanding!

## Common Mistakes to Avoid

❌ **Don't automatically remove outliers**
- Investigate first
- Outliers might be legitimate exceptional cases

❌ **Don't confuse median with mean**
- Line in box = median
- Diamond (if shown) = mean

❌ **Don't ignore scale differences**
- When comparing columns with different scales, consider normalizing

❌ **Don't use boxplots for detailed shape analysis**
- Use histograms to see modality and exact shape

## Customization Options

### Colors and Style
```python
bp = ax.boxplot(data, vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('coral')
bp['boxes'][0].set_alpha(0.7)
bp['whiskers'][0].set(color='blue', linewidth=2)
bp['medians'][0].set(color='red', linewidth=2)
```

### Multiple Box Colors
```python
colors = ['steelblue', 'coral', 'lightgreen']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
```

## When to Use Boxplots

✅ **Good for:**
- Comparing distributions across multiple groups
- Quick outlier detection
- Understanding quartile ranges
- Compact summaries for reports

❌ **Not ideal for:**
- Showing exact distribution shape
- Small datasets (< 10 points)
- Bimodal or multimodal distributions
- When you need to see every data point

## Practical Workflow

1. **Load data**
   ```python
   df = pd.read_csv('data.csv')
   ```

2. **Check data type**
   ```python
   df['column'].dtype  # Should be numeric
   ```

3. **Handle missing values**
   ```python
   df['column'].dropna()  # Or fillna()
   ```

4. **Create boxplot**
   ```python
   plt.boxplot(df['column'].dropna())
   ```

5. **Interpret results**
   - Note median position
   - Check box width (IQR)
   - Identify outliers
   - Compare with other columns

6. **Investigate outliers**
   ```python
   outliers = df[(df['column'] < lower) | (df['column'] > upper)]
   print(outliers)
   ```

## Advanced: Grouped Boxplots

```python
# Boxplots grouped by category (for future reference)
import seaborn as sns

sns.boxplot(data=df, x='category', y='numeric_column')
plt.show()
```

## Key Takeaways

1. **Boxplots show 5-number summary**: min, Q1, median, Q3, max
2. **IQR (Q3-Q1) is the box height**: Shows middle 50% spread
3. **Outliers are beyond 1.5×IQR from box**: Need investigation
4. **Median position reveals skewness**: Center = symmetric
5. **Compare variability easily**: Box width comparison
6. **Complement with histograms**: See full distribution shape
7. **Don't remove outliers blindly**: Context matters!

## Quick Checklist

- [ ] Data is numeric
- [ ] Missing values are handled
- [ ] Boxplot created and displayed
- [ ] Median identified
- [ ] IQR calculated or noted
- [ ] Outliers identified (if any)
- [ ] Outliers investigated (not just removed)
- [ ] Compared with other columns (if applicable)
- [ ] Combined with histogram for fuller picture

---

**Remember**: Boxplots are excellent for comparison and outlier detection, but combine them with histograms for complete distribution understanding!
