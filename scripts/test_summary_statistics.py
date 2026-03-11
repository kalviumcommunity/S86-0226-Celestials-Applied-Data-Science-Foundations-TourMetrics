"""
Quick Test Script for Summary Statistics
"""
import sys
sys.path.insert(0, 'scripts')

from summary_statistics_milestone import (
    load_products_data,
    compute_single_column_statistics,
    interpret_statistics,
    compare_multiple_columns
)

print("=" * 70)
print("TESTING SUMMARY STATISTICS MILESTONE")
print("=" * 70)
print()

# Load data
print("1. Loading data...")
df = load_products_data()
print(f"   ✓ Loaded {len(df)} rows")
print()

# Test Price statistics
print("2. Computing Price statistics...")
price_stats = compute_single_column_statistics(df, 'Price')
print("   ✓ Price statistics computed")
print()

# Test Stock statistics
print("3. Computing Stock statistics...")
stock_stats = compute_single_column_statistics(df, 'Stock')
print("   ✓ Stock statistics computed")
print()

# Test interpretation
print("4. Testing interpretation...")
interpret_statistics(df, 'Price', price_stats)
print("   ✓ Interpretation generated")
print()

# Test comparison
print("5. Testing column comparison...")
compare_multiple_columns(df, ['Price', 'Stock'])
print("   ✓ Comparison completed")
print()

print("=" * 70)
print("ALL TESTS PASSED! ✓")
print("=" * 70)
print()
print("The summary_statistics_milestone.py script is working correctly.")
print("You can now run it interactively with:")
print("  python scripts/summary_statistics_milestone.py")
