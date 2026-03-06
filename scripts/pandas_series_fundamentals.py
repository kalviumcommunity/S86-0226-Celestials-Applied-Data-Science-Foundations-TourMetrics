"""
Pandas Series Fundamentals
===========================
This script demonstrates the core concepts of Pandas Series:
- Creating Series from Python lists
- Creating Series from NumPy arrays
- Understanding index and values
- Comparing Series with NumPy arrays
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS SERIES FUNDAMENTALS")
print("=" * 60)

# ============================================================================
# 1. Understanding Pandas Series
# ============================================================================
print("\n1. WHAT IS A PANDAS SERIES?")
print("-" * 60)
print("A Series is a one-dimensional labeled array.")
print("Think of it as a NumPy array with labels (index).")
print("Each value has a corresponding label for easy access.\n")

# ============================================================================
# 2. Creating a Series from Python Lists
# ============================================================================
print("\n2. CREATING SERIES FROM PYTHON LISTS")
print("-" * 60)

# Example 1: Numeric list
temperatures = [72, 68, 75, 80, 77]
temp_series = pd.Series(temperatures)
print("Temperature readings (from list):")
print(temp_series)
print(f"\nType: {type(temp_series)}")

# Example 2: String list
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
city_series = pd.Series(cities)
print("\n\nCity names (from list):")
print(city_series)

# Example 3: Mixed data with custom index
scores = [95, 87, 92, 88, 90]
score_series = pd.Series(scores, index=["Alice", "Bob", "Charlie", "Diana", "Eve"])
print("\n\nStudent scores (with custom index):")
print(score_series)

# ============================================================================
# 3. Creating a Series from NumPy Arrays
# ============================================================================
print("\n\n3. CREATING SERIES FROM NUMPY ARRAYS")
print("-" * 60)

# Example 1: From NumPy array
np_array = np.array([10, 20, 30, 40, 50])
np_series = pd.Series(np_array)
print("Series from NumPy array:")
print(np_series)

# Example 2: From NumPy array with custom index
random_data = np.random.randint(1, 100, size=5)
random_series = pd.Series(random_data, index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print("\n\nRandom values by weekday:")
print(random_series)

# Example 3: Preserving data types
float_array = np.array([1.5, 2.7, 3.9, 4.2, 5.8])
float_series = pd.Series(float_array)
print("\n\nFloat Series (data type preserved):")
print(float_series)
print(f"Data type: {float_series.dtype}")

# ============================================================================
# 4. Understanding Index and Values
# ============================================================================
print("\n\n4. UNDERSTANDING INDEX AND VALUES")
print("-" * 60)

# Create a sample Series
products = pd.Series(
    [29.99, 49.99, 19.99, 99.99, 15.99],
    index=["Keyboard", "Mouse", "Cable", "Monitor", "Mousepad"]
)
print("Product prices:")
print(products)

# Accessing values
print("\n\nAccessing VALUES:")
print(f"Values as array: {products.values}")
print(f"Type of values: {type(products.values)}")

# Accessing index
print("\n\nAccessing INDEX:")
print(f"Index labels: {products.index}")
print(f"Type of index: {type(products.index)}")

# Positional access (like NumPy)
print("\n\nPositional access (0-based):")
print(f"First item: {products.iloc[0]}")
print(f"Last item: {products.iloc[-1]}")

# Label-based access (Pandas advantage)
print("\n\nLabel-based access:")
print(f"Mouse price: ${products['Mouse']}")
print(f"Monitor price: ${products['Monitor']}")

# ============================================================================
# 5. Comparing Series with NumPy Arrays
# ============================================================================
print("\n\n5. SERIES VS NUMPY ARRAYS")
print("-" * 60)

# NumPy array
np_sales = np.array([100, 150, 200, 175, 225])
print("NumPy Array (no labels):")
print(np_sales)
print(f"Access by position: np_sales[0] = {np_sales[0]}")

# Pandas Series
pd_sales = pd.Series(
    [100, 150, 200, 175, 225],
    index=["Jan", "Feb", "Mar", "Apr", "May"]
)
print("\n\nPandas Series (with labels):")
print(pd_sales)
print(f"Access by position: pd_sales.iloc[0] = {pd_sales.iloc[0]}")
print(f"Access by label: pd_sales['Jan'] = {pd_sales['Jan']}")

# Key differences
print("\n\nKEY DIFFERENCES:")
print("1. Series have meaningful labels (index)")
print("2. Series support label-based operations")
print("3. Series align data automatically by label")
print("4. Series are built on top of NumPy arrays")

# ============================================================================
# 6. Simple Operations on Series
# ============================================================================
print("\n\n6. SIMPLE OPERATIONS")
print("-" * 60)

# Mathematical operations
numbers = pd.Series([10, 20, 30, 40, 50], index=["A", "B", "C", "D", "E"])
print("Original Series:")
print(numbers)

print("\n\nMultiply by 2:")
print(numbers * 2)

print("\n\nAdd 5:")
print(numbers + 5)

print("\n\nStatistical operations:")
print(f"Mean: {numbers.mean()}")
print(f"Sum: {numbers.sum()}")
print(f"Max: {numbers.max()}")
print(f"Min: {numbers.min()}")

# ============================================================================
# Summary
# ============================================================================
print("\n\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("✓ Series are 1D labeled arrays")
print("✓ Can be created from lists or NumPy arrays")
print("✓ Have both index (labels) and values")
print("✓ Support positional AND label-based access")
print("✓ Built on NumPy but add powerful labeling")
print("=" * 60)
