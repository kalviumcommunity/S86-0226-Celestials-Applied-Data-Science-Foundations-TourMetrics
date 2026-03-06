"""
DataFrame Inspection Milestone - Demonstration Script

This script demonstrates the three essential DataFrame inspection methods:
1. head() - Preview data
2. info() - Understand structure
3. describe() - Summarize statistics

Learning Objectives:
- Use inspection methods intentionally
- Understand what each method reveals
- Build habits of inspecting before analyzing
"""

import pandas as pd
import numpy as np


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f"{title:^70}")
    print(f"{'='*70}\n")


def print_subsection(title):
    """Print a formatted subsection header."""
    print(f"\n{'-'*70}")
    print(f"{title}")
    print(f"{'-'*70}")


def demonstrate_head():
    """Demonstrate head() method for visual preview."""
    print_section("1. INSPECTING DATA WITH head()")
    
    # Load datasets
    df_employees = pd.read_csv('data/raw/employees.csv')
    df_books = pd.read_csv('data/raw/books.csv')
    
    print("Purpose: Quick visual preview of the first few rows")
    print("What it reveals: Column names, sample values, data alignment\n")
    
    # Default head()
    print_subsection("Employees - First 5 rows (default)")
    print(df_employees.head())
    
    # Custom number of rows
    print_subsection("Employees - First 3 rows (custom)")
    print(df_employees.head(3))
    
    # Books dataset
    print_subsection("Books - First 5 rows")
    print(df_books.head())
    
    print("\n✓ What we learned:")
    print("  - Column names are clear and descriptive")
    print("  - Data appears properly aligned")
    print("  - No obvious formatting issues")
    print("  - We can see sample values for each column")


def demonstrate_info():
    """Demonstrate info() method for structure inspection."""
    print_section("2. INSPECTING STRUCTURE WITH info()")
    
    # Load datasets
    df_employees = pd.read_csv('data/raw/employees.csv')
    df_books = pd.read_csv('data/raw/books.csv')
    
    print("Purpose: Understand DataFrame structure and data types")
    print("What it reveals: Rows, columns, types, null counts, memory\n")
    
    # Employees info
    print_subsection("Employees DataFrame Info")
    df_employees.info()
    
    # Books info
    print_subsection("Books DataFrame Info")
    df_books.info()
    
    print("\n✓ What we learned:")
    print("  Employees: 5 rows, 4 columns, no missing values")
    print("  - Text columns: Name, Department")
    print("  - Numeric columns: Salary, Years")
    print("\n  Books: 4 rows, 4 columns, no missing values")
    print("  - Text columns: Title, Author")
    print("  - Numeric columns: Year, Pages")


def demonstrate_describe():
    """Demonstrate describe() method for statistical summary."""
    print_section("3. SUMMARIZING DATA WITH describe()")
    
    # Load datasets
    df_employees = pd.read_csv('data/raw/employees.csv')
    df_books = pd.read_csv('data/raw/books.csv')
    
    print("Purpose: Get statistical summary of numeric columns")
    print("What it reveals: Count, mean, std, min, quartiles, max\n")
    
    # Employees describe
    print_subsection("Employees - Numeric Summary")
    print(df_employees.describe())
    
    # Books describe
    print_subsection("Books - Numeric Summary")
    print(df_books.describe())
    
    print("\n✓ What we learned:")
    print("  Employees:")
    print("  - Salary range: $65,000 - $80,000 (avg: $71,600)")
    print("  - Experience range: 2-5 years (avg: 3.4 years)")
    print("  - No extreme outliers detected")
    print("\n  Books:")
    print("  - Publication years: 1813-1960 (avg: 1911)")
    print("  - Page counts: 180-432 pages (avg: 305 pages)")
    print("  - Wide spread in publication years")


def demonstrate_when_to_use():
    """Demonstrate when to use each inspection method."""
    print_section("4. KNOWING WHEN TO USE EACH METHOD")
    
    # Create messy dataset
    messy_data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard', None, 'Monitor'],
        'Price': [999.99, 25.50, None, 150.00, 299.99],
        'Stock': [5, 50, 30, 0, 10],
        'Rating': [4.5, 4.2, 4.8, None, 4.6]
    }
    df_messy = pd.DataFrame(messy_data)
    
    print("Dataset with missing values to demonstrate inspection power:\n")
    
    # head() - Visual
    print_subsection("head() - Quick visual check")
    print(df_messy.head())
    print("\n→ We can SEE missing values (NaN) but not count them easily")
    
    # info() - Structure
    print_subsection("info() - Structure and null counts")
    df_messy.info()
    print("\n→ Shows EXACTLY how many non-null values per column")
    print("→ Product: 4/5 (1 missing)")
    print("→ Price: 4/5 (1 missing)")
    print("→ Rating: 4/5 (1 missing)")
    
    # describe() - Statistics
    print_subsection("describe() - Numeric summary")
    print(df_messy.describe())
    print("\n→ Count shows 4 values for Price and Rating (1 missing each)")
    print("→ Stock has all 5 values (no missing data)")
    print("→ Provides statistical context for numeric columns")
    
    # Decision guide
    print("\n" + "="*70)
    print("DECISION GUIDE:")
    print("="*70)
    print(f"{'Question':<35} {'Method':<15} {'Why'}")
    print("-"*70)
    print(f"{'What does the data look like?':<35} {'head()':<15} Visual preview")
    print(f"{'What are the column types?':<35} {'info()':<15} Shows dtypes")
    print(f"{'Are there missing values?':<35} {'info()':<15} Non-null counts")
    print(f"{'What is the numeric range?':<35} {'describe()':<15} Min/max/mean")
    print(f"{'Are there outliers?':<35} {'describe()':<15} Check extremes")
    print(f"{'How much memory is used?':<35} {'info()':<15} Memory usage")
    print("\n✓ Best Practice: Use all three methods together!")


