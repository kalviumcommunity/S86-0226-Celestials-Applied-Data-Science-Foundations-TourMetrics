"""Understanding DataFrame Shapes and Column Data Types Milestone

This script demonstrates:
1. Understanding DataFrame shape (rows × columns)
2. Identifying rows vs columns correctly
3. Understanding common Pandas data types
4. Inspecting column data types intentionally
5. Recognizing type-related issues early

Learning Objectives:
- Interpret DataFrame shape confidently
- Identify the number of rows and columns
- Understand column data types at a high level
- Detect incorrect or unexpected data types
"""

import pandas as pd
import numpy as np
import os


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


def create_sample_data():
    """Create sample CSV files with various data types for demonstration."""
    print("Creating sample datasets for demonstration...")
    
    # Ensure the data/raw directory exists
    os.makedirs('data/raw', exist_ok=True)
    
    # Dataset 1: Employee data with various data types
    employee_csv = """Name,Department,Salary,Years,StartDate
John Smith,Engineering,75000,3,2021-01-15
Sarah Johnson,Marketing,65000,2,2022-03-20
Mike Williams,Engineering,80000,5,2019-07-10
Emma Brown,Sales,70000,4,2020-02-28
David Lee,Marketing,68000,3,2021-06-05"""
    
    with open('data/raw/employees.csv', 'w') as f:
        f.write(employee_csv)
    
    # Dataset 2: Books data with numeric columns
    books_csv = """Title,Author,Year,Pages
1984,George Orwell,1949,328
To Kill a Mockingbird,Harper Lee,1960,281
The Great Gatsby,F. Scott Fitzgerald,1925,180
Pride and Prejudice,Jane Austen,1813,432"""
    
    with open('data/raw/books.csv', 'w') as f:
        f.write(books_csv)
    
    # Dataset 3: Tour data with potential type issues
    tour_csv = """TourID,Location,Visitors,Revenue,Rating
T001,Paris,1250,45000.50,4.8
T002,London,980,38000.00,4.5
T003,Rome,1500,52000.75,4.9
T004,Berlin,750,28000,4.3
T005,Madrid,Not Available,35000.00,4.6"""
    
    with open('data/raw/tours.csv', 'w') as f:
        f.write(tour_csv)
    
    print("✓ Sample CSV files created successfully\n")


def demonstrate_shape_understanding():
    """Milestone Part 1: Understanding DataFrame shape."""
    print_section("PART 1: UNDERSTANDING DATAFRAME SHAPE")
    
    # Load a dataset
    df = pd.read_csv('data/raw/employees.csv')
    
    print("What is DataFrame shape?")
    print("Shape tells you the dimensions of your data: (rows, columns)\n")
    
    # Display the shape
    print(f"DataFrame shape: {df.shape}")
    print(f"  → This is a tuple: ({df.shape[0]}, {df.shape[1]})")
    print(f"  → First number = rows (observations/records)")
    print(f"  → Second number = columns (features/variables)")
    
    print_subsection("Breaking Down the Shape")
    print(f"Number of rows: {df.shape[0]}")
    print(f"  → We have {df.shape[0]} employee records")
    print(f"  → Each row represents one observation")
    
    print(f"\nNumber of columns: {df.shape[1]}")
    print(f"  → We have {df.shape[1]} features per employee")
    print(f"  → Each column represents an attribute")
    
    print_subsection("Visualizing the Data")
    print("First few rows of the data:")
    print(df.head())
    
    print("\n✓ Key Takeaway:")
    print("  Shape (5, 5) means 5 employees × 5 attributes")
    print("  Always check shape before analyzing data!")


