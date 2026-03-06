"""
Understanding Array Shape, Dimensions, and Index Positions
===========================================================
This script demonstrates how to understand and work with NumPy array shapes,
dimensions, and index positions. Mastering these fundamentals is critical for
avoiding index errors and writing correct numerical code.

Author: Python Learner
Date: March 4, 2026
Purpose: Master array structure, shape interpretation, and indexing
"""

# ==============================================================================
# SECTION 1: IMPORTS AND SETUP
# ==============================================================================
import numpy as np


# ==============================================================================
# SECTION 2: UNDERSTANDING ARRAY SHAPE
# ==============================================================================
print("=" * 80)
print("SECTION 1: Understanding Array Shape")
print("=" * 80)
print()

print("What is Array Shape?")
print("-" * 40)
print("• Shape describes the dimensions of an array")
print("• It tells you how many elements exist along each axis")
print("• Shape is a tuple of integers")
print("• Each integer represents the size of that dimension")
print("• Shape is accessed using the .shape attribute")
print()

# 2.1 - Shape of 1D Arrays
print("2.1 - Shape of One-Dimensional Arrays")
print("-" * 40)

# Example 1: Simple 1D array
array_1d_a = np.array([10, 20, 30, 40, 50])
print(f"Array: {array_1d_a}")
print(f"Shape: {array_1d_a.shape}")
print(f"Interpretation: This array has {array_1d_a.shape[0]} elements")
print()

# Example 2: Longer 1D array
array_1d_b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {array_1d_b}")
print(f"Shape: {array_1d_b.shape}")
print(f"Interpretation: {array_1d_b.shape[0]} elements in a single dimension")
print()

# Example 3: Single element array
array_1d_c = np.array([100])
print(f"Array: {array_1d_c}")
print(f"Shape: {array_1d_c.shape}")
print(f"Note: Even a single-element array has shape (1,)")
print()

# 2.2 - Shape of 2D Arrays
print("2.2 - Shape of Two-Dimensional Arrays (Matrices)")
print("-" * 40)

# Example 1: Square matrix
array_2d_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Array:")
print(array_2d_a)
print(f"Shape: {array_2d_a.shape}")
print(f"Interpretation: {array_2d_a.shape[0]} rows, {array_2d_a.shape[1]} columns")
print(f"                This is a 3×3 matrix")
print()

# Example 2: Rectangular matrix
array_2d_b = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])
print("Array:")
print(array_2d_b)
print(f"Shape: {array_2d_b.shape}")
print(f"Interpretation: {array_2d_b.shape[0]} rows, {array_2d_b.shape[1]} columns")
print(f"                This is a 2×4 matrix")
print()

# Example 3: Tall matrix (more rows than columns)
array_2d_c = np.array([
    [100, 200],
    [300, 400],
    [500, 600],
    [700, 800]
])
print("Array:")
print(array_2d_c)
print(f"Shape: {array_2d_c.shape}")
print(f"Interpretation: {array_2d_c.shape[0]} rows, {array_2d_c.shape[1]} columns")
print(f"                This is a 4×2 matrix")
print()

# Example 4: Single row matrix
array_2d_d = np.array([[1, 2, 3, 4, 5]])
print("Array:")
print(array_2d_d)
print(f"Shape: {array_2d_d.shape}")
print(f"Note: Single row, but still 2D because it's a matrix structure")
print()

# Example 5: Single column matrix
array_2d_e = np.array([[10], [20], [30], [40]])
print("Array:")
print(array_2d_e)
print(f"Shape: {array_2d_e.shape}")
print(f"Note: Single column, but still 2D (4 rows × 1 column)")
print()

# 2.3 - Shape of 3D Arrays
print("2.3 - Shape of Three-Dimensional Arrays")
print("-" * 40)

# Example 1: Small 3D array
array_3d_a = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("Array:")
print(array_3d_a)
print(f"Shape: {array_3d_a.shape}")
print(f"Interpretation: {array_3d_a.shape[0]} layers (depth)")
print(f"                {array_3d_a.shape[1]} rows per layer")
print(f"                {array_3d_a.shape[2]} columns per row")
print(f"                Think of it as 2 matrices of 2×2 stacked together")
print()

