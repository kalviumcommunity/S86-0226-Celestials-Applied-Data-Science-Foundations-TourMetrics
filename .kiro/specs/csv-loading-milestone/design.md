# Design Document: CSV Loading Milestone

## Overview

The CSV Loading Milestone is an educational system designed to teach beginners how to load and inspect CSV files using Pandas. The system consists of three main deliverables: an interactive Jupyter notebook, a standalone Python script, and comprehensive documentation. All materials use the existing books.csv and employees.csv files in the data/raw/ directory as practical examples.

The design emphasizes simplicity, clarity, and hands-on learning. Each component builds progressively from basic CSV loading to data inspection techniques, with clear explanations and expected outputs to support self-directed learning.

## Architecture

The system follows a layered educational architecture:

```
┌─────────────────────────────────────────┐
│     Learning Materials Layer            │
│  (Notebook, Script, Documentation)      │
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│     Demonstration Layer                 │
│  (Code Examples, Exercises)             │
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│     Pandas API Layer                    │
│  (pd.read_csv, DataFrame methods)       │
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│     Data Layer                          │
│  (books.csv, employees.csv)             │
└─────────────────────────────────────────┘
```

The architecture separates concerns:
- **Learning Materials Layer**: Presents concepts and examples to learners
- **Demonstration Layer**: Provides executable code demonstrating techniques
- **Pandas API Layer**: The actual Pandas library functionality being taught
- **Data Layer**: The CSV files used for practical examples

## Components and Interfaces

### 1. Jupyter Notebook Component

**File**: `notebooks/csv_loading_milestone.ipynb`

**Purpose**: Interactive learning environment with explanations and executable code

**Structure**:
```python
# Cell 1: Introduction (Markdown)
# - Milestone objectives
# - Prerequisites
# - What learners will accomplish

# Cell 2: Import Libraries (Code)
import pandas as pd
import os

# Cell 3: Understanding CSV Files (Markdown)
# - What is a CSV file
# - Why use Pandas for CSV loading

# Cell 4: Loading First CSV (Code)
books_df = pd.read_csv('data/raw/books.csv')

# Cell 5: Inspecting with head() (Code + Markdown)
# - Explanation of head()
# - Code example
# - Expected output

# Cell 6: Inspecting with tail() (Code + Markdown)
# - Explanation of tail()
# - Code example
# - Expected output

# Cell 7: Getting DataFrame Info (Code + Markdown)
# - Explanation of info()
# - Code example
# - Expected output

# Cell 8: Statistical Summary (Code + Markdown)
# - Explanation of describe()
# - Code example
# - Expected output

# Cell 9: Verifying Structure (Code + Markdown)
# - Checking shape
# - Checking columns
# - Checking dtypes

# Cell 10: Loading Second CSV (Code)
employees_df = pd.read_csv('data/raw/employees.csv')

# Cell 11: Practice Exercise (Markdown + Code)
# - Prompt for learner to inspect employees_df
# - Empty code cell for practice

# Cell 12: Common Issues (Markdown)
# - File not found errors
# - Encoding issues
# - Delimiter issues

# Cell 13: Troubleshooting Examples (Code)
# - Examples with error handling
# - Examples with different parameters

# Cell 14: Summary (Markdown)
# - Key takeaways
# - Next steps
```

**Interface**:
- Input: User executes cells sequentially
- Output: Displayed DataFrames, inspection results, and explanatory text

### 2. Python Script Component

**File**: `scripts/csv_loading_demo.py`

**Purpose**: Standalone script demonstrating CSV loading and inspection

**Structure**:
```python
"""
CSV Loading Milestone - Demonstration Script

This script demonstrates how to load and inspect CSV files using Pandas.
It covers basic loading, data inspection methods, and structure verification.
"""

import pandas as pd
import os

def load_and_inspect_csv(filepath, filename):
    """
    Load a CSV file and perform basic inspection.
    
    Args:
        filepath: Path to the CSV file
        filename: Name of the file (for display purposes)
    
    Returns:
        DataFrame: The loaded DataFrame
    """
    # Implementation details
    pass

def demonstrate_inspection_methods(df, dataset_name):
    """
    Demonstrate all inspection methods on a DataFrame.
    
    Args:
        df: DataFrame to inspect
        dataset_name: Name of the dataset (for display purposes)
    """
    # Implementation details
    pass

def demonstrate_structure_verification(df, dataset_name):
    """
    Demonstrate structure verification techniques.
    
    Args:
        df: DataFrame to verify
        dataset_name: Name of the dataset (for display purposes)
    """
    # Implementation details
    pass

def main():
    """Main execution function."""
    # Load and inspect books.csv
    # Load and inspect employees.csv
    # Demonstrate error handling
    pass

if __name__ == "__main__":
    main()
```

**Interface**:
- Input: Executed from command line (`python scripts/csv_loading_demo.py`)
- Output: Printed inspection results to console

### 3. Documentation Component

**File**: `reports/csv_loading_milestone.md`

**Purpose**: Comprehensive reference documentation

