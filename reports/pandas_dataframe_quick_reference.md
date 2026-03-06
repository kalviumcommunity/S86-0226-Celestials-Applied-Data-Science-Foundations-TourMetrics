# Pandas DataFrame Quick Reference

## What is a DataFrame?

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. It's like a spreadsheet or SQL table in Python.

**Key Characteristics:**
- Rows and columns with labels
- Columns can have different data types
- Size-mutable (can add/remove columns)
- Primary data structure in Pandas

## Creating DataFrames

### From Dictionary

```python
import pandas as pd

# Dictionary with column-style data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
```

**Key Points:**
- Dictionary keys become column names
- Dictionary values become column data
- All columns must have same length

### From CSV File

```python
# Basic loading
df = pd.read_csv('file.csv')

# Common parameters
df = pd.read_csv('file.csv', 
                 sep=',',           # Delimiter
                 header=0,          # Row number for column names
                 index_col=None,    # Column to use as index
                 encoding='utf-8')  # File encoding
```

### From Other Sources

```python
# Excel file
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# JSON file
df = pd.read_json('file.json')

# From list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30}
]
df = pd.DataFrame(data)
```

## Inspecting DataFrames

### Basic Inspection

```python
# First n rows (default 5)
df.head()
df.head(10)

# Last n rows (default 5)
df.tail()
df.tail(3)

# Shape (rows, columns)
df.shape  # Returns tuple: (rows, cols)

# Column names
df.columns  # Returns Index object
df.columns.tolist()  # Returns list

# Index
df.index

# Data types
df.dtypes

# Comprehensive info
df.info()

# Basic statistics
df.describe()
```

### Accessing Data

```python
# Single column (returns Series)
df['Name']
df.Name  # Alternative (if no spaces in name)

# Multiple columns (returns DataFrame)
df[['Name', 'Age']]

# Single row by position
df.iloc[0]  # First row

# Single row by label
df.loc[0]  # Row with index 0

# Specific cell
df.loc[0, 'Name']  # Row 0, column 'Name'
df.iloc[0, 1]      # Row 0, column 1
```

## Common DataFrame Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| `df.shape` | Dimensions (rows, cols) | `(100, 5)` |
| `df.columns` | Column names | `Index(['A', 'B'])` |
| `df.index` | Row labels | `RangeIndex(0, 100)` |
| `df.dtypes` | Data types per column | `Name: object, Age: int64` |
| `df.size` | Total elements | `500` |
| `df.ndim` | Number of dimensions | `2` |
| `df.empty` | Is DataFrame empty? | `False` |

## Common Data Types

| Pandas Type | Python Type | Description |
|-------------|-------------|-------------|
| `object` | `str` | Text/strings |
| `int64` | `int` | Integers |
| `float64` | `float` | Decimals |
| `bool` | `bool` | True/False |
| `datetime64` | `datetime` | Dates/times |
| `category` | - | Categorical data |

## Common Issues and Solutions

### Issue: File Not Found
```python
# Problem
df = pd.read_csv('data.csv')  # FileNotFoundError

# Solution: Use correct path
df = pd.read_csv('data/raw/data.csv')
```

### Issue: Wrong Delimiter
```python
# Problem: CSV uses semicolon
df = pd.read_csv('file.csv')  # All data in one column

# Solution: Specify delimiter
df = pd.read_csv('file.csv', sep=';')
```

### Issue: Encoding Errors
```python
# Problem
df = pd.read_csv('file.csv')  # UnicodeDecodeError

# Solution: Specify encoding
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='utf-8-sig')
```

### Issue: Missing Column Names
```python
# Problem: CSV has no header
df = pd.read_csv('file.csv')  # First row becomes header

# Solution: Specify no header
df = pd.read_csv('file.csv', header=None)
# or provide names
df = pd.read_csv('file.csv', names=['Col1', 'Col2', 'Col3'])
```

## Best Practices

1. **Always inspect after loading**
   ```python
   df = pd.read_csv('file.csv')
   print(df.head())
   print(df.info())
   ```

2. **Check shape and types**
   ```python
   print(f"Shape: {df.shape}")
   print(df.dtypes)
   ```

3. **Use descriptive variable names**
   ```python
   # Good
   df_employees = pd.read_csv('employees.csv')
   
   # Avoid
   df1 = pd.read_csv('employees.csv')
   ```

4. **Handle missing data early**
   ```python
   print(df.isnull().sum())  # Count missing values
   ```

5. **Use relative paths**
   ```python
   # Good
   df = pd.read_csv('data/raw/file.csv')
   
   # Avoid absolute paths
   df = pd.read_csv('C:/Users/Name/data/file.csv')
   ```

## Quick Comparison: Series vs DataFrame

| Feature | Series | DataFrame |
|---------|--------|-----------|
| Dimensions | 1D | 2D |
| Structure | Single column | Multiple columns |
| Creation | `pd.Series([1,2,3])` | `pd.DataFrame({'A':[1,2,3]})` |
| Access | `series[0]` | `df['column']` or `df.iloc[0]` |
| Use Case | Single variable | Tabular data |

## Essential Methods Summary

```python
# Creation
pd.DataFrame(dict)
pd.read_csv('file.csv')

# Inspection
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes

# Access
df['column']
df[['col1', 'col2']]
df.iloc[row]
df.loc[label]
```

## Next Steps

After mastering DataFrame basics:
1. Learn data selection and filtering
2. Explore data cleaning techniques
3. Practice data aggregation
4. Study merging and joining DataFrames
5. Visualize data with plots

---

**Remember:** DataFrames are the foundation of all Pandas operations. Master creation and inspection first, then move to more advanced operations.