# Example 2: Tour data - 3 cities, 4 weeks, 5 shows per week
tour_data = np.array([
    [  # City 1
        [100, 120, 110, 130, 115],  # Week 1
        [105, 125, 115, 135, 120],  # Week 2
        [110, 130, 120, 140, 125],  # Week 3
        [115, 135, 125, 145, 130]   # Week 4
    ],
    [  # City 2
        [90, 100, 95, 110, 105],
        [95, 105, 100, 115, 110],
        [100, 110, 105, 120, 115],
        [105, 115, 110, 125, 120]
    ],
    [  # City 3
        [80, 95, 85, 100, 90],
        [85, 100, 90, 105, 95],
        [90, 105, 95, 110, 100],
        [95, 110, 100, 115, 105]
    ]
])
print(f"Tour Attendance Data Shape: {tour_data.shape}")
print(f"Interpretation: {tour_data.shape[0]} cities")
print(f"                {tour_data.shape[1]} weeks")
print(f"                {tour_data.shape[2]} shows per week")
print(f"Total data points: {tour_data.size} individual attendance values")
print()

# 2.4 - Understanding Shape Components
print("2.4 - Breaking Down Shape Components")
print("-" * 40)

demo_array = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
])
print(f"Array Shape: {demo_array.shape}")
print()
print("Breaking it down:")
print(f"  shape[0] = {demo_array.shape[0]} → First dimension (depth/layers)")
print(f"  shape[1] = {demo_array.shape[1]} → Second dimension (rows)")
print(f"  shape[2] = {demo_array.shape[2]} → Third dimension (columns)")
print()
print(f"You can think of this as:")
print(f"  • {demo_array.shape[0]} 'pages' or 'layers'")
print(f"  • Each page contains a {demo_array.shape[1]}×{demo_array.shape[2]} table")
print()


# ==============================================================================
# SECTION 3: UNDERSTANDING DIMENSIONS (ndim)
# ==============================================================================
print("=" * 80)
print("SECTION 2: Understanding Dimensions and Axes")
print("=" * 80)
print()

print("What are Dimensions?")
print("-" * 40)
print("• Dimensions (ndim) = the number of axes an array has")
print("• 1D array = single axis (like a list)")
print("• 2D array = two axes (like a table/matrix)")
print("• 3D array = three axes (like stacked tables)")
print("• Number of dimensions = length of the shape tuple")
print()

# 3.1 - Comparing Dimensions
print("3.1 - Comparing Different Dimensions")
print("-" * 40)

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr_1d}")
print(f"  Shape:      {arr_1d.shape}")
print(f"  Dimensions: {arr_1d.ndim}")
print(f"  Total size: {arr_1d.size}")
print()

# 2D array
arr_2d = np.array([[1, 2, 3, 4, 5]])
print(f"2D Array: {arr_2d}")
print(f"  Shape:      {arr_2d.shape}")
print(f"  Dimensions: {arr_2d.ndim}")
print(f"  Total size: {arr_2d.size}")
print(f"  Note: Same 5 elements, but structured as 1 row × 5 columns")
print()

# Another 2D arrangement
arr_2d_b = np.array([[1], [2], [3], [4], [5]])
print(f"2D Array (column):")
print(arr_2d_b)
print(f"  Shape:      {arr_2d_b.shape}")
print(f"  Dimensions: {arr_2d_b.ndim}")
print(f"  Total size: {arr_2d_b.size}")
print(f"  Note: Same 5 elements, but structured as 5 rows × 1 column")
print()

# 3.2 - Understanding Axes
print("3.2 - Understanding Axes")
print("-" * 40)

print("In NumPy:")
print("  • Axis 0 = first dimension (rows in 2D)")
print("  • Axis 1 = second dimension (columns in 2D)")
print("  • Axis 2 = third dimension (depth in 3D)")
print()

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Sample Matrix:")
print(matrix)
print(f"Shape: {matrix.shape} (3 rows, 3 columns)")
print()

print("Operations along different axes:")
print(f"  Sum along axis 0 (down columns):    {matrix.sum(axis=0)}")
print(f"  Sum along axis 1 (across rows):     {matrix.sum(axis=1)}")
print()
print(f"  Mean along axis 0 (down columns):   {matrix.mean(axis=0)}")
print(f"  Mean along axis 1 (across rows):    {matrix.mean(axis=1)}")
print()

# Visual representation
print("Visual representation of axes:")
print("    axis 1 →")
print("  ┌──────────┐")
print("a │ 10 20 30 │")
print("x │ 40 50 60 │")
print("i │ 70 80 90 │")
print("s └──────────┘")
print("0")
print("↓")
print()

# 3.3 - Dimension Examples with Different Shapes
print("3.3 - Dimension Summary Table")
print("-" * 40)

