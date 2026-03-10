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


def demonstrate_missing_values_strategies():
    """Demonstrate strategies for handling missing values."""
    print_section("DATA CLEANING PART 1: HANDLING MISSING VALUES")
    
    # Create dataset with missing values
    print("Creating sample dataset with missing values...\n")
    data = {
        'EmployeeID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008'],
        'Name': ['John Smith', 'Sarah Johnson', np.nan, 'Emma Brown', 'David Lee', 'Lisa Wang', np.nan, 'Tom Miller'],
        'Department': ['Engineering', 'Marketing', 'Engineering', np.nan, 'Marketing', 'Sales', 'Engineering', 'Sales'],
        'Salary': [75000, 65000, 80000, np.nan, 68000, 72000, 85000, np.nan],
        'Years': [3, 2, 5, 4, 3, np.nan, 6, 2],
        'Performance': [4.5, 4.2, np.nan, 4.8, 4.3, 4.6, np.nan, 4.1]
    }
    df = pd.DataFrame(data)
    
    print("Original Dataset:")
    print(df)
    print(f"\nShape: {df.shape}")
    
    print_subsection("1. DETECTING MISSING VALUES")
    print("\nMissing values per column:")
    missing_counts = df.isnull().sum()
    print(missing_counts)
    
    print("\nMissing value percentages:")
    missing_percentages = (df.isnull().sum() / len(df) * 100).round(2)
    for col, pct in missing_percentages.items():
        if pct > 0:
            print(f"  {col}: {pct}%")
    
    print_subsection("2. STRATEGY A: DROPPING MISSING VALUES")
    
    # Drop rows with ANY missing values
    print("\nOption 1: Drop rows with ANY missing value (dropna())")
    df_dropped_any = df.dropna()
    print(f"Original shape: {df.shape}")
    print(f"After dropping: {df_dropped_any.shape}")
    print(f"Rows removed: {df.shape[0] - df_dropped_any.shape[0]}")
    print("\n⚠ Warning: Very aggressive - lost most data!")
    print(df_dropped_any)
    
    # Drop rows where ALL values are missing
    print("\n\nOption 2: Drop rows only if ALL values are missing")
    df_dropped_all = df.dropna(how='all')
    print(f"Original shape: {df.shape}")
    print(f"After dropping: {df_dropped_all.shape}")
    print(f"Rows removed: {df.shape[0] - df_dropped_all.shape[0]}")
    print("✓ Better: Only removes completely empty rows")
    
    # Drop rows based on specific columns
    print("\n\nOption 3: Drop rows missing CRITICAL columns only")
    critical_columns = ['EmployeeID', 'Name']
    df_dropped_subset = df.dropna(subset=critical_columns)
    print(f"Critical columns: {critical_columns}")
    print(f"Original shape: {df.shape}")
    print(f"After dropping: {df_dropped_subset.shape}")
    print(f"Rows removed: {df.shape[0] - df_dropped_subset.shape[0]}")
    print("✓ Best practice: Keep rows unless critical data is missing")
    print(df_dropped_subset)
    
    # Drop columns with too many missing values
    print("\n\nOption 4: Drop COLUMNS with excessive missing values")
    threshold = 0.5  # Drop if >50% missing
    df_dropped_cols = df.dropna(axis=1, thresh=int(threshold * len(df)))
    print(f"Threshold: {threshold*100}% missing")
    print(f"Original columns: {df.shape[1]}")
    print(f"After dropping: {df_dropped_cols.shape[1]}")
    print(f"Columns kept: {list(df_dropped_cols.columns)}")
    
    print_subsection("3. STRATEGY B: FILLING MISSING VALUES")
    
    # Fill with a constant
    print("\nOption 1: Fill with a constant value")
    df_filled_constant = df.copy()
    df_filled_constant['Department'] = df_filled_constant['Department'].fillna('Unknown')
    print("Filled 'Department' with 'Unknown':")
    print(df_filled_constant[['EmployeeID', 'Department']])
    
    # Fill with mean (for numeric columns)
    print("\n\nOption 2: Fill numeric columns with MEAN")
    df_filled_mean = df.copy()
    df_filled_mean['Salary'] = df_filled_mean['Salary'].fillna(df_filled_mean['Salary'].mean())
    df_filled_mean['Years'] = df_filled_mean['Years'].fillna(df_filled_mean['Years'].mean())
    print(f"Mean Salary: ${df['Salary'].mean():.2f}")
    print(f"Mean Years: {df['Years'].mean():.2f}")
    print("\nFilled dataset:")
    print(df_filled_mean[['EmployeeID', 'Salary', 'Years']])
    
    # Fill with median (more robust to outliers)
    print("\n\nOption 3: Fill numeric columns with MEDIAN (better for skewed data)")
    df_filled_median = df.copy()
    df_filled_median['Salary'] = df_filled_median['Salary'].fillna(df_filled_median['Salary'].median())
    print(f"Median Salary: ${df['Salary'].median():.2f}")
    print("✓ Median is less affected by outliers than mean")
    
    # Forward fill (use previous value)
    print("\n\nOption 4: Forward Fill (ffill) - use previous value")
    df_forward = df.copy()
    df_forward['Performance'] = df_forward['Performance'].fillna(method='ffill')
    print("Filled 'Performance' using forward fill:")
    print(df_forward[['EmployeeID', 'Performance']])
    print("✓ Good for time-series data")
    
    # Backward fill
    print("\n\nOption 5: Backward Fill (bfill) - use next value")
    df_backward = df.copy()
    df_backward['Performance'] = df_backward['Performance'].fillna(method='bfill')
    print("Filled 'Performance' using backward fill:")
    print(df_backward[['EmployeeID', 'Performance']])
    
    # Interpolation for numeric data
    print("\n\nOption 6: INTERPOLATION (for numeric ordered data)")
    df_interpolated = df.copy()
    df_interpolated['Performance'] = df_interpolated['Performance'].interpolate()
    print("Filled 'Performance' using interpolation:")
    print(df_interpolated[['EmployeeID', 'Performance']])
    print("✓ Creates smooth transitions between values")
    
    print_subsection("4. BEST PRACTICES FOR HANDLING MISSING VALUES")
    print("\n✓ DECISION FRAMEWORK:")
    print("  1. Understand WHY data is missing")
    print("  2. Calculate missing percentage per column")
    print("  3. For <5% missing: Usually safe to drop rows")
    print("  4. For 5-30% missing: Consider filling strategies")
    print("  5. For >30% missing: Consider dropping the column")
    print("\n✓ FILLING STRATEGIES BY DATA TYPE:")
    print("  • Numeric data: Use mean, median, or interpolation")
    print("  • Categorical data: Use mode (most frequent) or 'Unknown'")
    print("  • Time series: Use forward/backward fill or interpolation")
    print("\n✓ WARNINGS:")
    print("  • Always analyze impact before dropping data")
    print("  • Document your imputation strategy")
    print("  • Consider domain knowledge when choosing fill method")
    print("  • Be cautious - filled values are estimates, not real data")


