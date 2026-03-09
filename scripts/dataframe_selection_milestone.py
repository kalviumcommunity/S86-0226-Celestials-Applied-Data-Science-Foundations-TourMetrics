"""
DataFrame Selection Milestone - Indexing and Slicing

This script demonstrates selecting rows and columns using indexing and slicing.
Mastering these techniques is essential for accurate data extraction and analysis.

Learning Objectives:
- Select columns by name (single and multiple)
- Select rows by position using integer-based indexing
- Select rows by label using label-based indexing
- Combine row and column selection safely
- Understand when to use each selection method

Skills Covered:
✓ Column selection (single and multiple)
✓ Positional indexing (.iloc)
✓ Label-based indexing (.loc)
✓ Combined row/column selection
✓ Safe and readable selection practices
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


def create_sample_data():
    """Create sample DataFrames for demonstration."""
    print_section("CREATING SAMPLE DATA")
    
    # Tour Performance Dataset
    tour_data = {
        'TourID': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
                 'Philadelphia', 'San Antonio', 'San Diego'],
        'Attendance': [15000, 18500, 12000, 14200, 11000, 13500, 9800, 16700],
        'Revenue': [450000, 555000, 360000, 426000, 330000, 405000, 294000, 501000],
        'Rating': [4.5, 4.8, 4.2, 4.6, 4.0, 4.4, 3.9, 4.7],
        'Duration_Hours': [2.5, 3.0, 2.0, 2.5, 2.0, 2.5, 2.0, 3.0]
    }
    
    df_tours = pd.DataFrame(tour_data)
    
    print("Sample Tour Performance Dataset Created:")
    print(df_tours)
    print(f"\nShape: {df_tours.shape} (rows, columns)")
    print(f"Columns: {df_tours.columns.tolist()}")
    print(f"Index: {df_tours.index.tolist()}")
    
    return df_tours


def demonstrate_column_selection(df):
    """Demonstrate selecting columns by name."""
    print_section("1. SELECTING COLUMNS BY NAME")
    
    print("Column selection is the most common DataFrame operation.")
    print("You can select single columns or multiple columns using their names.\n")
    
    # Single column selection (returns Series)
    print_subsection("A. Single Column Selection (Returns a Series)")
    print("\nCode: df['City']")
    city_series = df['City']
    print(city_series)
    print(f"\nType: {type(city_series)}")
    print(f"Shape: {city_series.shape}")
    
    # Alternative single column access (dot notation)
    print_subsection("B. Alternative: Dot Notation (Use with caution)")
    print("\nCode: df.City")
    print("Note: Only works if column name has no spaces or special characters")
    print(df.City)
    
    # Multiple column selection (returns DataFrame)
    print_subsection("C. Multiple Column Selection (Returns a DataFrame)")
    print("\nCode: df[['City', 'Attendance', 'Revenue']]")
    selected_columns = df[['City', 'Attendance', 'Revenue']]
    print(selected_columns)
    print(f"\nType: {type(selected_columns)}")
    print(f"Shape: {selected_columns.shape}")
    
    # Reordering columns
    print_subsection("D. Reordering Columns")
    print("\nCode: df[['Revenue', 'Attendance', 'City']]")
    reordered = df[['Revenue', 'Attendance', 'City']]
    print(reordered)
    
    print("\n⚠️  KEY POINTS:")
    print("   • Single brackets + string → Series (1D)")
    print("   • Double brackets + list → DataFrame (2D)")
    print("   • Column order in list determines output order")
    print("   • Use explicit bracket notation for reliability")


def demonstrate_row_selection_position(df):
    """Demonstrate selecting rows by position using .iloc."""
    print_section("2. SELECTING ROWS BY POSITION (.iloc)")
    
    print("Position-based indexing uses integer positions (0-based indexing).")
    print("Use .iloc for selecting rows by their integer location.\n")
    
    # Single row selection
    print_subsection("A. Single Row Selection")
    print("\nCode: df.iloc[0]  # First row")
    first_row = df.iloc[0]
    print(first_row)
    print(f"\nType: {type(first_row)}")
    print("\nNote: Single row selection returns a Series with column names as index")
    
    # Multiple specific rows
    print_subsection("B. Multiple Specific Rows")
    print("\nCode: df.iloc[[0, 2, 5]]  # Rows at index 0, 2, and 5")
    specific_rows = df.iloc[[0, 2, 5]]
    print(specific_rows)
    print(f"\nType: {type(specific_rows)}")
    
    # Slicing rows
    print_subsection("C. Slicing Rows (Range)")
    print("\nCode: df.iloc[1:4]  # Rows 1, 2, 3 (excludes 4)")
    sliced_rows = df.iloc[1:4]
    print(sliced_rows)
    print("\nNote: Slicing is EXCLUSIVE of the end index (like Python lists)")
    
    # First n rows
    print_subsection("D. First N Rows")
    print("\nCode: df.iloc[:3]  # First 3 rows")
    print(df.iloc[:3])
    
    # Last n rows
    print_subsection("E. Last N Rows")
    print("\nCode: df.iloc[-3:]  # Last 3 rows")
    print(df.iloc[-3:])
    
    # Every nth row
    print_subsection("F. Every Nth Row (Step)")
    print("\nCode: df.iloc[::2]  # Every 2nd row")
    print(df.iloc[::2])
    
    print("\n⚠️  KEY POINTS:")
    print("   • .iloc uses integer positions (0-based)")
    print("   • Slicing is EXCLUSIVE of end index")
    print("   • Negative indexing works (e.g., -1 is last row)")
    print("   • Returns Series for single row, DataFrame for multiple")


def demonstrate_row_selection_label(df):
    """Demonstrate selecting rows by label using .loc."""
    print_section("3. SELECTING ROWS BY LABEL (.loc)")
    
    print("Label-based indexing uses index labels (not positions).")
    print("Use .loc for selecting rows by their index label.\n")
    
    # First, create a DataFrame with meaningful index labels
    print_subsection("Setting Up: Creating DataFrame with Custom Index")
    df_labeled = df.set_index('TourID')
    print("\nCode: df_labeled = df.set_index('TourID')")
    print(df_labeled)
    print(f"\nIndex: {df_labeled.index.tolist()}")
    
    # Single row by label
    print_subsection("A. Single Row by Label")
    print("\nCode: df_labeled.loc['T003']")
    row_t003 = df_labeled.loc['T003']
    print(row_t003)
    print(f"\nType: {type(row_t003)}")
    
    # Multiple specific rows by label
    print_subsection("B. Multiple Specific Rows by Label")
    print("\nCode: df_labeled.loc[['T001', 'T004', 'T007']]")
    specific_rows = df_labeled.loc[['T001', 'T004', 'T007']]
    print(specific_rows)
    
    # Slicing rows by label
    print_subsection("C. Slicing Rows by Label Range")
    print("\nCode: df_labeled.loc['T002':'T005']")
    sliced_rows = df_labeled.loc['T002':'T005']
    print(sliced_rows)
    print("\n⚠️  IMPORTANT: .loc slicing is INCLUSIVE of both start AND end!")
    
    # Using default numeric index with .loc
    print_subsection("D. Using .loc with Default Numeric Index")
    print("\nCode: df.loc[2]  # Row with index label 2")
    print(df.loc[2])
    print("\nNote: With default index, .loc behaves like .iloc")
    print("But if index labels are not in order, results differ!")
    
    print("\n⚠️  KEY POINTS:")
    print("   • .loc uses index labels (not positions)")
    print("   • Slicing is INCLUSIVE of both start and end")
    print("   • Works with any index type (strings, dates, numeric)")
    print("   • More explicit and readable than position-based")


def demonstrate_combined_selection(df):
    """Demonstrate selecting rows and columns together."""
    print_section("4. COMBINING ROW AND COLUMN SELECTION")
    
    print("Real-world analysis often requires selecting specific rows AND columns.")
    print("Use .iloc or .loc with both row and column specifiers.\n")
    
    df_labeled = df.set_index('TourID')
    
    # Using .iloc for position-based selection
    print_subsection("A. Position-Based: .iloc[rows, columns]")
    
    print("\n1. Specific rows and columns by position")
    print("Code: df.iloc[0:3, 1:4]  # First 3 rows, columns 1-3")
    subset1 = df.iloc[0:3, 1:4]
    print(subset1)
    
    print("\n2. Specific rows, all columns")
    print("Code: df.iloc[0:3, :]  # First 3 rows, all columns")
    subset2 = df.iloc[0:3, :]
    print(subset2)
    
    print("\n3. All rows, specific columns")
    print("Code: df.iloc[:, [1, 2, 4]]  # All rows, columns at positions 1, 2, 4")
    subset3 = df.iloc[:, [1, 2, 4]]
    print(subset3)
    
    # Using .loc for label-based selection
    print_subsection("B. Label-Based: .loc[rows, columns]")
    
    print("\n1. Specific rows and columns by label")
    print("Code: df_labeled.loc['T002':'T004', ['City', 'Attendance', 'Rating']]")
    subset4 = df_labeled.loc['T002':'T004', ['City', 'Attendance', 'Rating']]
    print(subset4)
    
    print("\n2. Specific rows, all columns")
    print("Code: df_labeled.loc['T001':'T003', :]")
    subset5 = df_labeled.loc['T001':'T003', :]
    print(subset5)
    
    print("\n3. All rows, specific columns")
    print("Code: df_labeled.loc[:, ['City', 'Revenue']]")
    subset6 = df_labeled.loc[:, ['City', 'Revenue']]
    print(subset6)
    
    # Single value extraction
    print_subsection("C. Extracting Single Values")
    
    print("\n1. Using .iloc")
    print("Code: df.iloc[2, 3]  # Row 2, Column 3")
    single_value_pos = df.iloc[2, 3]
    print(f"Value: {single_value_pos}")
    print(f"Type: {type(single_value_pos)}")
    
    print("\n2. Using .loc")
    print("Code: df_labeled.loc['T005', 'Revenue']")
    single_value_label = df_labeled.loc['T005', 'Revenue']
    print(f"Value: {single_value_label}")
    print(f"Type: {type(single_value_label)}")
    
    print("\n⚠️  KEY POINTS:")
    print("   • Format: df.iloc[rows, columns] or df.loc[rows, columns]")
    print("   • Use : to select all rows or all columns")
    print("   • .iloc uses integer positions (exclusive slicing)")
    print("   • .loc uses labels (inclusive slicing)")
    print("   • Always verify your selection matches your intent")


def demonstrate_common_mistakes():
    """Show common selection mistakes and how to avoid them."""
    print_section("5. COMMON MISTAKES AND BEST PRACTICES")
    
    # Create sample data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)
    
    print("Sample DataFrame:")
    print(df)
    
    print_subsection("❌ MISTAKE 1: Confusing .loc and .iloc")
    print("\nWrong assumption: .loc and .iloc are interchangeable")
    print("\ndf.iloc[0:2]  # Gets rows at positions 0 and 1")
    print(df.iloc[0:2])
    print("\ndf.loc[0:2]  # Gets rows with labels 0, 1, AND 2")
    print(df.loc[0:2])
    print("\n✓ Remember: .iloc is exclusive, .loc is inclusive for slicing")
    
    print_subsection("❌ MISTAKE 2: Using single brackets for multiple columns")
    print("\nWrong: df['A', 'B']  # This will cause an error")
    print("✓ Correct: df[['A', 'B']]  # Need double brackets for multiple columns")
    print(df[['A', 'B']])
    
    print_subsection("❌ MISTAKE 3: Chained indexing (copy warning)")
    print("\nProblematic: df[df['A'] > 2]['B'] = 999  # May not work as expected")
    print("✓ Better: Use .loc for safe assignment")
    print("df.loc[df['A'] > 2, 'B'] = 999")
    
    print_subsection("✓ BEST PRACTICES")
    print("""
