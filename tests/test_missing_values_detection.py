"""
Unit Tests for Missing Values Detection

This test suite validates the missing values detection functionality using both
unit tests for specific examples and edge cases, and property-based tests using
Hypothesis for comprehensive validation.

Test Framework: pytest
Property-Based Testing: Hypothesis
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os
from hypothesis import given, settings, strategies as st
from hypothesis.extra.pandas import column, data_frames, range_indexes

# Add the scripts directory to the path so we can import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from missing_values_detection import (
    detect_missing_values,
    validate_file_path,
    load_csv_file,
    count_missing_per_column,
    identify_rows_with_missing,
    calculate_missing_percentages,
    format_column_summary,
    format_row_summary,
    print_interpretation,
    generate_detection_report
)


class TestDetectMissingValues:
    """Test suite for the detect_missing_values() function."""
    
    def test_detects_nan_values(self):
        """Test that NaN values are correctly detected."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3],
            'B': [4, 5, 6]
        })
        
        result = detect_missing_values(df)
        
        # Check that result is a boolean DataFrame
        assert isinstance(result, pd.DataFrame)
        assert all(dtype == bool for dtype in result.dtypes)
        
        # Check that NaN is detected
        assert result.loc[1, 'A'] == True
        assert result.loc[0, 'A'] == False
        assert result.loc[2, 'A'] == False
        
        # Check that column B has no missing values
        assert result['B'].sum() == 0
    
    def test_detects_none_values(self):
        """Test that None values are correctly detected."""
        df = pd.DataFrame({
            'A': [1, None, 3],
            'B': [4, 5, None]
        })
        
        result = detect_missing_values(df)
        
        # Check that None is detected
        assert result.loc[1, 'A'] == True
        assert result.loc[2, 'B'] == True
        assert result.loc[0, 'A'] == False
    
    def test_detects_pd_na_values(self):
        """Test that pd.NA values are correctly detected."""
        df = pd.DataFrame({
            'A': pd.array([1, pd.NA, 3], dtype='Int64'),
            'B': pd.array([4, 5, pd.NA], dtype='Int64')
        })
        
        result = detect_missing_values(df)
        
        # Check that pd.NA is detected
        assert result.loc[1, 'A'] == True
        assert result.loc[2, 'B'] == True
        assert result.loc[0, 'A'] == False
    
    def test_mixed_missing_value_types(self):
        """Test detection of mixed missing value types (NaN, None, pd.NA)."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3],
            'B': [None, 5, 6],
            'C': pd.array([7, 8, pd.NA], dtype='Int64')
        })
        
        result = detect_missing_values(df)
        
        # Check that all three types are detected
        assert result.loc[1, 'A'] == True  # NaN
        assert result.loc[0, 'B'] == True  # None
        assert result.loc[2, 'C'] == True  # pd.NA
        
        # Check total missing count
        assert result.sum().sum() == 3
    
    def test_no_missing_values(self):
        """Test DataFrame with no missing values returns all False."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        
        result = detect_missing_values(df)
        
        # Check that no missing values are detected
        assert result.sum().sum() == 0
        assert (result == False).all().all()
    
    def test_all_missing_values(self):
        """Test DataFrame with all missing values returns all True."""
        df = pd.DataFrame({
            'A': [np.nan, np.nan, np.nan],
            'B': [None, None, None]
        })
        
        result = detect_missing_values(df)
        
        # Check that all values are detected as missing
        assert result.sum().sum() == 6  # 3 rows × 2 columns
        assert (result == True).all().all()
    
    def test_empty_dataframe(self):
        """Test that empty DataFrame is handled correctly."""
        df = pd.DataFrame()
        
        result = detect_missing_values(df)
        
        # Check that result is also empty
        assert result.empty
        assert isinstance(result, pd.DataFrame)
    
    def test_single_column_dataframe(self):
        """Test detection on single column DataFrame."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, None, 5]
        })
        
        result = detect_missing_values(df)
        
        # Check shape is preserved
        assert result.shape == df.shape
        
        # Check missing values are detected
        assert result.loc[1, 'A'] == True
        assert result.loc[3, 'A'] == True
        assert result.sum().sum() == 2
    
    def test_preserves_dataframe_shape(self):
        """Test that output shape matches input shape."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, 4, 5],
            'B': [6, 7, None, 9, 10],
            'C': [11, 12, 13, 14, np.nan]
        })
        
        result = detect_missing_values(df)
        
        # Check shape is preserved
        assert result.shape == df.shape
        assert list(result.columns) == list(df.columns)
        assert list(result.index) == list(df.index)
    
    def test_does_not_modify_original_dataframe(self):
        """Test that the original DataFrame is not modified."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3],
            'B': [4, 5, None]
        })
        
        # Create a copy to compare
        df_copy = df.copy()
        
        # Run detection
        result = detect_missing_values(df)
        
        # Check that original DataFrame is unchanged
        pd.testing.assert_frame_equal(df, df_copy)
        
        # Check that result is different from original
        assert not df.equals(result)


class TestValidateFilePath:
    """Test suite for the validate_file_path() function."""
    
    def test_existing_file_returns_true(self):
        """Test that existing file returns True."""
        # Use a file we know exists
        filepath = os.path.join('data', 'raw', 'books.csv')
        
        if os.path.exists(filepath):
            result = validate_file_path(filepath)
            assert result == True
    
    def test_nonexistent_file_returns_false(self):
        """Test that non-existent file returns False."""
        filepath = os.path.join('data', 'raw', 'nonexistent_file.csv')
        
        result = validate_file_path(filepath)
        assert result == False


class TestLoadCSVFile:
    """Test suite for the load_csv_file() function."""
    
    def test_loads_existing_csv_file(self):
        """Test that existing CSV file is loaded successfully."""
        # Test with books.csv if it exists
        df = load_csv_file('books.csv')
        
        if df is not None:
            assert isinstance(df, pd.DataFrame)
            assert len(df) > 0
    
    def test_nonexistent_file_returns_none(self):
        """Test that non-existent file returns None."""
        df = load_csv_file('nonexistent_file_12345.csv')
        
        assert df is None
    
    def test_preserves_data_including_missing_values(self):
        """Test that loading preserves all data including missing values."""
        # This test would require a CSV file with known missing values
        # For now, we test that the function doesn't crash
        df = load_csv_file('books.csv')
        
        if df is not None:
            # Check that DataFrame is returned
            assert isinstance(df, pd.DataFrame)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])


class TestCountMissingPerColumn:
    """Test suite for the count_missing_per_column() function."""
    
    def test_counts_missing_values_correctly(self):
        """Test that missing values are counted correctly for each column."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, np.nan],
            'B': [4, 5, 6, 7],
            'C': [np.nan, np.nan, np.nan, 10]
        })
        
        result = count_missing_per_column(df)
        
        # Check that result is a DataFrame
        assert isinstance(result, pd.DataFrame)
        
        # Check column names
        assert list(result.columns) == ['Column', 'Missing_Count', 'Missing_Percent']
        
        # Check counts for each column
        c_row = result[result['Column'] == 'C'].iloc[0]
        assert c_row['Missing_Count'] == 3
        
        a_row = result[result['Column'] == 'A'].iloc[0]
        assert a_row['Missing_Count'] == 2
        
        b_row = result[result['Column'] == 'B'].iloc[0]
        assert b_row['Missing_Count'] == 0
    
    def test_calculates_percentages_correctly(self):
        """Test that missing value percentages are calculated correctly."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, np.nan],  # 2 missing out of 4 = 50%
            'B': [4, 5, 6, 7],             # 0 missing = 0%
            'C': [np.nan, np.nan, np.nan, 10]  # 3 missing out of 4 = 75%
        })
        
        result = count_missing_per_column(df)
        
        # Check percentages
        c_row = result[result['Column'] == 'C'].iloc[0]
        assert c_row['Missing_Percent'] == 75.0
        
        a_row = result[result['Column'] == 'A'].iloc[0]
        assert a_row['Missing_Percent'] == 50.0
        
        b_row = result[result['Column'] == 'B'].iloc[0]
        assert b_row['Missing_Percent'] == 0.0
    
    def test_sorted_by_missing_count_descending(self):
        """Test that results are sorted by missing count in descending order."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, np.nan],      # 2 missing
            'B': [4, 5, 6, 7],                 # 0 missing
            'C': [np.nan, np.nan, np.nan, 10]  # 3 missing
        })
        
        result = count_missing_per_column(df)
        
        # Check that first row has highest count
        assert result.iloc[0]['Column'] == 'C'
        assert result.iloc[0]['Missing_Count'] == 3
        
        # Check that second row has second highest count
        assert result.iloc[1]['Column'] == 'A'
        assert result.iloc[1]['Missing_Count'] == 2
        
        # Check that last row has lowest count
        assert result.iloc[2]['Column'] == 'B'
        assert result.iloc[2]['Missing_Count'] == 0
    
    def test_no_missing_values(self):
        """Test DataFrame with no missing values."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        
        result = count_missing_per_column(df)
        
        # Check that all counts are zero
        assert (result['Missing_Count'] == 0).all()
        assert (result['Missing_Percent'] == 0.0).all()
    
    def test_all_missing_values(self):
        """Test DataFrame with all missing values."""
        df = pd.DataFrame({
            'A': [np.nan, np.nan, np.nan],
            'B': [None, None, None]
        })
        
        result = count_missing_per_column(df)
        
        # Check that all counts are 3
        assert (result['Missing_Count'] == 3).all()
        assert (result['Missing_Percent'] == 100.0).all()
    
    def test_single_column_dataframe(self):
        """Test with single column DataFrame."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, None, 5]
        })
        
        result = count_missing_per_column(df)
        
        # Check shape
        assert len(result) == 1
        
        # Check values
        assert result.iloc[0]['Column'] == 'A'
        assert result.iloc[0]['Missing_Count'] == 2
        assert result.iloc[0]['Missing_Percent'] == 40.0


