"""
Summary Statistics Milestone
=============================
This script demonstrates computing and interpreting basic summary statistics
for individual columns in a Pandas DataFrame.

Summary statistics help you quickly understand:
- Central tendency (mean, median)
- Spread (min, max, standard deviation)
- Data distribution characteristics
- Unusual values and outliers

Author: Data Science Learner
Date: March 11, 2026
Purpose: Learn to compute and interpret column-level summary statistics
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
# SECTION 3: UNDERSTANDING COMMON SUMMARY STATISTICS
# ==============================================================================

def explain_summary_statistics():
    """
    Explain what each summary statistic represents.
    
    This function prints descriptions of key statistics:
    - count: Number of non-null values
    - mean: Average value (sum divided by count)
    - median: Middle value when sorted
    - min: Smallest value
    - max: Largest value
    - std: Standard deviation (measure of spread)
    """
    print("=" * 70)
    print("UNDERSTANDING SUMMARY STATISTICS")
    print("=" * 70)
    print()
    
    statistics_guide = {
        "count": "Number of non-null (non-missing) values in the column",
        "mean": "Average value - sum of all values divided by count",
        "median": "Middle value when data is sorted - less affected by outliers",
        "min": "Smallest value in the column",
        "max": "Largest value in the column",
        "std": "Standard deviation - measures how spread out the values are",
        "range": "Difference between max and min (not always shown by default)"
    }
    
    for stat, description in statistics_guide.items():
        print(f"{stat:8} : {description}")
    
    print()
    print("Key Insight:")
    print("- Mean vs Median: If they're very different, you may have outliers")
    print("- Standard Deviation: Higher values = more spread out data")
    print("- Min/Max: Check for unrealistic or unexpected values")
    print()


# ==============================================================================
# SECTION 4: COMPUTING STATISTICS FOR A SINGLE COLUMN
# ==============================================================================

def compute_single_column_statistics(df, column_name):
    """
    Compute comprehensive statistics for a single numeric column.
    
    Args:
        df: DataFrame containing the data
        column_name: Name of the column to analyze
    
    Returns:
        dict: Dictionary of computed statistics
    """
    print("=" * 70)
    print(f"STATISTICS FOR: {column_name}")
    print("=" * 70)
    print()
    
    # Select the column
    column_data = df[column_name]
    
    # Compute individual statistics
    stats = {
        'count': column_data.count(),
        'mean': column_data.mean(),
        'median': column_data.median(),
        'min': column_data.min(),
        'max': column_data.max(),
        'std': column_data.std(),
        'range': column_data.max() - column_data.min()
    }
    
    # Display statistics
    print(f"Column: {column_name}")
    print(f"Data Type: {column_data.dtype}")
    print()
    print("Basic Statistics:")
    print(f"  Count      : {stats['count']}")
    print(f"  Mean       : {stats['mean']:.2f}")
    print(f"  Median     : {stats['median']:.2f}")
    print(f"  Std Dev    : {stats['std']:.2f}")
    print()
    print("Range:")
    print(f"  Minimum    : {stats['min']:.2f}")
    print(f"  Maximum    : {stats['max']:.2f}")
    print(f"  Range      : {stats['range']:.2f}")
    print()
    
    return stats


# ==============================================================================
# SECTION 5: INTERPRETING RESULTS CORRECTLY
# ==============================================================================

def interpret_statistics(df, column_name, stats):
    """
    Interpret the computed statistics and provide insights.
    
    Args:
        df: DataFrame containing the data
        column_name: Name of the column analyzed
        stats: Dictionary of computed statistics
    """
    print("=" * 70)
    print(f"INTERPRETATION: {column_name}")
    print("=" * 70)
    print()
    
    # Compare mean vs median
    mean_median_diff = abs(stats['mean'] - stats['median'])
    mean_median_percent = (mean_median_diff / stats['mean']) * 100 if stats['mean'] != 0 else 0
    
    print("1. Central Tendency Analysis:")
    print(f"   Mean: ${stats['mean']:.2f}" if column_name == 'Price' else f"   Mean: {stats['mean']:.2f} units")
    print(f"   Median: ${stats['median']:.2f}" if column_name == 'Price' else f"   Median: {stats['median']:.2f} units")
    
    if mean_median_percent < 5:
        print("   → Mean and median are very close - data is likely symmetric")
    elif stats['mean'] > stats['median']:
        print("   → Mean > Median - data may be right-skewed (some high values)")
    else:
        print("   → Median > Mean - data may be left-skewed (some low values)")
    print()
    
    # Analyze spread
    coefficient_of_variation = (stats['std'] / stats['mean']) * 100 if stats['mean'] != 0 else 0
    
    print("2. Spread Analysis:")
    print(f"   Standard Deviation: {stats['std']:.2f}")
    print(f"   Coefficient of Variation: {coefficient_of_variation:.1f}%")
    
    if coefficient_of_variation < 15:
        print("   → Low variability - values are clustered near the mean")
    elif coefficient_of_variation < 30:
        print("   → Moderate variability - typical spread")
    else:
        print("   → High variability - values are very spread out")
    print()
    
    # Analyze range
    print("3. Range Analysis:")
    print(f"   Range: {stats['range']:.2f} (from {stats['min']:.2f} to {stats['max']:.2f})")
    range_ratio = stats['max'] / stats['min'] if stats['min'] != 0 else float('inf')
    print(f"   Max is {range_ratio:.1f}x the minimum")
    
    if range_ratio > 10:
        print("   → Large range suggests diverse values or potential outliers")
    else:
        print("   → Moderate range indicates relatively consistent values")
    print()
    
    # Check for unusual values
    print("4. Data Quality Check:")
    print(f"   Count: {stats['count']} values")
    total_rows = len(df)
    if stats['count'] < total_rows:
        missing = total_rows - stats['count']
        print(f"   ⚠ Warning: {missing} missing values detected")
    else:
        print("   ✓ No missing values detected")
    print()


# ==============================================================================
# SECTION 6: COMPARING COLUMNS USING STATISTICS
# ==============================================================================

def compare_multiple_columns(df, columns):
    """
    Compare statistics across multiple columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to compare
    """
    print("=" * 70)
    print("COMPARING COLUMNS")
    print("=" * 70)
    print()
    
    # Compute statistics for all columns
    all_stats = {}
    for col in columns:
        all_stats[col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'min': df[col].min(),
            'max': df[col].max(),
            'cv': (df[col].std() / df[col].mean() * 100) if df[col].mean() != 0 else 0
        }
    
    # Create comparison table
    print(f"{'Statistic':<15} {'Price':>15} {'Stock':>15}")
    print("-" * 47)
    print(f"{'Mean':<15} {all_stats['Price']['mean']:>15.2f} {all_stats['Stock']['mean']:>15.2f}")
    print(f"{'Median':<15} {all_stats['Price']['median']:>15.2f} {all_stats['Stock']['median']:>15.2f}")
    print(f"{'Std Dev':<15} {all_stats['Price']['std']:>15.2f} {all_stats['Stock']['std']:>15.2f}")
    print(f"{'Min':<15} {all_stats['Price']['min']:>15.2f} {all_stats['Stock']['min']:>15.2f}")
    print(f"{'Max':<15} {all_stats['Price']['max']:>15.2f} {all_stats['Stock']['max']:>15.2f}")
    print(f"{'CV (%)':<15} {all_stats['Price']['cv']:>15.1f} {all_stats['Stock']['cv']:>15.1f}")
    print()
    
    # Provide comparative insights
    print("Comparative Insights:")
    print()
    
    # Which column has more variability?
    if all_stats['Price']['cv'] > all_stats['Stock']['cv']:
        print(f"1. Price shows higher variability (CV: {all_stats['Price']['cv']:.1f}%)")
        print(f"   → Prices vary more relative to their mean than stock levels")
    else:
        print(f"1. Stock shows higher variability (CV: {all_stats['Stock']['cv']:.1f}%)")
        print(f"   → Stock levels vary more relative to their mean than prices")
    print()
    
    # Range comparison
    price_range = all_stats['Price']['max'] - all_stats['Price']['min']
    stock_range = all_stats['Stock']['max'] - all_stats['Stock']['min']
    
    print(f"2. Price range: ${price_range:.2f} (${all_stats['Price']['min']:.2f} to ${all_stats['Price']['max']:.2f})")
    print(f"   Stock range: {stock_range:.0f} units ({all_stats['Stock']['min']:.0f} to {all_stats['Stock']['max']:.0f})")
    print()
    
    # Mean vs Median comparison
    price_skew = "right" if all_stats['Price']['mean'] > all_stats['Price']['median'] else "left"
    stock_skew = "right" if all_stats['Stock']['mean'] > all_stats['Stock']['median'] else "left"
    
    print(f"3. Distribution shapes:")
    print(f"   Price appears {price_skew}-skewed (mean {'>' if price_skew == 'right' else '<'} median)")
    print(f"   Stock appears {stock_skew}-skewed (mean {'>' if stock_skew == 'right' else '<'} median)")
    print()


# ==============================================================================
# SECTION 7: USING PANDAS BUILT-IN METHODS
# ==============================================================================

def demonstrate_pandas_describe(df, column_name):
    """
    Demonstrate using Pandas' built-in describe() method.
    
    Args:
        df: DataFrame containing the data
        column_name: Name of the column to describe
    """
    print("=" * 70)
    print(f"PANDAS DESCRIBE() METHOD: {column_name}")
    print("=" * 70)
    print()
    
    print("The describe() method provides a quick statistical summary:")
    print()
    print(df[column_name].describe())
    print()
    
    print("This includes:")
    print("- count: Number of non-null values")
    print("- mean: Average value")
    print("- std: Standard deviation")
    print("- min: Minimum value")
    print("- 25%: First quartile (25th percentile)")
    print("- 50%: Median (50th percentile)")
    print("- 75%: Third quartile (75th percentile)")
    print("- max: Maximum value")
    print()


# ==============================================================================
# SECTION 8: VIDEO DEMONSTRATION SCRIPT
# ==============================================================================

def video_demonstration_script(df):
    """
    Complete demonstration script for video walkthrough.
    
    This function provides a step-by-step demonstration that can be
    recorded as a 2-minute video showing:
    1. Selecting a numeric column
    2. Computing basic summary statistics
    3. Explaining what each statistic means
    4. Comparing with another column
    
    Args:
        df: DataFrame containing the products data
    """
    print("\n" + "=" * 70)
    print("VIDEO DEMONSTRATION SCRIPT")
    print("Summary Statistics for Pandas DataFrames")
    print("=" * 70)
    print()
    
    # PART 1: Introduction (15 seconds)
    print("PART 1: INTRODUCTION")
    print("-" * 70)
    print("Hello! Today I'll show you how to compute and interpret")
    print("summary statistics for individual columns in a Pandas DataFrame.")
    print()
    print("Let's start by loading our products data:")
    print()
    print(df.head())
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 2: Selecting a Column (15 seconds)
    print("PART 2: SELECTING A NUMERIC COLUMN")
    print("-" * 70)
    print("First, let's select the Price column:")
    print()
    price_column = df['Price']
    print("price_column = df['Price']")
    print()
    print("This gives us a Series:")
    print(price_column.head(10))
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 3: Computing Statistics (30 seconds)
    print("PART 3: COMPUTING SUMMARY STATISTICS")
    print("-" * 70)
    print("Now let's compute basic statistics for Price:")
    print()
    
    print("Mean (Average):")
    mean_val = price_column.mean()
    print(f"  price_column.mean() = ${mean_val:.2f}")
    print(f"  → The average price is ${mean_val:.2f}")
    print()
    
    print("Median (Middle Value):")
    median_val = price_column.median()
    print(f"  price_column.median() = ${median_val:.2f}")
    print(f"  → Half the products cost less than ${median_val:.2f}")
    print()
    
    print("Min and Max:")
    min_val = price_column.min()
    max_val = price_column.max()
    print(f"  price_column.min() = ${min_val:.2f}")
    print(f"  price_column.max() = ${max_val:.2f}")
    print(f"  → Prices range from ${min_val:.2f} to ${max_val:.2f}")
    print()
    
    print("Standard Deviation (Spread):")
    std_val = price_column.std()
    print(f"  price_column.std() = ${std_val:.2f}")
    print(f"  → Typical price deviation from the mean is ${std_val:.2f}")
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 4: Interpretation (30 seconds)
    print("PART 4: INTERPRETING THE STATISTICS")
    print("-" * 70)
    print("What do these numbers tell us?")
    print()
    
    print(f"1. Central Tendency:")
    print(f"   Mean: ${mean_val:.2f}, Median: ${median_val:.2f}")
    if abs(mean_val - median_val) < 10:
        print("   → These are close, suggesting balanced distribution")
    else:
        print("   → These differ, suggesting some outliers affecting the mean")
    print()
    
    print(f"2. Spread:")
    cv = (std_val / mean_val) * 100
    print(f"   Coefficient of Variation: {cv:.1f}%")
    print(f"   → Prices vary moderately across products")
    print()
    
    print(f"3. Range:")
    print(f"   From ${min_val:.2f} to ${max_val:.2f}")
    print(f"   → We have both budget and premium products")
    print()
    input("Press Enter to continue...")
    print()
    
    # PART 5: Comparison (30 seconds)
    print("PART 5: COMPARING WITH ANOTHER COLUMN")
    print("-" * 70)
    print("Let's compare Price with Stock:")
    print()
    
    stock_column = df['Stock']
    print(f"{'Statistic':<15} {'Price':>12} {'Stock':>12}")
    print("-" * 41)
    print(f"{'Mean':<15} ${price_column.mean():>11.2f} {stock_column.mean():>11.1f}")
    print(f"{'Median':<15} ${price_column.median():>11.2f} {stock_column.median():>11.1f}")
    print(f"{'Std Dev':<15} ${price_column.std():>11.2f} {stock_column.std():>11.1f}")
    print(f"{'Min':<15} ${price_column.min():>11.2f} {stock_column.min():>11.0f}")
    print(f"{'Max':<15} ${price_column.max():>11.2f} {stock_column.max():>11.0f}")
    print()
    
    price_cv = (price_column.std() / price_column.mean()) * 100
    stock_cv = (stock_column.std() / stock_column.mean()) * 100
    
    print("Key Observations:")
    print(f"1. Price has CV of {price_cv:.1f}% - moderate variability")
    print(f"2. Stock has CV of {stock_cv:.1f}% - {'higher' if stock_cv > price_cv else 'lower'} variability")
    print(f"3. Both columns have complete data (no missing values)")
    print()
    
    print("Using describe() for quick summary:")
    print()
    print(df[['Price', 'Stock']].describe())
    print()


# ==============================================================================
# SECTION 9: MAIN EXECUTION
# ==============================================================================

def main():
    """
    Main function to execute the summary statistics milestone.
    """
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*" + "  SUMMARY STATISTICS MILESTONE".center(68) + "*")
    print("*" + "  Computing and Interpreting Basic Column Statistics".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    print("\n")
    
    # Load data
    print("Loading products data...")
    df = load_products_data()
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    print()
    
    # Part 1: Explain statistics
    explain_summary_statistics()
    input("Press Enter to continue...")
    print("\n")
    
    # Part 2: Compute for Price column
    price_stats = compute_single_column_statistics(df, 'Price')
    input("Press Enter to continue...")
    print("\n")
    
    # Part 3: Interpret Price statistics
    interpret_statistics(df, 'Price', price_stats)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 4: Compute for Stock column
    stock_stats = compute_single_column_statistics(df, 'Stock')
    input("Press Enter to continue...")
    print("\n")
    
    # Part 5: Interpret Stock statistics
    interpret_statistics(df, 'Stock', stock_stats)
    input("Press Enter to continue...")
    print("\n")
    
    # Part 6: Compare columns
    compare_multiple_columns(df, ['Price', 'Stock'])
    input("Press Enter to continue...")
    print("\n")
    
    # Part 7: Demonstrate describe()
    demonstrate_pandas_describe(df, 'Price')
    input("Press Enter to continue...")
    print("\n")
    
    # Part 8: Video demonstration
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
    print("✓ Understand what summary statistics represent")
    print("✓ Compute basic statistics for numeric columns")
    print("✓ Interpret statistical outputs correctly")
    print("✓ Compare statistics across different columns")
    print("✓ Build intuition about data distributions")
    print()
    print("Next steps:")
    print("- Practice with different datasets")
    print("- Look for patterns in your statistics")
    print("- Use statistics to identify data quality issues")
    print("- Combine statistics with visualization")
    print()


if __name__ == "__main__":
    main()