examples = [
    (np.array([1, 2, 3]), "Simple list"),
    (np.array([[1, 2, 3]]), "Single row matrix"),
    (np.array([[1], [2], [3]]), "Single column matrix"),
    (np.array([[1, 2], [3, 4]]), "2×2 matrix"),
    (np.array([[[1, 2], [3, 4]]]), "3D with one layer"),
]

print(f"{'Description':<25} {'Shape':<15} {'Dims':<6} {'Size':<6}")
print("-" * 60)
for arr, desc in examples:
    print(f"{desc:<25} {str(arr.shape):<15} {arr.ndim:<6} {arr.size:<6}")
print()


# ==============================================================================
# SECTION 4: ACCESSING ELEMENTS USING INDEX POSITIONS
# ==============================================================================
print("=" * 80)
print("SECTION 3: Accessing Elements Using Index Positions")
print("=" * 80)
print()

print("Index Position Rules:")
print("-" * 40)
print("• NumPy uses zero-based indexing (first element is at index 0)")
print("• Negative indices count from the end (-1 is last element)")
print("• 1D arrays: array[index]")
print("• 2D arrays: array[row, column] or array[row][column]")
print("• 3D arrays: array[layer, row, column]")
print()

# 4.1 - Indexing 1D Arrays
print("4.1 - Indexing One-Dimensional Arrays")
print("-" * 40)

numbers = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Array: {numbers}")
print(f"Shape: {numbers.shape} (7 elements)")
print()

print("Index positions:")
print("Index:   0   1   2   3   4   5   6")
print(f"Value: {numbers[0]:3} {numbers[1]:3} {numbers[2]:3} {numbers[3]:3} {numbers[4]:3} {numbers[5]:3} {numbers[6]:3}")
print()

print("Accessing elements:")
print(f"  numbers[0]  = {numbers[0]}  (first element)")
print(f"  numbers[3]  = {numbers[3]}  (fourth element)")
print(f"  numbers[6]  = {numbers[6]}  (last element)")
print(f"  numbers[-1] = {numbers[-1]}  (last element using negative index)")
print(f"  numbers[-2] = {numbers[-2]}  (second to last)")
print()

# 4.2 - Indexing 2D Arrays
print("4.2 - Indexing Two-Dimensional Arrays")
print("-" * 40)

sales = np.array([
    [100, 150, 200],  # Row 0
    [110, 160, 210],  # Row 1
    [120, 170, 220],  # Row 2
    [130, 180, 230]   # Row 3
])
print("Sales Data (4 weeks × 3 products):")
print(sales)
print(f"Shape: {sales.shape}")
print()

print("Understanding the layout:")
print("        Col 0  Col 1  Col 2")
print("Row 0:   100    150    200")
print("Row 1:   110    160    210")
print("Row 2:   120    170    220")
print("Row 3:   130    180    230")
print()

print("Accessing specific elements:")
print(f"  sales[0, 0] = {sales[0, 0]}  (row 0, column 0 - top-left)")
print(f"  sales[0, 2] = {sales[0, 2]}  (row 0, column 2 - top-right)")
print(f"  sales[3, 0] = {sales[3, 0]}  (row 3, column 0 - bottom-left)")
print(f"  sales[3, 2] = {sales[3, 2]}  (row 3, column 2 - bottom-right)")
print(f"  sales[1, 1] = {sales[1, 1]}  (row 1, column 1 - center-ish)")
print()

print("Using negative indices:")
print(f"  sales[-1, -1] = {sales[-1, -1]}  (last row, last column)")
print(f"  sales[-1, 0]  = {sales[-1, 0]}  (last row, first column)")
print(f"  sales[0, -1]  = {sales[0, -1]}  (first row, last column)")
print()

# 4.3 - Accessing Entire Rows and Columns
print("4.3 - Accessing Entire Rows and Columns")
print("-" * 40)

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("Matrix:")
print(matrix)
print(f"Shape: {matrix.shape}")
print()

print("Accessing entire rows:")
print(f"  matrix[0]    = {matrix[0]}  (entire first row)")
print(f"  matrix[1]    = {matrix[1]}  (entire second row)")
print(f"  matrix[2]    = {matrix[2]}  (entire third row)")
print(f"  matrix[-1]   = {matrix[-1]}  (last row)")
print()

print("Accessing entire columns:")
print(f"  matrix[:, 0] = {matrix[:, 0]}  (entire first column)")
print(f"  matrix[:, 1] = {matrix[:, 1]}  (entire second column)")
print(f"  matrix[:, 2] = {matrix[:, 2]}  (entire third column)")
print(f"  matrix[:, 3] = {matrix[:, 3]}  (entire fourth column)")
print(f"  matrix[:, -1] = {matrix[:, -1]}  (last column)")
print()