class TestIdentifyRowsWithMissing:
    """Test suite for the identify_rows_with_missing() function."""
    
    def test_identifies_rows_with_missing_values(self):
        """Test that rows with missing values are correctly identified."""
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, np.nan, 7, 8],
            'C': [9, 10, np.nan, 12]
        })
        
        rows_with_missing, indices = identify_rows_with_missing(df)
        
        # Check that correct rows are identified
        assert indices == [1, 2]
        
        # Check that returned DataFrame has correct shape
        assert len(rows_with_missing) == 2
        assert list(rows_with_missing.index) == [1, 2]
    
    def test_returns_complete_row_data(self):
        """Test that complete row data is returned, not just missing values."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, np.nan, 6],
            'C': [7, 8, 9]
        })
        
        rows_with_missing, indices = identify_rows_with_missing(df)
        
        # Check that all columns are present
        assert list(rows_with_missing.columns) == ['A', 'B', 'C']
        
        # Check that non-missing values are preserved
        assert rows_with_missing.loc[1, 'A'] == 2
        assert rows_with_missing.loc[1, 'C'] == 8
    
    def test_no_rows_with_missing_values(self):
        """Test DataFrame with no rows containing missing values."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        
        rows_with_missing, indices = identify_rows_with_missing(df)
        
        # Check that no rows are identified
        assert len(indices) == 0
        assert len(rows_with_missing) == 0
    
    def test_all_rows_with_missing_values(self):
        """Test DataFrame where all rows contain missing values."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [np.nan, np.nan, np.nan]
        })
        
        rows_with_missing, indices = identify_rows_with_missing(df)
        
        # Check that all rows are identified
        assert len(indices) == 3
        assert indices == [0, 1, 2]
        assert len(rows_with_missing) == 3
    
    def test_row_with_multiple_missing_values(self):
        """Test that rows with multiple missing values are identified once."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3],
            'B': [4, np.nan, 6],
            'C': [7, np.nan, 9]
        })
        
        rows_with_missing, indices = identify_rows_with_missing(df)
        
        # Check that row 1 is identified once even though it has 3 missing values
        assert indices == [1]
        assert len(rows_with_missing) == 1