**Structure**:
```markdown
# CSV Loading Milestone Documentation

## Learning Objectives
[List of objectives]

## Prerequisites
[Required knowledge]

## Core Concepts

### Loading CSV Files
[Explanation of pd.read_csv()]

### Inspecting Data
[Explanation of inspection methods]

### Verifying Structure
[Explanation of verification techniques]

## Reference Guide

### pd.read_csv() Parameters
[Table of common parameters]

### Inspection Methods
[Table of methods with descriptions]

## Troubleshooting

### Common Issues
[List of issues with solutions]

### Error Messages
[Common errors and how to fix them]

## Practice Exercises
[Additional exercises for learners]

## Next Steps
[Recommendations for continued learning]
```

**Interface**:
- Input: Read by learners as reference material
- Output: Markdown-formatted documentation

## Data Models

### CSV File Specifications

**books.csv**:
- Expected columns: Variable (to be discovered by learner)
- Expected format: Standard CSV with header row
- Location: `data/raw/books.csv`

**employees.csv**:
- Expected columns: Variable (to be discovered by learner)
- Expected format: Standard CSV with header row
- Location: `data/raw/employees.csv`

### DataFrame Representation

```python
# DataFrame structure after loading
DataFrame {
    columns: Index,        # Column names
    index: RangeIndex,     # Row indices
    dtypes: Series,        # Data types per column
    shape: tuple,          # (rows, columns)
    values: ndarray        # Underlying data
}
```

### Inspection Output Models

**head() / tail() Output**:
```python
# Returns DataFrame with n rows (default 5)
DataFrame with shape (n, num_columns)
```