def demonstrate_rows_vs_columns():
    """Milestone Part 2: Understanding rows and columns."""
    print_section("PART 2: UNDERSTANDING ROWS VS COLUMNS")
    
    df = pd.read_csv('data/raw/employees.csv')
    
    print("Rows represent observations (horizontal)")
    print("Columns represent variables (vertical)\n")
    
    print_subsection("Identifying Rows (Records/Observations)")
    print(f"Total rows: {len(df)}")
    print(f"  → Using len(df): {len(df)}")
    print(f"  → Using df.shape[0]: {df.shape[0]}")
    print(f"  → Both give the same result: number of records\n")
    
    print("Example - Looking at one row (one employee):")
    print(df.iloc[0])
    print("  → This is ONE observation with MULTIPLE attributes")
    
    print_subsection("Identifying Columns (Features/Variables)")
    print(f"Total columns: {len(df.columns)}")
    print(f"Column names: {list(df.columns)}")
    print(f"  → Each column represents a different attribute")
    
    print("\nExample - Looking at one column (all salaries):")
    print(df['Salary'].head())
    print("  → This is ONE attribute across MULTIPLE observations")
    
    print("\n✓ Key Takeaway:")
    print("  Rows = How many observations (records/entries)")
    print("  Columns = How many variables (features/attributes)")


def demonstrate_data_types():
    """Milestone Part 3: Understanding column data types."""
    print_section("PART 3: UNDERSTANDING COLUMN DATA TYPES")
    
    df = pd.read_csv('data/raw/employees.csv')
    
    print("Why data types matter:")
    print("  → They determine what operations are valid")
    print("  → Wrong types lead to errors or incorrect results")
    print("  → Type awareness prevents bugs\n")
    
    print_subsection("Inspecting Data Types with dtypes")
    print("Column data types:")
    print(df.dtypes)
    
    print("\n\nExplanation of common Pandas data types:")
    print("  • object   = Text/string data or mixed types")
    print("  • int64    = Integer numbers (whole numbers)")
    print("  • float64  = Decimal numbers")
    print("  • bool     = True/False values")
    print("  • datetime64 = Date and time values")
    
    print_subsection("Breaking Down Each Column Type")
    for col in df.columns:
        dtype = df[col].dtype
        sample = df[col].iloc[0]
        print(f"\n{col}:")
        print(f"  Type: {dtype}")
        print(f"  Sample value: {sample}")
        print(f"  Example type: {type(sample).__name__}")
    
    print("\n✓ Key Takeaway:")
    print("  Always inspect dtypes after loading data")
    print("  Ensure numeric columns are int64/float64, not object")


def demonstrate_type_inspection_methods():
    """Demonstrate multiple ways to inspect data types."""
    print_section("PART 4: METHODS FOR INSPECTING DATA TYPES")
    
    df = pd.read_csv('data/raw/books.csv')
    
    print("Multiple ways to inspect data types:\n")
    
    # Method 1: dtypes attribute
    print_subsection("Method 1: Using df.dtypes")
    print(df.dtypes)
    print("  → Quick overview of all column types")
    
    # Method 2: info() method
    print_subsection("Method 2: Using df.info()")
    df.info()
    print("  → Shows types, non-null counts, and memory usage")
    
    # Method 3: Checking specific column
    print_subsection("Method 3: Checking specific column")
    print(f"Type of 'Year' column: {df['Year'].dtype}")
    print(f"Type of 'Title' column: {df['Title'].dtype}")
    print("  → Check individual columns when needed")
    
    # Method 4: Selecting by type
    print_subsection("Method 4: Selecting columns by type")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    print(f"Numeric columns: {numeric_cols}")
    print(f"Text columns: {text_cols}")
    print("  → Useful for bulk operations on specific types")
    
    print("\n✓ Key Takeaway:")
    print("  Use df.dtypes for quick checks")
    print("  Use df.info() for comprehensive overview")
    print("  Use select_dtypes() for filtering columns by type")