1. Be Explicit:
   • Use .loc for label-based selection
   • Use .iloc for position-based selection
   • Avoid chained indexing

2. Double-Check Your Selection:
   • Print shape after selection
   • Verify first/last rows
   • Check data types

3. Use Readable Code:
   • Use meaningful column lists
   • Add comments for complex selections
   • Break complex selections into steps

4. When to Use Each Method:
   • df['column'] → Quick single column access
   • df[['col1', 'col2']] → Multiple columns
   • .iloc → When position matters (e.g., first 10 rows)
   • .loc → When labels matter (e.g., specific tour IDs)
    """)


def demonstrate_practical_examples(df):
    """Show practical real-world selection scenarios."""
    print_section("6. PRACTICAL EXAMPLES")
    
    print_subsection("Example 1: Extract Top Performers")
    print("\nScenario: Get top 3 cities by revenue")
    print("\nStep 1: Sort by revenue")
    df_sorted = df.sort_values('Revenue', ascending=False)
    print(df_sorted)
    
    print("\nStep 2: Select top 3 with relevant columns")
    print("Code: df_sorted[['City', 'Revenue', 'Rating']].iloc[:3]")
    top_performers = df_sorted[['City', 'Revenue', 'Rating']].iloc[:3]
    print(top_performers)
    
    print_subsection("Example 2: Analyze Specific Tour Range")
    print("\nScenario: Compare middle tours (indices 2-5)")
    print("Code: df[['City', 'Attendance', 'Revenue']].iloc[2:6]")
    middle_tours = df[['City', 'Attendance', 'Revenue']].iloc[2:6]
    print(middle_tours)
    
    print_subsection("Example 3: Quick Revenue Check")
    print("\nScenario: Get revenue for specific cities")
    print("Code: df.loc[df['City'].isin(['New York', 'Los Angeles', 'Chicago']), ['City', 'Revenue']]")
    revenue_check = df.loc[df['City'].isin(['New York', 'Los Angeles', 'Chicago']), ['City', 'Revenue']]
    print(revenue_check)
    
    print("\n💡 TIP: Combine filtering with selection for powerful data extraction!")


def selection_quick_reference():
    """Provide a quick reference guide."""
    print_section("QUICK REFERENCE GUIDE")
    
    print("""
