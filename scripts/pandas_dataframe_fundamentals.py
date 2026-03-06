"""
Pandas DataFrame Fundamentals
Demonstrates creating and inspecting DataFrames from dictionaries and files
"""

import pandas as pd

def demonstrate_dataframe_basics():
    """Show what a DataFrame represents"""
    print("=" * 60)
    print("1. UNDERSTANDING PANDAS DATAFRAMES")
    print("=" * 60)
    print("A DataFrame is a 2D labeled data structure")
    print("- Similar to a spreadsheet or SQL table")
    print("- Has rows and columns with labels")
    print("- Columns can have different data types\n")

def create_dataframe_from_dict():
    """Create DataFrames from Python dictionaries"""
    print("=" * 60)
    print("2. CREATING DATAFRAMES FROM DICTIONARIES")
    print("=" * 60)
    
    # Example 1: Student data
    student_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [23, 25, 22, 24],
        'Grade': ['A', 'B', 'A', 'B'],
        'Score': [92, 85, 95, 88]
    }
    
    df_students = pd.DataFrame(student_data)
    print("\nStudent DataFrame:")
    print(df_students)
    print(f"\nColumn Names: {df_students.columns.tolist()}")
    print(f"Index: {df_students.index.tolist()}")
    
    # Example 2: Sales data
    sales_data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Price': [999.99, 25.50, 75.00, 299.99],
        'Quantity': [5, 50, 30, 10]
    }
    
    df_sales = pd.DataFrame(sales_data)
    print("\n\nSales DataFrame:")
    print(df_sales)
    
    return df_students, df_sales

def create_sample_csv_files():
    """Create sample CSV files for demonstration"""
    # Employee data
    employee_csv = """Name,Department,Salary,Years
John,Engineering,75000,3
Sarah,Marketing,65000,2
Mike,Engineering,80000,5
Emma,Sales,70000,4
David,Marketing,68000,3"""
    
    with open('data/raw/employees.csv', 'w') as f:
        f.write(employee_csv)
    
    # Books data
    books_csv = """Title,Author,Year,Pages
1984,George Orwell,1949,328
To Kill a Mockingbird,Harper Lee,1960,281
The Great Gatsby,F. Scott Fitzgerald,1925,180
Pride and Prejudice,Jane Austen,1813,432"""
    
    with open('data/raw/books.csv', 'w') as f:
        f.write(books_csv)
    
    print("\nSample CSV files created in data/raw/")

def load_dataframe_from_file():
    """Load DataFrames from CSV files"""
    print("\n" + "=" * 60)
    print("3. CREATING DATAFRAMES FROM FILES")
    print("=" * 60)
    
    # Load employee data
    df_employees = pd.read_csv('data/raw/employees.csv')
    print("\nEmployee DataFrame loaded from CSV:")
    print(df_employees)
    
    print("\n\nHeaders (Column Names):")
    print(df_employees.columns.tolist())
    
    print("\nFirst row of data:")
    print(df_employees.iloc[0])
    
    # Load books data
    df_books = pd.read_csv('data/raw/books.csv')
    print("\n\nBooks DataFrame loaded from CSV:")
    print(df_books)
    
    return df_employees, df_books

def inspect_dataframe_structure(df, name="DataFrame"):
    """Inspect DataFrame structure and contents"""
    print("\n" + "=" * 60)
    print(f"4. INSPECTING {name.upper()} STRUCTURE")
    print("=" * 60)
    
    # First few rows
    print(f"\nFirst 3 rows of {name}:")
    print(df.head(3))
    
    # Last few rows
    print(f"\nLast 2 rows of {name}:")
    print(df.tail(2))
    
    # Shape
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Column names
    print(f"\nColumn Names: {df.columns.tolist()}")
    
    # Data types
    print(f"\nData Types:")
    print(df.dtypes)
    
    # Info
    print(f"\nDataFrame Info:")
    df.info()
    
    # Basic statistics
    print(f"\nBasic Statistics:")
    print(df.describe())

def main():
    """Main execution function"""
    print("\n" + "=" * 60)
    print("PANDAS DATAFRAME FUNDAMENTALS")
    print("=" * 60 + "\n")
    
    # 1. Understand DataFrames
    demonstrate_dataframe_basics()
    
    # 2. Create from dictionaries
    df_students, df_sales = create_dataframe_from_dict()
    
    # 3. Create sample files and load
    create_sample_csv_files()
    df_employees, df_books = load_dataframe_from_file()
    
    # 4. Inspect structure
    inspect_dataframe_structure(df_employees, "Employees")
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("✓ DataFrames are 2D labeled structures (rows × columns)")
    print("✓ Create from dictionaries: pd.DataFrame(dict)")
    print("✓ Load from files: pd.read_csv('file.csv')")
    print("✓ Inspect with: .head(), .shape, .dtypes, .info()")
    print("✓ DataFrames are the foundation of Pandas analysis")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
