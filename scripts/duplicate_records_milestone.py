"""
Duplicate Records Detection and Removal Milestone
==================================================
This script demonstrates how to identify and remove duplicate records
in Pandas DataFrames to ensure data quality and integrity.
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("DUPLICATE RECORDS DETECTION AND REMOVAL MILESTONE")
print("=" * 70)
print()

# ============================================================================
# 1. UNDERSTANDING DUPLICATE RECORDS
# ============================================================================
print("1. UNDERSTANDING DUPLICATE RECORDS")
print("-" * 70)
print()

print("What are duplicate records?")
print("- Rows that have identical values across all or selected columns")
print("- Can occur due to data entry errors, system glitches, or merging")
print("- May be exact duplicates or partial duplicates")
print()

# Load the dataset
df = pd.read_csv('data/raw/products.csv')

print("Original Dataset:")
print(df)
print()
print(f"Dataset shape: {df.shape}")
print(f"Total records: {len(df)}")
print()

# ============================================================================
# 2. DETECTING DUPLICATE ROWS
# ============================================================================
print("\n" + "=" * 70)
print("2. DETECTING DUPLICATE ROWS")
print("-" * 70)
print()

# Check for duplicates (returns boolean Series)
duplicates_mask = df.duplicated()
print("Boolean mask showing duplicate rows:")
print(duplicates_mask)
print()

# Count duplicates
num_duplicates = duplicates_mask.sum()
print(f"Number of duplicate rows: {num_duplicates}")
print(f"Percentage of duplicates: {(num_duplicates / len(df)) * 100:.2f}%")
print()

# Show which rows are duplicates
print("Rows marked as duplicates (keeps first occurrence):")
print(df[duplicates_mask])
print()

# Show all occurrences of duplicated records (including first)
duplicates_all = df.duplicated(keep=False)
print("All occurrences of duplicated records:")
print(df[duplicates_all].sort_values('ProductID'))
print()

# Detect duplicates keeping last occurrence
duplicates_keep_last = df.duplicated(keep='last')
print(f"Duplicates (keeping last): {duplicates_keep_last.sum()}")
print()

# ============================================================================
# 3. DETECTING DUPLICATES ON SPECIFIC COLUMNS
# ============================================================================
print("\n" + "=" * 70)
print("3. DETECTING DUPLICATES ON SPECIFIC COLUMNS")
print("-" * 70)
print()

# Check duplicates based on ProductID only
duplicates_by_id = df.duplicated(subset=['ProductID'])
print("Duplicates based on ProductID only:")
print(df[duplicates_by_id])
print(f"Count: {duplicates_by_id.sum()}")
print()

# Check duplicates based on multiple columns
duplicates_by_name_category = df.duplicated(subset=['ProductName', 'Category'])
print("Duplicates based on ProductName and Category:")
print(df[duplicates_by_name_category])
print(f"Count: {duplicates_by_name_category.sum()}")
print()

# ============================================================================
# 4. REMOVING DUPLICATE RECORDS
# ============================================================================
print("\n" + "=" * 70)
print("4. REMOVING DUPLICATE RECORDS")
print("-" * 70)
print()

print("Before deduplication:")
print(f"Shape: {df.shape}")
print(f"Total records: {len(df)}")
print()

# Remove duplicates (keeps first occurrence by default)
df_cleaned = df.drop_duplicates()

print("After deduplication (keeping first occurrence):")
print(df_cleaned)
print()
print(f"Shape: {df_cleaned.shape}")
print(f"Total records: {len(df_cleaned)}")
print(f"Records removed: {len(df) - len(df_cleaned)}")
print()

# Remove duplicates keeping last occurrence
df_cleaned_last = df.drop_duplicates(keep='last')
print("After deduplication (keeping last occurrence):")
print(f"Shape: {df_cleaned_last.shape}")
print()

# Remove duplicates based on specific columns
df_cleaned_by_id = df.drop_duplicates(subset=['ProductID'])
print("After deduplication based on ProductID only:")
print(df_cleaned_by_id)
print(f"Shape: {df_cleaned_by_id.shape}")
print()

# ============================================================================
# 5. VERIFYING DEDUPLICATION RESULTS
# ============================================================================
print("\n" + "=" * 70)
print("5. VERIFYING DEDUPLICATION RESULTS")
print("-" * 70)
print()

print("Verification Summary:")
print("-" * 70)
print(f"Original dataset size: {len(df)} rows")
print(f"Cleaned dataset size: {len(df_cleaned)} rows")
print(f"Duplicates removed: {len(df) - len(df_cleaned)} rows")
print(f"Reduction: {((len(df) - len(df_cleaned)) / len(df)) * 100:.2f}%")
print()

# Verify no duplicates remain
remaining_duplicates = df_cleaned.duplicated().sum()
print(f"Remaining duplicates in cleaned data: {remaining_duplicates}")
print()

# Compare unique values
print("Unique ProductIDs:")
print(f"Original: {df['ProductID'].nunique()}")
print(f"Cleaned: {df_cleaned['ProductID'].nunique()}")
print()

# Show the final cleaned dataset
print("Final Cleaned Dataset:")
print(df_cleaned)
print()

# ============================================================================
# 6. SAVING CLEANED DATA
# ============================================================================
print("\n" + "=" * 70)
print("6. SAVING CLEANED DATA")
print("-" * 70)
print()

# Save to processed folder
output_path = 'data/processed/products_cleaned.csv'
df_cleaned.to_csv(output_path, index=False)
print(f"Cleaned data saved to: {output_path}")
print()

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("-" * 70)
print()
print("✓ duplicated() identifies duplicate rows (returns boolean mask)")
print("✓ drop_duplicates() removes duplicate rows")
print("✓ keep parameter controls which duplicate to retain ('first', 'last', False)")
print("✓ subset parameter allows checking specific columns")
print("✓ Always verify results after deduplication")
print("✓ Deduplication improves data quality and analysis accuracy")
print()
print("=" * 70)
print("MILESTONE COMPLETE!")
print("=" * 70)