def demonstrate_type_issues():
    """Milestone Part 4: Detecting type-related issues."""
    print_section("PART 5: DETECTING TYPE-RELATED ISSUES")
    
    df = pd.read_csv('data/raw/tours.csv')
    
    print("Common type-related problems:\n")
    
    print_subsection("1. Inspecting the Dataset")
    print("First, let's look at our tour data:")
    print(df)
    
    print_subsection("2. Checking Data Types")
    print("\nColumn data types:")
    print(df.dtypes)
    
    print_subsection("3. Identifying Issues")
    print("\nPotential issues detected:")
    
    # Issue 1: Check for numeric columns stored as object
    for col in df.columns:
        if df[col].dtype == 'object':
            # Try to see if it should be numeric
            print(f"\n'{col}' is type 'object' (string)")
            print(f"  Sample values: {df[col].head(3).tolist()}")
            
            # Check if it looks numeric
            if col in ['Visitors', 'Revenue', 'Rating']:
                print(f"  ⚠ WARNING: '{col}' should probably be numeric!")
                print(f"  → Contains non-numeric value: {df[col].loc[df[col] == 'Not Available'].values}")
    
    # Issue 2: Attempting numeric operation on wrong type
    print_subsection("4. Why This Matters - Example Error")
    print("\nTrying to calculate average visitors...")
    try:
        avg_visitors = df['Visitors'].mean()
        print(f"Average visitors: {avg_visitors}")
    except Exception as e:
        print(f"✗ Error occurred: {type(e).__name__}")
        print(f"  Message: Cannot calculate mean on text data")
        print(f"  → This happens because 'Visitors' contains 'Not Available'")
    
    # Show what type it actually is
    print(f"\nActual type of 'Visitors' column: {df['Visitors'].dtype}")
    print("  → It's 'object' (string), not numeric!")
    print("  → Pandas treats entire column as text when any value is non-numeric")
    
    print_subsection("5. How to Detect Issues Early")
    print("\n✓ Best Practices:")
    print("  1. Always check df.dtypes immediately after loading")
    print("  2. Verify numeric columns are int64/float64")
    print("  3. Look for 'object' type on columns that should be numbers")
    print("  4. Use df.info() to spot missing values")
    print("  5. Preview data with df.head() to see actual values")
    
    print("\n✓ Key Takeaway:")
    print("  Type issues cause analysis to fail")
    print("  Early detection saves debugging time")
    print("  Always verify types match expectations!")


def demonstrate_comprehensive_inspection():
    """Complete workflow for inspecting shape and types."""
    print_section("COMPLETE INSPECTION WORKFLOW")
    
    df = pd.read_csv('data/raw/employees.csv')
    
    print("Standard workflow for inspecting a new dataset:\n")
    
    print("STEP 1: Check shape")
    print(f"  → Shape: {df.shape}")
    print(f"  → {df.shape[0]} rows × {df.shape[1]} columns")
    
    print("\nSTEP 2: Preview the data")
    print("  → First few rows:")
    print(df.head(3))
    
    print("\n\nSTEP 3: Check data types")
    print("  → Column types:")
    print(df.dtypes)
    
    print("\n\nSTEP 4: Get full summary")
    print("  → Complete info:")
    df.info()
    
    print("\n\nSTEP 5: Verify expectations")
    print("  ✓ Shape matches expected size")
    print("  ✓ Column names are correct")
    print("  ✓ Data types are appropriate")
    print("  ✓ No obvious missing values (in this clean dataset)")
    
    print("\n✓ This workflow should become automatic!")
    print("  Run it every time you load data")


def main() -> None:
    """Main execution function."""
    print("\n" + "="*70)
    print("  UNDERSTANDING DATAFRAME SHAPES AND COLUMN DATA TYPES")
    print("="*70)
    print("\nThis milestone teaches you to understand DataFrame structure")
    print("and data types before performing any analysis.\n")
    
    # Create sample data
    create_sample_data()
    
    # Part 1: Understanding shape
    demonstrate_shape_understanding()
    
    # Part 2: Rows vs columns
    demonstrate_rows_vs_columns()
    
    # Part 3: Understanding data types
    demonstrate_data_types()
    
    # Part 4: Type inspection methods
    demonstrate_type_inspection_methods()
    
    # Part 5: Detecting type issues
    demonstrate_type_issues()
    
    # Part 6: Complete workflow
    demonstrate_comprehensive_inspection()
    
    # Summary
    print_section("KEY TAKEAWAYS - MILESTONE COMPLETE")
    print("✓ Shape tells you dimensions: (rows, columns)")
    print("✓ Rows = observations, Columns = variables")
    print("✓ Always check dtypes after loading data")
    print("✓ Numeric columns should be int64/float64, not object")
    print("✓ Type issues cause analysis errors - detect early")
    print("✓ Use df.shape, df.dtypes, and df.info() routinely")
    print("\n" + "="*70)
    print("  MILESTONE COMPLETE - You understand shapes and types!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