╔════════════════════════════════════════════════════════════════════╗
║                    DATAFRAME SELECTION METHODS                     ║
╠════════════════════════════════════════════════════════════════════╣
║ COLUMNS                                                            ║
║ df['A']              → Single column (Series)                      ║
║ df[['A', 'B']]       → Multiple columns (DataFrame)                ║
║                                                                    ║
║ ROWS BY POSITION (.iloc)                                           ║
║ df.iloc[0]           → First row (Series)                          ║
║ df.iloc[0:3]         → Rows 0, 1, 2 (DataFrame)                    ║
║ df.iloc[[0, 2, 5]]   → Specific rows (DataFrame)                   ║
║ df.iloc[-1]          → Last row (Series)                           ║
║                                                                    ║
║ ROWS BY LABEL (.loc)                                               ║
║ df.loc[0]            → Row with index label 0 (Series)             ║
║ df.loc[0:3]          → Rows 0, 1, 2, 3 (inclusive!)                ║
║ df.loc[['A', 'B']]   → Rows with index labels 'A' and 'B'         ║
║                                                                    ║
║ COMBINED SELECTION                                                 ║
║ df.iloc[0:3, 1:4]    → Rows 0-2, Columns at positions 1-3         ║
║ df.loc[:, ['A', 'B']]→ All rows, Columns 'A' and 'B'              ║
║ df.iloc[2, 3]        → Single value at row 2, column 3            ║
║                                                                    ║
║ KEY DIFFERENCES                                                    ║
║ .iloc → Position-based, 0-indexed, EXCLUSIVE slicing              ║
║ .loc  → Label-based, INCLUSIVE slicing                            ║
╚════════════════════════════════════════════════════════════════════╝
    """)


def main():
    """Main function to run all demonstrations."""
    print_section("DATAFRAME SELECTION MILESTONE")
    print("This script demonstrates all essential row and column selection techniques.")
    print("Follow along and observe how each method works.\n")
    
    # Create sample data
    df_tours = create_sample_data()
    
    # Run all demonstrations
    demonstrate_column_selection(df_tours)
    demonstrate_row_selection_position(df_tours)
    demonstrate_row_selection_label(df_tours)
    demonstrate_combined_selection(df_tours)
    demonstrate_common_mistakes()
    demonstrate_practical_examples(df_tours)
    selection_quick_reference()
    
    # Summary
    print_section("MILESTONE COMPLETE")
    print("""
✓ You've learned how to:
  • Select columns by name (single and multiple)
  • Select rows by position using .iloc
  • Select rows by label using .loc
  • Combine row and column selection
  • Avoid common selection mistakes

Next Steps:
1. Practice these techniques with your own data
2. Record a 2-minute video demonstrating these concepts
3. Apply selection in data cleaning and analysis tasks

Remember: Accurate data selection is the foundation of reliable analysis!
    """)
    
    print("\n" + "="*70)
    print("📹 VIDEO CHECKLIST")
    print("="*70)
    print("""
Your 2-minute video should demonstrate:
□ Selecting one or more columns
□ Selecting rows by position (.iloc)
□ Selecting rows by label (.loc)
□ Selecting rows and columns together
□ Explaining when to use each approach
□ Screen clearly visible with code and output
    """)


if __name__ == "__main__":
    main()
