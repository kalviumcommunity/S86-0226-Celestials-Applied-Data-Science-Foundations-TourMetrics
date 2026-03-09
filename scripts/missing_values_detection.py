"""
Missing Values Detection Milestone - Demonstration Script

This script demonstrates how to detect and analyze missing values in Pandas DataFrames.
It covers detection methods, counting techniques, and interpretation of missing data patterns.

Learning Objectives:
- Detect missing values using standard Pandas methods (isna, isnull)
- Count missing values at column and row levels
- Calculate missing value percentages and statistics
- Interpret missing data patterns for data quality assessment
- Understand the distinction between detection and cleaning operations

Educational Purpose:
This is a detection-focused tool that helps learners identify and understand missing
data patterns WITHOUT modifying the original data. Detection must precede cleaning to
ensure informed decision-making about how to handle missing values.
"""

import pandas as pd
import os


def print_section_header(title):
    """
    Print a formatted section header for better readability.
    
    Args:
        title: Section title to display
    """
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def print_subsection(title):
    """
    Print a formatted subsection header for better readability.
    
    Args:
        title: Subsection title to display
    """
    print(f"\n{'-' * 70}")
    print(f"{title}")
    print(f"{'-' * 70}")


def validate_file_path(filepath):
    """
    Check if a file exists at the specified path.
    
    This helper function validates file existence before attempting to load,
    enabling better error handling and user feedback.
    
    Args:
        filepath: Full path to the file
    
    Returns:
        bool: True if file exists, False otherwise
    
    Examples:
        >>> filepath = os.path.join('data', 'raw', 'books.csv')
        >>> if validate_file_path(filepath):
        ...     print("File exists!")
    """
    return os.path.exists(filepath)


def load_csv_file(filename):
    """
    Load a CSV file from the data/raw directory.
    
    This function handles CSV loading with comprehensive error handling to provide
    educational feedback when issues occur. It preserves all data including missing
    values represented as NaN.
    
    Args:
        filename: Name of the CSV file (e.g., 'books.csv')
    
    Returns:
        pd.DataFrame if successful, None if loading fails
    
    Examples:
        >>> df = load_csv_file('books.csv')
        >>> if df is not None:
        ...     print(f"Loaded {len(df)} rows")
    """
    # Construct the full file path to data/raw directory
    filepath = os.path.join('data', 'raw', filename)
    
    try:
        # Load CSV file, preserving all data including missing values
        df = pd.read_csv(filepath)
        print(f"✓ Successfully loaded {filename}")
        print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        return df
        
    except FileNotFoundError:
        # Handle case where file doesn't exist
        print(f"✗ Error: File not found at {filepath}")
        print("  Tip: Check that the file path is correct and the file exists")
        return None
        
    except pd.errors.ParserError:
        # Handle case where CSV is malformed
        print(f"✗ Error: Failed to parse CSV file {filename}")
        print("  Tip: Check for inconsistent columns or wrong delimiter")
        return None
        
    except UnicodeDecodeError:
        # Handle encoding issues
        print(f"✗ Error: Encoding issue detected in {filename}")
        print("  Tip: Try specifying encoding parameter, e.g., encoding='latin-1'")
        return None
        
    except Exception as e:
        # Catch any unexpected errors
        print(f"✗ Error: Unexpected error loading {filename}")
        print(f"  Details: {str(e)}")
        return None


def detect_missing_values(df):
    """
    Create a boolean DataFrame indicating missing values.
    
    This function uses Pandas' isna() method to detect missing values across the
    entire DataFrame. It recognizes all three standard missing value types in Pandas:
    NaN (Not a Number), None (Python's null), and pd.NA (Pandas' nullable type).
    
    The function is non-destructive and does not modify the original DataFrame.
    Immutability is verified by checking the DataFrame before and after detection.
    
    Args:
        df: Input DataFrame to analyze
    
    Returns:
        pd.DataFrame: Boolean DataFrame where True indicates a missing value
                     and False indicates a present value. The returned DataFrame
                     has the same shape as the input.
    
    Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> df = pd.DataFrame({
        ...     'A': [1, np.nan, 3],
        ...     'B': [None, 5, 6],
        ...     'C': [7, 8, pd.NA]
        ... })
        >>> missing_mask = detect_missing_values(df)
        >>> print(missing_mask)
               A      B      C
        0  False   True  False
        1   True  False  False
        2  False  False   True
    
    Notes:
        - pd.isna() is equivalent to pd.isnull() - both detect the same missing types
        - This function detects missing values but does NOT modify the DataFrame
        - Detection should always precede any cleaning or imputation operations
        - Immutability is verified to ensure the original DataFrame remains unchanged
    """
    # IMMUTABILITY CHECK: Store original DataFrame state for verification
    # This ensures detection operations don't accidentally modify the data
    original_shape = df.shape
    original_missing_count = df.isna().sum().sum()
    
    # Use pd.isna() to create a boolean mask of missing values
    # This detects NaN, None, and pd.NA across all columns and rows
    result = pd.isna(df)
    
    # IMMUTABILITY VERIFICATION: Confirm DataFrame unchanged after detection
    # Check that shape and missing value count remain identical
    assert df.shape == original_shape, \
        "DataFrame shape changed during detection!"
    assert df.isna().sum().sum() == original_missing_count, \
        "DataFrame values changed during detection!"
    
    return result