# 4.4 - Indexing 3D Arrays
print("4.4 - Indexing Three-Dimensional Arrays")
print("-" * 40)

data_3d = np.array([
    [  # Layer 0
        [1, 2, 3],
        [4, 5, 6]
    ],
    [  # Layer 1
        [7, 8, 9],
        [10, 11, 12]
    ]
])
print("3D Array:")
print(data_3d)
print(f"Shape: {data_3d.shape} (2 layers, 2 rows, 3 columns)")
print()

print("Accessing elements:")
print(f"  data_3d[0, 0, 0] = {data_3d[0, 0, 0]}  (layer 0, row 0, col 0)")
print(f"  data_3d[0, 1, 2] = {data_3d[0, 1, 2]}  (layer 0, row 1, col 2)")
print(f"  data_3d[1, 0, 1] = {data_3d[1, 0, 1]}  (layer 1, row 0, col 1)")
print(f"  data_3d[1, 1, 2] = {data_3d[1, 1, 2]}  (layer 1, row 1, col 2)")
print()

print("Accessing entire matrices:")
print(f"  data_3d[0] (entire first layer):")
print(f"    {data_3d[0]}")
print(f"  data_3d[1] (entire second layer):")
print(f"    {data_3d[1]}")
print()

# 4.5 - Alternative Indexing Syntax
print("4.5 - Alternative Indexing Syntax")
print("-" * 40)

arr = np.array([[10, 20, 30], [40, 50, 60]])
print(f"Array:")
print(arr)
print()

print("Both syntaxes work (but comma notation is preferred):")
print(f"  arr[0, 1]  = {arr[0, 1]}  (preferred)")
print(f"  arr[0][1]  = {arr[0][1]}  (also works, but less efficient)")
print()
print("Recommendation: Use comma notation arr[row, col] for clarity and performance")
print()


# ==============================================================================
# SECTION 5: VISUALIZING ARRAY LAYOUT
# ==============================================================================
print("=" * 80)
print("SECTION 4: Visualizing Array Layout")
print("=" * 80)
print()

# 5.1 - Visualizing 1D Arrays
print("5.1 - Visualizing 1D Arrays")
print("-" * 40)

vec = np.array([5, 10, 15, 20, 25])
print(f"Array: {vec}")
print()
print("Visual representation:")
print("┌────┬────┬────┬────┬────┐")
print(f"│ {vec[0]:2} │ {vec[1]:2} │ {vec[2]:2} │ {vec[3]:2} │ {vec[4]:2} │")
print("└────┴────┴────┴────┴────┘")
print("  [0] [1]  [2]  [3]  [4]  ← indices")
print()

# 5.2 - Visualizing 2D Arrays
print("5.2 - Visualizing 2D Arrays as Tables")
print("-" * 40)

revenue = np.array([
    [1000, 1500, 2000],
    [1100, 1600, 2100],
    [1200, 1700, 2200]
])
print("Revenue Array:")
print(revenue)
print()

print("Table visualization with indices:")
print("       Col[0]  Col[1]  Col[2]")
print("     ┌───────┬───────┬───────┐")
print(f"Row[0]│ {revenue[0,0]:5} │ {revenue[0,1]:5} │ {revenue[0,2]:5} │")
print("     ├───────┼───────┼───────┤")
print(f"Row[1]│ {revenue[1,0]:5} │ {revenue[1,1]:5} │ {revenue[1,2]:5} │")
print("     ├───────┼───────┼───────┤")
print(f"Row[2]│ {revenue[2,0]:5} │ {revenue[2,1]:5} │ {revenue[2,2]:5} │")
print("     └───────┴───────┴───────┘")
print()

print("Business interpretation:")
print("  Rows represent: Time periods (Week 1, Week 2, Week 3)")
print("  Columns represent: Products (Product A, Product B, Product C)")
print(f"  revenue[1, 2] = ${revenue[1, 2]} → Week 2, Product C")
print()

# 5.3 - Visualizing 3D Arrays
print("5.3 - Visualizing 3D Arrays as Stacked Layers")
print("-" * 40)

cube = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D Array:")
print(cube)
print()

