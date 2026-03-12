"""
Boxplot Visualization Milestone
================================
This milestone demonstrates visualizing data distributions using boxplots.

Learning Objectives:
- Understand what a boxplot represents
- Create boxplots for single and multiple columns
- Interpret median, quartiles, IQR, and outliers
- Compare distributions across columns
- Use boxplots as part of EDA

Dataset: tours.csv
Columns: TourID, Location, Visitors, Revenue, Rating
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# SECTION 1: Understanding Boxplots
# ============================================================================
print("=" * 70)
print("SECTION 1: Understanding Boxplots")
print("=" * 70)
print("""
A boxplot shows five key statistics:
1. Minimum (lower whisker) - smallest value within 1.5*IQR from Q1
2. Q1 (First Quartile) - 25th percentile
3. Median (Q2) - 50th percentile (middle line in box)
4. Q3 (Third Quartile) - 75th percentile
5. Maximum (upper whisker) - largest value within 1.5*IQR from Q3
6. Outliers - points beyond the whiskers (shown as individual points)

Key Concepts:
- IQR (Interquartile Range) = Q3 - Q1 (height of the box)
- Whiskers extend to 1.5 * IQR from Q1 and Q3
- Wider boxes = more variability
- Outliers appear as individual dots beyond whiskers
""")

# ============================================================================
# SECTION 2: Load and Prepare Data
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 2: Load and Prepare Data")
print("=" * 70)

# Load the dataset
df = pd.read_csv('data/raw/tours.csv')
print(f"\nDataset loaded: {len(df)} rows, {len(df.columns)} columns")
print(f"Columns: {df.columns.tolist()}")

# Convert numeric columns, handling errors
df['Visitors'] = pd.to_numeric(df['Visitors'], errors='coerce')
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Show basic info
print("\nNumeric columns summary:")
print(df[['Visitors', 'Revenue', 'Rating']].describe())

# ============================================================================
# SECTION 3: Creating a Boxplot for a Single Column
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 3: Creating a Boxplot for a Single Column")
print("=" * 70)

# Create a boxplot for Visitors column
fig, ax = plt.subplots(figsize=(8, 6))

# Create boxplot
bp = ax.boxplot(df['Visitors'].dropna(), 
                vert=True,  # Vertical orientation
                patch_artist=True,  # Fill with color
                showmeans=True,  # Show mean as a point
                meanprops=dict(marker='D', markerfacecolor='red', markersize=8))

# Customize appearance
bp['boxes'][0].set_facecolor('steelblue')
bp['boxes'][0].set_alpha(0.7)

ax.set_ylabel('Number of Visitors', fontsize=12)
ax.set_title('Distribution of Tour Visitors\n(Single Column Boxplot)', 
             fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Calculate and display key statistics
visitors_data = df['Visitors'].dropna()
q1 = visitors_data.quantile(0.25)
median = visitors_data.median()
q3 = visitors_data.quantile(0.75)
iqr = q3 - q1
lower_whisker = visitors_data.min()
upper_whisker = visitors_data.max()

# Add text annotation with statistics
stats_text = f"""
Key Statistics:
Median: {median:.0f}
Q1 (25%): {q1:.0f}
Q3 (75%): {q3:.0f}
IQR: {iqr:.0f}
Range: {lower_whisker:.0f} - {upper_whisker:.0f}
"""
ax.text(1.15, 0.5, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='center',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_single_column.png', dpi=300, bbox_inches='tight')
print("✓ Single column boxplot created: boxplot_single_column.png")
print(f"\nInterpretation:")
print(f"- Median (middle line): {median:.0f} visitors")
print(f"- 50% of tours have between {q1:.0f} and {q3:.0f} visitors (the box)")
print(f"- IQR shows middle 50% spread: {iqr:.0f} visitors")
plt.show()

# ============================================================================
# SECTION 4: Comparing Boxplots Across Multiple Columns
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 4: Comparing Boxplots Across Multiple Columns")
print("=" * 70)

# Method 1: Side-by-side boxplots of different columns (need to normalize)
fig, axes = plt.subplots(1, 3, figsize=(15, 6))

# Create individual boxplots for each column
columns = ['Visitors', 'Revenue', 'Rating']
colors = ['steelblue', 'coral', 'lightgreen']

for idx, (col, color) in enumerate(zip(columns, colors)):
    data = df[col].dropna()
    bp = axes[idx].boxplot(data, 
                           vert=True,
                           patch_artist=True,
                           showmeans=True,
                           meanprops=dict(marker='D', markerfacecolor='red', markersize=8))
    
    bp['boxes'][0].set_facecolor(color)
    bp['boxes'][0].set_alpha(0.7)
    
    axes[idx].set_ylabel(col, fontsize=12)
    axes[idx].set_title(f'{col} Distribution', fontsize=12, fontweight='bold')
    axes[idx].grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add statistics
    median_val = data.median()
    iqr_val = data.quantile(0.75) - data.quantile(0.25)
    axes[idx].text(0.5, 0.95, f'Median: {median_val:.1f}\nIQR: {iqr_val:.1f}',
                   transform=axes[idx].transAxes,
                   fontsize=9, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

fig.suptitle('Comparing Distributions Across Columns', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_multiple_columns_separate.png', dpi=300, bbox_inches='tight')
print("✓ Multiple column boxplots created: boxplot_multiple_columns_separate.png")
plt.show()

# Method 2: Normalized comparison (all columns on same scale)
print("\n" + "-" * 70)
print("Creating normalized comparison boxplot...")
print("-" * 70)

# Normalize the data for fair comparison
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_normalized = df[['Visitors', 'Revenue', 'Rating']].copy()
df_normalized = pd.DataFrame(
    scaler.fit_transform(df_normalized.dropna()),
    columns=['Visitors', 'Revenue', 'Rating']
)

# Create comparison boxplot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot([df_normalized['Visitors'], 
                  df_normalized['Revenue'], 
                  df_normalized['Rating']],
                labels=['Visitors', 'Revenue', 'Rating'],
                patch_artist=True,
                showmeans=True,
                meanprops=dict(marker='D', markerfacecolor='red', markersize=8))

# Color each box differently
colors = ['steelblue', 'coral', 'lightgreen']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_ylabel('Standardized Values (Z-scores)', fontsize=12)
ax.set_xlabel('Columns', fontsize=12)
ax.set_title('Normalized Distribution Comparison\n(All columns on same scale)', 
             fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Mean (0)')
ax.legend()

plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_normalized_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Normalized comparison boxplot created: boxplot_normalized_comparison.png")

# Compare variability
print("\nComparison Insights:")
for col in ['Visitors', 'Revenue', 'Rating']:
    data = df[col].dropna()
    iqr = data.quantile(0.75) - data.quantile(0.25)
    range_val = data.max() - data.min()
    print(f"- {col}: IQR={iqr:.1f}, Range={range_val:.1f}")
plt.show()

# ============================================================================
# SECTION 5: Identifying and Interpreting Outliers
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 5: Identifying and Interpreting Outliers")
print("=" * 70)

# Create detailed boxplot with outlier analysis
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Revenue boxplot with outlier detection
revenue_data = df['Revenue'].dropna()
q1_rev = revenue_data.quantile(0.25)
q3_rev = revenue_data.quantile(0.75)
iqr_rev = q3_rev - q1_rev
lower_bound = q1_rev - 1.5 * iqr_rev
upper_bound = q3_rev + 1.5 * iqr_rev

# Identify outliers
outliers_rev = revenue_data[(revenue_data < lower_bound) | (revenue_data > upper_bound)]

bp1 = axes[0].boxplot(revenue_data, 
                      vert=True,
                      patch_artist=True,
                      showmeans=True,
                      showfliers=True,  # Show outliers
                      meanprops=dict(marker='D', markerfacecolor='red', markersize=8),
                      flierprops=dict(marker='o', markerfacecolor='red', markersize=10, 
                                     alpha=0.7, label='Outliers'))

bp1['boxes'][0].set_facecolor('coral')
bp1['boxes'][0].set_alpha(0.7)

axes[0].set_ylabel('Revenue ($)', fontsize=12)
axes[0].set_title('Revenue Distribution with Outliers', fontsize=12, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3, linestyle='--')

# Add outlier bounds
axes[0].axhline(y=lower_bound, color='green', linestyle='--', alpha=0.5, 
                label=f'Lower bound: ${lower_bound:.0f}')
axes[0].axhline(y=upper_bound, color='orange', linestyle='--', alpha=0.5,
                label=f'Upper bound: ${upper_bound:.0f}')
axes[0].legend(fontsize=9)

# Visitors boxplot with outlier detection
visitors_data = df['Visitors'].dropna()
q1_vis = visitors_data.quantile(0.25)
q3_vis = visitors_data.quantile(0.75)
iqr_vis = q3_vis - q1_vis
lower_bound_vis = q1_vis - 1.5 * iqr_vis
upper_bound_vis = q3_vis + 1.5 * iqr_vis

outliers_vis = visitors_data[(visitors_data < lower_bound_vis) | (visitors_data > upper_bound_vis)]

bp2 = axes[1].boxplot(visitors_data,
                      vert=True,
                      patch_artist=True,
                      showmeans=True,
                      showfliers=True,
                      meanprops=dict(marker='D', markerfacecolor='red', markersize=8),
                      flierprops=dict(marker='o', markerfacecolor='red', markersize=10, alpha=0.7))

bp2['boxes'][0].set_facecolor('steelblue')
bp2['boxes'][0].set_alpha(0.7)

axes[1].set_ylabel('Number of Visitors', fontsize=12)
axes[1].set_title('Visitors Distribution with Outliers', fontsize=12, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3, linestyle='--')

axes[1].axhline(y=lower_bound_vis, color='green', linestyle='--', alpha=0.5,
                label=f'Lower bound: {lower_bound_vis:.0f}')
axes[1].axhline(y=upper_bound_vis, color='orange', linestyle='--', alpha=0.5,
                label=f'Upper bound: {upper_bound_vis:.0f}')
axes[1].legend(fontsize=9)

fig.suptitle('Outlier Detection Using Boxplots', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_outlier_detection.png', dpi=300, bbox_inches='tight')
print("✓ Outlier detection boxplot created: boxplot_outlier_detection.png")

print(f"\nOutlier Analysis:")
print(f"Revenue outliers: {len(outliers_rev)} found")
if len(outliers_rev) > 0:
    print(f"  Values: {outliers_rev.values}")
    print(f"  These are {len(outliers_rev)/len(revenue_data)*100:.1f}% of the data")

print(f"\nVisitors outliers: {len(outliers_vis)} found")
if len(outliers_vis) > 0:
    print(f"  Values: {outliers_vis.values}")
    print(f"  These are {len(outliers_vis)/len(visitors_data)*100:.1f}% of the data")

print(f"\nImportant: Outliers are not always errors!")
print(f"- They might represent exceptional tours")
print(f"- Investigate before removing")
print(f"- Ask: Why is this value unusual?")

plt.show()

# ============================================================================
# SECTION 6: Advanced Comparison - Horizontal Boxplots
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 6: Advanced Comparison - Horizontal Boxplots")
print("=" * 70)

# Create horizontal boxplot for easier label reading
fig, ax = plt.subplots(figsize=(10, 6))

data_to_plot = [df['Rating'].dropna(), 
                df['Visitors'].dropna(), 
                df['Revenue'].dropna()]
labels = ['Rating\n(1-5 scale)', 
          'Visitors\n(count)', 
          'Revenue\n($)']

bp = ax.boxplot(data_to_plot,
                labels=labels,
                vert=False,  # Horizontal
                patch_artist=True,
                showmeans=True,
                meanprops=dict(marker='D', markerfacecolor='red', markersize=8))

colors = ['lightgreen', 'steelblue', 'coral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_xlabel('Values', fontsize=12)
ax.set_title('Horizontal Boxplot Comparison\n(Easier to read labels)', 
             fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_horizontal.png', dpi=300, bbox_inches='tight')
print("✓ Horizontal boxplot created: boxplot_horizontal.png")
plt.show()

# ============================================================================
# SECTION 7: Summary and Key Takeaways
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 7: Summary and Key Takeaways")
print("=" * 70)
print("""
✓ MILESTONE COMPLETED!

What You Learned:
1. Boxplot Components
   - Median (Q2): Middle line in the box
   - Q1 and Q3: Bottom and top of the box
   - IQR: Height of the box (Q3 - Q1)
   - Whiskers: Extend to 1.5*IQR from quartiles
   - Outliers: Individual points beyond whiskers

2. Single Column Boxplots
   - Show distribution at a glance
   - Reveal median and spread
   - Highlight symmetry or skewness

3. Multiple Column Comparisons
   - Side-by-side shows relative spread
   - Normalized views allow fair comparison
   - Easy to spot which columns vary more

4. Outlier Interpretation
   - Not always errors or bad data
   - Require context and investigation
   - Help identify exceptional cases

5. When to Use Boxplots
   - Comparing distributions across groups
   - Quick outlier detection
   - Showing spread and central tendency
   - Complement to histograms

Next Steps:
- Use boxplots in your EDA workflow
- Combine with histograms for complete picture
- Always investigate outliers before deciding what to do
- Compare distributions across categorical groups (future milestone)
""")

print("\n" + "=" * 70)
print("All visualizations saved to outputs/visualizations/")
print("=" * 70)