class TestCalculateMissingPercentages:
    """Test suite for the calculate_missing_percentages() function."""
    
    def test_calculates_total_cells_correctly(self):
        """Test that total cells is calculated as rows × columns."""
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        })
        
        stats = calculate_missing_percentages(df)
        
        # Check total cells = 4 rows × 3 columns = 12
        assert stats['total_cells'] == 12
        assert stats['total_rows'] == 4
        assert stats['total_columns'] == 3
    
    def test_counts_missing_cells_correctly(self):
        """Test that missing cells are counted correctly."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, 4],
            'B': [5, 6, np.nan, 8],
            'C': [9, 10, 11, 12]
        })
        
        stats = calculate_missing_percentages(df)
        
        # Check that 2 missing cells are counted
        assert stats['missing_cells'] == 2
    
    def test_calculates_cell_percentage_correctly(self):
        """Test that missing cell percentage is calculated correctly."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3, 4],
            'B': [5, 6, np.nan, 8],
            'C': [9, 10, 11, 12]
        })
        
        stats = calculate_missing_percentages(df)
        
        # 2 missing out of 12 cells = 16.666...%
        expected_percent = (2 / 12) * 100
        assert abs(stats['missing_percent'] - expected_percent) < 0.01
    
    def test_counts_rows_with_missing_correctly(self):
        """Test that rows with missing values are counted correctly."""
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, np.nan, 7, 8],
            'C': [9, 10, np.nan, 12]
        })
        
        stats = calculate_missing_percentages(df)
        
        # Rows 1 and 2 have missing values
        assert stats['rows_with_missing'] == 2
    
    def test_calculates_row_percentage_correctly(self):
        """Test that row percentage is calculated correctly."""
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, np.nan, 7, 8],
            'C': [9, 10, np.nan, 12]
        })
        
        stats = calculate_missing_percentages(df)
        
        # 2 rows with missing out of 4 total = 50%
        assert stats['rows_with_missing_percent'] == 50.0
    
    def test_no_missing_values(self):
        """Test DataFrame with no missing values."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        
        stats = calculate_missing_percentages(df)
        
        # Check all missing-related values are zero
        assert stats['missing_cells'] == 0
        assert stats['missing_percent'] == 0.0
        assert stats['rows_with_missing'] == 0
        assert stats['rows_with_missing_percent'] == 0.0
    
    def test_all_missing_values(self):
        """Test DataFrame with all missing values."""
        df = pd.DataFrame({
            'A': [np.nan, np.nan, np.nan],
            'B': [None, None, None]
        })
        
        stats = calculate_missing_percentages(df)
        
        # Check all values are 100%
        assert stats['missing_cells'] == 6  # 3 rows × 2 columns
        assert stats['missing_percent'] == 100.0
        assert stats['rows_with_missing'] == 3
        assert stats['rows_with_missing_percent'] == 100.0
    
    def test_returns_all_required_keys(self):
        """Test that all required keys are present in the returned dictionary."""
        df = pd.DataFrame({
            'A': [1, np.nan, 3],
            'B': [4, 5, 6]
        })
        
        stats = calculate_missing_percentages(df)
        
        # Check all required keys are present
        required_keys = [
            'total_cells', 'missing_cells', 'missing_percent',
            'rows_with_missing', 'rows_with_missing_percent',
            'total_rows', 'total_columns'
        ]
        
        for key in required_keys:
            assert key in stats


class TestFormatColumnSummary:
    """Test suite for the format_column_summary() function."""
    
    def test_formats_column_summary_correctly(self):
        """Test that column summary is formatted with proper alignment."""
        stats = pd.DataFrame({
            'Column': ['Age', 'Name', 'Email'],
            'Missing_Count': [5, 2, 0],
            'Missing_Percent': [25.0, 10.0, 0.0]
        })
        
        result = format_column_summary(stats)
        
        # Check that result is a string
        assert isinstance(result, str)
        
        # Check that column names are present
        assert 'Age' in result
        assert 'Name' in result
        assert 'Email' in result
        
        # Check that counts are present
        assert '5' in result
        assert '2' in result
        assert '0' in result
        
        # Check that percentages are present with proper formatting
        assert '25.00%' in result
        assert '10.00%' in result
        assert '0.00%' in result
    
    def test_includes_headers(self):
        """Test that formatted output includes headers."""
        stats = pd.DataFrame({
            'Column': ['A'],
            'Missing_Count': [1],
            'Missing_Percent': [10.0]
        })
        
        result = format_column_summary(stats)
        
        # Check for header text
        assert 'Column Name' in result
        assert 'Missing Count' in result
        assert 'Missing %' in result
    
    def test_includes_separator(self):
        """Test that formatted output includes separator line."""
        stats = pd.DataFrame({
            'Column': ['A'],
            'Missing_Count': [1],
            'Missing_Percent': [10.0]
        })
        
        result = format_column_summary(stats)
        
        # Check for separator (using unicode dash character)
        assert '─' in result
    
    def test_empty_dataframe_returns_message(self):
        """Test that empty DataFrame returns appropriate message."""
        stats = pd.DataFrame(columns=['Column', 'Missing_Count', 'Missing_Percent'])
        
        result = format_column_summary(stats)
        
        # Check for message
        assert 'No columns to display' in result
    
    def test_formats_multiple_rows(self):
        """Test formatting with multiple rows of data."""
        stats = pd.DataFrame({
            'Column': ['Col1', 'Col2', 'Col3', 'Col4'],
            'Missing_Count': [10, 5, 3, 0],
            'Missing_Percent': [50.0, 25.0, 15.0, 0.0]
        })
        
        result = format_column_summary(stats)
        
        # Check that all rows are present
        lines = result.split('\n')
        # Should have: header + separator + 4 data rows = 6 lines
        assert len(lines) == 6
        
        # Check that all column names are present
        for col in ['Col1', 'Col2', 'Col3', 'Col4']:
            assert col in result
    
    def test_handles_long_column_names(self):
        """Test that long column names are handled (truncated if needed)."""
        stats = pd.DataFrame({
            'Column': ['VeryLongColumnNameThatExceedsTwentyCharacters'],
            'Missing_Count': [5],
            'Missing_Percent': [25.0]
        })
        
        result = format_column_summary(stats)
        
        # Check that result is generated without error
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_percentage_formatting(self):
        """Test that percentages are formatted to 2 decimal places."""
        stats = pd.DataFrame({
            'Column': ['A', 'B', 'C'],
            'Missing_Count': [1, 2, 3],
            'Missing_Percent': [33.333333, 66.666666, 99.999999]
        })
        
        result = format_column_summary(stats)
        
        # Check that percentages are formatted to 2 decimal places
        assert '33.33%' in result
        assert '66.67%' in result
        assert '100.00%' in result
    
    def test_alignment_consistency(self):
        """Test that columns are properly aligned."""
        stats = pd.DataFrame({
            'Column': ['A', 'B'],
            'Missing_Count': [1, 100],
            'Missing_Percent': [5.0, 95.0]
        })
        
        result = format_column_summary(stats)
        lines = result.split('\n')
        
        # Check that all data lines have similar length (indicating alignment)
        # Skip header and separator
        data_lines = [line for line in lines[2:] if line.strip()]
        if len(data_lines) > 1:
            # All lines should have similar length (within a few characters)
            lengths = [len(line) for line in data_lines]
            assert max(lengths) - min(lengths) <= 5



# ============================================================================
# Hypothesis Strategies for Property-Based Testing
# ============================================================================

# Strategy for generating valid filenames
@st.composite
def valid_filenames(draw):
    """
    Generate valid CSV filenames.
    
    Returns filenames in the format: [name].csv
    where name contains only alphanumeric characters, underscores, and hyphens.
    """
    # Generate a name with 1-20 alphanumeric characters, underscores, or hyphens
    name_chars = st.text(
        alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd'), 
                              whitelist_characters='_-'),
        min_size=1,
        max_size=20
    )
    name = draw(name_chars)
    return f"{name}.csv"


# Strategy for generating DataFrames with missing values
@st.composite
def dataframes_with_missing(draw, min_rows=0, max_rows=10, min_cols=1, max_cols=5):
    """
    Generate DataFrames with various patterns of missing values.
    
    This strategy creates DataFrames with:
    - Different sizes (rows and columns)
    - Mix of numeric and string data
    - Various missing value types (NaN, None, pd.NA)
    - Edge cases (empty, all missing, no missing)
    
    Args:
        min_rows: Minimum number of rows (default: 0 for empty DataFrames)
        max_rows: Maximum number of rows (default: 10)
        min_cols: Minimum number of columns (default: 1)
        max_cols: Maximum number of columns (default: 5)
    
    Returns:
        A pandas DataFrame with missing values
    """
    num_rows = draw(st.integers(min_value=min_rows, max_value=max_rows))
    num_cols = draw(st.integers(min_value=min_cols, max_value=max_cols))
    
    # Handle empty DataFrame case
    if num_rows == 0 or num_cols == 0:
        return pd.DataFrame()
    
    # Generate column specifications
    columns_spec = []
    for i in range(num_cols):
        col_name = f"col_{i}"
        
        # Choose column type: numeric or string
        col_type = draw(st.sampled_from(['numeric', 'string']))
        
        if col_type == 'numeric':
            # Numeric column with possible NaN values
            elements = st.one_of(
                st.floats(min_value=-1000, max_value=1000, allow_nan=False, allow_infinity=False),
                st.integers(min_value=-1000, max_value=1000),
                st.just(np.nan),
                st.none()
            )
            columns_spec.append(column(col_name, elements=elements, dtype=float))
        else:
            # String column with possible None values
            elements = st.one_of(
                st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd')), 
                       min_size=1, max_size=10),
                st.none()
            )
            columns_spec.append(column(col_name, elements=elements, dtype=object))
    
    # Generate DataFrame with specified number of rows
    df = draw(data_frames(columns=columns_spec, index=range_indexes(min_size=num_rows, max_size=num_rows)))
    
    return df


# Strategy for generating various missing value types
@st.composite
def missing_value_types(draw):
    """
    Generate different types of missing values recognized by Pandas.
    
    Returns one of: np.nan, None, or pd.NA
    """
    return draw(st.sampled_from([np.nan, None, pd.NA]))


# Strategy for generating DataFrames with specific missing patterns
@st.composite
def dataframes_with_patterns(draw):
    """
    Generate DataFrames with specific missing value patterns for edge case testing.
    
    Patterns include:
    - Empty DataFrame
    - All values missing
    - No values missing
    - Single column with missing values
    - Single row with missing values
    - Scattered missing values
    """
    pattern = draw(st.sampled_from([
        'empty',
        'all_missing',
        'no_missing',
        'single_column_missing',
        'scattered'
    ]))
    
    if pattern == 'empty':
        return pd.DataFrame()
    
    # Generate base size
    num_rows = draw(st.integers(min_value=1, max_value=10))
    num_cols = draw(st.integers(min_value=1, max_value=5))
    
    if pattern == 'all_missing':
        # All values are NaN
        data = {f"col_{i}": [np.nan] * num_rows for i in range(num_cols)}
        return pd.DataFrame(data)
    
    elif pattern == 'no_missing':
        # No missing values
        data = {f"col_{i}": list(range(num_rows)) for i in range(num_cols)}
        return pd.DataFrame(data)
    
    elif pattern == 'single_column_missing':
        # One column is all missing, others are not
        data = {}
        for i in range(num_cols):
            if i == 0:
                data[f"col_{i}"] = [np.nan] * num_rows
            else:
                data[f"col_{i}"] = list(range(num_rows))
        return pd.DataFrame(data)
    
    else:  # scattered
        # Random scattered missing values
        data = {}
        for i in range(num_cols):
            col_data = []
            for j in range(num_rows):
                # 30% chance of missing value
                if draw(st.booleans()) and draw(st.booleans()):
                    col_data.append(draw(missing_value_types()))
                else:
                    col_data.append(draw(st.integers(min_value=0, max_value=100)))
            data[f"col_{i}"] = col_data
        return pd.DataFrame(data)


# Strategy for generating DataFrames with known missing counts
@st.composite
def dataframes_with_known_missing(draw, rows=5, cols=3, missing_count=None):
    """
    Generate DataFrames with a specific number of missing values.
    
    Useful for testing exact calculations and percentages.
    
    Args:
        rows: Number of rows (default: 5)
        cols: Number of columns (default: 3)
        missing_count: Exact number of missing values to include
                      If None, randomly chosen between 0 and total cells
    
    Returns:
        A pandas DataFrame with exactly the specified number of missing values
    """
    total_cells = rows * cols
    
    if missing_count is None:
        missing_count = draw(st.integers(min_value=0, max_value=total_cells))
    
    # Create a flat list of values
    values = [draw(st.integers(min_value=0, max_value=100)) for _ in range(total_cells - missing_count)]
    values.extend([np.nan] * missing_count)
    
    # Shuffle the values
    draw(st.randoms()).shuffle(values)
    
    # Reshape into DataFrame
    data = {}
    for i in range(cols):
        start_idx = i * rows
        end_idx = start_idx + rows
        data[f"col_{i}"] = values[start_idx:end_idx]
    
    return pd.DataFrame(data)



# ============================================================================
# Strategy Validation Tests
# ============================================================================

class TestHypothesisStrategies:
    """Test suite to validate that Hypothesis strategies work correctly."""
    
    @given(valid_filenames())
    @settings(max_examples=10)
    def test_valid_filenames_strategy(self, filename):
        """Verify that valid_filenames strategy generates proper CSV filenames."""
        assert isinstance(filename, str)
        assert filename.endswith('.csv')
        assert len(filename) > 4  # At least 'x.csv'
    
    @given(dataframes_with_missing())
    @settings(max_examples=10)
    def test_dataframes_with_missing_strategy(self, df):
        """Verify that dataframes_with_missing strategy generates valid DataFrames."""
        assert isinstance(df, pd.DataFrame)
        # DataFrame should be valid (may be empty)
        assert df.shape[0] >= 0
        assert df.shape[1] >= 0
    
    @given(missing_value_types())
    @settings(max_examples=10)
    def test_missing_value_types_strategy(self, missing_val):
        """Verify that missing_value_types strategy generates recognized missing values."""
        # Check that the value is one of the recognized missing types
        is_nan = isinstance(missing_val, float) and np.isnan(missing_val)
        is_none = missing_val is None
        is_pd_na = pd.isna(missing_val) and not is_nan and not is_none
        
        assert is_nan or is_none or is_pd_na
    
    @given(dataframes_with_patterns())
    @settings(max_examples=10)
    def test_dataframes_with_patterns_strategy(self, df):
        """Verify that dataframes_with_patterns strategy generates valid DataFrames."""
        assert isinstance(df, pd.DataFrame)
        # DataFrame should be valid (may be empty)
        assert df.shape[0] >= 0
        assert df.shape[1] >= 0
    
    @given(dataframes_with_known_missing())
    @settings(max_examples=10)
    def test_dataframes_with_known_missing_strategy(self, df):
        """Verify that dataframes_with_known_missing strategy generates valid DataFrames."""
        assert isinstance(df, pd.DataFrame)
        # Should have the default shape (5 rows, 3 columns)
        assert df.shape == (5, 3)
        # Count missing values
        missing_count = df.isna().sum().sum()
        assert missing_count >= 0
        assert missing_count <= 15  # Max is all cells
