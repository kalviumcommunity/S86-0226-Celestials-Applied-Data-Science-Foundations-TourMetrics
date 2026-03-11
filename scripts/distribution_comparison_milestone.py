"""
Distribution Comparison Milestone
==================================
This script demonstrates comparing distributions across multiple columns
in a Pandas DataFrame.

Comparing distributions helps you:
- Understand how different variables behave relative to each other
- Reveal patterns that single-column analysis cannot show
- Build context for analysis decisions
- Identify relationships and differences between variables

Author: Data Science Learner
Date: March 11, 2026
Purpose: Learn to compare and interpret distributions across multiple columns
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
import pandas as pd
import numpy as np


# ==============================================================================
# SECTION 2: LOAD DATA
# ==============================================================================

def load_products_data():
    """
    Load the products dataset.
    
    Returns:
        DataFrame: Products data with ProductID, ProductName, Category, Price, Stock
    """
    df = pd.read_csv('data/raw/products.csv')
    return df


# ==============================================================================
# SECTION 3: UNDERSTANDING DISTRIBUTIONS ACROSS COLUMNS
# ==============================================================================

def explain_distributions():
    """
    Explain what a distribution represents and why comparison matters.
    """
    print("=" * 70)
    print("UNDERSTANDING DISTRIBUTIONS")
    print("=" * 70)
    print()
    
    print("What is a Distribution?")
    print("-" * 70)
    print("A distribution describes how values are spread across a column:")
    print("  • Where most values are located (central tendency)")
    print("  • How spread out the values are (variability)")
    print("  • The shape of the data (symmetric, skewed)")
    print("  • The presence of outliers or unusual values")
    print()
    
    print("Why Compare Distributions?")
    print("-" * 70)
    print("Comparing distributions reveals:")
    print("  • Which columns are more variable than others")
    print("  • Which columns have higher or lower averages")
    print("  • Patterns that exist across multiple variables")
    print("  • Columns that behave differently from the rest")
    print()
    
    print("Key Principle:")
    print("-" * 70)
    print("Never analyze a column in isolation.")
    print("Context comes from comparison.")
    print("Most insights emerge when you compare, not when you isolate.")
    print()
    
    print("What to Compare:")
    print("-" * 70)
    print("  1. Central Tendency: Mean, median across columns")
    print("  2. Spread: Range, standard deviation across columns")
    print("  3. Variability: Coefficient of variation (CV)")
    print("  4. Shape: Skewness patterns")
    print("  5. Outliers: Which columns have extreme values")
    print()


# ==============================================================================
# SECTION 4: COMPUTING STATISTICS FOR MULTIPLE COLUMNS
# ==============================================================================

def compute_multi_column_statistics(df, columns):
    """
    Compute summary statistics for multiple columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to analyze
    
    Returns:
        dict: Dictionary mapping column names to their statistics
    """
    print("=" * 70)
    print("COMPUTING STATISTICS FOR MULTIPLE COLUMNS")
    print("=" * 70)
    print()
    
    all_stats = {}
    
    for col in columns:
        col_data = df[col]
        
        stats = {
            'count': col_data.count(),
            'mean': col_data.mean(),
            'median': col_data.median(),
            'std': col_data.std(),
            'min': col_data.min(),
            'max': col_data.max(),
            'range': col_data.max() - col_data.min(),
            'cv': (col_data.std() / col_data.mean() * 100) if col_data.mean() != 0 else 0
        }
        
        all_stats[col] = stats
        
        print(f"Column: {col}")
        print(f"  Count:  {stats['count']}")
        print(f"  Mean:   {stats['mean']:.2f}")
        print(f"  Median: {stats['median']:.2f}")
        print(f"  Std:    {stats['std']:.2f}")
        print(f"  Range:  {stats['min']:.2f} to {stats['max']:.2f}")
        print(f"  CV:     {stats['cv']:.1f}%")
        print()
    
    return all_stats


# ==============================================================================
# SECTION 5: COMPARING CENTRAL TENDENCY
# ==============================================================================

def compare_central_tendency(df, columns):
    """
    Compare central tendency (mean and median) across columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to compare
    """
    print("=" * 70)
    print("COMPARING CENTRAL TENDENCY ACROSS COLUMNS")
    print("=" * 70)
    print()
    
    print("Central Tendency Comparison Table:")
    print("-" * 70)
    
    # Create comparison table
    print(f"{'Measure':<15} ", end="")
    for col in columns:
        print(f"{col:>15} ", end="")
    print()
    print("-" * (15 + 16 * len(columns)))
    
    # Mean comparison
    print(f"{'Mean':<15} ", end="")
    means = []
    for col in columns:
        mean_val = df[col].mean()
        means.append(mean_val)
        print(f"{mean_val:>15.2f} ", end="")
    print()
    
    # Median comparison
    print(f"{'Median':<15} ", end="")
    medians = []
    for col in columns:
        median_val = df[col].median()
        medians.append(median_val)
        print(f"{median_val:>15.2f} ", end="")
    print()
    
    # Mean-Median difference
    print(f"{'Mean-Median':<15} ", end="")
    for i, col in enumerate(columns):
        diff = means[i] - medians[i]
        print(f"{diff:>15.2f} ", end="")
    print()
    print()
    
    # Interpretation
    print("Interpretation:")
    print("-" * 70)
    
    # Find highest and lowest mean
    max_mean_idx = means.index(max(means))
    min_mean_idx = means.index(min(means))
    
    print(f"1. Central Tendency Levels:")
    print(f"   • Highest average: {columns[max_mean_idx]} (mean: {means[max_mean_idx]:.2f})")
    print(f"   • Lowest average: {columns[min_mean_idx]} (mean: {means[min_mean_idx]:.2f})")
    print()
    
    # Skewness analysis
    print(f"2. Distribution Shape (Mean vs Median):")
    for i, col in enumerate(columns):
        diff_percent = abs(means[i] - medians[i]) / means[i] * 100 if means[i] != 0 else 0
        if diff_percent < 5:
            shape = "symmetric"
        elif means[i] > medians[i]:
            shape = "right-skewed"
        else:
            shape = "left-skewed"
        print(f"   • {col}: {shape} (diff: {diff_percent:.1f}%)")
    print()
    
    # Comparative insight
    print(f"3. Comparative Insight:")
    if all(means[i] > medians[i] for i in range(len(columns))):
        print("   • All columns are right-skewed")
        print("   • Each has high values pulling the average up")
    elif all(means[i] < medians[i] for i in range(len(columns))):
        print("   • All columns are left-skewed")
        print("   • Each has low values pulling the average down")
    else:
        print("   • Columns have different distribution shapes")
        print("   • Mixed patterns suggest different underlying behaviors")
    print()


# ==============================================================================
# SECTION 6: COMPARING SPREAD AND VARIABILITY
# ==============================================================================

def compare_spread_and_variability(df, columns):
    """
    Compare spread and variability across columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to compare
    """
    print("=" * 70)
    print("COMPARING SPREAD AND VARIABILITY ACROSS COLUMNS")
    print("=" * 70)
    print()
    
    print("Variability Comparison Table:")
    print("-" * 70)
    
    # Create comparison table
    print(f"{'Measure':<20} ", end="")
    for col in columns:
        print(f"{col:>15} ", end="")
    print()
    print("-" * (20 + 16 * len(columns)))
    
    # Standard deviation
    print(f"{'Std Deviation':<20} ", end="")
    stds = []
    for col in columns:
        std_val = df[col].std()
        stds.append(std_val)
        print(f"{std_val:>15.2f} ", end="")
    print()
    
    # Range
    print(f"{'Range':<20} ", end="")
    ranges = []
    for col in columns:
        range_val = df[col].max() - df[col].min()
        ranges.append(range_val)
        print(f"{range_val:>15.2f} ", end="")
    print()
    
    # Coefficient of variation
    print(f"{'CV (%)':<20} ", end="")
    cvs = []
    for col in columns:
        mean_val = df[col].mean()
        std_val = df[col].std()
        cv = (std_val / mean_val * 100) if mean_val != 0 else 0
        cvs.append(cv)
        print(f"{cv:>15.1f} ", end="")
    print()
    
    # Min and Max
    print(f"{'Min':<20} ", end="")
    for col in columns:
        print(f"{df[col].min():>15.2f} ", end="")
    print()
    
    print(f"{'Max':<20} ", end="")
    for col in columns:
        print(f"{df[col].max():>15.2f} ", end="")
    print()
    print()
    
    # Interpretation
    print("Interpretation:")
    print("-" * 70)
    
    # Find most and least variable
    max_cv_idx = cvs.index(max(cvs))
    min_cv_idx = cvs.index(min(cvs))
    
    print(f"1. Variability Levels:")
    print(f"   • Most variable: {columns[max_cv_idx]} (CV: {cvs[max_cv_idx]:.1f}%)")
    print(f"   • Least variable: {columns[min_cv_idx]} (CV: {cvs[min_cv_idx]:.1f}%)")
    print()
    
    # Classify variability
    print(f"2. Variability Classification:")
    for i, col in enumerate(columns):
        if cvs[i] < 15:
            level = "Low (consistent values)"
        elif cvs[i] < 30:
            level = "Moderate (typical spread)"
        else:
            level = "High (diverse values)"
        print(f"   • {col}: {level}")
    print()
    
    # Range comparison
    print(f"3. Range Comparison:")
    max_range_idx = ranges.index(max(ranges))
    print(f"   • Widest range: {columns[max_range_idx]} ({ranges[max_range_idx]:.2f})")
    print(f"   • This column has the most diverse values")
    print()
    
    # Comparative insight
    print(f"4. Comparative Insight:")
    cv_diff = max(cvs) - min(cvs)
    if cv_diff < 20:
        print("   • Columns have similar variability levels")
        print("   • Data shows consistent patterns across variables")
    else:
        print("   • Columns have very different variability levels")
        print(f"   • {columns[max_cv_idx]} is much more variable than {columns[min_cv_idx]}")
        print("   • This suggests different underlying processes or scales")
    print()


# ==============================================================================
# SECTION 7: IDENTIFYING PATTERNS AND ANOMALIES
# ==============================================================================

def identify_patterns_and_anomalies(df, columns):
    """
    Identify patterns and anomalies across columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to analyze
    """
    print("=" * 70)
    print("IDENTIFYING PATTERNS AND ANOMALIES")
    print("=" * 70)
    print()
    
    # Compute statistics
    stats = {}
    for col in columns:
        stats[col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'cv': (df[col].std() / df[col].mean() * 100) if df[col].mean() != 0 else 0,
            'range': df[col].max() - df[col].min(),
            'min': df[col].min(),
            'max': df[col].max()
        }
    
    print("Pattern Detection:")
    print("-" * 70)
    
    # Pattern 1: Similar distributions
    cvs = [stats[col]['cv'] for col in columns]
    cv_range = max(cvs) - min(cvs)
    
    print("1. Distribution Similarity:")
    if cv_range < 20:
        print("   ✓ Columns have similar variability patterns")
        print("   → All variables behave consistently")
    else:
        print("   ✗ Columns have different variability patterns")
        print("   → Variables behave differently - investigate why")
    print()
    
    # Pattern 2: Skewness consistency
    print("2. Skewness Consistency:")
    skewness = []
    for col in columns:
        if stats[col]['mean'] > stats[col]['median'] * 1.05:
            skewness.append('right')
        elif stats[col]['mean'] < stats[col]['median'] * 0.95:
            skewness.append('left')
        else:
            skewness.append('symmetric')
    
    if len(set(skewness)) == 1:
        print(f"   ✓ All columns are {skewness[0]}-skewed")
        print("   → Consistent distribution shapes across variables")
    else:
        print("   ✗ Columns have different skewness patterns")
        for i, col in enumerate(columns):
            print(f"   • {col}: {skewness[i]}")
    print()
    
    # Pattern 3: Unusual ranges
    print("3. Unusual Value Ranges:")
    for col in columns:
        max_to_min_ratio = stats[col]['max'] / stats[col]['min'] if stats[col]['min'] != 0 else float('inf')
        if max_to_min_ratio > 100:
            print(f"   ⚠ {col}: Very wide range (max is {max_to_min_ratio:.0f}x min)")
            print(f"     → Investigate potential outliers or data quality issues")
        elif max_to_min_ratio > 10:
            print(f"   • {col}: Wide range (max is {max_to_min_ratio:.1f}x min)")
            print(f"     → Normal for diverse datasets")
    print()
    
    # Pattern 4: Comparative insights
    print("4. Comparative Insights:")
    
    # Check for correlated variability
    if len(columns) == 2:
        cv_ratio = max(cvs) / min(cvs) if min(cvs) != 0 else float('inf')
        if cv_ratio < 1.5:
            print("   • Both columns have similar relative variability")
            print("   → Variables may be related or measured on similar scales")
        else:
            print("   • Columns have different relative variability")
            print("   → Variables behave independently or on different scales")
    print()
    
    # Anomaly detection
    print("Anomaly Detection:")
    print("-" * 70)
    
    anomalies_found = False
    
    for col in columns:
        # Check for extreme CV
        if stats[col]['cv'] > 100:
            print(f"⚠ {col}: Extremely high variability (CV: {stats[col]['cv']:.1f}%)")
            print(f"  → Values are highly dispersed - may contain outliers")
            anomalies_found = True
        
        # Check for very low CV
        if stats[col]['cv'] < 5:
            print(f"ℹ {col}: Very low variability (CV: {stats[col]['cv']:.1f}%)")
            print(f"  → Values are very consistent - may be constant or restricted")
            anomalies_found = True
    
    if not anomalies_found:
        print("✓ No obvious anomalies detected")
        print("  All columns show reasonable distribution characteristics")
    
    print()


# ==============================================================================
# SECTION 8: COMPREHENSIVE COMPARISON SUMMARY
# ==============================================================================

def create_comparison_summary(df, columns):
    """
    Create a comprehensive comparison summary across all columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to compare
    """
    print("=" * 70)
    print("COMPREHENSIVE COMPARISON SUMMARY")
    print("=" * 70)
    print()
    
    # Full statistics table
    print("Complete Statistics Table:")
    print("-" * 70)
    
    # Use pandas describe for comprehensive view
    summary = df[columns].describe()
    print(summary)
    print()
    
    # Additional metrics
    print("Additional Metrics:")
    print("-" * 70)
    
    for col in columns:
        cv = (df[col].std() / df[col].mean() * 100) if df[col].mean() != 0 else 0
        range_val = df[col].max() - df[col].min()
        print(f"\n{col}:")
        print(f"  Range: {range_val:.2f}")
        print(f"  CV: {cv:.1f}%")
        print(f"  Mean > Median: {'Yes' if df[col].mean() > df[col].median() else 'No'}")
    
    print()
    print()
    
    # Key findings
    print("Key Findings:")
    print("-" * 70)
    
    findings = []
    
    # Finding 1: Highest and lowest averages
    means = {col: df[col].mean() for col in columns}
    max_mean_col = max(means, key=means.get)
    min_mean_col = min(means, key=means.get)
    findings.append(f"• {max_mean_col} has the highest average ({means[max_mean_col]:.2f})")
    findings.append(f"• {min_mean_col} has the lowest average ({means[min_mean_col]:.2f})")
    
    # Finding 2: Most and least variable
    cvs = {col: (df[col].std() / df[col].mean() * 100) if df[col].mean() != 0 else 0 
           for col in columns}
    max_cv_col = max(cvs, key=cvs.get)
    min_cv_col = min(cvs, key=cvs.get)
    findings.append(f"• {max_cv_col} is most variable (CV: {cvs[max_cv_col]:.1f}%)")
    findings.append(f"• {min_cv_col} is least variable (CV: {cvs[min_cv_col]:.1f}%)")
    
    # Finding 3: Distribution shapes
    right_skewed = []
    left_skewed = []
    symmetric = []
    
    for col in columns:
        mean_val = df[col].mean()
        median_val = df[col].median()
        if mean_val > median_val * 1.05:
            right_skewed.append(col)
        elif mean_val < median_val * 0.95:
            left_skewed.append(col)
        else:
            symmetric.append(col)
    
    if right_skewed:
        findings.append(f"• Right-skewed: {', '.join(right_skewed)}")
    if left_skewed:
        findings.append(f"• Left-skewed: {', '.join(left_skewed)}")
    if symmetric:
        findings.append(f"• Symmetric: {', '.join(symmetric)}")
    
    for finding in findings:
        print(finding)
    
    print()
    
    # Recommendations
    print("Recommendations for Further Analysis:")
    print("-" * 70)
    print("1. Investigate why some columns are more variable than others")
    print("2. Examine the relationship between variables")
    print("3. Consider visualizing distributions for better understanding")
    print("4. Look for outliers in high-variability columns")
    print("5. Compare these patterns with business context")
    print()


# ==============================================================================
# SECTION 9: VIDEO DEMONSTRATION SCRIPT
# ==============================================================================

def video_demonstration_script(df):
    """
    Complete demonstration script for video walkthrough.
    
    This function provides a step-by-step demonstration for a 2-minute
    video showing distribution comparison across columns.
    
    Args:
        df: DataFrame containing the products data
    """
    print("\n" + "=" * 70)
    print("VIDEO DEMONSTRATION SCRIPT")
    print("Comparing Distributions Across Columns")
    print("=" * 70)
    print()
    
    # PART 1: Introduction (15 seconds)
    print("PART 1: INTRODUCTION")
    print("-" * 70)
    print("Hello! Today I'll demonstrate how to compare distributions")
    print("across multiple columns in a Pandas DataFrame.")
    print()
    print("Here's our products data:")
    print(df.head(10))
    print()
    print("We'll compare Price and Stock distributions.")
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 2: Computing Statistics (30 seconds)
    print("PART 2: COMPUTING STATISTICS FOR BOTH COLUMNS")
    print("-" * 70)
    
    columns = ['Price', 'Stock']
    
    print("Let's compute summary statistics for both columns:")
    print()
    print(df[columns].describe())
    print()
    
    print("Quick comparison:")
    for col in columns:
        print(f"\n{col}:")
        print(f"  Mean:   {df[col].mean():.2f}")
        print(f"  Median: {df[col].median():.2f}")
        print(f"  Std:    {df[col].std():.2f}")
        print(f"  Range:  {df[col].min():.2f} to {df[col].max():.2f}")
    
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 3: Comparing Central Tendency (30 seconds)
    print("PART 3: COMPARING CENTRAL TENDENCY")
    print("-" * 70)
    
    print(f"{'Measure':<15} {'Price':>12} {'Stock':>12}")
    print("-" * 41)
    print(f"{'Mean':<15} {df['Price'].mean():>12.2f} {df['Stock'].mean():>12.2f}")
    print(f"{'Median':<15} {df['Price'].median():>12.2f} {df['Stock'].median():>12.2f}")
    print()
    
    print("Interpretation:")
    print(f"• Both columns: Mean > Median")
    print(f"• This indicates both distributions are right-skewed")
    print(f"• High values pull the average up in both cases")
    print()
    
    price_diff = ((df['Price'].mean() - df['Price'].median()) / df['Price'].mean()) * 100
    stock_diff = ((df['Stock'].mean() - df['Stock'].median()) / df['Stock'].mean()) * 100
    
    print(f"• Price skew: {price_diff:.1f}%")
    print(f"• Stock skew: {stock_diff:.1f}%")
    print()
    
    input("Press Enter to continue...")
    print()
    
    # PART 4: Comparing Spread (30 seconds)
    print("PART 4: COMPARING SPREAD AND VARIABILITY")
    print("-" * 70)
    
    price_cv = (df['Price'].std() / df['Price'].mean()) * 100
    stock_cv = (df['Stock'].std() / df['Stock'].mean()) * 100
    
    print(f"{'Measure':<20} {'Price':>12} {'Stock':>12}")
    print("-" * 46)
    print(f"{'Std Deviation':<20} {df['Price'].std():>12.2f} {df['Stock'].std():>12.2f}")
    print(f"{'Range':<20} {df['Price'].max() - df['Price'].min():>12.2f} {df['Stock'].max() - df['Stock'].min():>12.2f}")
    print(f"{'CV (%)':<20} {price_cv:>12.1f} {stock_cv:>12.1f}")
    print()
    
    print("Interpretation:")
    print(f"• Price CV: {price_cv:.1f}% - Very high variability")
    print(f"• Stock CV: {stock_cv:.1f}% - High variability")
    print()
    
    if price_cv > stock_cv:
        print(f"• Price is more variable than Stock")
        print(f"• Prices are more diverse relative to their mean")
    else:
        print(f"• Stock is more variable than Price")
        print(f"• Stock levels are more diverse relative to their mean")
    
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 5: Key Insights (30 seconds)
    print("PART 5: KEY INSIGHTS")
    print("-" * 70)
    
    print("Summary of Comparison:")
    print()
    print("1. Distribution Shape:")
    print("   • Both columns are right-skewed")
    print("   • Similar distribution patterns")
    print()
    
    print("2. Variability:")
    print(f"   • Both columns show high variability")
    print(f"   • Price: {price_cv:.1f}% CV")
    print(f"   • Stock: {stock_cv:.1f}% CV")
    print()
    
    print("3. Practical Meaning:")
    print("   • We have diverse products (budget to premium)")
    print("   • We have diverse inventory levels (low to high stock)")
    print("   • Both variables show wide ranges")
    print()
    
    print("4. Next Steps:")
    print("   • Investigate why variability is so high")
    print("   • Look at distributions by category")
    print("   • Consider visualizing the data")
    print()
    
    print("This comparison reveals patterns that single-column")
    print("analysis would miss. Always compare, never isolate!")
    print()


# ==============================================================================
# SECTION 10: MAIN EXECUTION
# ==============================================================================

def main():
    """
    Main function to execute the distribution comparison milestone.
    """
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*" + "  DISTRIBUTION COMPARISON MILESTONE".center(68) + "*")
    print("*" + "  Comparing Distributions Across Multiple Columns".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    print("\n")
    
    # Load data
    print("Loading products data...")
    df = load_products_data()
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    print()
    
    # Select numeric columns for comparison
    numeric_columns = ['Price', 'Stock']
    
    # Part 1: Explain distributions
    explain_distributions()
    input("Press Enter to continue...")
    print("\n")
    
    # Part 2: Compute multi-column statistics
    stats = compute_multi_column_statistics(df, numeric_columns)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 3: Compare central tendency
    compare_central_tendency(df, numeric_columns)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 4: Compare spread and variability
    compare_spread_and_variability(df, numeric_columns)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 5: Identify patterns and anomalies
    identify_patterns_and_anomalies(df, numeric_columns)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 6: Create comprehensive summary
    create_comparison_summary(df, numeric_columns)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 7: Video demonstration
    print("=" * 70)
    print("VIDEO DEMONSTRATION")
    print("=" * 70)
    print("The following section provides a complete walkthrough")
    print("suitable for a 2-minute video demonstration.")
    print()
    response = input("Run video demonstration script? (y/n): ")
    if response.lower() == 'y':
        video_demonstration_script(df)
    
    print("\n")
    print("=" * 70)
    print("MILESTONE COMPLETED!")
    print("=" * 70)
    print()
    print("You have learned to:")
    print("✓ Understand what distributions represent across columns")
    print("✓ Compare central tendency across multiple columns")
    print("✓ Compare spread and variability")
    print("✓ Identify patterns and anomalies")
    print("✓ Build comparative analytical thinking")
    print()
    print("Key Takeaways:")
    print("• Never analyze columns in isolation")
    print("• Context comes from comparison")
    print("• Look at both average AND spread")
    print("• Similar patterns suggest relationships")
    print("• Different patterns suggest independent behaviors")
    print()
    print("Next steps:")
    print("- Practice comparing different column combinations")
    print("- Look for patterns across more than two columns")
    print("- Combine comparison with visualization")
    print("- Use comparisons to drive deeper investigation")
    print()


if __name__ == "__main__":
    main()