def count_missing_per_column(df):
    """
    Count missing values for each column.
    
    This function analyzes each column in the DataFrame to count missing values
    and calculate the percentage of missing data. Results are sorted by missing
    count in descending order to highlight columns with the most missing data.
    
    The function is non-destructive and verifies that the original DataFrame
    remains unchanged after analysis.
    
    Args:
        df: Input DataFrame to analyze
    
    Returns:
        pd.DataFrame: DataFrame with columns:
            - Column: Name of the column
            - Missing_Count: Number of missing values in that column
            - Missing_Percent: Percentage of values that are missing
        Sorted by Missing_Count in descending order
    
    Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> df = pd.DataFrame({
        ...     'A': [1, np.nan, 3, np.nan],
        ...     'B': [4, 5, 6, 7],
        ...     'C': [np.nan, np.nan, np.nan, 10]
        ... })
        >>> stats = count_missing_per_column(df)
        >>> print(stats)
          Column  Missing_Count  Missing_Percent
        0      C              3            75.00
        1      A              2            50.00
        2      B              0             0.00
    
    Notes:
        - Uses df.isna().sum() to count missing values per column
        - Percentage formula: (missing_count / total_rows) * 100
        - Sorting helps identify problematic columns quickly
        - This function does NOT modify the original DataFrame
        - Immutability is verified to ensure data integrity
    """
    # IMMUTABILITY CHECK: Store original DataFrame state for verification
    original_shape = df.shape
    original_dtypes = df.dtypes.to_dict()
    
    # Get total number of rows for percentage calculation
    total_rows = len(df)
    
    # Count missing values for each column using isna().sum()
    missing_counts = df.isna().sum()
    
    # Calculate percentages: (missing_count / total_rows) * 100
    missing_percentages = (missing_counts / total_rows) * 100
    
    # Create a DataFrame with column names, counts, and percentages
    stats_df = pd.DataFrame({
        'Column': missing_counts.index,
        'Missing_Count': missing_counts.values,
        'Missing_Percent': missing_percentages.values
    })
    
    # Sort by Missing_Count in descending order to show most problematic
    # columns first
    stats_df = stats_df.sort_values('Missing_Count', ascending=False)
    stats_df = stats_df.reset_index(drop=True)
    
    # IMMUTABILITY VERIFICATION: Confirm DataFrame unchanged after analysis
    assert df.shape == original_shape, "DataFrame shape changed during analysis!"
    assert df.dtypes.to_dict() == original_dtypes, "DataFrame dtypes changed during analysis!"
    
    return stats_df


def identify_rows_with_missing(df):
    """
    Identify rows containing at least one missing value.
    
    This function finds all rows in the DataFrame that contain one or more missing
    values. It returns both the complete row data and a list of row indices for
    further analysis or inspection.
    
    The function is non-destructive and verifies that the original DataFrame
    remains unchanged after identification.
    
    Args:
        df: Input DataFrame to analyze
    
    Returns:
        tuple: A tuple containing:
            - pd.DataFrame: Rows that contain at least one missing value
            - list[int]: List of indices for rows with missing values
    
    Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> df = pd.DataFrame({
        ...     'A': [1, 2, 3, 4],
        ...     'B': [5, np.nan, 7, 8],
        ...     'C': [9, 10, np.nan, 12]
        ... })
        >>> rows_with_missing, indices = identify_rows_with_missing(df)
        >>> print(indices)
        [1, 2]
        >>> print(rows_with_missing)
             A    B     C
        1  2.0  NaN  10.0
        2  3.0  7.0   NaN
    
    Notes:
        - Uses df.isna().any(axis=1) to check if any value in each row is missing
        - axis=1 means "check across columns" for each row
        - Returns complete row data, not just the missing values
        - This function does NOT modify the original DataFrame
        - Useful for inspecting specific records with incomplete data
        - Immutability is verified to ensure data integrity
    """
    # IMMUTABILITY CHECK: Store original DataFrame state for verification
    original_shape = df.shape
    original_index = df.index.tolist()
    
    # Use isna().any(axis=1) to create a boolean mask for rows with any missing values
    # axis=1 means "check across columns" - returns True if any column has missing value
    rows_mask = df.isna().any(axis=1)
    
    # Filter the DataFrame to get only rows where the mask is True
    rows_with_missing = df[rows_mask]
    
    # Extract the indices of these rows as a list
    indices_list = rows_with_missing.index.tolist()
    
    # IMMUTABILITY VERIFICATION: Confirm DataFrame unchanged after identification
    assert df.shape == original_shape, "DataFrame shape changed during identification!"
    assert df.index.tolist() == original_index, "DataFrame index changed during identification!"
    
    # Return both the rows DataFrame and the list of indices
    return rows_with_missing, indices_list