print("Layer-by-layer visualization:")
print()
print("Layer 0 (cube[0]):")
print("  ┌───┬───┐")
print(f"  │ {cube[0,0,0]} │ {cube[0,0,1]} │")
print("  ├───┼───┤")
print(f"  │ {cube[0,1,0]} │ {cube[0,1,1]} │")
print("  └───┴───┘")
print()
print("Layer 1 (cube[1]):")
print("  ┌───┬───┐")
print(f"  │ {cube[1,0,0]} │ {cube[1,0,1]} │")
print("  ├───┼───┤")
print(f"  │ {cube[1,1,0]} │ {cube[1,1,1]} │")
print("  └───┴───┘")
print()
print("Think of 3D arrays as multiple 2D tables stacked on top of each other")
print()

# 5.4 - Mental Model for Index Order
print("5.4 - Mental Model for Index Order")
print("-" * 40)

print("Remember the order: [layer, row, column] or [depth, height, width]")
print()
print("For 1D: array[position]")
print("For 2D: array[row, column]")
print("For 3D: array[layer, row, column]")
print()
print("Analogy:")
print("  1D → A line of items")
print("  2D → A spreadsheet/table")
print("  3D → A stack of spreadsheets")
print()


# ==============================================================================
# SECTION 6: COMMON INDEXING MISTAKES AND HOW TO AVOID THEM
# ==============================================================================
print("=" * 80)
print("SECTION 5: Common Indexing Mistakes and Prevention")
print("=" * 80)
print()

# 6.1 - Index Out of Range Errors
print("6.1 - Avoiding Index Out of Range Errors")
print("-" * 40)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}")
print(f"Shape: {arr.shape} → Valid indices: 0 to {arr.shape[0]-1}")
print()

print("Safe access:")
print(f"  arr[0] = {arr[0]}  ✓")
print(f"  arr[4] = {arr[4]}  ✓ (last element)")
print()

print("Unsafe access (would cause error):")
print(f"  arr[5] → IndexError! (array only has indices 0-4)")
print(f"  arr[10] → IndexError! (way out of range)")
print()

print("Always check:")
print(f"  Max valid index = shape[dimension] - 1")
print(f"  For this array: max index = {arr.shape[0]} - 1 = {arr.shape[0]-1}")
print()

# 6.2 - Row vs Column Confusion
print("6.2 - Avoiding Row/Column Confusion")
print("-" * 40)

table = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Array:")
print(table)
print(f"Shape: {table.shape} → {table.shape[0]} rows, {table.shape[1]} columns")
print()

print("Correct understanding:")
print(f"  table[0, 2] = {table[0, 2]}  → First row, third column ✓")
print(f"  table[1, 0] = {table[1, 0]}  → Second row, first column ✓")
print()

print("Remember: array[row, column] NOT array[column, row]")
print()

# 6.3 - Dimension Mismatch
print("6.3 - Avoiding Dimension Mismatch")
print("-" * 40)

arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3]])

print(f"1D Array: {arr_1d}")
print(f"  Shape: {arr_1d.shape}")
print(f"  Access: arr_1d[0] = {arr_1d[0]} ✓")
print()

print(f"2D Array: {arr_2d}")
print(f"  Shape: {arr_2d.shape}")
print(f"  Access: arr_2d[0, 0] = {arr_2d[0, 0]} ✓")
print(f"  Wrong:  arr_2d[0] = {arr_2d[0]} (returns whole row, not single element)")
print()

print("Tip: Always check .ndim and .shape before indexing")
print()

# 6.4 - Best Practices
print("6.4 - Indexing Best Practices")
print("-" * 40)

print("1. Always inspect shape before accessing elements")
data = np.array([[10, 20], [30, 40], [50, 60]])
print(f"   data.shape = {data.shape} → {data.shape[0]} rows, {data.shape[1]} columns")
print()

print("2. Use descriptive variable names for indices")
print("   Good: sales[week_index, product_index]")
print("   Bad:  sales[i, j]")
print()

print("3. Validate indices are within bounds")
row_idx = 2
col_idx = 1
print(f"   if row_idx < data.shape[0] and col_idx < data.shape[1]:")
if row_idx < data.shape[0] and col_idx < data.shape[1]:
    print(f"       value = data[{row_idx}, {col_idx}] = {data[row_idx, col_idx]} ✓")
print()

print("4. Use negative indices carefully")
print(f"   data[-1, -1] = {data[-1, -1]}  (last row, last column) ✓")
print()


# ==============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# ==============================================================================
print("=" * 80)
print("SECTION 6: Practical Examples")
print("=" * 80)
print()

# Example 1: Concert Ticket Sales
print("Example 1: Concert Attendance by Day and Section")
print("-" * 40)