def inspect_dataframe(df, name="DataFrame"):
    """
    Complete inspection workflow for any DataFrame.
    
    Parameters:
    - df: DataFrame to inspect
    - name: Name for display purposes
    """
    print(f"\n{'='*70}")
    print(f"INSPECTING: {name}")
    print(f"{'='*70}")
    
    # Step 1: Visual preview
    print("\n[1] PREVIEW - First 5 rows:")
    print("-" * 70)
    print(df.head())
    
    # Step 2: Structure and types
    print("\n[2] STRUCTURE - Info:")
    print("-" * 70)
    df.info()
    
    # Step 3: Numeric summary
    print("\n[3] STATISTICS - Numeric summary:")
    print("-" * 70)
    print(df.describe())
    
    # Step 4: Quick insights
    print("\n[4] QUICK INSIGHTS:")
    print("-" * 70)
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("\nMissing values detected:")
        print(missing[missing > 0])
    else:
        print("\nNo missing values detected ✓")
    
    print(f"\n{'='*70}\n")


def demonstrate_complete_workflow():
    """Demonstrate complete inspection workflow."""
    print_section("5. COMPLETE INSPECTION WORKFLOW")
    
    print("Recommended inspection sequence for any new dataset:\n")
    
    # Load datasets
    df_employees = pd.read_csv('data/raw/employees.csv')
    df_books = pd.read_csv('data/raw/books.csv')
    
    # Create messy dataset
    messy_data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard', None, 'Monitor'],
        'Price': [999.99, 25.50, None, 150.00, 299.99],
        'Stock': [5, 50, 30, 0, 10],
        'Rating': [4.5, 4.2, 4.8, None, 4.6]
    }
    df_messy = pd.DataFrame(messy_data)
    
    # Inspect all datasets
    inspect_dataframe(df_employees, "Employees Dataset")
    inspect_dataframe(df_books, "Books Dataset")
    inspect_dataframe(df_messy, "Messy Dataset (with missing values)")


def print_key_takeaways():
    """Print key takeaways and best practices."""
    print_section("KEY TAKEAWAYS")
    
    print("Why Inspection Matters:")
    print("  1. Prevents mistakes - Catch issues before analysis")
    print("  2. Saves time - Understand data structure immediately")
    print("  3. Builds confidence - Know what you're working with")
    print("  4. Industry standard - Every data professional does this")
    
    print("\nThe Three Essential Methods:")
    print("  1. head()     - Visual preview, quick sanity check")
    print("  2. info()     - Structure, types, missing values")
    print("  3. describe() - Numeric statistics, outlier detection")
    
    print("\nCommon Mistakes to Avoid:")
    print("  ❌ Starting analysis without inspection")
    print("  ❌ Assuming column types are correct")
    print("  ❌ Missing hidden null values")
    print("  ❌ Not checking for outliers")
    
    print("\nBest Practices:")
    print("  ✓ Always inspect immediately after loading")
    print("  ✓ Use all three methods together")
    print("  ✓ Document what you find")
    print("  ✓ Re-inspect after transformations")
    
    print("\n" + "="*70)
    print("Remember: Inspection is not optional—it's the foundation of")
    print("          reliable data analysis!")
    print("="*70 + "\n")


def main():
    """Run all demonstrations."""
    print("\n" + "="*70)
    print("DATAFRAME INSPECTION MILESTONE - DEMONSTRATION")
    print("="*70)
    print("\nThis script demonstrates the three essential inspection methods:")
    print("  • head()     - Preview data")
    print("  • info()     - Understand structure")
    print("  • describe() - Summarize statistics")
    
    # Run demonstrations
    demonstrate_head()
    demonstrate_info()
    demonstrate_describe()
    demonstrate_when_to_use()
    demonstrate_complete_workflow()
    print_key_takeaways()


if __name__ == "__main__":
    main()