def calculate_missing_percentages(df):
    """
    Calculate overall missing value statistics for the entire DataFrame.
    
    This function provides DataFrame-level statistics about missing values,
    including total cell counts, missing cell counts, and percentages at both
    the cell level and row level. These statistics give a comprehensive view
    of data quality and completeness.
    
    The function is non-destructive and verifies that the original DataFrame
    remains unchanged after calculation.
    
    Args:
        df: Input DataFrame to analyze
    
    Returns:
        dict: Dictionary containing:
            - total_cells (int): Total number of cells in the DataFrame
            - missing_cells (int): Number of cells with missing values
            - missing_percent (float): Percentage of cells that are missing
            - rows_with_missing (int): Number of rows containing at least one missing value
            - rows_with_missing_percent (float): Percentage of rows with missing values
            - total_rows (int): Total number of rows in the DataFrame
            - total_columns (int): Total number of columns in the DataFrame
    
    Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> df = pd.DataFrame({
        ...     'A': [1, np.nan, 3, 4],
        ...     'B': [5, 6, np.nan, 8],
        ...     'C': [9, 10, 11, 12]
        ... })
        >>> stats = calculate_missing_percentages(df)
        >>> print(f"Total cells: {stats['total_cells']}")
        Total cells: 12
        >>> print(f"Missing cells: {stats['missing_cells']}")
        Missing cells: 2
        >>> print(f"Missing percent: {stats['missing_percent']:.2f}%")
        Missing percent: 16.67%
        >>> print(f"Rows with missing: {stats['rows_with_missing']}")
        Rows with missing: 2
    
    Notes:
        - Total cells = rows × columns
        - Missing cells counted using df.isna().sum().sum()
        - Cell percentage = (missing_cells / total_cells) * 100
        - Rows with missing counted using df.isna().any(axis=1).sum()
        - Row percentage = (rows_with_missing / total_rows) * 100
        - This function does NOT modify the original DataFrame
        - Useful for overall data quality assessment
        - Immutability is verified to ensure data integrity
    """
    # IMMUTABILITY CHECK: Store original DataFrame state for verification
    original_shape = df.shape
    original_columns = df.columns.tolist()
    
    # Get DataFrame dimensions
    total_rows = len(df)
    total_columns = len(df.columns)
    
    # Calculate total cells: rows * columns
    total_cells = total_rows * total_columns
    
    # Count missing cells: df.isna().sum().sum()
    # First sum() counts missing per column, second sum() totals across all columns
    missing_cells = df.isna().sum().sum()
    
    # Calculate percentage of missing cells
    missing_percent = (missing_cells / total_cells * 100) if total_cells > 0 else 0.0
    
    # Count rows with at least one missing value
    # df.isna().any(axis=1) returns True for rows with any missing value
    # .sum() counts the True values
    rows_with_missing = df.isna().any(axis=1).sum()
    
    # Calculate percentage of rows with missing values
    rows_with_missing_percent = (rows_with_missing / total_rows * 100) if total_rows > 0 else 0.0
    
    # IMMUTABILITY VERIFICATION: Confirm DataFrame unchanged after calculation
    assert df.shape == original_shape, "DataFrame shape changed during calculation!"
    assert df.columns.tolist() == original_columns, "DataFrame columns changed during calculation!"
    
    # Return dictionary with all statistics
    return {
        'total_cells': total_cells,
        'missing_cells': missing_cells,
        'missing_percent': missing_percent,
        'rows_with_missing': rows_with_missing,
        'rows_with_missing_percent': rows_with_missing_percent,
        'total_rows': total_rows,
        'total_columns': total_columns
    }


