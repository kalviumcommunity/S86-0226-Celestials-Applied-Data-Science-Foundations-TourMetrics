"""
Quick Test Script for Distribution Comparison Milestone
"""
import sys
sys.path.insert(0, 'scripts')

from distribution_comparison_milestone import (
    load_products_data,
    compute_multi_column_statistics,
    compare_central_tendency,
    compare_spread_and_variability,
    identify_patterns_and_anomalies,
    create_comparison_summary
)

print("=" * 70)
print("TESTING DISTRIBUTION COMPARISON MILESTONE")
print("=" * 70)
print()

# Load data
print("1. Loading data...")
df = load_products_data()
print(f"   ✓ Loaded {len(df)} rows")
print()

# Select columns to compare
columns = ['Price', 'Stock']

# Test multi-column statistics
print("2. Computing multi-column statistics...")
stats = compute_multi_column_statistics(df, columns)
print("   ✓ Multi-column statistics computed")
print()

# Test central tendency comparison
print("3. Testing central tendency comparison...")
compare_central_tendency(df, columns)
print("   ✓ Central tendency comparison completed")
print()

# Test spread and variability comparison
print("4. Testing spread and variability comparison...")
compare_spread_and_variability(df, columns)
print("   ✓ Spread and variability comparison completed")
print()

# Test pattern identification
print("5. Testing pattern and anomaly identification...")
identify_patterns_and_anomalies(df, columns)
print("   ✓ Pattern identification completed")
print()

# Test comprehensive summary
print("6. Testing comprehensive comparison summary...")
create_comparison_summary(df, columns)
print("   ✓ Comprehensive summary completed")
print()

print("=" * 70)
print("ALL TESTS PASSED! ✓")
print("=" * 70)
print()
print("The distribution_comparison_milestone.py script is working correctly.")
print("You can now run it interactively with:")
print("  python scripts/distribution_comparison_milestone.py")
