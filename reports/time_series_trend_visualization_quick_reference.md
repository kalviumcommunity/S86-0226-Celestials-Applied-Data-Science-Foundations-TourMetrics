# Time-Series Trend Visualization - Quick Reference

## When to Use Line Plots

✅ **Use line plots for:**
- Time-series data with temporal ordering
- Tracking changes over time
- Identifying trends and patterns
- Showing continuity between data points
- Detecting anomalies and outliers

❌ **Don't use line plots for:**
- Categorical data without time component
- Comparing distributions (use histograms)
- Part-to-whole relationships (use pie charts)
- Correlations between variables (use scatter plots)

## Essential Code Snippets

### 1. Load and Prepare Time-Series Data

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Parse dates
df['date'] = pd.to_datetime(df['date'])

# Sort by time (CRITICAL!)
df = df.sort_values('date').reset_index(drop=True)
```

### 2. Create Basic Line Plot

```python
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['value'], 
         linewidth=2, marker='o', markersize=4)
plt.xlabel('Date', fontsize=12, fontweight='bold')
plt.ylabel('Value', fontsize=12, fontweight='bold')
plt.title('Value Over Time', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### 3. Identify Trend

```python
# Calculate trend using linear regression
x = np.arange(len(df))
y = df['value'].values
slope = np.polyfit(x, y, 1)[0]

# Calculate percent change
start_val = df['value'].iloc[0]
end_val = df['value'].iloc[-1]
percent_change = ((end_val - start_val) / start_val) * 100

# Classify trend
if abs(percent_change) < 5:
    direction = "STABLE"
elif slope > 0:
    direction = "UPWARD"
else:
    direction = "DOWNWARD"

print(f"Trend: {direction} ({percent_change:.2f}% change)")
```

### 4. Add Trend Line to Plot

```python
# Calculate trend line
x = np.arange(len(df))
y = df['value'].values
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
trend_line = p(x)

# Plot with trend line
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['value'], 
         linewidth=2, marker='o', label='Actual')
plt.plot(df['date'], trend_line, 
         '--', linewidth=2, color='red', 
         alpha=0.7, label='Trend')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Value Over Time with Trend')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### 5. Detect Anomalies

```python
# Calculate z-scores
mean = df['value'].mean()
std = df['value'].std()
df['z_score'] = np.abs((df['value'] - mean) / std)

# Identify anomalies (threshold = 2 standard deviations)
threshold = 2.0
anomalies = df[df['z_score'] > threshold]

print(f"Anomalies found: {len(anomalies)}")
for idx, row in anomalies.iterrows():
    print(f"  {row['date']}: {row['value']:.2f} (z-score: {row['z_score']:.2f})")
```

### 6. Highlight Anomalies on Plot

```python
plt.figure(figsize=(10, 6))

# Plot main line
plt.plot(df['date'], df['value'], 
         linewidth=2, marker='o', label='Value')

# Highlight anomalies
if len(anomalies) > 0:
    plt.scatter(anomalies['date'], anomalies['value'], 
               color='red', s=150, marker='X', 
               label='Anomalies', zorder=5)

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time-Series with Anomalies Highlighted')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### 7. Plot Multiple Time Series

```python
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# First series
axes[0].plot(df['date'], df['sales'], 
            linewidth=2, color='#2E86AB')
axes[0].set_ylabel('Sales')
axes[0].set_title('Sales Over Time')
axes[0].grid(True, alpha=0.3)

# Second series
axes[1].plot(df['date'], df['temperature'], 
            linewidth=2, color='#A23B72')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Temperature')
axes[1].set_title('Temperature Over Time')
axes[1].grid(True, alpha=0.3)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### 8. Overlay Multiple Series

```python
plt.figure(figsize=(12, 6))

plt.plot(df['date'], df['sales'], 
         linewidth=2, marker='o', label='Sales')
plt.plot(df['date'], df['temperature'], 
         linewidth=2, marker='s', label='Temperature')

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Multiple Time Series Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

## Common Patterns and Solutions

### Pattern 1: Upward Trend
**Characteristics:** Values generally increase over time
**Interpretation:** Growth, improvement, or accumulation
**Example:** Sales growth, user adoption, temperature rise

### Pattern 2: Downward Trend
**Characteristics:** Values generally decrease over time
**Interpretation:** Decline, reduction, or depletion
**Example:** Cost reduction, error rates, inventory depletion

### Pattern 3: Stable/Flat Trend
**Characteristics:** Values remain relatively constant
**Interpretation:** Equilibrium, consistency, or stagnation
**Example:** Steady-state operations, mature products

### Pattern 4: Seasonal Pattern
**Characteristics:** Regular, repeating fluctuations
**Interpretation:** Cyclical behavior, periodic effects
**Example:** Holiday sales, weather patterns, daily traffic

### Pattern 5: Spike/Anomaly
**Characteristics:** Sudden, sharp increase or decrease
**Interpretation:** Unusual event, outlier, or data error
**Example:** Viral event, system failure, data collection error

## Best Practices Checklist

### Data Preparation
- [ ] Parse dates into datetime objects
- [ ] Sort data chronologically
- [ ] Handle missing values appropriately
- [ ] Validate data completeness
- [ ] Check for duplicate timestamps

### Visualization
- [ ] Use appropriate figure size (10x6 minimum)
- [ ] Add clear axis labels
- [ ] Include descriptive title
- [ ] Add grid lines for readability
- [ ] Rotate x-axis labels if needed
- [ ] Use colorblind-friendly colors
- [ ] Include legend for multiple series

### Analysis
- [ ] Require minimum 3 data points for trends
- [ ] Use statistical methods for anomaly detection
- [ ] Calculate both absolute and percent changes
- [ ] Distinguish signal from noise
- [ ] Provide human-readable interpretations

### Reporting
- [ ] Document data source and time range
- [ ] Describe observed trends clearly
- [ ] Explain anomalies and their potential causes
- [ ] Include visualizations with captions
- [ ] Provide actionable insights

## Troubleshooting

### Problem: X-axis labels overlap
**Solution:** Rotate labels and adjust figure size
```python
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
```

### Problem: Plot looks cluttered
**Solution:** Reduce marker size or remove markers
```python
plt.plot(df['date'], df['value'], linewidth=2)  # No markers
```

### Problem: Can't see trend clearly
**Solution:** Add trend line or apply smoothing
```python
# Add trend line (see snippet #4 above)
# Or apply moving average
df['smoothed'] = df['value'].rolling(window=7).mean()
```

### Problem: Too many data points
**Solution:** Resample or aggregate data
```python
# Resample to weekly data
df_weekly = df.resample('W', on='date').mean()
```

### Problem: Multiple series have different scales
**Solution:** Use secondary y-axis or normalize
```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(df['date'], df['sales'], color='blue')
ax2.plot(df['date'], df['temperature'], color='red')
```

## Key Formulas

### Percent Change
```
percent_change = ((end_value - start_value) / start_value) × 100
```

### Z-Score (for anomaly detection)
```
z_score = |value - mean| / standard_deviation
```

### Linear Trend (slope)
```
slope = Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)²)
```

### Moving Average (smoothing)
```
MA(t) = (1/n) × Σ(value[t-n+1] to value[t])
```

## Resources

### Python Libraries
- **pandas**: Data manipulation and time-series handling
- **matplotlib**: Static plotting and visualization
- **numpy**: Numerical computations and statistics
- **seaborn**: Statistical visualization (built on matplotlib)

### Further Reading
- Pandas Time Series Documentation
- Matplotlib Line Plot Examples
- Time Series Analysis Best Practices
- Statistical Anomaly Detection Methods

---

**Quick Tip:** Always sort your time-series data chronologically before plotting. This is the most common mistake that leads to confusing visualizations!