def format_column_summary(column_stats):
    """
    Format column-level missing value statistics as a readable table.
    
    This function takes the DataFrame output from count_missing_per_column() and
    formats it into a clear, aligned table with headers and separators for easy
    reading and interpretation.
    
    Args:
        column_stats: DataFrame from count_missing_per_column() with columns:
                     Column, Missing_Count, Missing_Percent
    
    Returns:
        str: Formatted string representation of the table
    
    Examples:
        >>> import pandas as pd
        >>> stats = pd.DataFrame({
        ...     'Column': ['Age', 'Name', 'Email'],
        ...     'Missing_Count': [5, 2, 0],
        ...     'Missing_Percent': [25.0, 10.0, 0.0]
        ... })
        >>> print(format_column_summary(stats))
        Column Name          Missing Count    Missing %
        ─────────────────────────────────────────────────
        Age                              5        25.00%
        Name                             2        10.00%
        Email                            0         0.00%
    
    Notes:
        - Uses fixed-width formatting for column alignment
        - Percentages formatted to 2 decimal places
        - Includes header separator for visual clarity
        - Returns empty string if column_stats is empty
    """
    if column_stats.empty:
        return "No columns to display."
    
    # Build the formatted table
    lines = []
    
    # Header
    header = f"{'Column Name':<20} {'Missing Count':>15} {'Missing %':>12}"
    lines.append(header)
    
    # Separator line
    separator = "─" * len(header)
    lines.append(separator)
    
    # Data rows
    for _, row in column_stats.iterrows():
        column_name = str(row['Column'])[:20]  # Truncate long names
        missing_count = int(row['Missing_Count'])
        missing_percent = float(row['Missing_Percent'])
        
        line = f"{column_name:<20} {missing_count:>15} {missing_percent:>11.2f}%"
        lines.append(line)
    
    return "\n".join(lines)


def format_row_summary(rows_with_missing, indices):
    """
    Format row-level missing value information as a readable summary.
    
    This function takes rows containing missing values and their indices, then
    formats them into a clear display. To avoid overwhelming output, it limits
    the display to the first 5 rows when many rows have missing values.
    
    Args:
        rows_with_missing: DataFrame containing rows with at least one missing value
        indices: List of row indices that have missing values
    
    Returns:
        str: Formatted string showing row indices and sample rows
    
    Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> df = pd.DataFrame({
        ...     'A': [1, 2, 3, 4, 5, 6],
        ...     'B': [np.nan, 7, np.nan, 9, np.nan, 11],
        ...     'C': [12, 13, 14, 15, 16, 17]
        ... })
        >>> rows, idx = identify_rows_with_missing(df)
        >>> print(format_row_summary(rows, idx))
        Row Indices with Missing Values: [0, 2, 4]
        
        Sample Rows (showing first 5):
        ...
    
    Notes:
        - Limits display to first 5 rows to keep output manageable
        - Shows complete row data including non-missing values
        - Useful for inspecting specific records with incomplete data
        - Returns informative message if no rows have missing values
    """
    if len(indices) == 0:
        return "No rows with missing values found."
    
    lines = []
    
    # Display row indices
    lines.append(f"Row Indices with Missing Values: {indices}")
    lines.append("")
    
    # Limit display to first 5 rows if there are many
    display_limit = 5
    rows_to_show = rows_with_missing.head(display_limit)
    
    if len(rows_with_missing) > display_limit:
        lines.append(f"Sample Rows (showing first {display_limit} of {len(rows_with_missing)}):")
    else:
        lines.append(f"Rows with Missing Values ({len(rows_with_missing)} total):")
    
    lines.append("")
    
    # Convert DataFrame to string representation
    lines.append(rows_to_show.to_string())
    
    # Add note if there are more rows
    if len(rows_with_missing) > display_limit:
        lines.append("")
        remaining = len(rows_with_missing) - display_limit
        lines.append(f"... and {remaining} more rows with missing values")
    
    return "\n".join(lines)


