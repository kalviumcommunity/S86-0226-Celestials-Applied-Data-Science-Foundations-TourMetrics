"""
Quick Test Script for Boxplot Visualization
==========================================
This script quickly tests that the boxplot visualization functions work correctly.
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
        
        # Convert numeric columns
        df['Visitors'] = pd.to_numeric(df['Visitors'], errors='coerce')
        df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
        df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
        
        # Check for numeric columns
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        print(f"✓ Numeric columns found: {numeric_cols}")
        
        return df
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None


def test_basic_boxplot(df):
    """Test that a basic boxplot can be created."""
    print("\n" + "=" * 60)
    print("TEST 2: Basic Boxplot Creation")
    print("=" * 60)
    
    try:
        # Create a simple boxplot
        fig, ax = plt.subplots(figsize=(8, 5))
        data = df['Visitors'].dropna()
        
        bp = ax.boxplot(data, vert=True, patch_artist=True)
        bp['boxes'][0].set_facecolor('steelblue')
        bp['boxes'][0].set_alpha(0.7)
        
        ax.set_ylabel('Visitors')
        ax.set_title('Test Boxplot')
        
        plt.close(fig)
        print("✓ Basic boxplot created successfully")
        
        # Check data
        print(f"✓ Data points: {len(data)}")
        print(f"✓ Median: {data.median():.1f}")
        print(f"✓ Q1: {data.quantile(0.25):.1f}")
        print(f"✓ Q3: {data.quantile(0.75):.1f}")
        
        return True
    except Exception as e:
        print(f"✗ Error creating boxplot: {e}")
        return False


def test_multiple_boxplots(df):
    """Test that multiple boxplots can be compared."""
    print("\n" + "=" * 60)
    print("TEST 3: Multiple Boxplots Comparison")
    print("=" * 60)
    
    try:
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        columns = ['Visitors', 'Revenue', 'Rating']
        for idx, col in enumerate(columns):
            data = df[col].dropna()
            axes[idx].boxplot(data, vert=True)
            axes[idx].set_title(col)
        
        plt.close(fig)
        print("✓ Multiple boxplots created successfully")
        
        for col in columns:
            data = df[col].dropna()
            print(f"✓ {col}: {len(data)} values, median={data.median():.1f}")
        
        return True
    except Exception as e:
        print(f"✗ Error creating multiple boxplots: {e}")
        return False


def test_outlier_detection(df):
    """Test that outliers can be detected."""
    print("\n" + "=" * 60)
    print("TEST 4: Outlier Detection")
    print("=" * 60)
    
    try:
        data = df['Revenue'].dropna()
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = data[(data < lower_bound) | (data > upper_bound)]
        
        print(f"✓ Q1: ${Q1:.2f}")
        print(f"✓ Q3: ${Q3:.2f}")
        print(f"✓ IQR: ${IQR:.2f}")
        print(f"✓ Lower bound: ${lower_bound:.2f}")
        print(f"✓ Upper bound: ${upper_bound:.2f}")
        print(f"✓ Outliers found: {len(outliers)}")
        
        if len(outliers) > 0:
            print(f"  Values: {outliers.values}")
        
        return True
    except Exception as e:
        print(f"✗ Error detecting outliers: {e}")
        return False


def test_output_directory():
    """Test that output directory exists."""
    print("\n" + "=" * 60)
    print("TEST 5: Output Directory")
    print("=" * 60)
    
    output_dir = 'outputs/visualizations'
    
    if os.path.exists(output_dir):
        print(f"✓ Output directory exists: {output_dir}")
        return True
    else:
        try:
            os.makedirs(output_dir, exist_ok=True)
            print(f"✓ Output directory created: {output_dir}")
            return True
        except Exception as e:
            print(f"✗ Error creating output directory: {e}")
            return False


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("BOXPLOT VISUALIZATION - TEST SUITE")
    print("=" * 60)
    print()
    
    results = []
    
    # Test 1: Data loading
    df = test_data_loading()
    results.append(df is not None)
    
    if df is None:
        print("\n✗ FAILED: Cannot proceed without data")
        return False
    
    # Test 2: Basic boxplot
    results.append(test_basic_boxplot(df))
    
    # Test 3: Multiple boxplots
    results.append(test_multiple_boxplots(df))
    
    # Test 4: Outlier detection
    results.append(test_outlier_detection(df))
    
    # Test 5: Output directory
    results.append(test_output_directory())
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    total_tests = len(results)
    passed_tests = sum(results)
    
    print(f"Tests passed: {passed_tests}/{total_tests}")
    
    if all(results):
        print("\n✅ ALL TESTS PASSED!")
        print("\nYou're ready to run the main milestone script:")
        print("  python scripts/boxplot_visualization_milestone.py")
        print("\nOr work with the notebook:")
        print("  notebooks/boxplot_visualization_milestone.ipynb")
        return True
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("Please fix the issues above before proceeding.")
        return False


if __name__ == "__main__":
    # Change to project root directory if needed
    if not os.path.exists('data/raw/tours.csv'):
        if os.path.exists('../data/raw/tours.csv'):
            os.chdir('..')
            print("Changed to project root directory\n")
        else:
            print("ERROR: Cannot find data/raw/tours.csv")
            print("Please run this script from the project root directory")
            sys.exit(1)
    
    success = run_all_tests()
    sys.exit(0 if success else 1)