def demonstrate_duplicate_handling():
    """Demonstrate identifying and removing duplicate records."""
    print_section("DATA CLEANING PART 2: HANDLING DUPLICATE RECORDS")
    
    # Create dataset with duplicates
    print("Creating sample dataset with duplicates...\n")
    data = {
        'CustomerID': ['C001', 'C002', 'C003', 'C002', 'C004', 'C001', 'C005', 'C003'],
        'Name': ['Alice Brown', 'Bob Smith', 'Carol White', 'Bob Smith', 'David Lee', 
                 'Alice Brown', 'Emma Davis', 'Carol White'],
        'Email': ['alice@email.com', 'bob@email.com', 'carol@email.com', 'bob@email.com',
                  'david@email.com', 'alice@email.com', 'emma@email.com', 'carol@email.com'],
        'Purchase': [100, 200, 150, 250, 300, 100, 175, 150],
        'Date': ['2024-01-15', '2024-01-20', '2024-01-18', '2024-01-20', 
                 '2024-01-22', '2024-01-15', '2024-01-25', '2024-01-18']
    }
    df = pd.DataFrame(data)
    
    print("Original Dataset:")
    print(df)
    print(f"\nShape: {df.shape}")
    
    print_subsection("1. DETECTING DUPLICATES")
    
    # Check for any duplicates
    print("\nChecking for duplicate rows...")
    has_duplicates = df.duplicated().any()
    print(f"Has duplicates: {has_duplicates}")
    print(f"Number of duplicate rows: {df.duplicated().sum()}")
    
    # Show which rows are duplicates
    print("\n\nIdentifying duplicate rows (boolean mask):")
    print(df.duplicated())
    print("✓ True = duplicate, False = unique (keeps first occurrence)")
    
    print("\n\nShowing the actual duplicate rows:")
    duplicate_rows = df[df.duplicated(keep=False)]  # keep=False marks all duplicates
    print(duplicate_rows.sort_values('CustomerID'))
    print(f"\nTotal duplicate entries: {len(duplicate_rows)}")
    
    print_subsection("2. CHECKING DUPLICATES IN SPECIFIC COLUMNS")
    
    # Check duplicates based on CustomerID only
    print("\nDuplicates based on 'CustomerID' only:")
    customer_duplicates = df[df.duplicated(subset=['CustomerID'], keep=False)]
    print(customer_duplicates.sort_values('CustomerID'))
    print(f"Rows with duplicate CustomerID: {df.duplicated(subset=['CustomerID']).sum()}")
    
    # Check duplicates based on multiple columns
    print("\n\nDuplicates based on 'CustomerID' AND 'Date':")
    key_duplicates = df[df.duplicated(subset=['CustomerID', 'Date'], keep=False)]
    print(key_duplicates.sort_values(['CustomerID', 'Date']))
    print(f"Exact match duplicates: {df.duplicated(subset=['CustomerID', 'Date']).sum()}")
    
    print_subsection("3. REMOVING DUPLICATES")
    
    # Remove complete duplicate rows
    print("\nOption 1: Remove complete duplicate rows (all columns match)")
    df_no_complete_dupes = df.drop_duplicates()
    print(f"Original shape: {df.shape}")
    print(f"After removing: {df_no_complete_dupes.shape}")
    print(f"Rows removed: {df.shape[0] - df_no_complete_dupes.shape[0]}")
    print("\nCleaned dataset:")
    print(df_no_complete_dupes)
    
    # Remove duplicates based on specific columns
    print("\n\nOption 2: Remove duplicates based on 'CustomerID' only")
    df_unique_customers = df.drop_duplicates(subset=['CustomerID'])
    print(f"Original shape: {df.shape}")
    print(f"After removing: {df_unique_customers.shape}")
    print(f"Rows removed: {df.shape[0] - df_unique_customers.shape[0]}")
    print("\nUnique customers (keeps first occurrence):")
    print(df_unique_customers)
    
    # Keep last occurrence instead of first
    print("\n\nOption 3: Keep LAST occurrence instead of first")
    df_keep_last = df.drop_duplicates(subset=['CustomerID'], keep='last')
    print("Keeps the most recent entry per customer:")
    print(df_keep_last)
    print("✓ Useful for keeping most recent transaction")
    
    # Keep none (remove all duplicates)
    print("\n\nOption 4: Remove ALL occurrences of duplicates")
    df_remove_all = df.drop_duplicates(subset=['CustomerID'], keep=False)
    print("Removes all rows where CustomerID appears more than once:")
    print(df_remove_all)
    print(f"Shape: {df_remove_all.shape}")
    print("⚠ Warning: Very aggressive - use with caution!")
    
    print_subsection("4. ANALYZING DUPLICATE PATTERNS")
    
    print("\nAnalyzing duplicate patterns...")
    
    # Count occurrences of each CustomerID
    print("\nCustomer occurrence counts:")
    customer_counts = df['CustomerID'].value_counts().sort_index()
    print(customer_counts)
    
    # Find customers with multiple entries
    print("\n\nCustomers with multiple entries:")
    multiple_entries = customer_counts[customer_counts > 1]
    print(multiple_entries)
    print(f"Number of customers with duplicates: {len(multiple_entries)}")
    
    # Detailed view of duplicates
    print("\n\nDetailed view of duplicate customer records:")
    for customer_id in multiple_entries.index:
        print(f"\n{customer_id}:")
        customer_records = df[df['CustomerID'] == customer_id]
        print(customer_records.to_string(index=False))
    
    print_subsection("5. BEST PRACTICES FOR HANDLING DUPLICATES")
    print("\n✓ DETECTION STRATEGY:")
    print("  1. Always check for duplicates after loading data")
    print("  2. Use df.duplicated().sum() for quick count")
    print("  3. Examine duplicates before removing: df[df.duplicated(keep=False)]")
    print("  4. Check specific key columns (ID fields, email, etc.)")
    
    print("\n✓ REMOVAL STRATEGY:")
    print("  • Exact duplicates: Usually safe to remove")
    print("  • Partial duplicates: Investigate before removing")
    print("  • Use subset parameter to define uniqueness criteria")
    print("  • keep='first': Default, keeps earliest record")
    print("  • keep='last': Useful for time-series (most recent)")
    print("  • keep=False: Removes all duplicates (rarely needed)")
    
    print("\n✓ WHEN TO KEEP DUPLICATES:")
    print("  • Multiple purchases by same customer (valid duplicates)")
    print("  • Time-series data with repeated measurements")
    print("  • When duplicates contain different non-key information")
    
    print("\n✓ DOCUMENTATION:")
    print("  • Always document duplicate removal decisions")
    print("  • Record which columns defined uniqueness")
    print("  • Note how many records were affected")