def print_interpretation(stats, dataset_name):
    """
    Print educational interpretation of missing value patterns.
    
    This function analyzes the missing value statistics and generates an
    educational interpretation that explains what the statistics mean for
    data quality and provides recommendations for next steps. The interpretation
    adapts based on the severity and patterns of missing data.
    
    Args:
        stats: Dictionary from calculate_missing_percentages() containing:
               total_cells, missing_cells, missing_percent, rows_with_missing,
               rows_with_missing_percent, total_rows, total_columns
        dataset_name: Name of the dataset being analyzed
    
    Returns:
        None (prints interpretation directly to console)
    
    Examples:
        >>> stats = {
        ...     'total_cells': 100,
        ...     'missing_cells': 5,
        ...     'missing_percent': 5.0,
        ...     'rows_with_missing': 3,
        ...     'rows_with_missing_percent': 15.0,
        ...     'total_rows': 20,
        ...     'total_columns': 5
        ... }
        >>> print_interpretation(stats, 'sample_data')
        
        📊 INTERPRETATION & RECOMMENDATIONS
        ════════════════════════════════════════════════════════════════════
        
        Data Quality Assessment for sample_data:
        ...
    
    Notes:
        - Provides context-aware interpretation based on missing percentages
        - Explains what the statistics mean in practical terms
        - Offers actionable recommendations for handling missing data
        - Educational tone suitable for learners
        - Does not prescribe specific cleaning methods (detection only)
    """
    print("\n📊 INTERPRETATION & RECOMMENDATIONS")
    print("═" * 70)
    print(f"\nData Quality Assessment for {dataset_name}:")
    print()
    
    # Extract statistics
    missing_percent = stats['missing_percent']
    rows_percent = stats['rows_with_missing_percent']
    missing_cells = stats['missing_cells']
    rows_with_missing = stats['rows_with_missing']
    total_rows = stats['total_rows']
    
    # Provide interpretation based on missing data severity
    if missing_cells == 0:
        print("✓ Excellent! This dataset has NO missing values.")
        print("  Your data is complete and ready for analysis.")
        print()
        print("Next Steps:")
        print("  • Proceed with exploratory data analysis")
        print("  • No cleaning or imputation needed for missing values")
        print("  • Focus on other data quality checks (duplicates, outliers, etc.)")
    
    elif missing_percent < 5:
        print(f"✓ Good data quality! Only {missing_percent:.2f}% of cells are missing.")
        print(f"  {rows_with_missing} out of {total_rows} rows ({rows_percent:.2f}%) are affected.")
        print()
        print("What this means:")
        print("  • The dataset is mostly complete with minimal missing data")
        print("  • Missing values are unlikely to significantly impact analysis")
        print()
        print("Next Steps:")
        print("  • Examine which columns have missing values (see column analysis above)")
        print("  • Consider simple imputation (mean, median, mode) if appropriate")
        print("  • Or drop the few affected rows if they won't impact your analysis")
        print("  • Document your decision for reproducibility")
    
    elif missing_percent < 20:
        print(f"⚠ Moderate missing data: {missing_percent:.2f}% of cells are missing.")
        print(f"  {rows_with_missing} out of {total_rows} rows ({rows_percent:.2f}%) are affected.")
        print()
        print("What this means:")
        print("  • Missing data is noticeable and requires careful handling")
        print("  • The pattern of missing values matters (random vs. systematic)")
        print("  • Your choice of handling method will impact analysis results")
        print()
        print("Next Steps:")
        print("  • Investigate WHY values are missing (data collection issue? intentional?)")
        print("  • Check if missing values are random or follow a pattern")
        print("  • Consider domain-appropriate imputation methods")
        print("  • Evaluate impact of different handling strategies")
        print("  • Document assumptions and limitations")
    
    else:
        print(f"⚠ Significant missing data: {missing_percent:.2f}% of cells are missing!")
        print(f"  {rows_with_missing} out of {total_rows} rows ({rows_percent:.2f}%) are affected.")
        print()
        print("What this means:")
        print("  • This dataset has substantial missing data that requires careful attention")
        print("  • Analysis results may be unreliable without proper handling")
        print("  • Consider whether this dataset is suitable for your analysis goals")
        print()
        print("Next Steps:")
        print("  • CRITICAL: Investigate the root cause of missing data")
        print("  • Determine if missing data is Missing Completely At Random (MCAR),")
        print("    Missing At Random (MAR), or Missing Not At Random (MNAR)")
        print("  • Consider advanced imputation techniques or domain expert consultation")
        print("  • Evaluate if you need additional or alternative data sources")
        print("  • Be transparent about limitations in any analysis using this data")
    
    print()
    print("Remember:")
    print("  • Detection precedes cleaning - understand your data first!")
    print("  • Different handling methods are appropriate for different situations")
    print("  • Always document your decisions and their rationale")
    print("  • Consider the impact of missing data on your specific analysis goals")


