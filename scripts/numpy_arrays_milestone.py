"""
NumPy Arrays from Python Lists Milestone
=========================================
This script demonstrates how to create and work with NumPy arrays from Python lists.
NumPy arrays are the foundation of numerical computing in Python and are essential
for data science, machine learning, and scientific computing.

Author: Python Learner
Date: March 4, 2026
Purpose: Learn NumPy array fundamentals and conversion from Python lists
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
import numpy as np


# ==============================================================================
# SECTION 2: UNDERSTANDING NUMPY ARRAYS
# ==============================================================================
print("=" * 80)
print("SECTION 1: Understanding NumPy Arrays")
print("=" * 80)
print()

print("What is a NumPy Array?")
print("-" * 40)
print("• A NumPy array is a grid of values, all of the same type")
print("• Arrays are indexed by a tuple of non-negative integers")
print("• Arrays are homogeneous (all elements must be the same data type)")
print("• Arrays are faster and more memory-efficient than Python lists")
print("• Arrays support vectorized operations (element-wise operations)")
print()

print("Why Use NumPy Arrays Instead of Python Lists?")
print("-" * 40)
print("• Performance: NumPy arrays are 10-100x faster for numerical operations")
print("• Memory: NumPy arrays use less memory than Python lists")
print("• Convenience: Element-wise operations work naturally on arrays")
print("• Ecosystem: Required by Pandas, scikit-learn, TensorFlow, etc.")
print("• Functionality: Built-in mathematical and statistical functions")
print()


# ==============================================================================
# SECTION 3: CREATING NUMPY ARRAYS FROM PYTHON LISTS
# ==============================================================================
print("=" * 80)
print("SECTION 2: Creating NumPy Arrays from Python Lists")
print("=" * 80)
print()

# 3.1 - Creating 1D Arrays from Lists
print("3.1 - Creating One-Dimensional Arrays")
print("-" * 40)

# Example 1: Simple integer list to array
python_list_int = [1, 2, 3, 4, 5]
numpy_array_int = np.array(python_list_int)

print(f"Python List: {python_list_int}")
print(f"NumPy Array: {numpy_array_int}")
print(f"Type of List: {type(python_list_int)}")
print(f"Type of Array: {type(numpy_array_int)}")
print()

# Example 2: Float list to array
python_list_float = [1.5, 2.7, 3.2, 4.8, 5.1]
numpy_array_float = np.array(python_list_float)

print(f"Float List: {python_list_float}")
print(f"Float Array: {numpy_array_float}")
print()

# Example 3: Mixed numeric types (NumPy will upcast to most general type)
python_list_mixed = [1, 2.5, 3, 4.7, 5]
numpy_array_mixed = np.array(python_list_mixed)

print(f"Mixed List: {python_list_mixed}")
print(f"Mixed Array: {numpy_array_mixed}")
print(f"Note: All elements are converted to float (the most general numeric type)")
print()

# Example 4: Creating array directly without intermediate list
direct_array = np.array([10, 20, 30, 40, 50])
print(f"Direct Array Creation: {direct_array}")
print()

# 3.2 - Creating 2D Arrays from Nested Lists
print("3.2 - Creating Two-Dimensional Arrays (Matrices)")
print("-" * 40)

# Example 1: Simple 2D array (matrix)
python_list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
numpy_array_2d = np.array(python_list_2d)

print("Python Nested List (3x3):")
for row in python_list_2d:
    print(f"  {row}")
print()

print("NumPy 2D Array (3x3):")
print(numpy_array_2d)
print()

# Example 2: Rectangle matrix (different dimensions)
revenue_data = [
    [1000, 1500, 2000],  # Week 1
    [1200, 1600, 2100],  # Week 2
    [1100, 1400, 1900],  # Week 3
    [1300, 1700, 2200]   # Week 4
]
revenue_array = np.array(revenue_data)

print("Revenue Data (4 weeks x 3 products):")
print(revenue_array)
print()

# 3.3 - Creating 3D Arrays from Nested Lists
print("3.3 - Creating Three-Dimensional Arrays")
print("-" * 40)

# Example: 3D array representing data across multiple dimensions
# Shape: (2 stores, 3 weeks, 4 products)
sales_3d = [
    [  # Store 1
        [100, 150, 200, 120],  # Week 1
        [110, 160, 210, 130],  # Week 2
        [105, 155, 205, 125]   # Week 3
    ],
    [  # Store 2
        [90, 140, 190, 110],   # Week 1
        [95, 145, 195, 115],   # Week 2
        [92, 142, 192, 112]    # Week 3
    ]
]
sales_array_3d = np.array(sales_3d)

print("3D Sales Array (2 stores x 3 weeks x 4 products):")
print(sales_array_3d)
print()


# ==============================================================================
# SECTION 4: INSPECTING ARRAY PROPERTIES
# ==============================================================================
print("=" * 80)
print("SECTION 3: Inspecting Array Properties")
print("=" * 80)
print()

# 4.1 - Array Shape
print("4.1 - Array Shape (dimensions)")
print("-" * 40)

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = sales_array_3d

print(f"1D Array: {array_1d}")
print(f"Shape: {array_1d.shape}")
print(f"Interpretation: {array_1d.shape[0]} elements")
print()

print(f"2D Array:")
print(array_2d)
print(f"Shape: {array_2d.shape}")
print(f"Interpretation: {array_2d.shape[0]} rows, {array_2d.shape[1]} columns")
print()

print(f"3D Array Shape: {array_3d.shape}")
print(f"Interpretation: {array_3d.shape[0]} stores, {array_3d.shape[1]} weeks, {array_3d.shape[2]} products")
print()

# 4.2 - Array Data Type
print("4.2 - Array Data Type (dtype)")
print("-" * 40)

int_array = np.array([1, 2, 3, 4, 5])
float_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
mixed_array = np.array([1, 2.5, 3, 4.7])

print(f"Integer Array: {int_array}")
print(f"Data Type: {int_array.dtype}")
print()

print(f"Float Array: {float_array}")
print(f"Data Type: {float_array.dtype}")
print()

print(f"Mixed Array: {mixed_array}")
print(f"Data Type: {mixed_array.dtype}")
print(f"Note: NumPy automatically chose float64 to accommodate all values")
print()

# 4.3 - Array Dimensionality
print("4.3 - Array Dimensionality (ndim)")
print("-" * 40)

print(f"1D Array: {array_1d}")
print(f"Number of Dimensions: {array_1d.ndim}")
print()

print(f"2D Array:")
print(array_2d)
print(f"Number of Dimensions: {array_2d.ndim}")
print()

print(f"3D Array Dimensions: {array_3d.ndim}")
print()

# 4.4 - Array Size
print("4.4 - Array Size (total number of elements)")
print("-" * 40)

print(f"1D Array Size: {array_1d.size} elements")
print(f"2D Array Size: {array_2d.size} elements")
print(f"3D Array Size: {array_3d.size} elements")
print()

# 4.5 - Complete Array Information Summary
print("4.5 - Complete Array Information Summary")
print("-" * 40)

demo_array = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])

print(f"Array:")
print(demo_array)
print(f"Shape:      {demo_array.shape}")
print(f"Dimensions: {demo_array.ndim}")
print(f"Size:       {demo_array.size}")
print(f"Data Type:  {demo_array.dtype}")
print(f"Item Size:  {demo_array.itemsize} bytes per element")
print(f"Total Mem:  {demo_array.nbytes} bytes")
print()


# ==============================================================================
# SECTION 5: BASIC OPERATIONS ON ARRAYS
# ==============================================================================
print("=" * 80)
print("SECTION 4: Basic Operations on Arrays")
print("=" * 80)
print()

# 5.1 - Element-wise Arithmetic Operations
print("5.1 - Element-wise Arithmetic Operations")
print("-" * 40)

numbers = np.array([10, 20, 30, 40, 50])

print(f"Original Array: {numbers}")
print()

# Addition
print(f"Add 5 to each element:       {numbers + 5}")

# Subtraction
print(f"Subtract 3 from each:        {numbers - 3}")

# Multiplication
print(f"Multiply each by 2:          {numbers * 2}")

# Division
print(f"Divide each by 10:           {numbers / 10}")

# Exponentiation
print(f"Square each element:         {numbers ** 2}")

# Modulo
print(f"Modulo 15:                   {numbers % 15}")
print()

# 5.2 - Array-to-Array Operations
print("5.2 - Array-to-Array Operations")
print("-" * 40)

array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([10, 20, 30, 40, 50])

print(f"Array A: {array_a}")
print(f"Array B: {array_b}")
print()

print(f"A + B: {array_a + array_b}")
print(f"B - A: {array_b - array_a}")
print(f"A * B: {array_a * array_b}")
print(f"B / A: {array_b / array_a}")
print()

# 5.3 - Mathematical Functions
print("5.3 - Mathematical Functions on Arrays")
print("-" * 40)

values = np.array([1, 4, 9, 16, 25])

print(f"Values: {values}")
print(f"Square Root:    {np.sqrt(values)}")
print(f"Exponential:    {np.exp([1, 2, 3])}")
print(f"Logarithm:      {np.log([1, 10, 100])}")
print()

# 5.4 - Statistical Operations
print("5.4 - Statistical Operations")
print("-" * 40)

data = np.array([12, 15, 18, 21, 24, 27, 30])

print(f"Data: {data}")
print(f"Sum:        {np.sum(data)}")
print(f"Mean:       {np.mean(data)}")
print(f"Median:     {np.median(data)}")
print(f"Std Dev:    {np.std(data):.2f}")
print(f"Variance:   {np.var(data):.2f}")
print(f"Min:        {np.min(data)}")
print(f"Max:        {np.max(data)}")
print(f"Range:      {np.ptp(data)}")  # Peak to peak (max - min)
print()

# 5.5 - Operations on 2D Arrays
print("5.5 - Operations on 2D Arrays")
print("-" * 40)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix:")
print(matrix)
print()

print(f"Sum of all elements:          {np.sum(matrix)}")
print(f"Sum of each column (axis=0):  {np.sum(matrix, axis=0)}")
print(f"Sum of each row (axis=1):     {np.sum(matrix, axis=1)}")
print()

print(f"Mean of all elements:         {np.mean(matrix):.2f}")
print(f"Mean of each column:          {np.mean(matrix, axis=0)}")
print(f"Mean of each row:             {np.mean(matrix, axis=1)}")
print()

# Multiply entire matrix by a scalar
print("Matrix multiplied by 10:")
print(matrix * 10)
print()


# ==============================================================================
# SECTION 6: COMPARISON - LISTS VS ARRAYS
# ==============================================================================
print("=" * 80)
print("SECTION 5: Lists vs Arrays - Key Differences")
print("=" * 80)
print()

# 6.1 - Homogeneity
print("6.1 - Data Type Homogeneity")
print("-" * 40)

# Lists can contain mixed types
mixed_list = [1, "hello", 3.14, True, None]
print(f"Python List (mixed types):  {mixed_list}")
print(f"List allows mixed types: integers, strings, floats, booleans, None")
print()

# Arrays enforce single type
array_from_mixed = np.array([1, 2, 3.5, 4])  # Will convert to floats
print(f"NumPy Array from [1, 2, 3.5, 4]: {array_from_mixed}")
print(f"All elements converted to: {array_from_mixed.dtype}")
print()

# 6.2 - Arithmetic Operations Behavior
print("6.2 - Arithmetic Operations Behavior")
print("-" * 40)

py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

print(f"Python List:  {py_list}")
print(f"NumPy Array:  {np_array}")
print()

# List multiplication repeats the list
print(f"List * 3:     {py_list * 3}")
print(f"Result: List is repeated 3 times")
print()

# Array multiplication is element-wise
print(f"Array * 3:    {np_array * 3}")
print(f"Result: Each element is multiplied by 3")
print()

# List addition concatenates
print(f"List + [10]:  {py_list + [10]}")
print(f"Result: Lists are concatenated")
print()

# Array addition is element-wise (requires same shape)
array_to_add = np.array([10, 10, 10, 10, 10])
print(f"Array + 10:   {np_array + 10}")
print(f"Result: 10 is added to each element (broadcasting)")
print()

# 6.3 - Memory and Performance
print("6.3 - Memory Efficiency")
print("-" * 40)

import sys

large_list = list(range(1000))
large_array = np.array(range(1000))

list_size = sys.getsizeof(large_list)
array_size = large_array.nbytes

print(f"Python List with 1000 integers:  ~{list_size} bytes")
print(f"NumPy Array with 1000 integers:   {array_size} bytes")
print(f"NumPy array uses ~{list_size / array_size:.1f}x less memory")
print()

# 6.4 - Mathematical Operations
print("6.4 - Mathematical Operations")
print("-" * 40)

list_nums = [10, 20, 30, 40, 50]
array_nums = np.array([10, 20, 30, 40, 50])

print(f"Python List: {list_nums}")
print(f"NumPy Array: {array_nums}")
print()

# To get sum of list items, use built-in sum() or loop
print(f"Sum of list:  sum(list_nums) = {sum(list_nums)}")

# Arrays have built-in methods and support direct operations
print(f"Sum of array: array_nums.sum() = {array_nums.sum()}")
print(f"Mean:         array_nums.mean() = {array_nums.mean()}")
print(f"Std:          array_nums.std() = {array_nums.std():.2f}")
print()

# Try to square all elements
print("Squaring all elements:")
print(f"List approach: [x**2 for x in list_nums] = {[x**2 for x in list_nums]}")
print(f"Array approach: array_nums ** 2 = {array_nums ** 2}")
print(f"Note: Array approach is more concise and much faster for large datasets")
print()

# 6.5 - When to Use Each
print("6.5 - When to Use Lists vs Arrays")
print("-" * 40)
print("Use Python Lists when:")
print("  • You need mixed data types (strings, numbers, objects)")
print("  • You need to append/remove items frequently")
print("  • Data size is small and performance doesn't matter")
print("  • You need flexible, dynamic data structures")
print()

print("Use NumPy Arrays when:")
print("  • Working with numerical data exclusively")
print("  • Performing mathematical or statistical operations")
print("  • Working with large datasets (performance matters)")
print("  • Preparing data for Pandas, scikit-learn, or other libraries")
print("  • Need multi-dimensional data (matrices, tensors)")
print()


# ==============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# ==============================================================================
print("=" * 80)
print("SECTION 6: Practical Examples")
print("=" * 80)
print()

# Example 1: Calculating percentage changes
print("Example 1: Tour Ticket Sales Analysis")
print("-" * 40)

# Weekly ticket sales
weekly_sales = [150, 165, 142, 178, 190, 185, 200]
sales_array = np.array(weekly_sales)

print(f"Weekly Sales: {sales_array}")
print(f"Total Sales:  {sales_array.sum()} tickets")
print(f"Average:      {sales_array.mean():.1f} tickets/week")
print(f"Best Week:    {sales_array.max()} tickets")
print(f"Worst Week:   {sales_array.min()} tickets")
print(f"Std Dev:      {sales_array.std():.2f}")
print()

# Example 2: Multi-city tour revenue
print("Example 2: Multi-City Tour Revenue")
print("-" * 40)

# Rows: Cities (5), Columns: Shows (3)
city_revenue = np.array([
    [12000, 15000, 18000],  # New York
    [10000, 12000, 14000],  # Los Angeles
    [8000, 9500, 11000],    # Chicago
    [7000, 8500, 9000],     # Houston
    [9000, 11000, 13000]    # Miami
])

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

print("Revenue per City per Show (3 shows each):")
print(city_revenue)
print()

print("Analysis:")
for i, city in enumerate(cities):
    total = city_revenue[i].sum()
    avg = city_revenue[i].mean()
    print(f"{city:15} - Total: ${total:6,}  Avg: ${avg:7,.2f}")

print()
print(f"Total Revenue Across All Cities: ${city_revenue.sum():,}")
print(f"Average Revenue Per Show:        ${city_revenue.mean():,.2f}")
print(f"Revenue per show (all cities):   {city_revenue.sum(axis=0)}")
print(f"Total revenue per city:          {city_revenue.sum(axis=1)}")
print()

# Example 3: Temperature data conversion
print("Example 3: Temperature Conversion (Celsius to Fahrenheit)")
print("-" * 40)

celsius_temps = np.array([20, 22, 25, 18, 30, 28, 24])
fahrenheit_temps = (celsius_temps * 9/5) + 32

print(f"Celsius:    {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")
print()

# Example 4: Normalizing data
print("Example 4: Normalizing Data (0-1 scale)")
print("-" * 40)

scores = np.array([85, 92, 78, 95, 88, 76, 90])
normalized_scores = (scores - scores.min()) / (scores.max() - scores.min())

print(f"Original Scores:    {scores}")
print(f"Normalized (0-1):   {normalized_scores.round(3)}")
print()


# ==============================================================================
# SUMMARY
# ==============================================================================
print("=" * 80)
print("MILESTONE COMPLETE - SUMMARY")
print("=" * 80)
print()
print("✓ Learned what NumPy arrays are and why they're used")
print("✓ Created 1D, 2D, and 3D arrays from Python lists")
print("✓ Inspected array properties: shape, dtype, ndim, size")
print("✓ Performed arithmetic and statistical operations on arrays")
print("✓ Compared arrays with Python lists and understood key differences")
print("✓ Applied arrays to practical examples")
print()
print("You are now ready to:")
print("  • Use NumPy arrays for numerical computing")
print("  • Work with Pandas DataFrames (built on NumPy)")
print("  • Prepare data for machine learning")
print("  • Perform efficient data analysis")
print()
print("Next Steps: Learn array indexing, slicing, and advanced operations")
print("=" * 80)
