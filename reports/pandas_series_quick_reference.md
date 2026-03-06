# Pandas Series Quick Reference

## What is a Series?
A one-dimensional labeled array capable of holding any data type.

## Creating Series

### From Python List
```python
import pandas as pd

# Default index (0, 1, 2, ...)
s = pd.Series([10, 20, 30, 40, 50])

# Custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

### From NumPy Array
```python
import numpy as np

# From array
arr = np.array([1, 2, 3, 4, 5])
s = pd.Series(arr)

# With custom index
s = pd.Series(arr, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
```

### From Dictionary
```python
# Keys become index
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
```

## Accessing Data

### By Position (iloc)
```python
s.iloc[0]      # First element
s.iloc[-1]     # Last element
s.iloc[1:3]    # Slice by position
```

### By Label
```python
s['a']         # Single label
s[['a', 'c']]  # Multiple labels
```

## Series Attributes

```python
s.values       # Get values as NumPy array
s.index        # Get index object
s.dtype        # Data type
s.shape        # Dimensions
s.size         # Number of elements
s.name         # Series name (optional)
```

## Common Operations

### Mathematical
```python
s + 10         # Add to all elements
s * 2          # Multiply all elements
s ** 2         # Square all elements
s1 + s2        # Element-wise addition (aligned by index)
```

### Statistical
```python
s.mean()       # Average
s.sum()        # Sum
s.max()        # Maximum
s.min()        # Minimum
s.std()        # Standard deviation
s.median()     # Median
s.describe()   # Summary statistics
```

### Filtering
```python
s[s > 20]      # Boolean indexing
s[s.isin([10, 30])]  # Filter by values
```

## Key Differences: Series vs NumPy Array

| Feature | NumPy Array | Pandas Series |
|---------|-------------|---------------|
| Labels | No | Yes (index) |
| Access | Position only | Position + Label |
| Alignment | Manual | Automatic by label |
| Missing data | Limited support | Built-in (NaN) |
| Use case | Numerical computation | Labeled data analysis |

## Why Use Series?

1. **Meaningful labels** - Access data by name, not just position
2. **Automatic alignment** - Operations align by label
3. **Missing data handling** - Built-in NaN support
4. **Integration** - Works seamlessly with DataFrames
5. **Readability** - Code is more intuitive and maintainable

## Common Patterns

### Temperature readings
```python
temps = pd.Series([72, 68, 75, 80, 77], 
                  index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
```

### Student scores
```python
scores = pd.Series([95, 87, 92], 
                   index=['Alice', 'Bob', 'Charlie'])
```

### Product prices
```python
prices = pd.Series([29.99, 49.99, 19.99], 
                   index=['Keyboard', 'Mouse', 'Cable'])
```

## Next Steps
- Practice creating Series with different data types
- Experiment with index operations
- Learn about DataFrames (2D labeled data)
- Explore time series with DatetimeIndex