def generate_detection_report(df, dataset_name):
    """
    Generate and print a comprehensive missing value detection report.
    
    This is the main reporting function that orchestrates all detection and
    analysis functions to create a complete, formatted report. The report
    includes dataset information, overall statistics, column-level analysis,
    row-level analysis, and educational interpretation.
    
    IMPORTANT: This function is completely non-destructive. All detection
    operations verify that the original DataFrame remains unchanged through
    immutability checks built into each detection function.
    
    Args:
        df: DataFrame to analyze for missing values
        dataset_name: Name of the dataset for display purposes
    
    Returns:
        None (prints complete report directly to console)
    
    Examples:
        >>> import pandas as pd
        >>> import numpy as np
        >>> df = pd.DataFrame({
        ...     'Name': ['Alice', 'Bob', None],
        ...     'Age': [25, np.nan, 30],
        ...     'City': ['NYC', 'LA', 'Chicago']
        ... })
        >>> generate_detection_report(df, 'people_data')
        
        ══════════════════════════════════════════════════════════════════════
          MISSING VALUES DETECTION REPORT: people_data
        ══════════════════════════════════════════════════════════════════════
        ...
    
    Notes:
        - Calls all detection functions to gather comprehensive statistics
        - Formats output in clear sections for easy reading
        - Provides both quantitative statistics and qualitative interpretation
        - Non-destructive - does not modify the input DataFrame
        - Educational format suitable for learning and teaching
        - All detection functions include immutability verification
    """
    # IMMUTABILITY NOTE: All detection functions called below include built-in
    # immutability checks to ensure the original DataFrame is never modified.
    # This is a core principle of detection-only operations.
    
    print_section_header(f"MISSING VALUES DETECTION REPORT: {dataset_name}")
    
    # Section 1: Dataset Information
    print("📋 DATASET INFORMATION")
    print("─" * 70)
    print(f"Dataset Name: {dataset_name}")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Total Cells: {df.shape[0] * df.shape[1]}")
    print()
    
    # Section 2: Overall Statistics
    print("📊 OVERALL MISSING VALUE STATISTICS")
    print("─" * 70)
    stats = calculate_missing_percentages(df)
    print(f"Total Missing Cells: {stats['missing_cells']}")
    print(f"Percentage of Missing Cells: {stats['missing_percent']:.2f}%")
    print(f"Rows with Missing Values: {stats['rows_with_missing']} out of {stats['total_rows']}")
    print(f"Percentage of Rows Affected: {stats['rows_with_missing_percent']:.2f}%")
    print()
    
    # Section 3: Column-Level Analysis
    print("📋 COLUMN-LEVEL ANALYSIS")
    print("─" * 70)
    column_stats = count_missing_per_column(df)
    print(format_column_summary(column_stats))
    print()
    
    # Section 4: Row-Level Analysis
    print("📋 ROW-LEVEL ANALYSIS")
    print("─" * 70)
    rows_with_missing, indices = identify_rows_with_missing(df)
    print(format_row_summary(rows_with_missing, indices))
    print()
    
    # Section 5: Interpretation and Recommendations
    print_interpretation(stats, dataset_name)
    
    print("\n" + "═" * 70)
    print(f"  End of Detection Report for {dataset_name}")
    print("═" * 70 + "\n")