**info() Output**:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: X entries, 0 to X-1
Data columns (total Y columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   col1    X non-null      dtype1
 1   col2    X non-null      dtype2
dtypes: ...
memory usage: ...
```

**describe() Output**:
```python
# Returns DataFrame with statistical summaries
DataFrame with index: ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
Columns: All numeric columns from original DataFrame
```

**shape Output**:
```python
# Returns tuple
(num_rows, num_columns)
```

**columns Output**:
```python
# Returns Index object
Index(['col1', 'col2', 'col3', ...], dtype='object')
```

**dtypes Output**:
```python
# Returns Series
col1    dtype1
col2    dtype2
col3    dtype3
dtype: object
```

## Correctness Properties


A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.

### Property 1: Valid CSV Loading Preserves Structure

*For any* valid CSV file with a header row, loading it with pd.read_csv() should produce a DataFrame where the number of columns matches the number of comma-separated values in the header, and the number of rows matches the number of data lines in the file.

**Validates: Requirements 1.1**

### Property 2: Non-existent File Raises FileNotFoundError

*For any* file path that does not exist in the filesystem, attempting to load it with pd.read_csv() should raise a FileNotFoundError.

**Validates: Requirements 1.4**

### Property 3: Invalid CSV Format Raises Parsing Error

*For any* file containing malformed CSV data (such as inconsistent column counts or invalid delimiters), attempting to load it with pd.read_csv() should raise a parsing error.

**Validates: Requirements 1.5**

### Property 4: head() Returns First N Rows

*For any* DataFrame with at least 5 rows, calling head() without arguments should return a DataFrame containing exactly the first 5 rows in order.

**Validates: Requirements 2.1**

### Property 5: tail() Returns Last N Rows

*For any* DataFrame with at least 5 rows, calling tail() without arguments should return a DataFrame containing exactly the last 5 rows in order.

**Validates: Requirements 2.2**

### Property 6: info() Contains Required Information

*For any* DataFrame, calling info() should produce output that includes all column names, the data type of each column, the count of non-null values per column, and memory usage information.

**Validates: Requirements 2.3**

### Property 7: describe() Summarizes Numeric Columns

*For any* DataFrame containing numeric columns, calling describe() should return a DataFrame with statistical summaries (count, mean, std, min, 25%, 50%, 75%, max) for each numeric column.

**Validates: Requirements 2.4**

### Property 8: shape Returns Correct Dimensions

*For any* DataFrame, the shape attribute should return a tuple (rows, columns) where rows equals the number of data rows and columns equals the number of columns.

**Validates: Requirements 2.5**

### Property 9: columns Returns Column Names in Order

*For any* DataFrame, the columns attribute should return an Index containing all column names in the same order they appear in the DataFrame.

**Validates: Requirements 3.1**

### Property 10: len() Returns Row Count

*For any* DataFrame, calling len() should return an integer equal to the number of rows in the DataFrame.

**Validates: Requirements 3.2**

### Property 11: dtypes Returns Column Data Types

*For any* DataFrame, the dtypes attribute should return a Series where each entry maps a column name to its data type, covering all columns in the DataFrame.

**Validates: Requirements 3.3**

## Error Handling

### File Loading Errors

**FileNotFoundError**:
- Raised when the specified CSV file path does not exist
- Error message should include the attempted file path
- Educational materials should demonstrate this error and explain how to verify file paths

**ParserError**:
- Raised when CSV file has malformed structure
- Error message should indicate the line number where parsing failed
- Educational materials should demonstrate common causes (inconsistent columns, wrong delimiter)

**UnicodeDecodeError**:
- Raised when file encoding doesn't match the default (UTF-8)
- Educational materials should demonstrate using the `encoding` parameter
- Common encodings to document: 'utf-8', 'latin-1', 'cp1252'

### Handling Errors in Educational Materials

The notebook and script should include examples of:

1. **Try-except blocks** for graceful error handling:
```python
try:
    df = pd.read_csv('data/raw/nonexistent.csv')
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
```

2. **Checking file existence** before loading:
```python
import os
if os.path.exists('data/raw/books.csv'):
    df = pd.read_csv('data/raw/books.csv')
else:
    print("File does not exist")
```

3. **Handling encoding issues**:
```python
try:
    df = pd.read_csv('data/raw/file.csv')
except UnicodeDecodeError:
    df = pd.read_csv('data/raw/file.csv', encoding='latin-1')
```

### Edge Cases

**Empty CSV Files**:
- File with only headers: Should create DataFrame with 0 rows
- Completely empty file: Should raise EmptyDataError
- Educational materials should demonstrate both cases

**DataFrames with Fewer Than 5 Rows**:
- head() and tail() should return all available rows
- No error should be raised
- Educational materials should demonstrate this behavior

**DataFrames with No Numeric Columns**:
- describe() should return an empty DataFrame or only count statistics
- No error should be raised
- Educational materials should explain this behavior

## Testing Strategy

### Dual Testing Approach

This feature requires both unit tests and property-based tests to ensure comprehensive coverage:

**Unit Tests**: Focus on specific examples and edge cases
- Test loading books.csv and employees.csv specifically
- Test specific error messages for known malformed files
- Test notebook and script file existence
- Test documentation structure and required sections

**Property-Based Tests**: Verify universal properties across all inputs
- Test CSV loading with randomly generated valid CSV content
- Test inspection methods with randomly generated DataFrames
- Test error handling with randomly generated invalid inputs
- Run minimum 100 iterations per property test

### Property-Based Testing Configuration

We will use **Hypothesis** (Python's property-based testing library) for implementing property tests.

**Configuration**:
- Minimum 100 iterations per property test
- Each test tagged with: **Feature: csv-loading-milestone, Property {number}: {property_text}**
- Use Hypothesis strategies for generating:
  - Random CSV content with valid structure
  - Random DataFrames with various shapes and dtypes
  - Random invalid file paths
  - Random malformed CSV content

**Example Property Test Structure**:
```python
from hypothesis import given, strategies as st
import pandas as pd
import tempfile
import os

# Feature: csv-loading-milestone, Property 1: Valid CSV Loading Preserves Structure
@given(st.lists(st.lists(st.text(), min_size=3, max_size=3), min_size=2, max_size=10))
def test_csv_loading_preserves_structure(rows):
    # Generate CSV content
    # Write to temporary file
    # Load with pd.read_csv()
    # Verify structure matches
    pass
```

### Unit Testing Strategy

**Test Categories**:

1. **File Loading Tests**:
   - Test loading books.csv successfully
   - Test loading employees.csv successfully
   - Test FileNotFoundError with specific non-existent path
   - Test ParserError with specific malformed CSV

2. **Inspection Method Tests**:
   - Test head() on DataFrame with known content
   - Test tail() on DataFrame with known content
   - Test info() output format
   - Test describe() output format
   - Test shape, columns, dtypes on known DataFrame

3. **Educational Material Tests**:
   - Test notebook file exists at correct path
   - Test script file exists at correct path
   - Test documentation file exists at correct path
   - Test script executes without errors
   - Test notebook contains required cells

4. **Edge Case Tests**:
   - Test head() on DataFrame with < 5 rows
   - Test tail() on DataFrame with < 5 rows
   - Test describe() on DataFrame with no numeric columns
   - Test loading empty CSV file

### Integration Testing

**End-to-End Workflow Tests**:
1. Execute the Python script and verify it completes without errors
2. Verify the script produces expected console output
3. Verify all code examples in documentation are syntactically correct
4. Verify notebook cells can be executed in sequence without errors

### Test Organization

```
tests/
├── unit/
│   ├── test_csv_loading.py          # Unit tests for CSV loading
│   ├── test_inspection_methods.py   # Unit tests for inspection methods
│   └── test_educational_materials.py # Unit tests for file existence
├── property/
│   ├── test_csv_loading_properties.py      # Properties 1-3
│   ├── test_inspection_properties.py       # Properties 4-11
│   └── conftest.py                         # Hypothesis configuration
└── integration/
    └── test_end_to_end.py           # Integration tests
```

### Test Execution

**Running Unit Tests**:
```bash
pytest tests/unit/ -v
```

**Running Property Tests**:
```bash
pytest tests/property/ -v --hypothesis-show-statistics
```

**Running All Tests**:
```bash
pytest tests/ -v
```

### Success Criteria

All tests must pass before the milestone is considered complete:
- All unit tests pass (100% pass rate)
- All property tests pass with minimum 100 iterations each
- Integration tests verify end-to-end workflows
- Script executes without errors
- Notebook cells execute in sequence without errors
