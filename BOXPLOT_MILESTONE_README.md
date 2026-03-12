# Boxplot Visualization Milestone

## 📊 Overview

This milestone teaches you how to visualize data distributions using **boxplots** (box-and-whisker plots). Boxplots are essential tools for exploratory data analysis, providing a compact summary of distribution, spread, and outliers.

## 🎯 Learning Objectives

By completing this milestone, you will:
- ✅ Understand what each component of a boxplot represents
- ✅ Create boxplots for single and multiple columns
- ✅ Interpret median, quartiles (Q1, Q3), and IQR
- ✅ Identify and interpret outliers
- ✅ Compare distributions across columns
- ✅ Use boxplots effectively in EDA workflows

## 📁 Files in This Milestone

### Main Resources
1. **[boxplot_visualization_milestone.py](scripts/boxplot_visualization_milestone.py)**
   - Complete implementation with 7 sections
   - Creates 5 different visualization types
   - Comprehensive explanations and examples

2. **[boxplot_visualization_milestone.ipynb](notebooks/boxplot_visualization_milestone.ipynb)**
   - Interactive Jupyter notebook
   - Cell-by-cell exploration
   - Practice exercises included

3. **[boxplot_visualization_quick_reference.md](reports/boxplot_visualization_quick_reference.md)**
   - Quick code snippets
   - Component definitions
   - Interpretation guidelines
   - Common mistakes to avoid

### Testing & Validation
4. **[test_boxplot_visualization.py](scripts/test_boxplot_visualization.py)**
   - Pre-flight checks before running main script
   - Verifies data loading, plotting, and outlier detection
   - Ensures output directories exist

### Documentation
5. **[BOXPLOT_VISUALIZATION_COMPLETION.md](BOXPLOT_VISUALIZATION_COMPLETION.md)**
   - Milestone completion summary
   - Learning objectives checklist
   - Key concepts recap
   - Next steps

## 🚀 Quick Start

### Step 1: Run Tests (Recommended)
```bash
# From project root directory
python scripts/test_boxplot_visualization.py
```

This verifies:
- ✓ Data loads correctly
- ✓ Boxplots can be created
- ✓ Multiple column comparisons work
- ✓ Outlier detection functions
- ✓ Output directory exists

### Step 2: Run Main Script
```bash
python scripts/boxplot_visualization_milestone.py
```

This generates:
- 5 boxplot visualizations
- Console output explaining each concept
- Saved images in `outputs/visualizations/`

### Step 3: Interactive Exploration (Optional)
```bash
jupyter notebook notebooks/boxplot_visualization_milestone.ipynb
```

Work through the notebook cell-by-cell for hands-on practice.

## 📊 What You'll Create

### 1. Single Column Boxplot
Shows distribution of one variable (e.g., Visitors)
- **File**: `boxplot_single_column.png`
- **Highlights**: Median, quartiles, IQR annotations

### 2. Multiple Columns Comparison (Separate)
Three side-by-side boxplots for Visitors, Revenue, Rating
- **File**: `boxplot_multiple_columns_separate.png`
- **Highlights**: Compare medians and variability across columns

### 3. Normalized Comparison
All columns on same scale (standardized Z-scores)
- **File**: `boxplot_normalized_comparison.png`
- **Highlights**: Fair comparison of variability

### 4. Outlier Detection
Revenue and Visitors with outlier bounds marked
- **File**: `boxplot_outlier_detection.png`
- **Highlights**: Visual identification of outliers beyond 1.5×IQR

### 5. Horizontal Boxplot
Easier to read labels with horizontal orientation
- **File**: `boxplot_horizontal.png`
- **Highlights**: Better for many categories or long labels

## 🔑 Key Concepts

### Boxplot Components

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
    
    ● ● = Outliers (beyond 1.5×IQR)