def demonstrate_detection_methods():
    """
    Demonstrate different Pandas methods for detecting missing values.
    
    This function creates a sample DataFrame with various types of missing values
    and demonstrates the four main Pandas methods for detecting them:
    - isna(): Returns True for missing values
    - isnull(): Equivalent to isna(), returns True for missing values
    - notna(): Returns True for non-missing values (opposite of isna)
    - notnull(): Equivalent to notna(), returns True for non-missing values
    
    The demonstration includes educational commentary explaining the differences
    and similarities between these methods, helping learners understand when to
    use each one.
    
    Returns:
        None (prints demonstration output directly to console)
    
    Examples:
        >>> demonstrate_detection_methods()
        
        ══════════════════════════════════════════════════════════════════════
          DEMONSTRATION: PANDAS MISSING VALUE DETECTION METHODS
        ══════════════════════════════════════════════════════════════════════
        ...
    
    Notes:
        - All four methods recognize NaN, None, and pd.NA as missing values
        - isna() and isnull() are identical - use whichever you prefer
        - notna() and notnull() are identical - use whichever you prefer
        - isna()/isnull() are more commonly used in modern Pandas code
        - These methods work on Series, DataFrames, and individual values
    """
    print_section_header("DEMONSTRATION: PANDAS MISSING VALUE DETECTION METHODS")
    
    print("Let's explore the different methods Pandas provides for detecting missing values.")
    print("We'll create a sample DataFrame with various types of missing values.\n")
    
    # Create a sample DataFrame with different types of missing values
    import numpy as np
    
    sample_data = {
        'Name': ['Alice', 'Bob', None, 'David', 'Eve'],
        'Age': [25, np.nan, 30, 35, np.nan],
        'City': ['NYC', 'LA', 'Chicago', None, 'Boston'],
        'Salary': [50000, 60000, np.nan, 75000, 80000]
    }
    
    df = pd.DataFrame(sample_data)
    
    print("Sample DataFrame:")
    print("─" * 70)
    print(df)
    print()
    
    # Demonstrate isna()
    print_subsection("Method 1: isna() - Detect Missing Values")
    print("\nThe isna() method returns True where values are missing (NaN, None, pd.NA).")
    print("This is the most commonly used method in modern Pandas code.\n")
    print("df.isna():")
    print(df.isna())
    print()
    
    # Demonstrate isnull()
    print_subsection("Method 2: isnull() - Detect Missing Values")
    print("\nThe isnull() method is IDENTICAL to isna() - they do exactly the same thing.")
    print("Use whichever name you prefer. isna() is more common in recent code.\n")
    print("df.isnull():")
    print(df.isnull())
    print()
    print("Notice: isna() and isnull() produce identical results!")
    print()
    
    # Demonstrate notna()
    print_subsection("Method 3: notna() - Detect NON-Missing Values")
    print("\nThe notna() method returns True where values are NOT missing.")
    print("It's the opposite of isna() - useful when you want to filter for complete data.\n")
    print("df.notna():")
    print(df.notna())
    print()
    
    # Demonstrate notnull()
    print_subsection("Method 4: notnull() - Detect NON-Missing Values")
    print("\nThe notnull() method is IDENTICAL to notna() - they do exactly the same thing.")
    print("Use whichever name you prefer. notna() is more common in recent code.\n")
    print("df.notnull():")
    print(df.notnull())
    print()
    print("Notice: notna() and notnull() produce identical results!")
    print()
    
    # Educational summary
    print_subsection("Key Differences and When to Use Each Method")
    print()
    print("📚 Understanding the Methods:")
    print()
    print("1. isna() vs isnull():")
    print("   • These are IDENTICAL - just different names for the same function")
    print("   • Both return True for missing values (NaN, None, pd.NA)")
    print("   • Recommendation: Use isna() as it's more intuitive and modern")
    print()
    print("2. notna() vs notnull():")
    print("   • These are IDENTICAL - just different names for the same function")
    print("   • Both return True for NON-missing values")
    print("   • Recommendation: Use notna() as it's more intuitive and modern")
    print()
    print("3. When to use isna() vs notna():")
    print("   • Use isna() when you want to FIND or COUNT missing values")
    print("   • Use notna() when you want to FILTER for complete data")
    print()
    print("Common Usage Examples:")
    print("   • Count missing: df.isna().sum()")
    print("   • Filter complete rows: df[df['Age'].notna()]")
    print("   • Check if any missing: df.isna().any()")
    print("   • Check if all present: df.notna().all()")
    print()


def demonstrate_detection_on_dataset(filename):
    """
    Run complete detection workflow on a single dataset.
    
    This function demonstrates the full missing value detection process on a
    real CSV file. It loads the file, generates a comprehensive detection report,
    and includes educational commentary between steps to explain what's happening
    and why each step is important.
    
    Args:
        filename: CSV filename in data/raw directory (e.g., 'books.csv')
    
    Returns:
        None (prints analysis with educational commentary to console)
    
    Examples:
        >>> demonstrate_detection_on_dataset('books.csv')
        
        ══════════════════════════════════════════════════════════════════════
          ANALYZING DATASET: books.csv
        ══════════════════════════════════════════════════════════════════════
        
        Step 1: Loading the CSV file...
        ...
    
    Notes:
        - Demonstrates the complete workflow from loading to interpretation
        - Includes educational commentary explaining each step
        - Uses the generate_detection_report() function for comprehensive analysis
        - Handles errors gracefully if file cannot be loaded
        - Non-destructive - does not modify the original data file
    """
    print_section_header(f"ANALYZING DATASET: {filename}")
    
    print("Let's walk through the complete missing value detection process.")
    print("We'll load the data, analyze it, and interpret the results.\n")
    
    # Step 1: Load the CSV file
    print("Step 1: Loading the CSV file...")
    print("─" * 70)
    df = load_csv_file(filename)
    
    if df is None:
        print("\n⚠ Cannot proceed with analysis - file loading failed.")
        print("Please check the error message above and fix the issue.\n")
        return
    
    print()
    
    # Step 2: Preview the data
    print("Step 2: Previewing the data...")
    print("─" * 70)
    print("First few rows of the dataset:")
    print(df.head())
    print()
    print("💡 Educational Note:")
    print("   Before detecting missing values, it's good practice to preview your data.")
    print("   This helps you understand the structure and spot obvious issues.")
    print()
    
    # Step 3: Run detection analysis
    print("Step 3: Running missing value detection analysis...")
    print("─" * 70)
    print("Now we'll analyze the entire dataset for missing values.")
    print("This includes column-level, row-level, and overall statistics.\n")
    
    # Generate the comprehensive detection report
    generate_detection_report(df, filename)
    
    # Step 4: Educational wrap-up
    print("Step 4: What we learned from this analysis...")
    print("─" * 70)
    print("💡 Key Insights:")
    print("   • We identified exactly where missing values occur (columns and rows)")
    print("   • We calculated percentages to understand the severity")
    print("   • We received recommendations for next steps")
    print("   • The original data remains unchanged (detection only)")
    print()
    print("Remember: Detection is the first step. Next comes decision-making about")
    print("how to handle missing values based on your specific analysis goals.")
    print()


