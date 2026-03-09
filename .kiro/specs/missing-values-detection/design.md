# Design Document: Missing Values Detection

## Overview

The Missing Values Detection system is an educational tool built on Pandas that helps learners identify and understand missing data patterns in DataFrames. The system follows a detection-only philosophy, ensuring that learners can thoroughly analyze their data before making any cleaning decisions.

The system consists of three main components:
1. **CSV Loader** - Handles loading CSV files from the data/raw directory with proper error handling
2. **Missing Value Analyzer** - Detects and counts missing values at both column and row levels
3. **Report Generator** - Creates clear, educational summaries with interpretations

The design emphasizes educational clarity, following the established patterns from existing milestone scripts (csv_loading_demo.py and dataframe_inspection_demo.py) to maintain consistency with the learner's experience.

## Architecture

The system follows a functional programming approach with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Main Demonstration Script                 │
│                  (missing_values_detection.py)               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         CSV Loading Functions           │
        │  - load_csv_file()                      │
        │  - validate_file_path()                 │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │    Missing Value Detection Functions    │
        │  - detect_missing_values()              │
        │  - count_missing_per_column()           │
        │  - identify_rows_with_missing()         │
        │  - calculate_missing_percentages()      │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │      Report Generation Functions        │
        │  - generate_detection_report()          │
        │  - format_column_summary()              │
        │  - format_row_summary()                 │
        │  - print_interpretation()               │
        └─────────────────────────────────────────┘
```

The architecture is intentionally flat and functional to match the educational context and existing codebase patterns.

## Components and Interfaces

### 1. CSV Loading Module

**Purpose**: Load CSV files from the data/raw directory with comprehensive error handling.

**Functions**:

```python
def load_csv_file(filename: str) -> pd.DataFrame | None:
    """
    Load a CSV file from the data/raw directory.
    
    Args:
        filename: Name of the CSV file (e.g., 'books.csv')
    
    Returns:
        DataFrame if successful, None if loading fails
    
    Raises:
        No exceptions - all errors are caught and reported
    """
```

```python
def validate_file_path(filepath: str) -> bool:
    """
    Check if a file exists at the specified path.
    
    Args:
        filepath: Full path to the file
    
    Returns:
        True if file exists, False otherwise
    """
```

**Error Handling**:
- FileNotFoundError: Report missing file with helpful message
- pd.errors.ParserError: Report CSV parsing issues
- UnicodeDecodeError: Suggest encoding alternatives
- Generic Exception: Catch-all for unexpected errors

### 2. Missing Value Detection Module

**Purpose**: Detect and analyze missing values using Pandas methods.

**Functions**:

```python
def detect_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a boolean DataFrame indicating missing values.
    
    Args:
        df: Input DataFrame
    
    Returns:
        Boolean DataFrame where True indicates missing value
    
    Implementation:
        Uses pd.isna() to detect NaN, None, and pd.NA
    """
```

```python
def count_missing_per_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count missing values for each column.
    
    Args:
        df: Input DataFrame
    
    Returns:
        DataFrame with columns: ['Column', 'Missing_Count', 'Missing_Percent']
        Sorted by Missing_Count descending
    """
```

```python
def identify_rows_with_missing(df: pd.DataFrame) -> tuple[pd.DataFrame, list[int]]:
    """
    Identify rows containing at least one missing value.
    
    Args:
        df: Input DataFrame
    
    Returns:
        Tuple of (rows_with_missing, list_of_indices)
    """
```

```python
def calculate_missing_percentages(df: pd.DataFrame) -> dict:
    """
    Calculate overall missing value statistics.
    
    Args:
        df: Input DataFrame
    
    Returns:
        Dictionary with keys:
        - 'total_cells': Total number of cells
        - 'missing_cells': Number of missing cells
        - 'missing_percent': Percentage of missing cells
        - 'rows_with_missing': Number of rows with missing values
        - 'rows_with_missing_percent': Percentage of rows with missing
    """
