# CSV Loading Milestone Documentation

## Table of Contents
1. [Learning Objectives](#learning-objectives)
2. [Prerequisites](#prerequisites)
3. [Core Concepts](#core-concepts)
4. [Reference Guide](#reference-guide)
5. [Troubleshooting](#troubleshooting)
6. [Practice Exercises](#practice-exercises)
7. [Next Steps](#next-steps)

---

## Learning Objectives

This milestone teaches you the essential skills for loading and inspecting CSV files with Pandas. By completing this milestone, you will:

- **Understand** what CSV files are and how they represent tabular data
- **Load** CSV files into Pandas DataFrames using `pd.read_csv()`
- **Inspect** loaded data using head(), tail(), info(), and describe()
- **Verify** data structure using shape, columns, dtypes, and len()
- **Identify** common CSV loading issues and their solutions
- **Prepare** data safely for further analysis

### Why This Matters

CSV loading is the foundation of data analysis. Most data science workflows begin with loading external data, and errors at this stage cascade through your entire analysis. This milestone ensures you:

- Load data correctly the first time
- Catch errors early before they affect analysis
- Understand your data structure before processing
- Build confidence in your data pipeline

---

## Prerequisites

### Required Knowledge
- Basic Python syntax (variables, functions, imports)
- Understanding of tabular data (rows and columns)
- Familiarity with file paths

### Required Software
- Python 3.7 or higher
- Pandas library: `pip install pandas`
- Jupyter Notebook (optional but recommended): `pip install jupyter`

### Required Files
This milestone uses two CSV files in the `data/raw/` directory:
- `books.csv` - Classic books with Title, Author, Year, Pages
- `employees.csv` - Employee data with Name, Department, Salary, Years

---

## Core Concepts

### What is a CSV File?

**CSV** stands for **Comma-Separated Values**. It's a plain text format for storing tabular data:

```
Title,Author,Year,Pages
1984,George Orwell,1949,328
To Kill a Mockingbird,Harper Lee,1960,281
```

**Key characteristics:**
- Each line is a row
- Values are separated by commas (the delimiter)
- First row typically contains column headers
- Simple, universal format readable by any text editor
- Equivalent to a spreadsheet saved as text

### Why Use Pandas?

Pandas provides powerful tools for working with CSV files:

1. **Simple loading:** One function (`pd.read_csv()`) handles most cases
2. **Automatic type detection:** Recognizes numbers, strings, dates
3. **Intelligent parsing:** Handles headers, missing values, quotes
4. **Rich inspection tools:** Built-in methods to explore data
5. **Industry standard:** Used by data scientists worldwide

### The DataFrame Object

When you load a CSV, Pandas creates a **DataFrame**:

```python
df = pd.read_csv('file.csv')
```

A DataFrame is a 2D labeled data structure with:
- **Rows:** Indexed by numbers (0, 1, 2, ...) or custom labels
- **Columns:** Named based on CSV headers
- **Data types:** Each column has a type (int, float, string, etc.)
- **Methods:** Built-in functions for inspection and manipulation

---

## Reference Guide

### pd.read_csv() Parameters

The `pd.read_csv()` function has many parameters. Here are the most important:

| Parameter | Type | Default | Description | Example |
|-----------|------|---------|-------------|---------|
| `filepath_or_buffer` | str | Required | Path to CSV file | `'data/file.csv'` |
| `sep` | str | `','` | Delimiter character | `sep=';'` for semicolons |
| `header` | int or None | `0` | Row number for column names | `header=None` if no header |
| `names` | list | None | Custom column names | `names=['A', 'B', 'C']` |
| `index_col` | int or str | None | Column to use as row index | `index_col=0` |
| `usecols` | list | None | Columns to load | `usecols=['Name', 'Age']` |
| `dtype` | dict | None | Data types for columns | `dtype={'Age': int}` |
| `encoding` | str | `'utf-8'` | File encoding | `encoding='latin-1'` |
| `nrows` | int | None | Number of rows to read | `nrows=100` |
| `skiprows` | int or list | None | Rows to skip | `skiprows=2` |

**Basic usage:**
```python
# Simple load
df = pd.read_csv('data/file.csv')

# With parameters
df = pd.read_csv('data/file.csv', 
                 sep=';',
                 encoding='latin-1',
                 usecols=['Name', 'Age'])
```

### Inspection Methods

After loading, always inspect your data. Here are the essential methods:

#### 1. head(n=5)
**Purpose:** Display the first n rows  
**Returns:** DataFrame with first n rows  
**Use when:** You want a quick preview of the data

```python
df.head()      # First 5 rows (default)
df.head(10)    # First 10 rows
```

**Example output:**
```
                   Title               Author  Year  Pages
0                   1984        George Orwell  1949    328
1  To Kill a Mockingbird           Harper Lee  1960    281
```

---

#### 2. tail(n=5)
**Purpose:** Display the last n rows  
**Returns:** DataFrame with last n rows  
**Use when:** You want to verify the file loaded completely

```python
df.tail()      # Last 5 rows (default)
df.tail(3)     # Last 3 rows
```

---

#### 3. info()
**Purpose:** Display DataFrame structure and metadata  
**Returns:** None (prints to console)  
**Use when:** You need to understand data types and missing values

```python
df.info()
```

**Example output:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Title   4 non-null      str
 1   Author  4 non-null      str
 2   Year    4 non-null      int64
 3   Pages   4 non-null      int64
dtypes: int64(2), str(2)
memory usage: 260.0 bytes
```

**What to check:**
- Number of entries (rows)
- Column names
- Non-null counts (missing values)
- Data types (Dtype)

---

#### 4. describe()
**Purpose:** Generate statistical summary of numeric columns  
**Returns:** DataFrame with statistics  
**Use when:** You want to understand numeric data distribution

```python
df.describe()
```

**Example output:**
```
              Year       Pages
count     4.000000    4.000000
mean   1911.750000  305.250000
std      67.435772  104.656183
min    1813.000000  180.000000
25%    1897.000000  255.750000
50%    1937.000000  304.500000
75%    1951.750000  354.000000
max    1960.000000  432.000000
```

**Statistics explained:**
- **count:** Number of non-null values
- **mean:** Average value
- **std:** Standard deviation (spread)
- **min/max:** Minimum and maximum values
- **25%/50%/75%:** Quartiles (percentiles)

---

### Structure Verification Attributes

#### 1. shape
**Purpose:** Get dimensions (rows, columns)  
**Returns:** Tuple (rows, columns)  
**Use when:** You need to verify the size of your data

```python
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")
```

**Example:**
```python
>>> df.shape
(4, 4)  # 4 rows, 4 columns
```

---

#### 2. columns
**Purpose:** Get column names  
**Returns:** Index object with column names  
**Use when:** You need to verify or list column names

```python
print(df.columns)
print(list(df.columns))  # Convert to list
```

**Example:**
```python
>>> df.columns
Index(['Title', 'Author', 'Year', 'Pages'], dtype='object')

>>> list(df.columns)
['Title', 'Author', 'Year', 'Pages']
```

---

#### 3. dtypes
**Purpose:** Get data type of each column  
**Returns:** Series mapping column names to types  
**Use when:** You need to verify data types are correct

```python
print(df.dtypes)
```

**Example:**
```python
>>> df.dtypes
Title       str
Author      str
Year      int64
Pages     int64
dtype: object
```

**Common data types:**
- `int64`: Integer numbers
- `float64`: Decimal numbers
- `str` or `object`: Text strings
- `bool`: True/False values
- `datetime64`: Dates and times

---

#### 4. len()
**Purpose:** Get number of rows  
**Returns:** Integer row count  
**Use when:** You need just the row count

```python
num_rows = len(df)
```

**Example:**
```python
>>> len(df)
4
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: FileNotFoundError

**Error message:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/file.csv'
```

**Cause:** The file path is incorrect or the file doesn't exist.

**Solutions:**

1. **Check the file path:**
```python
import os
filepath = 'data/raw/books.csv'
print(f"File exists: {os.path.exists(filepath)}")
```

2. **Use absolute paths:**
```python
import os
filepath = os.path.abspath('data/raw/books.csv')
df = pd.read_csv(filepath)
```

3. **Check current directory:**
```python
import os
print(f"Current directory: {os.getcwd()}")
```

4. **Handle gracefully:**
```python
try:
    df = pd.read_csv('data/file.csv')
except FileNotFoundError:
    print("Error: File not found. Check the path.")
```

---

#### Issue 2: UnicodeDecodeError

**Error message:**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x... in position ...
```

**Cause:** File uses a different character encoding than UTF-8.

**Solutions:**

1. **Try Latin-1 encoding:**
```python
df = pd.read_csv('file.csv', encoding='latin-1')
```

2. **Try Windows encoding:**
```python
df = pd.read_csv('file.csv', encoding='cp1252')
```

3. **Try ISO encoding:**
```python
df = pd.read_csv('file.csv', encoding='iso-8859-1')
```

4. **Detect encoding automatically:**
```python
import chardet

with open('file.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

df = pd.read_csv('file.csv', encoding=encoding)
```

---

#### Issue 3: ParserError

**Error message:**
```
ParserError: Error tokenizing data. C error: Expected 4 fields in line 5, saw 6
```

**Cause:** Inconsistent number of columns, or wrong delimiter.

**Solutions:**

1. **Check delimiter:**
```python
# For semicolon-separated
df = pd.read_csv('file.csv', sep=';')

# For tab-separated
df = pd.read_csv('file.tsv', sep='\t')

# For pipe-separated
df = pd.read_csv('file.txt', sep='|')
```

2. **Handle bad lines:**
```python
df = pd.read_csv('file.csv', on_bad_lines='skip')
```

3. **Inspect the file manually:**
```python
with open('file.csv', 'r') as f:
    for i, line in enumerate(f):
        if i < 10:  # First 10 lines
            print(f"Line {i}: {line}")
```

---

#### Issue 4: Wrong Data Types

**Problem:** Numeric columns loaded as strings (object type).

**Example:**
```python
>>> df.dtypes
Price    object  # Should be float!
```

**Cause:** Non-numeric characters in the column (e.g., "$1,234").

**Solutions:**

1. **Specify data types:**
```python
df = pd.read_csv('file.csv', dtype={'Price': float})
```

2. **Convert after loading:**
```python
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
```

3. **Clean and convert:**
```python
df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '')
df['Price'] = df['Price'].astype(float)
```

---

#### Issue 5: Missing Header Row

**Problem:** First row contains data, not column names.

**Solution:**

1. **Specify no header:**
```python
df = pd.read_csv('file.csv', header=None)
```

2. **Provide custom column names:**
```python
df = pd.read_csv('file.csv', 
                 header=None,
                 names=['Name', 'Age', 'City'])
```

3. **Header on different row:**
```python
# If header is on row 2 (0-indexed)
df = pd.read_csv('file.csv', header=2)
```

---

#### Issue 6: Extra Whitespace

**Problem:** Column names or values have leading/trailing spaces.

**Example:**
```python
>>> df.columns
Index([' Name', 'Age ', ' City '], dtype='object')
```

**Solutions:**

1. **Strip whitespace from column names:**
```python
df.columns = df.columns.str.strip()
```

2. **Strip whitespace from all string columns:**
```python
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
```

3. **Handle during loading:**
```python
df = pd.read_csv('file.csv', skipinitialspace=True)
```

---

## Practice Exercises

### Exercise 1: Basic Loading
Load the `books.csv` file and answer these questions:
1. How many rows and columns does it have?
2. What are the column names?
3. What data types are the columns?
4. What is the average number of pages?

**Solution:**
```python
import pandas as pd

df = pd.read_csv('data/raw/books.csv')
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}")
print(f"Average pages: {df['Pages'].mean()}")
```

---

### Exercise 2: Inspection Practice
Load the `employees.csv` file and:
1. Display the first 3 rows
2. Display the last 2 rows
3. Show the DataFrame info
4. Get statistical summary

**Solution:**
```python
df = pd.read_csv('data/raw/employees.csv')
print(df.head(3))
print(df.tail(2))
df.info()
print(df.describe())
```

---

### Exercise 3: Error Handling
Write code that:
1. Checks if a file exists before loading
2. Handles FileNotFoundError gracefully
3. Prints a helpful error message

**Solution:**
```python
import os
import pandas as pd

def safe_load_csv(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None
    
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Successfully loaded {filepath}")
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

df = safe_load_csv('data/raw/books.csv')
```

---

### Exercise 4: Structure Verification
Create a function that verifies a DataFrame has:
- Expected number of rows
- Expected column names
- Expected data types

**Solution:**
```python
def verify_dataframe(df, expected_rows, expected_cols, expected_dtypes):
    """Verify DataFrame structure matches expectations."""
    
    # Check row count
    if len(df) != expected_rows:
        print(f"✗ Row count mismatch: expected {expected_rows}, got {len(df)}")
        return False
    
    # Check column names
    if list(df.columns) != expected_cols:
        print(f"✗ Column mismatch: expected {expected_cols}, got {list(df.columns)}")
        return False
    
    # Check data types
    for col, dtype in expected_dtypes.items():
        if df[col].dtype != dtype:
            print(f"✗ Type mismatch in {col}: expected {dtype}, got {df[col].dtype}")
            return False
    
    print("✓ DataFrame structure verified!")
    return True

# Example usage
df = pd.read_csv('data/raw/books.csv')
verify_dataframe(df, 
                 expected_rows=4,
                 expected_cols=['Title', 'Author', 'Year', 'Pages'],
                 expected_dtypes={'Year': 'int64', 'Pages': 'int64'})
```

---

## Next Steps

### Immediate Next Steps
Now that you can load and inspect CSV files, you're ready to:

1. **Data Cleaning**
   - Handle missing values
   - Remove duplicates
   - Fix data type issues
   - Clean string data

2. **Data Transformation**
   - Filter rows based on conditions
   - Select specific columns
   - Create new calculated columns
   - Sort and group data

3. **Data Analysis**
   - Calculate statistics
   - Find patterns and trends
   - Answer business questions
   - Generate insights

### Recommended Learning Path

**Week 1-2: Data Cleaning**
- Handling missing values with `fillna()` and `dropna()`
- Removing duplicates with `drop_duplicates()`
- Data type conversions
- String manipulation

**Week 3-4: Data Selection and Filtering**
- Boolean indexing
- `loc[]` and `iloc[]` for selection
- Filtering with conditions
- Selecting columns

**Week 5-6: Data Transformation**
- Creating new columns
- Applying functions with `apply()`
- Grouping with `groupby()`
- Merging and joining DataFrames

**Week 7-8: Data Analysis**
- Aggregation functions
- Pivot tables
- Time series analysis
- Statistical analysis

### Additional Resources

**Official Documentation:**
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

**Practice Datasets:**
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Data.gov](https://www.data.gov/)

**Books:**
- "Python for Data Analysis" by Wes McKinney (Pandas creator)
- "Pandas Cookbook" by Theodore Petrou

---

## Summary

You've completed the CSV Loading Milestone! You now know how to:

✓ Load CSV files with `pd.read_csv()`  
✓ Inspect data with head(), tail(), info(), describe()  
✓ Verify structure with shape, columns, dtypes, len()  
✓ Handle common loading errors  
✓ Troubleshoot encoding, delimiter, and header issues  

**Remember the golden rule:** Always inspect your data after loading. This simple habit prevents countless downstream problems and builds confidence in your analysis.

Happy data loading! 🎉