def main():
    """
    Main execution function for the missing values detection demonstration.
    
    This function orchestrates the complete demonstration by:
    1. Printing a welcome header explaining the script's purpose
    2. Demonstrating the different Pandas detection methods
    3. Analyzing the books.csv dataset
    4. Analyzing the employees.csv dataset
    5. Printing key takeaways for learners
    
    The demonstration follows a logical progression from basic concepts
    (detection methods) to practical application (real datasets), providing
    an educational experience for learners.
    
    Returns:
        None (prints complete demonstration to console)
    
    Examples:
        >>> main()
        
        ══════════════════════════════════════════════════════════════════════
          MISSING VALUES DETECTION MILESTONE - PANDAS DEMONSTRATION
        ══════════════════════════════════════════════════════════════════════
        ...
    
    Notes:
        - Designed for educational purposes with clear explanations
        - Demonstrates both theory (methods) and practice (real data)
        - Non-destructive - does not modify any data files
        - Can be run multiple times safely
        - Follows the established pattern from other milestone scripts
    """
    print("\n" + "=" * 70)
    print("  MISSING VALUES DETECTION MILESTONE - PANDAS DEMONSTRATION")
    print("=" * 70)
    print("\nWelcome to the Missing Values Detection demonstration!")
    print()
    print("In this script, you'll learn how to:")
    print("  • Detect missing values using Pandas methods")
    print("  • Analyze missing data patterns at column and row levels")
    print("  • Calculate statistics to assess data quality")
    print("  • Interpret results and plan next steps")
    print()
    print("This is a DETECTION-ONLY tool - we identify missing values without")
    print("modifying the data. Understanding what's missing is the crucial first")
    print("step before making any cleaning decisions.")
    print()
    
    # Part 1: Demonstrate detection methods
    demonstrate_detection_methods()
    
    # Part 2: Analyze books.csv
    demonstrate_detection_on_dataset('books.csv')
    
    # Part 3: Analyze employees.csv
    demonstrate_detection_on_dataset('employees.csv')
    
    # Summary: Key Takeaways
    print_section_header("KEY TAKEAWAYS - WHAT YOU'VE LEARNED")
    print("Congratulations! You've completed the missing values detection demonstration.")
    print("Here are the essential concepts to remember:\n")
    print()
    print("🎯 Core Concepts:")
    print()
    print("1. Detection Methods:")
    print("   ✓ Use isna() or isnull() to identify missing values")
    print("   ✓ Use notna() or notnull() to identify non-missing values")
    print("   ✓ isna() and isnull() are identical (prefer isna())")
    print("   ✓ notna() and notnull() are identical (prefer notna())")
    print()
    print("2. Analysis Levels:")
    print("   ✓ Column-level: Which features have missing data?")
    print("   ✓ Row-level: Which records are incomplete?")
    print("   ✓ Overall: What's the total data quality picture?")
    print()
    print("3. Key Statistics:")
    print("   ✓ Count missing values per column")
    print("   ✓ Calculate percentages to understand severity")
    print("   ✓ Identify patterns (random vs. systematic)")
    print()
    print("4. Best Practices:")
    print("   ✓ ALWAYS detect before cleaning or analysis")
    print("   ✓ Detection is non-destructive - data stays unchanged")
    print("   ✓ Understand WHY values are missing before deciding how to handle them")
    print("   ✓ Document your findings and decisions")
    print()
    print("5. Next Steps After Detection:")
    print("   ✓ Investigate the cause of missing values")
    print("   ✓ Decide on appropriate handling strategy (drop, impute, etc.)")
    print("   ✓ Consider the impact on your specific analysis goals")
    print("   ✓ Be transparent about limitations in your results")
    print()
    print("\n" + "=" * 70)
    print("  End of demonstration. Happy data quality assessment!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
