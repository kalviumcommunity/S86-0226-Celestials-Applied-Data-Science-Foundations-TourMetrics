"""
CSV Loading Milestone - Demonstration Script

This script demonstrates how to load and inspect CSV files using Pandas.
It covers basic loading, data inspection methods, and structure verification.

Learning Objectives:
- Load CSV files into Pandas DataFrames
- Inspect data structure using various methods
- Verify data integrity after loading
- Handle common CSV loading errors
"""

import pandas as pd
import os


def print_section_header(title):
    """Print a formatted section header for better readability."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def load_and_inspect_csv(filepath, filename):
    """
    Load a CSV file and perform basic inspection.
    
    Args:
        filepath: Path to the CSV file
        filename: Name of the file (for display purposes)
    
    Returns:
        DataFrame: The loaded DataFrame, or None if loading fails
    """
    print(f"Loading {filename}...")
    
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(filepath)
        print(f"✓ Successfully loaded {filename}")
        return df
    
    except FileNotFoundError:
        print(f"✗ Error: File not found at {filepath}")
        print("  Tip: Check that the file path is correct and the file exists")
        return None
    
    except pd.errors.ParserError as e:
        print(f"✗ Error: Failed to parse CSV file")
        print(f"  Details: {e}")
        print("  Tip: Check for inconsistent columns or wrong delimiter")
        return None
    
    except UnicodeDecodeError:
        print(f"✗ Error: Encoding issue detected")
        print("  Tip: Try specifying encoding parameter, e.g., encoding='latin-1'")
        return None


def demonstrate_inspection_methods(df, dataset_name):
    """
    Demonstrate all inspection methods on a DataFrame.
    
    Args:
        df: DataFrame to inspect
        dataset_name: Name of the dataset (for display purposes)
    """
    print_section_header(f"Inspecting {dataset_name} Dataset")
    
    # Method 1: head() - View first 5 rows
    print("1. Using head() - First 5 rows:")
    print(df.head())
    print("\n   → head() shows the beginning of your data")
    print("   → Default is 5 rows, but you can specify: head(10)")
    
    # Method 2: tail() - View last 5 rows
    print("\n2. Using tail() - Last 5 rows:")
    print(df.tail())
    print("\n   → tail() shows the end of your data")
    print("   → Useful for checking if data loaded completely")
    
    # Method 3: info() - Get DataFrame information
    print("\n3. Using info() - DataFrame structure:")
    df.info()
    print("\n   → info() shows column names, data types, and non-null counts")
    print("   → Helps identify missing data and data type issues")
    
    # Method 4: describe() - Statistical summary
    print("\n4. Using describe() - Statistical summary:")
    print(df.describe())
    print("\n   → describe() provides statistics for numeric columns")
    print("   → Shows count, mean, std, min, quartiles, and max")


def demonstrate_structure_verification(df, dataset_name):
    """
    Demonstrate structure verification techniques.
    
    Args:
        df: DataFrame to verify
        dataset_name: Name of the dataset (for display purposes)
    """
    print_section_header(f"Verifying {dataset_name} Structure")
    
    # Check shape
    print(f"1. Shape (rows, columns): {df.shape}")
    print(f"   → This dataset has {df.shape[0]} rows and {df.shape[1]} columns")
    
    # Check column names
    print(f"\n2. Column names: {list(df.columns)}")
    print("   → Always verify column names match your expectations")
    
    # Check data types
    print("\n3. Data types:")
    print(df.dtypes)
    print("   → Ensure numeric columns are int/float, not object (string)")
    
    # Check row count using len()
    print(f"\n4. Row count using len(): {len(df)}")
    print(f"   → len(df) returns the number of rows: {len(df)}")


def demonstrate_error_handling():
    """Demonstrate common CSV loading errors and how to handle them."""
    print_section_header("Common CSV Loading Issues")
    
    # Error 1: File not found
    print("1. File Not Found Error:")
    print("   Attempting to load non-existent file...")
    result = load_and_inspect_csv('data/raw/nonexistent.csv', 'nonexistent.csv')
    if result is None:
        print("   ✓ Error handled gracefully\n")
    
    # Error 2: Checking file existence before loading
    print("2. Checking File Existence:")
    filepath = 'data/raw/books.csv'
    if os.path.exists(filepath):
        print(f"   ✓ File exists at {filepath}")
        print("   → Safe to proceed with loading")
    else:
        print(f"   ✗ File does not exist at {filepath}")
    
    # Error 3: Encoding issues (demonstration)
    print("\n3. Handling Encoding Issues:")
    print("   If you encounter UnicodeDecodeError, try:")
    print("   → df = pd.read_csv('file.csv', encoding='latin-1')")
    print("   → df = pd.read_csv('file.csv', encoding='cp1252')")
    print("   → df = pd.read_csv('file.csv', encoding='utf-8')")
    
    # Error 4: Delimiter issues (demonstration)
    print("\n4. Handling Different Delimiters:")
    print("   If your file uses semicolons or tabs:")
    print("   → df = pd.read_csv('file.csv', sep=';')  # for semicolons")
    print("   → df = pd.read_csv('file.tsv', sep='\\t')  # for tabs")
    
    # Error 5: Header issues (demonstration)
    print("\n5. Handling Header Row Issues:")
    print("   If your CSV has no header row:")
    print("   → df = pd.read_csv('file.csv', header=None)")
    print("   If header is on a different row:")
    print("   → df = pd.read_csv('file.csv', header=2)  # use row 2 as header")


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print("  CSV LOADING MILESTONE - PANDAS DEMONSTRATION")
    print("=" * 70)
    print("\nThis script demonstrates CSV loading and inspection with Pandas.")
    print("Follow along to learn essential data loading techniques.\n")
    
    # Load and inspect books.csv
    books_df = load_and_inspect_csv('data/raw/books.csv', 'books.csv')
    if books_df is not None:
        demonstrate_inspection_methods(books_df, "Books")
        demonstrate_structure_verification(books_df, "Books")
    
    # Load and inspect employees.csv
    employees_df = load_and_inspect_csv('data/raw/employees.csv', 'employees.csv')
    if employees_df is not None:
        demonstrate_inspection_methods(employees_df, "Employees")
        demonstrate_structure_verification(employees_df, "Employees")
    
    # Demonstrate error handling
    demonstrate_error_handling()
    
    # Summary
    print_section_header("Key Takeaways")
    print("✓ Always inspect data after loading with head(), tail(), and info()")
    print("✓ Verify structure with shape, columns, and dtypes")
    print("✓ Check for missing values and unexpected data types")
    print("✓ Handle errors gracefully with try-except blocks")
    print("✓ CSV loading is the foundation - get it right first!")
    print("\n" + "=" * 70)
    print("  End of demonstration. Happy data loading!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
