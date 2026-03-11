"""
Quick Test Script for Histogram Visualization
==============================================
This script quickly tests that the histogram visualization functions work correctly.
Run this before recording your video to ensure everything is set up properly.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def test_data_loading():
    """Test that data loads correctly."""
    print("=" * 60)
    print("TEST 1: Data Loading")
    print("=" * 60)
    
    try:
        df = pd.read_csv('data/raw/tours.csv')
        print(f"✓ Data loaded successfully: {len(df)} rows")
        print(f"✓ Columns: {df.columns.tolist()}")
        
        # Check for numeric columns
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        print(f"✓ Numeric columns found: {numeric_cols}")
        
        return df
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None


def test_histogram_creation(df):
    """Test that histograms can be created."""
    print("\n" + "=" * 60)
    print("TEST 2: Histogram Creation")
    print("=" * 60)
    
    try:
        # Convert to numeric, coercing errors to NaN, then drop NaN
        visitors_numeric = pd.to_numeric(df['Visitors'], errors='coerce')
        
        # Create a simple histogram
        plt.figure(figsize=(8, 5))
        plt.hist(visitors_numeric.dropna(), bins=10, color='steelblue', 
                 edgecolor='black', alpha=0.7)
        plt.xlabel('Visitors')
        plt.ylabel('Frequency')
        plt.title('Test Histogram')
        plt.close()  # Don't display, just test
        
        print("✓ Histogram created successfully")
        return True
    except Exception as e:
        print(f"✗ Error creating histogram: {e}")
        return False


def test_statistics(df):
    """Test that statistics can be calculated."""
    print("\n" + "=" * 60)
    print("TEST 3: Statistical Calculations")
    print("=" * 60)
    
    try:
        # Convert to numeric, coercing errors to NaN
        visitors_numeric = pd.to_numeric(df['Visitors'], errors='coerce')
        visitors_clean = visitors_numeric.dropna()
        
        if len(visitors_clean) == 0:
            print("✗ No valid numeric data found in Visitors column")
            return False
        
        mean_val = visitors_clean.mean()
        median_val = visitors_clean.median()
        std_val = visitors_clean.std()
        skewness = visitors_clean.skew()
        
        print(f"✓ Valid data points: {len(visitors_clean)} (dropped {len(df) - len(visitors_clean)} invalid)")
        print(f"✓ Mean:     {mean_val:.2f}")
        print(f"✓ Median:   {median_val:.2f}")
        print(f"✓ Std Dev:  {std_val:.2f}")
        print(f"✓ Skewness: {skewness:.3f}")
        
        return True
    except Exception as e:
        print(f"✗ Error calculating statistics: {e}")
        return False


def test_output_directory():
    """Test that output directory exists."""
    print("\n" + "=" * 60)
    print("TEST 4: Output Directory")
    print("=" * 60)
    
    output_dir = 'outputs/visualizations'
    
    if os.path.exists(output_dir):
        print(f"✓ Output directory exists: {output_dir}")
        return True
    else:
        print(f"✗ Output directory missing: {output_dir}")
        print("  Creating directory...")
        try:
            os.makedirs(output_dir, exist_ok=True)
            print(f"✓ Created: {output_dir}")
            return True
        except Exception as e:
            print(f"✗ Could not create directory: {e}")
            return False


def test_save_histogram(df):
    """Test that histograms can be saved to file."""
    print("\n" + "=" * 60)
    print("TEST 5: Saving Histogram")
    print("=" * 60)
    
    try:
        # Convert to numeric, coercing errors to NaN
        visitors_numeric = pd.to_numeric(df['Visitors'], errors='coerce')
        
        plt.figure(figsize=(8, 5))
        plt.hist(visitors_numeric.dropna(), bins=10, color='steelblue', 
                 edgecolor='black', alpha=0.7)
        plt.xlabel('Visitors')
        plt.ylabel('Frequency')
        plt.title('Test Histogram')
        
        test_file = 'outputs/visualizations/test_histogram.png'
        plt.savefig(test_file, dpi=150, bbox_inches='tight')
        plt.close()
        
        if os.path.exists(test_file):
            print(f"✓ Histogram saved successfully: {test_file}")
            return True
        else:
            print(f"✗ File not created: {test_file}")
            return False
    except Exception as e:
        print(f"✗ Error saving histogram: {e}")
        return False


def run_all_tests():
    """Run all tests and report results."""
    print("\n")
    print("*" * 60)
    print("HISTOGRAM VISUALIZATION - QUICK TEST")
    print("*" * 60)
    print()
    
    results = []
    
    # Test 1: Load data
    df = test_data_loading()
    results.append(df is not None)
    
    if df is None:
        print("\n✗ Cannot continue - data loading failed")
        return False
    
    # Test 2: Create histogram
    results.append(test_histogram_creation(df))
    
    # Test 3: Statistics
    results.append(test_statistics(df))
    
    # Test 4: Output directory
    results.append(test_output_directory())
    
    # Test 5: Save histogram
    results.append(test_save_histogram(df))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests Passed: {passed}/{total}")
    print()
    
    if passed == total:
        print("✓ ALL TESTS PASSED!")
        print()
        print("You are ready to:")
        print("  1. Run the main script: python scripts/histogram_visualization_milestone.py")
        print("  2. Use the Jupyter notebook: notebooks/histogram_visualization_milestone.ipynb")
        print("  3. Record your video demonstration")
        print()
    else:
        print("✗ Some tests failed")
        print()
        print("Please fix the issues above before proceeding.")
        print()
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