def demonstrate_standardization():
    """Demonstrate standardizing column names and data formats."""
    print_section("DATA CLEANING PART 3: STANDARDIZING COLUMNS AND FORMATS")
    
    # Create dataset with inconsistent naming and formats
    print("Creating sample dataset with inconsistent formatting...\n")
    data = {
        'Product ID': ['P001', 'p002', 'P003', 'p 004', 'P005'],
        'Product Name': ['  Laptop  ', 'SMARTPHONE', 'tablet', 'Headphones', 'SMARTWATCH  '],
        'category': ['Electronics', 'electronics', 'ELECTRONICS', 'Electronics', 'electronics'],
        'Price($)': ['$1,200.00', '$800', '$450.50', '$150.00', '$350'],
        'Stock_Quantity': [50, 120, 75, 200, 90],
        'Last Updated': ['2024-01-15', '15/01/2024', '2024/01/17', '01-20-2024', '2024.01.22'],
        'Is_Available': ['yes', 'YES', 'no', 'Yes', 'YES']
    }
    df = pd.DataFrame(data)
    
    print("Original Dataset (inconsistent formatting):")
    print(df)
    print("\nColumn names:", list(df.columns))
    print("Data types:\n", df.dtypes)
    
    print_subsection("1. STANDARDIZING COLUMN NAMES")
    
    # Current column names
    print("\nProblems with current column names:")
    print("  • Mixed case: 'Product ID' vs 'category'")
    print("  • Spaces: 'Product ID', 'Product Name'")
    print("  • Special characters: 'Price($)'")
    print("  • Mixed separators: 'Stock_Quantity' vs 'Product Name'")
    
    # Create standardized column names
    print("\n\nOption 1: Convert to lowercase with underscores (snake_case)")
    df_clean = df.copy()
    df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_').str.replace('[$()]', '', regex=True)
    print("Standardized columns:", list(df_clean.columns))
    print("✓ Best practice: Consistent, Python-friendly, no spaces")
    
    print("\n\nOption 2: Strip whitespace and standardize case")
    df_clean2 = df.copy()
    df_clean2.columns = df_clean2.columns.str.strip().str.replace(' ', '_').str.title()
    print("Title case columns:", list(df_clean2.columns))
    
    print("\n\nOption 3: Manual renaming for clarity")
    rename_mapping = {
        'Product ID': 'product_id',
        'Product Name': 'product_name',
        'category': 'category',
        'Price($)': 'price_usd',
        'Stock_Quantity': 'stock_quantity',
        'Last Updated': 'last_updated',
        'Is_Available': 'is_available'
    }
    df_clean3 = df.rename(columns=rename_mapping)
    print("Manually renamed columns:", list(df_clean3.columns))
    print("✓ Provides most control and clarity")
    
    # Use the cleanest version for further demos
    df = df_clean3.copy()
    
    print_subsection("2. STANDARDIZING TEXT DATA")
    
    print("\nCleaning 'product_name' column...")
    print("Original values:")
    print(df['product_name'].to_list())
    
    # Strip whitespace and standardize case
    df['product_name'] = df['product_name'].str.strip().str.title()
    print("\nAfter standardization (title case, no extra spaces):")
    print(df['product_name'].to_list())
    print("✓ Consistent capitalization and no leading/trailing spaces")
    
    print("\n\nCleaning 'category' column...")
    print("Original values:", df['category'].unique())
    
    # Standardize to lowercase
    df['category'] = df['category'].str.lower().str.strip()
    print("After standardization (lowercase):", df['category'].unique())
    print("✓ All variations now match")
    
    print("\n\nCleaning 'product_id' column...")
    print("Original values:", df['product_id'].to_list())
    
    # Standardize IDs: uppercase, remove spaces
    df['product_id'] = df['product_id'].str.upper().str.replace(' ', '')
    print("After standardization (uppercase, no spaces):", df['product_id'].to_list())
    print("✓ Consistent ID format")
    
    print_subsection("3. STANDARDIZING NUMERIC DATA")
    
    print("\nCleaning 'price_usd' column...")
    print("Original values:", df['price_usd'].to_list())
    print("Current type:", df['price_usd'].dtype)
    
    # Remove $, commas, and convert to float
    df['price_usd'] = df['price_usd'].str.replace('$', '').str.replace(',', '').astype(float)
    print("\nAfter standardization:")
    print("Values:", df['price_usd'].to_list())
    print("Type:", df['price_usd'].dtype)
    print("✓ Now a numeric type - can perform calculations")
    print(f"✓ Can calculate: Mean price = ${df['price_usd'].mean():.2f}")
    
    print_subsection("4. STANDARDIZING BOOLEAN DATA")
    
    print("\nCleaning 'is_available' column...")
    print("Original values:", df['is_available'].to_list())
    print("Current type:", df['is_available'].dtype)
    
    # Convert to boolean
    df['is_available'] = df['is_available'].str.lower().map({'yes': True, 'no': False})
    print("\nAfter standardization:")
    print("Values:", df['is_available'].to_list())
    print("Type:", df['is_available'].dtype)
    print("✓ Now true boolean values")
    print(f"✓ Can filter easily: {df['is_available'].sum()} products available")
    
    print_subsection("5. STANDARDIZING DATE FORMATS")
    
    print("\nCleaning 'last_updated' column...")
    print("Original values:", df['last_updated'].to_list())
    print("Current type:", df['last_updated'].dtype)
    
    # Convert to datetime
    df['last_updated'] = pd.to_datetime(df['last_updated'], format='mixed', dayfirst=False)
    print("\nAfter standardization:")
    print("Values:", df['last_updated'].to_list())
    print("Type:", df['last_updated'].dtype)
    print("✓ Now datetime type - can perform date operations")
    print(f"✓ Earliest update: {df['last_updated'].min()}")
    print(f"✓ Latest update: {df['last_updated'].max()}")
    
    print_subsection("6. FINAL CLEANED DATASET")
    
    print("\n✓ FULLY STANDARDIZED DATASET:")
    print(df)
    
    print("\n✓ COLUMN NAMES:")
    print(list(df.columns))
    print("  → All lowercase with underscores")
    print("  → No spaces or special characters")
    print("  → Descriptive and consistent")
    
    print("\n✓ DATA TYPES:")
    print(df.dtypes)
    print("  → Numeric columns are numeric types")
    print("  → Boolean column is bool type")
    print("  → Date column is datetime type")
    print("  → Text columns are clean and consistent")
    
    print_subsection("7. BEST PRACTICES FOR STANDARDIZATION")
    
    print("\n✓ COLUMN NAMING CONVENTIONS:")
    print("  • Use snake_case (lowercase with underscores)")
    print("  • Remove spaces and special characters")
    print("  • Be descriptive but concise")
    print("  • Use consistent naming patterns")
    print("  • Avoid ambiguous abbreviations")
    
    print("\n✓ TEXT DATA STANDARDIZATION:")
    print("  • Remove leading/trailing whitespace: str.strip()")
    print("  • Standardize case: str.lower(), str.upper(), str.title()")
    print("  • Remove extra spaces: str.replace('  ', ' ')")
    print("  • Standardize categories to consistent format")
    
    print("\n✓ NUMERIC DATA STANDARDIZATION:")
    print("  • Remove currency symbols and commas")
    print("  • Convert to appropriate numeric type (int, float)")
    print("  • Handle percentage signs if present")
    print("  • Ensure decimal consistency")
    
    print("\n✓ DATE/TIME STANDARDIZATION:")
    print("  • Convert to datetime type using pd.to_datetime()")
    print("  • Specify format when possible for faster parsing")
    print("  • Handle mixed formats with format='mixed'")
    print("  • Store in consistent timezone if applicable")
    
    print("\n✓ BOOLEAN STANDARDIZATION:")
    print("  • Convert text to True/False boolean")
    print("  • Common mappings: yes/no, y/n, 1/0, true/false")
    print("  • Use case-insensitive matching")
    
    print("\n✓ OVERALL WORKFLOW:")
    print("  1. Standardize column names first")
    print("  2. Identify data types that need conversion")
    print("  3. Clean and standardize each column")
    print("  4. Verify final data types")
    print("  5. Document transformations applied")