```

### Statistical Measures
- **Q1**: First Quartile (25th percentile)
- **Median (Q2)**: Middle value (50th percentile)
- **Q3**: Third Quartile (75th percentile)
- **IQR**: Interquartile Range = Q3 - Q1 (box height)
- **Whiskers**: Extend to 1.5 × IQR from Q1 and Q3
- **Outliers**: Points beyond whiskers

### Interpretation Guide
- **Wide box** → High variability in middle 50%
- **Narrow box** → Low variability
- **Median near center** → Symmetric distribution
- **Median off-center** → Skewed distribution
- **Long whiskers** → Wide overall range
- **Many outliers** → High variability or data quality issues

## 💡 Why Boxplots Matter

### Strengths
✅ **Quick comparison** across multiple groups  
✅ **Clear outlier identification** at a glance  
✅ **Show quartiles** explicitly  
✅ **Compact** - take less space than histograms  
✅ **Standardized** - everyone reads them the same way

### Limitations
⚠️ **Don't show exact distribution shape** (use histograms)  
⚠️ **Can't see modality** (bimodal distributions look similar)  
⚠️ **Less effective for small datasets** (< 10 points)

### Best Practice
**Use boxplots AND histograms together** for complete understanding:
- Boxplot → Quick comparison, outliers, quartiles
- Histogram → Detailed shape, modality, exact distribution

## 📖 What You'll Learn

### Section 1: Understanding Boxplots
- Component definitions
- Statistical foundations
- Visual interpretation

### Section 2: Data Loading & Preparation
- Read CSV data
- Handle missing values
- Convert to numeric types

### Section 3: Single Column Boxplots
- Create basic boxplot
- Add customization (colors, labels)
- Calculate and display statistics

### Section 4: Multiple Column Comparisons
- Side-by-side boxplots
- Normalized comparisons
- Identify variability differences

### Section 5: Outlier Detection
- Calculate outlier bounds (Q1 - 1.5×IQR, Q3 + 1.5×IQR)
- Visual identification
- Programmatic detection
- Interpretation guidelines

### Section 6: Advanced Layouts
- Horizontal boxplots
- Custom color schemes
- Enhanced annotations

### Section 7: Summary & Next Steps
- Recap key concepts
- When to use boxplots
- Integration with EDA workflows

## 🎓 Success Criteria

You've completed this milestone when you can:
- [ ] Explain what Q1, median, Q3, and IQR represent
- [ ] Create a boxplot for a numeric column
- [ ] Compare multiple columns side-by-side
- [ ] Identify outliers visually and programmatically
- [ ] Interpret box width, median position, and whisker length
- [ ] Understand when to use boxplots vs histograms
- [ ] Investigate outliers (not just remove them)
- [ ] Customize boxplot appearance

## 📊 Dataset

**File**: `data/raw/tours.csv`

| Column | Type | Description |
|--------|------|-------------|
| TourID | String | Unique tour identifier |
| Location | String | Tour location |
| Visitors | Numeric | Number of visitors |
| Revenue | Numeric | Revenue generated ($) |
| Rating | Numeric | Customer rating (1-5) |

**Note**: Some values may be missing or non-numeric (e.g., "Not Available")

## ⚠️ Common Mistakes to Avoid

1. ❌ **Auto-removing outliers** → ✅ Investigate first
2. ❌ **Confusing median with mean** → ✅ Line in box = median
3. ❌ **Comparing different scales directly** → ✅ Use normalization
4. ❌ **Using only boxplots** → ✅ Combine with histograms
5. ❌ **Ignoring box asymmetry** → ✅ Shows skewness

## 🔧 Dependencies

Required libraries:
```python
import pandas as pd          # Data manipulation
import matplotlib.pyplot as plt  # Plotting
import numpy as np           # Numeric operations
```

Optional (for normalized comparisons):
```python
from sklearn.preprocessing import StandardScaler
```

Install with:
```bash
pip install pandas matplotlib numpy scikit-learn
```

## 📚 Further Reading

### In This Repository
- [Quick Reference Guide](reports/boxplot_visualization_quick_reference.md)
- [Completion Summary](BOXPLOT_VISUALIZATION_COMPLETION.md)

### Related Milestones
- Histogram Visualization (complement this milestone)
- Distribution Comparison
- Summary Statistics

### External Resources
- [Matplotlib Boxplot Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)
- Statistical interpretation of quartiles
- Advanced outlier detection methods

## 🎯 Next Steps

After completing this milestone:

1. **Combine with Histograms**
   - Create both boxplot and histogram for same data
   - Compare insights from each

2. **Grouped Boxplots** (Future Milestone)
   - Compare distributions across categories
   - Example: Revenue by Location

3. **Advanced Customization**
   - Violin plots (combines boxplot + histogram)
   - Notched boxplots (confidence intervals)
   - Seaborn for enhanced styling

4. **Real EDA Workflow**
   - Integrate boxplots into your standard EDA process
   - Use for quick data quality checks
   - Communicate findings to stakeholders

## 💬 Tips for Success

1. **Start with tests** - Run `test_boxplot_visualization.py` first
2. **Read the Quick Reference** - Keep it open while working
3. **Run the full script** - See all visualizations generated
4. **Explore the notebook** - Hands-on practice
5. **Experiment** - Change colors, orientations, data columns
6. **Compare with histograms** - Create both for complete picture

## 🆘 Troubleshooting

### "Cannot find data/raw/tours.csv"
**Solution**: Run script from project root directory

### "Module not found" error
**Solution**: Install dependencies: `pip install pandas matplotlib numpy`

### Plots don't display
**Solution**: Check if `plt.show()` is called, or run in Jupyter

### Outliers not showing
**Solution**: Ensure `showfliers=True` in boxplot() parameters

## ✅ Completion Checklist

- [ ] Run test script successfully (5/5 tests passed)
- [ ] Run main script and generate 5 visualizations
- [ ] Understand all boxplot components
- [ ] Can calculate IQR and outlier bounds manually
- [ ] Can interpret box width, median position, whiskers
- [ ] Completed notebook or reviewed all code
- [ ] Read Quick Reference Guide
- [ ] Can explain when to use boxplots vs histograms

## 📝 Notes

- Boxplots are **standardized** - same interpretation across datasets
- **1.5 × IQR rule** is convention, not absolute truth
- **Outliers need investigation**, not automatic removal
- **Combine visualizations** for complete understanding
- **Practice makes perfect** - try with different datasets

---

**Ready to get started?**

```bash
# 1. Run tests
python scripts/test_boxplot_visualization.py

# 2. Run main script
python scripts/boxplot_visualization_milestone.py

# 3. Review outputs in outputs/visualizations/
```

**Happy visualizing! 📊**
