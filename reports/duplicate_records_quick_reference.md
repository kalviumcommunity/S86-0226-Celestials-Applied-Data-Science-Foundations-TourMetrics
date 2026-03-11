# Duplicate Records Quick Reference

## Detection

### Check for duplicates
```python
df.duplicated()  # Returns boolean Series
```

### Count duplicates
```python
df.duplicated().sum()  # Number of duplicates
```

### Show duplicate rows
```python
df[df.duplicated()]  # Display duplicates
```

### Show all occurrences
```python
df[df.duplicated(keep=False)]  # Include first occurrence
```

### Check specific columns
```python
df.duplicated(subset=['column1', 'column2'])
```

## Removal

### Remove duplicates (keep first)
```python
df.drop_duplicates()
```

### Remove duplicates (keep last)
```python
df.drop_duplicates(keep='last')
```

### Remove all duplicates
```python
df.drop_duplicates(keep=False)
```

### Remove based on specific columns
```python
df.drop_duplicates(subset=['ProductID'])
```

### Remove in place
```python
df.drop_duplicates(inplace=True)
```

## Verification

### Check shape
```python
print(f"Before: {df.shape}")
print(f"After: {df_cleaned.shape}")
```

### Verify no duplicates remain
```python
df_cleaned.duplicated().sum()  # Should be 0
```

### Compare unique counts
```python
print(f"Original unique: {df['column'].nunique()}")
print(f"Cleaned unique: {df_cleaned['column'].nunique()}")
```

## Parameters

### `keep` parameter
- `'first'`: Keep first occurrence (default)
- `'last'`: Keep last occurrence
- `False`: Drop all duplicates

### `subset` parameter
- `None`: Check all columns (default)
- `['col1']`: Check single column
- `['col1', 'col2']`: Check multiple columns

## Common Patterns

### Inspect then remove
```python
# 1. Detect
duplicates = df.duplicated()
print(f"Found {duplicates.sum()} duplicates")

# 2. Inspect
print(df[duplicates])

# 3. Remove
df_cleaned = df.drop_duplicates()

# 4. Verify
print(f"Removed {len(df) - len(df_cleaned)} records")
```

### Remove by ID, keep latest
```python
df_cleaned = df.drop_duplicates(subset=['ID'], keep='last')
```

### Find duplicates in specific columns
```python
# Find products with same name but different IDs
name_dupes = df[df.duplicated(subset=['ProductName'], keep=False)]
print(name_dupes.sort_values('ProductName'))
```

## Best Practices

✓ Always inspect duplicates before removing
✓ Use `subset` for partial duplicate detection
✓ Verify results after deduplication
✓ Save cleaned data separately
✓ Document deduplication decisions

## Quick Workflow

```python
import pandas as pd

# 1. Load data
df = pd.read_csv('data.csv')

# 2. Check for duplicates
print(f"Duplicates: {df.duplicated().sum()}")

# 3. Inspect duplicates
print(df[df.duplicated(keep=False)])

# 4. Remove duplicates
df_cleaned = df.drop_duplicates()

# 5. Verify
print(f"Remaining duplicates: {df_cleaned.duplicated().sum()}")

# 6. Save
df_cleaned.to_csv('data_cleaned.csv', index=False)
```
