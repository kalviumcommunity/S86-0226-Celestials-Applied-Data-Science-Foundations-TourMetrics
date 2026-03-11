# Duplicate Records Detection and Removal Milestone

## Overview
This milestone demonstrates how to identify and remove duplicate records in Pandas DataFrames to ensure data quality and integrity.

## Learning Objectives
- Understand what duplicate records are
- Detect duplicate rows in a DataFrame
- Identify duplicates across all or selected columns
- Remove duplicates safely and intentionally
- Verify results after deduplication

## Dataset Used
**File:** `data/raw/products.csv`

The dataset contains product information with intentional duplicates:
- 14 total records
- 4 duplicate records
- Duplicates based on ProductID: 101, 102, 105

## Key Concepts

### 1. Understanding Duplicate Records
Duplicate records are rows with identical values across all or selected columns. They can occur due to:
- Data entry errors
- System glitches during data collection
- Merging datasets from multiple sources
- Import/export issues

### 2. Types of Duplicates
- **Exact duplicates:** All column values are identical
- **Partial duplicates:** Selected column values are identical
- **First occurrence:** The original record
- **Subsequent occurrences:** The duplicate copies

## Methods Used

### Detection Methods

#### `duplicated()`
Returns a boolean Series indicating duplicate rows.

**Parameters:**
- `subset`: Column(s) to check for duplicates
- `keep`: Which duplicates to mark
  - `'first'` (default): Mark duplicates except first occurrence
  - `'last'`: Mark duplicates except last occurrence
  - `False`: Mark all duplicates

**Examples:**
```python
# Detect all duplicates
df.duplicated()

# Detect duplicates based on specific columns
df.duplicated(subset=['ProductID'])

# Show all occurrences including first
df.duplicated(keep=False)
```

### Removal Methods

#### `drop_duplicates()`
Removes duplicate rows from DataFrame.

**Parameters:**
- `subset`: Column(s) to consider for identifying duplicates
- `keep`: Which duplicates to keep
  - `'first'` (default): Keep first occurrence
  - `'last'`: Keep last occurrence
  - `False`: Drop all duplicates
- `inplace`: Modify DataFrame in place (default: False)

**Examples:**
```python
# Remove duplicates (keep first)
df.drop_duplicates()

# Remove duplicates (keep last)
df.drop_duplicates(keep='last')

# Remove duplicates based on specific columns
df.drop_duplicates(subset=['ProductID'])
```

## Results

### Before Deduplication
- Total records: 14
- Unique ProductIDs: 10
- Duplicate records: 4

### After Deduplication
- Total records: 10
- Unique ProductIDs: 10
- Records removed: 4
- Reduction: 28.57%

### Verification
- Remaining duplicates: 0
- Data integrity: Preserved
- All unique products retained

## Best Practices

1. **Always inspect before removing**
   - Use `duplicated()` to identify duplicates first
   - Examine duplicate records to understand why they exist
   - Decide which occurrence to keep

2. **Choose appropriate columns**
   - Use `subset` parameter for partial duplicate detection
   - Consider business logic when selecting columns
   - Primary keys should be unique

3. **Verify results**
   - Compare dataset shape before and after
   - Check for remaining duplicates
   - Ensure important records are retained

4. **Document decisions**
   - Record why duplicates were removed
   - Note which occurrence was kept
   - Track the impact on dataset size

5. **Save cleaned data**
   - Store deduplicated data separately
   - Preserve original data for reference
   - Use descriptive filenames

## Common Pitfalls to Avoid

❌ Removing duplicates without inspection
❌ Losing important information during cleanup
❌ Not verifying results after deduplication
❌ Assuming all duplicates are errors
❌ Forgetting to save cleaned data

## Key Takeaways

✓ `duplicated()` identifies duplicate rows (returns boolean mask)
✓ `drop_duplicates()` removes duplicate rows
✓ `keep` parameter controls which duplicate to retain
✓ `subset` parameter allows checking specific columns
✓ Always verify results after deduplication
✓ Deduplication improves data quality and analysis accuracy

## Files Created

1. **Script:** `scripts/duplicate_records_milestone.py`
   - Comprehensive demonstration with detailed output
   - All detection and removal methods
   - Verification steps

2. **Notebook:** `notebooks/duplicate_records_milestone.ipynb`
   - Interactive exploration
   - Step-by-step execution
   - Visual verification

3. **Dataset:** `data/raw/products.csv`
   - Sample data with duplicates
   - Realistic product information

4. **Cleaned Data:** `data/processed/products_cleaned.csv`
   - Deduplicated dataset
   - Ready for analysis

## Running the Code

### Python Script
```bash
python scripts/duplicate_records_milestone.py
```

### Jupyter Notebook
```bash
jupyter notebook notebooks/duplicate_records_milestone.ipynb
```

## Next Steps

After completing this milestone, you can:
- Apply deduplication to your own datasets
- Combine with missing value detection for comprehensive cleaning
- Use cleaned data for accurate analysis
- Build data quality pipelines

## Additional Resources

- [Pandas duplicated() Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
- [Pandas drop_duplicates() Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)
- [Handling Duplicate Data in Pandas](https://realpython.com/pandas-python-explore-dataset/#removing-duplicate-data)

---

**Milestone Status:** ✓ Complete

This milestone ensures you can detect and eliminate duplicates confidently while preserving data integrity.