```

### 3. Report Generation Module

**Purpose**: Create clear, educational summaries of missing value analysis.

**Functions**:

```python
def generate_detection_report(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Generate and print a comprehensive missing value detection report.
    
    Args:
        df: DataFrame to analyze
        dataset_name: Name for display purposes
    
    Output:
        Prints formatted report to console including:
        - Overall statistics
        - Column-level analysis
        - Row-level analysis
        - Interpretation and recommendations
    """
```

```python
def format_column_summary(column_stats: pd.DataFrame) -> str:
    """
    Format column-level missing value statistics.
    
    Args:
        column_stats: DataFrame from count_missing_per_column()
    
    Returns:
        Formatted string for display
    """
```

```python
def format_row_summary(rows_with_missing: pd.DataFrame, indices: list[int]) -> str:
    """
    Format row-level missing value information.
    
    Args:
        rows_with_missing: DataFrame containing rows with missing values
        indices: List of row indices
    
    Returns:
        Formatted string for display
    """
```

```python
def print_interpretation(stats: dict, dataset_name: str) -> None:
    """
    Print educational interpretation of missing value patterns.
    
    Args:
        stats: Dictionary from calculate_missing_percentages()
        dataset_name: Name of the dataset
    
    Output:
        Prints interpretation text explaining what the statistics mean
        and what decisions might be appropriate
    """
```

### 4. Demonstration Module

**Purpose**: Provide educational demonstration of missing value detection.

**Functions**:

```python
def demonstrate_detection_on_dataset(filename: str) -> None:
    """
    Run complete detection workflow on a single dataset.
    
    Args:
        filename: CSV filename in data/raw directory
    
    Output:
        Prints complete analysis with educational commentary
    """
```

```python
def demonstrate_detection_methods() -> None:
    """
    Demonstrate different Pandas methods for detecting missing values.
    
    Output:
        Shows isna(), isnull(), notna(), and notnull() with examples
    """
```

```python
def print_section_header(title: str) -> None:
    """
    Print formatted section header for readability.
    
    Args:
        title: Section title
    """
```

## Data Models

### MissingValueStats

A dictionary structure containing overall missing value statistics:

```python
{
    'total_cells': int,              # Total number of cells in DataFrame
    'missing_cells': int,            # Number of cells with missing values
    'missing_percent': float,        # Percentage of cells that are missing
    'rows_with_missing': int,        # Number of rows containing missing values
    'rows_with_missing_percent': float,  # Percentage of rows with missing
    'total_rows': int,               # Total number of rows
    'total_columns': int             # Total number of columns
}
```

### ColumnMissingStats

A DataFrame structure for column-level statistics:

```python
pd.DataFrame({
    'Column': str,           # Column name
    'Missing_Count': int,    # Number of missing values
    'Missing_Percent': float # Percentage of values that are missing
})
```

Sorted by `Missing_Count` in descending order.

### DetectionReport

The complete report structure (conceptual, not a class):

```
Detection Report
├── Dataset Information
│   ├── Name
│   ├── Shape (rows × columns)
│   └── Total cells
├── Overall Statistics
│   ├── Total missing cells
│   ├── Percentage missing
│   ├── Rows with missing values
│   └── Percentage of rows affected
├── Column-Level Analysis
│   └── Table of columns with missing counts and percentages
├── Row-Level Analysis
│   ├── Indices of affected rows
│   └── Sample of rows with missing values
└── Interpretation
    ├── Data quality assessment
    ├── Patterns identified
    └── Recommendations for next steps
```


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: CSV Loading Preserves Data Integrity

*For any* valid CSV file with missing values, loading the file into a DataFrame should preserve all data including missing values represented as NaN.

**Validates: Requirements 1.1, 1.5**

### Property 2: Path Construction Correctness

*For any* valid filename, constructing the file path for the data/raw directory should produce a path that correctly combines the directory and filename.

**Validates: Requirements 1.2**

### Property 3: Missing Value Type Recognition

*For any* DataFrame containing NaN, None, or pd.NA values, the detection system should recognize all three types as missing values.

**Validates: Requirements 2.2**

### Property 4: Comprehensive Missing Value Detection

*For any* DataFrame, the detection system should identify missing values in all columns and all rows, with the total count equal to the sum of missing values across all positions.

**Validates: Requirements 2.3, 2.4, 3.1**

### Property 5: Column Statistics Accuracy

*For any* DataFrame, the column-level statistics should include column names, accurate missing counts, accurate percentages, and be sorted by missing count in descending order.

**Validates: Requirements 3.2, 3.3, 3.5**

### Property 6: Row Identification Correctness

*For any* DataFrame, all identified rows with missing values should actually contain at least one missing value, and the count should equal the number of unique row indices returned.

**Validates: Requirements 4.1, 4.2, 4.3**

### Property 7: Complete Row Data Display

*For any* DataFrame, when displaying rows with missing values, the output should include all columns from the original DataFrame for each identified row.

**Validates: Requirements 4.4**

### Property 8: Row Percentage Calculation

*For any* DataFrame, the percentage of rows with missing values should equal (rows_with_missing / total_rows) * 100.

**Validates: Requirements 4.5**

### Property 9: Report Completeness and Accuracy

*For any* DataFrame, the detection report should contain total missing cells, percentage of missing cells, rows with missing values, and all percentages should be mathematically correct.

**Validates: Requirements 5.1, 5.2, 5.3**

### Property 10: DataFrame Immutability During Detection

*For any* DataFrame, running detection operations should leave the DataFrame completely unchanged - same shape, same values, same missing value count, and same data types.

**Validates: Requirements 7.1, 7.2, 7.3, 7.4**

## Error Handling

The system implements comprehensive error handling following these principles:

### File Loading Errors

**FileNotFoundError**:
- Catch when CSV file doesn't exist
- Return None from load function
- Print clear message: "✗ Error: File not found at {filepath}"
- Suggest: "Tip: Check that the file path is correct and the file exists"

**pd.errors.ParserError**:
- Catch when CSV is malformed
- Return None from load function
- Print clear message: "✗ Error: Failed to parse CSV file"
- Suggest: "Tip: Check for inconsistent columns or wrong delimiter"

**UnicodeDecodeError**:
- Catch when encoding issues occur
- Return None from load function
- Print clear message: "✗ Error: Encoding issue detected"
- Suggest: "Tip: Try specifying encoding parameter, e.g., encoding='latin-1'"

**Generic Exception**:
- Catch any unexpected errors
- Return None from load function
- Print error details for debugging

### Detection Errors

**Empty DataFrame**:
- Check if DataFrame is empty before detection
- Return appropriate zero-value statistics
- Print message: "Note: DataFrame is empty, no missing values to detect"

**Invalid Input Type**:
- Validate that input is a pandas DataFrame
- Raise TypeError with clear message if not
- Message: "Input must be a pandas DataFrame"

### Error Handling Strategy

1. **Fail Gracefully**: Never crash, always return sensible defaults
2. **Informative Messages**: Tell users what went wrong and how to fix it
3. **Educational Tone**: Use errors as teaching moments
4. **Consistent Format**: All error messages follow the same pattern (✗ Error: ... / Tip: ...)

## Testing Strategy

The testing strategy employs both unit tests and property-based tests to ensure comprehensive coverage and correctness.

### Property-Based Testing

Property-based tests verify universal properties across many generated inputs using the Hypothesis library for Python. Each property test should run a minimum of 100 iterations to ensure thorough coverage.

**Property Test Configuration**:
```python
from hypothesis import given, settings
import hypothesis.strategies as st

@settings(max_examples=100)
@given(...)
def test_property_name(...):
    # Feature: missing-values-detection, Property N: [property text]
    ...
```

**Property Tests to Implement**:

1. **CSV Loading Preserves Data** (Property 1)
   - Generate random DataFrames with missing values
   - Save to CSV, load back, verify equality
   - Tag: Feature: missing-values-detection, Property 1: CSV loading preserves data integrity

2. **Path Construction** (Property 2)
   - Generate random valid filenames
   - Verify constructed path format
   - Tag: Feature: missing-values-detection, Property 2: Path construction correctness

3. **Missing Type Recognition** (Property 3)
   - Generate DataFrames with NaN, None, pd.NA
   - Verify all are detected
   - Tag: Feature: missing-values-detection, Property 3: Missing value type recognition

4. **Comprehensive Detection** (Property 4)
   - Generate random DataFrames with missing values
   - Verify total count equals sum across all positions
   - Tag: Feature: missing-values-detection, Property 4: Comprehensive missing value detection

5. **Column Statistics** (Property 5)
   - Generate random DataFrames
   - Verify statistics accuracy and sorting
   - Tag: Feature: missing-values-detection, Property 5: Column statistics accuracy

6. **Row Identification** (Property 6)
   - Generate random DataFrames
   - Verify all identified rows have missing values
   - Tag: Feature: missing-values-detection, Property 6: Row identification correctness

7. **Complete Row Display** (Property 7)
   - Generate random DataFrames
   - Verify displayed rows have all columns
   - Tag: Feature: missing-values-detection, Property 7: Complete row data display

8. **Percentage Calculations** (Property 8)
   - Generate random DataFrames
   - Verify percentage formula correctness
   - Tag: Feature: missing-values-detection, Property 8: Row percentage calculation

9. **Report Accuracy** (Property 9)
   - Generate random DataFrames
   - Verify all report statistics are correct
   - Tag: Feature: missing-values-detection, Property 9: Report completeness and accuracy

10. **DataFrame Immutability** (Property 10)
    - Generate random DataFrames
    - Run detection, verify DataFrame unchanged
    - Tag: Feature: missing-values-detection, Property 10: DataFrame immutability during detection

### Unit Testing

Unit tests verify specific examples, edge cases, and integration points. They complement property tests by testing concrete scenarios.

**Unit Tests to Implement**:

1. **Edge Case: Non-existent File**
   - Test loading a file that doesn't exist
   - Verify None is returned and error message is printed
   - Validates: Requirements 1.3

2. **Edge Case: Malformed CSV**
   - Test loading a malformed CSV file
   - Verify error handling works correctly
   - Validates: Requirements 1.4

3. **Edge Case: DataFrame with No Missing Values**
   - Test detection on DataFrame with no missing values
   - Verify zero counts are reported correctly
   - Validates: Requirements 2.5

4. **Edge Case: Column with No Missing Values**
   - Test column statistics when some columns have no missing values
   - Verify zero is displayed correctly
   - Validates: Requirements 3.4

5. **Example: Demonstration Script Runs**
   - Test that the demonstration script executes without errors
   - Validates: Requirements 6.1

6. **Example: Demo Uses Correct Files**
   - Test that demo analyzes books.csv and employees.csv
   - Validates: Requirements 6.2

7. **Example: Code Has Comments**
   - Verify that demonstration code includes explanatory comments
   - Validates: Requirements 6.4

8. **Example: Interpretation Text Exists**
   - Test that interpretation function produces output
   - Validates: Requirements 5.4

9. **Example: Documentation Exists**
   - Verify documentation files exist and contain required topics
   - Validates: Requirements 8.1, 8.2, 8.3

10. **Integration: Complete Workflow**
    - Test full workflow: load CSV → detect → generate report
    - Verify all components work together correctly

### Testing Best Practices

1. **Balance**: Use property tests for universal correctness, unit tests for specific scenarios
2. **Coverage**: Aim for 100% code coverage, but focus on meaningful tests
3. **Clarity**: Each test should have a clear purpose and descriptive name
4. **Independence**: Tests should not depend on each other
5. **Speed**: Keep tests fast to encourage frequent running
6. **Documentation**: Tag all property tests with their corresponding design property

### Test Data

Use the existing CSV files for integration testing:
- `data/raw/books.csv` - Clean data with no missing values
- `data/raw/employees.csv` - Clean data with no missing values

For testing missing value detection, create synthetic test data with known missing patterns:
- DataFrames with specific missing value counts
- DataFrames with different missing value types (NaN, None, pd.NA)
- DataFrames with missing values in specific patterns (entire columns, scattered, etc.)

The Hypothesis library will generate random test cases for property-based tests, ensuring coverage of edge cases we might not think of manually.