# Rows: Days (Mon-Fri), Columns: Sections (VIP, Regular, Balcony)
attendance = np.array([
    [150, 450, 300],  # Monday
    [180, 500, 350],  # Tuesday
    [200, 550, 400],  # Wednesday
    [220, 600, 420],  # Thursday
    [250, 650, 450]   # Friday
])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
sections = ["VIP", "Regular", "Balcony"]

print(f"Attendance Array Shape: {attendance.shape}")
print(f"Interpretation: {attendance.shape[0]} days, {attendance.shape[1]} sections")
print()

print("Full attendance data:")
print(attendance)
print()

print("Accessing specific information:")
print(f"  Wednesday VIP attendance: {attendance[2, 0]} people")
print(f"  Friday Regular attendance: {attendance[4, 1]} people")
print(f"  Monday Balcony attendance: {attendance[0, 2]} people")
print()

print("Total attendance by day:")
for day_idx, day in enumerate(days):
    total = attendance[day_idx].sum()
    print(f"  {day:10} → {total:4} people")
print()

print("Total attendance by section:")
for sec_idx, section in enumerate(sections):
    total = attendance[:, sec_idx].sum()
    print(f"  {section:10} → {total:4} people")
print()

# Example 2: Multi-City Tour Performance
print("Example 2: Multi-City Tour Revenue Matrix")
print("-" * 40)

# 3 cities × 4 weeks × 3 show types
cities = ["New York", "Los Angeles", "Chicago"]
weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
show_types = ["Matinee", "Evening", "Late"]

tour_revenue = np.array([
    [  # New York
        [5000, 8000, 6000],   # Week 1
        [5500, 8500, 6500],   # Week 2
        [6000, 9000, 7000],   # Week 3
        [6500, 9500, 7500]    # Week 4
    ],
    [  # Los Angeles
        [4500, 7500, 5500],
        [5000, 8000, 6000],
        [5500, 8500, 6500],
        [6000, 9000, 7000]
    ],
    [  # Chicago
        [4000, 7000, 5000],
        [4500, 7500, 5500],
        [5000, 8000, 6000],
        [5500, 8500, 6500]
    ]
])

print(f"Tour Revenue Shape: {tour_revenue.shape}")
print(f"Structure: {tour_revenue.shape[0]} cities × {tour_revenue.shape[1]} weeks × {tour_revenue.shape[2]} show types")
print()

print("Example queries:")
# New York, Week 3, Evening show
ny_w3_evening = tour_revenue[0, 2, 1]
print(f"  New York Week 3 Evening revenue: ${ny_w3_evening:,}")

# Los Angeles, Week 1, Matinee
la_w1_matinee = tour_revenue[1, 0, 0]
print(f"  Los Angeles Week 1 Matinee revenue: ${la_w1_matinee:,}")

# Chicago, Week 4, Late show
chi_w4_late = tour_revenue[2, 3, 2]
print(f"  Chicago Week 4 Late show revenue: ${chi_w4_late:,}")
print()

print("Total revenue by city:")
for city_idx, city in enumerate(cities):
    total = tour_revenue[city_idx].sum()
    print(f"  {city:15} → ${total:,}")
print()

print(f"Overall tour revenue: ${tour_revenue.sum():,}")
print(f"Average show revenue: ${tour_revenue.mean():,.2f}")
print()


# ==============================================================================
# SUMMARY
# ==============================================================================
print("=" * 80)
print("MILESTONE COMPLETE - SUMMARY")
print("=" * 80)
print()
print("✓ Understood array shape and how to interpret it")
print("✓ Learned about dimensions (ndim) and axes")
print("✓ Mastered accessing elements using index positions")
print("✓ Developed mental models for visualizing array layouts")
print("✓ Learned to prevent common indexing mistakes")
print("✓ Applied concepts to practical tour metrics examples")
print()
print("Key Takeaways:")
print("  • Shape defines array structure: (rows, columns) for 2D")
print("  • Zero-based indexing: first element is at index 0")
print("  • 2D access: array[row, column]")
print("  • 3D access: array[layer, row, column]")
print("  • Always check shape before accessing elements")
print("  • Use : to access entire rows or columns")
print()
print("You are now ready to:")
print("  • Safely access and modify array elements")
print("  • Work with array slicing (next topic)")
print("  • Reshape arrays confidently")
print("  • Debug index-related errors effectively")
print()
print("Next Steps: Learn array slicing, boolean indexing, and fancy indexing")
print("=" * 80)
