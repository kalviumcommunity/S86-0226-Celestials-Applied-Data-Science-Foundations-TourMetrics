"""
Histogram Visualization Milestone
==================================
This script demonstrates creating and interpreting histograms for numeric data.

Histograms help you:
- Visualize how values are distributed across a column
- Identify skewness, spread, and patterns
- Detect potential outliers visually
- Support exploratory data analysis (EDA)

Author: Data Science Learner
Date: March 11, 2026
Purpose: Learn to create and interpret histograms for data distributions
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==============================================================================
# SECTION 2: LOAD DATA
# ==============================================================================

def load_tours_data():
    """
    Load the tours dataset.
    
    Returns:
        DataFrame: Tours data with TourID, Location, Visitors, Revenue, Rating
    """
    df = pd.read_csv('data/raw/tours.csv')
    
    # Convert numeric columns, handling non-numeric values
    numeric_columns = ['Visitors', 'Revenue', 'Rating']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df


# ==============================================================================
# SECTION 3: UNDERSTANDING HISTOGRAMS
# ==============================================================================

def explain_histograms():
    """
    Explain what histograms are and why they matter.
    """
    print("=" * 70)
    print("UNDERSTANDING HISTOGRAMS")
    print("=" * 70)
    print()
    
    print("What is a Histogram?")
    print("-" * 70)
    print("A histogram is a visual representation of data distribution:")
    print("  • X-axis: Range of values (divided into bins)")
    print("  • Y-axis: Frequency (count of values in each bin)")
    print("  • Bars: Height shows how many values fall in that range")
    print()
    
    print("Histogram vs Bar Chart:")
    print("-" * 70)
    print("  Histogram:")
    print("    - For continuous numeric data")
    print("    - Bars touch each other")
    print("    - Shows distribution shape")
    print()
    print("  Bar Chart:")
    print("    - For categorical data")
    print("    - Bars are separated")
    print("    - Shows comparisons between categories")
    print()
    
    print("Why Histograms Matter:")
    print("-" * 70)
    print("  • Reveal patterns that summary statistics hide")
    print("  • Show distribution shape (normal, skewed, bimodal)")
    print("  • Identify outliers and unusual values visually")
    print("  • Guide statistical analysis decisions")
    print("  • Make data behavior intuitive and obvious")
    print()
    
    print("Key Principle:")
    print("-" * 70)
    print("'Numbers describe the data. Histograms let you SEE the data.'")
    print()


# ==============================================================================
# SECTION 4: HISTOGRAMS - KEY CONCEPTS
# ==============================================================================

def explain_bins_and_frequencies():
    """
    Explain bins, frequencies, and range in histograms.
    """
    print("=" * 70)
    print("BINS AND FREQUENCIES")
    print("=" * 70)
    print()
    
    print("What are Bins?")
    print("-" * 70)
    print("Bins are intervals that divide the data range:")
    print("  • Each bin represents a range of values")
    print("  • Example: 0-10, 10-20, 20-30")
    print("  • More bins = more detailed view")
    print("  • Fewer bins = simpler, smoother view")
    print()
    
    print("What is Frequency?")
    print("-" * 70)
    print("Frequency is the count of values in each bin:")
    print("  • Height of bar = number of data points in that range")
    print("  • Tall bar = many values in that range")
    print("  • Short bar = few values in that range")
    print("  • Empty bar = no values in that range")
    print()
    
    print("Range:")
    print("-" * 70)
    print("Range is the span from minimum to maximum value:")
    print("  • Shows the full extent of the data")
    print("  • Helps understand data scale")
    print("  • Reveals presence of outliers")
    print()
    
    print("Choosing the Right Number of Bins:")
    print("-" * 70)
    print("  • Too few bins: Lose important detail")
    print("  • Too many bins: Too noisy, hard to interpret")
    print("  • Default (10-20 bins) works for most cases")
    print("  • Adjust based on data size and distribution")
    print()


# ==============================================================================
# SECTION 5: CREATING A SINGLE-COLUMN HISTOGRAM
# ==============================================================================

def create_single_histogram(df, column_name):
    """
    Create a histogram for a single numeric column.
    
    Args:
        df: DataFrame containing the data
        column_name: Name of the numeric column to visualize
    """
    print("=" * 70)
    print(f"HISTOGRAM FOR '{column_name}'")
    print("=" * 70)
    print()
    
    # Display basic statistics first
    print(f"Statistics for {column_name}:")
    print(f"  Count:  {df[column_name].count()}")
    print(f"  Mean:   {df[column_name].mean():.2f}")
    print(f"  Median: {df[column_name].median():.2f}")
    print(f"  Std:    {df[column_name].std():.2f}")
    print(f"  Min:    {df[column_name].min():.2f}")
    print(f"  Max:    {df[column_name].max():.2f}")
    print()
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_name].dropna(), bins=10, color='steelblue', 
             edgecolor='black', alpha=0.7)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Distribution of {column_name}', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'outputs/visualizations/histogram_{column_name.lower()}.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✓ Histogram saved to outputs/visualizations/histogram_{column_name.lower()}.png")
    print()


# ==============================================================================
# SECTION 6: INTERPRETING DISTRIBUTION SHAPE
# ==============================================================================

def interpret_distribution_shape(df, column_name):
    """
    Analyze and interpret the shape of a distribution.
    
    Args:
        df: DataFrame containing the data
        column_name: Name of the column to interpret
    """
    print("=" * 70)
    print(f"INTERPRETING DISTRIBUTION SHAPE: '{column_name}'")
    print("=" * 70)
    print()
    
    # Calculate skewness
    column_data = df[column_name].dropna()
    mean_val = column_data.mean()
    median_val = column_data.median()
    std_val = column_data.std()
    skewness = column_data.skew()
    
    print("Distribution Characteristics:")
    print("-" * 70)
    print(f"  Mean:     {mean_val:.2f}")
    print(f"  Median:   {median_val:.2f}")
    print(f"  Skewness: {skewness:.3f}")
    print()
    
    # Interpret skewness
    print("Skewness Interpretation:")
    print("-" * 70)
    
    if abs(skewness) < 0.5:
        print("  ✓ Approximately Symmetric (Normal-like)")
        print("    → Mean ≈ Median")
        print("    → Data is evenly distributed around the center")
        print("    → No strong tail on either side")
    elif skewness > 0.5:
        print("  ✓ Right-Skewed (Positively Skewed)")
        print("    → Mean > Median")
        print("    → Long tail extends to the right")
        print("    → Most values are on the lower end")
        print("    → Few high values pull the mean up")
    else:
        print("  ✓ Left-Skewed (Negatively Skewed)")
        print("    → Mean < Median")
        print("    → Long tail extends to the left")
        print("    → Most values are on the higher end")
        print("    → Few low values pull the mean down")
    print()
    
    # Spread interpretation
    print("Spread Analysis:")
    print("-" * 70)
    cv = (std_val / mean_val * 100) if mean_val != 0 else 0
    print(f"  Coefficient of Variation: {cv:.1f}%")
    
    if cv < 15:
        print("  → Low variability: Values are tightly clustered")
    elif cv < 30:
        print("  → Moderate variability: Typical spread")
    else:
        print("  → High variability: Values are widely dispersed")
    print()
    
    # Outlier detection using IQR
    Q1 = column_data.quantile(0.25)
    Q3 = column_data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = column_data[(column_data < lower_bound) | (column_data > upper_bound)]
    
    print("Potential Outliers:")
    print("-" * 70)
    if len(outliers) > 0:
        print(f"  {len(outliers)} potential outlier(s) detected")
        print(f"  Values outside range: [{lower_bound:.2f}, {upper_bound:.2f}]")
        print(f"  Outlier values: {outliers.values}")
    else:
        print("  No significant outliers detected")
    print()


# ==============================================================================
# SECTION 7: COMPARING MULTIPLE HISTOGRAMS
# ==============================================================================

def compare_multiple_histograms(df, columns):
    """
    Create side-by-side histograms for multiple columns.
    
    Args:
        df: DataFrame containing the data
        columns: List of column names to compare
    """
    print("=" * 70)
    print("COMPARING MULTIPLE DISTRIBUTIONS")
    print("=" * 70)
    print()
    
    num_columns = len(columns)
    fig, axes = plt.subplots(1, num_columns, figsize=(6 * num_columns, 5))
    
    # If only one column, axes is not a list
    if num_columns == 1:
        axes = [axes]
    
    for idx, col in enumerate(columns):
        col_data = df[col].dropna()
        
        axes[idx].hist(col_data, bins=10, color='steelblue', 
                       edgecolor='black', alpha=0.7)
        axes[idx].set_xlabel(col, fontsize=11)
        axes[idx].set_ylabel('Frequency', fontsize=11)
        axes[idx].set_title(f'{col} Distribution', fontsize=12, fontweight='bold')
        axes[idx].grid(axis='y', alpha=0.3)
        
        # Add statistics to each plot
        mean_val = col_data.mean()
        median_val = col_data.median()
        axes[idx].axvline(mean_val, color='red', linestyle='--', 
                          linewidth=2, label=f'Mean: {mean_val:.1f}')
        axes[idx].axvline(median_val, color='green', linestyle='--', 
                          linewidth=2, label=f'Median: {median_val:.1f}')
        axes[idx].legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig('outputs/visualizations/histogram_comparison.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Comparison histogram saved to outputs/visualizations/histogram_comparison.png")
    print()
    
    # Print comparison summary
    print("Comparison Summary:")
    print("-" * 70)
    for col in columns:
        col_data = df[col].dropna()
        print(f"{col}:")
        print(f"  Mean:     {col_data.mean():.2f}")
        print(f"  Median:   {col_data.median():.2f}")
        print(f"  Skewness: {col_data.skew():.3f}")
        print(f"  Std Dev:  {col_data.std():.2f}")
        print()


# ==============================================================================
# SECTION 8: HISTOGRAM WITH DIFFERENT BIN SIZES
# ==============================================================================

def demonstrate_bin_effects(df, column_name):
    """
    Show how different bin sizes affect histogram interpretation.
    
    Args:
        df: DataFrame containing the data
        column_name: Name of the column to visualize
    """
    print("=" * 70)
    print("EFFECT OF BIN SIZE ON VISUALIZATION")
    print("=" * 70)
    print()
    
    bin_sizes = [5, 10, 20]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    col_data = df[column_name].dropna()
    
    for idx, bins in enumerate(bin_sizes):
        axes[idx].hist(col_data, bins=bins, color='steelblue', 
                       edgecolor='black', alpha=0.7)
        axes[idx].set_xlabel(column_name, fontsize=11)
        axes[idx].set_ylabel('Frequency', fontsize=11)
        axes[idx].set_title(f'{bins} Bins', fontsize=12, fontweight='bold')
        axes[idx].grid(axis='y', alpha=0.3)
    
    plt.suptitle(f'Effect of Bin Size on {column_name} Distribution', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('outputs/visualizations/histogram_bin_comparison.png', 
                dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Bin comparison saved to outputs/visualizations/histogram_bin_comparison.png")
    print()
    
    print("Bin Size Guidelines:")
    print("-" * 70)
    print("  5 bins:  Simple, smooth view - good for overview")
    print("  10 bins: Balanced detail - default choice")
    print("  20 bins: Detailed view - reveals fine patterns")
    print()
    print("Choose bins based on:")
    print("  • Data size (more data → can use more bins)")
    print("  • Analysis goal (overview vs detailed examination)")
    print("  • Distribution complexity (simple vs multi-modal)")
    print()


# ==============================================================================
# SECTION 9: MAIN EXECUTION
# ==============================================================================

def main():
    """
    Main function to run the histogram visualization milestone.
    """
    print("\n")
    print("=" * 70)
    print("HISTOGRAM VISUALIZATION MILESTONE")
    print("=" * 70)
    print("Purpose: Learn to create and interpret histograms")
    print("Date: March 11, 2026")
    print("=" * 70)
    print("\n")
    
    # Step 1: Explain histograms
    explain_histograms()
    input("Press Enter to continue...")
    print("\n")
    
    # Step 2: Explain bins and frequencies
    explain_bins_and_frequencies()
    input("Press Enter to continue...")
    print("\n")
    
    # Step 3: Load data
    print("Loading tours dataset...")
    df = load_tours_data()
    print(f"✓ Loaded {len(df)} rows")
    print()
    print("Dataset Preview:")
    print(df.head())
    print()
    input("Press Enter to continue...")
    print("\n")
    
    # Step 4: Create single histogram for Visitors
    create_single_histogram(df, 'Visitors')
    input("Press Enter to continue...")
    print("\n")
    
    # Step 5: Interpret distribution shape
    interpret_distribution_shape(df, 'Visitors')
    input("Press Enter to continue...")
    print("\n")
    
    # Step 6: Create histogram for Revenue
    create_single_histogram(df, 'Revenue')
    input("Press Enter to continue...")
    print("\n")
    
    # Step 7: Interpret Revenue distribution
    interpret_distribution_shape(df, 'Revenue')
    input("Press Enter to continue...")
    print("\n")
    
    # Step 8: Compare multiple histograms
    compare_multiple_histograms(df, ['Visitors', 'Revenue', 'Rating'])
    input("Press Enter to continue...")
    print("\n")
    
    # Step 9: Demonstrate bin effects
    demonstrate_bin_effects(df, 'Visitors')
    input("Press Enter to continue...")
    print("\n")
    
    # Final summary
    print("=" * 70)
    print("MILESTONE COMPLETE")
    print("=" * 70)
    print()
    print("You have successfully:")
    print("  ✓ Understood what histograms represent")
    print("  ✓ Created histograms for numeric columns")
    print("  ✓ Interpreted distribution shapes and spread")
    print("  ✓ Identified skewed distributions visually")
    print("  ✓ Compared distributions across multiple columns")
    print("  ✓ Understood the effect of bin sizes")
    print()
    print("Key Takeaways:")
    print("  • Histograms reveal patterns that statistics hide")
    print("  • Always visualize data before deep analysis")
    print("  • Distribution shape guides statistical choices")
    print("  • Comparison provides essential context")
    print()
    print("Next Steps:")
    print("  • Practice with different datasets")
    print("  • Combine histograms with box plots")
    print("  • Use distributions to guide modeling decisions")
    print("=" * 70)


if __name__ == "__main__":
    main()