def main() -> None:
    """Main execution function."""
    print("\n" + "="*70)
    print("  DATA ANALYSIS: SHAPES, TYPES, AND DATA CLEANING")
    print("="*70)
    print("\nThis comprehensive guide covers:")
    print("  • Understanding DataFrame structure and data types")
    print("  • Handling missing values with drop and fill strategies")
    print("  • Identifying and removing duplicate records")
    print("  • Standardizing column names and data formats")
    print()
    
    # Create sample data
    create_sample_data()
    
    # Original demonstrations
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
    
    # New Data Cleaning Demonstrations
    # Part 7: Missing values strategies
    demonstrate_missing_values_strategies()
    
    # Part 8: Duplicate handling
    demonstrate_duplicate_handling()
    
    # Part 9: Standardization
    demonstrate_standardization()
    
    # Summary
    print_section("COMPLETE DATA ANALYSIS WORKFLOW - KEY TAKEAWAYS")
    
    print("✓ UNDERSTANDING DATA STRUCTURE:")
    print("  • Shape tells you dimensions: (rows, columns)")
    print("  • Rows = observations, Columns = variables")
    print("  • Always check dtypes after loading data")
    print("  • Use df.shape, df.dtypes, and df.info() routinely")
    
    print("\n✓ HANDLING MISSING VALUES:")
    print("  • Detect with df.isnull().sum()")
    print("  • Drop strategically: dropna(subset=['key_cols'])")
    print("  • Fill intelligently: mean/median for numbers, mode for categories")
    print("  • Document your imputation strategy")
    
    print("\n✓ MANAGING DUPLICATES:")
    print("  • Check with df.duplicated().sum()")
    print("  • Examine before removing: df[df.duplicated(keep=False)]")
    print("  • Remove with drop_duplicates(subset=['key_cols'])")
    print("  • Choose appropriate keep strategy (first/last)")
    
    print("\n✓ STANDARDIZING DATA:")
    print("  • Standardize column names (snake_case recommended)")
    print("  • Clean text: strip(), lower(), standardize format")
    print("  • Convert types: numeric, datetime, boolean")
    print("  • Ensure consistency across all records")
    
    print("\n" + "="*70)
    print("  COMPLETE DATA CLEANING WORKFLOW MASTERED!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
