# Pandas DataFrame Fundamentals - Quick Start Guide

## 🚀 Get Started in 5 Minutes

This guide helps you quickly complete the Pandas DataFrame Fundamentals milestone.

## 📋 Prerequisites

- Python 3.x installed
- Pandas library installed (`pip install pandas`)
- Jupyter Notebook (optional, for interactive work)

## 🎯 Three Ways to Learn

### Option 1: Run the Python Script (Fastest)

```bash
python scripts/pandas_dataframe_fundamentals.py
```

This will:
- Show you DataFrame concepts
- Create sample CSV files
- Demonstrate all inspection methods
- Display formatted output

**Time:** 2 minutes

### Option 2: Use the Jupyter Notebook (Interactive)

```bash
jupyter notebook notebooks/pandas_dataframe_fundamentals.ipynb
```

This allows you to:
- Run code cells interactively
- Modify examples
- Experiment with your own data
- See explanations alongside code

**Time:** 15-30 minutes

### Option 3: Follow the Quick Reference (Study)

Open `reports/pandas_dataframe_quick_reference.md` to:
- Review concepts at your own pace
- Copy code snippets
- Understand best practices
- Troubleshoot issues

**Time:** 10-15 minutes

## 📝 Essential Code Snippets

### Create DataFrame from Dictionary

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
```

### Load DataFrame from CSV

```python
df = pd.read_csv('data/raw/employees.csv')
print(df.head())
```

### Inspect DataFrame

```python
# Basic inspection
print(df.head())           # First 5 rows
print(df.shape)            # (rows, columns)
print(df.columns.tolist()) # Column names
print(df.dtypes)           # Data types

# Comprehensive overview
df.info()                  # Structure and types
df.describe()              # Statistics
```

## 🎥 Video Recording Checklist

Record a 2-minute video showing:

1. ✅ Create DataFrame from dictionary (30 sec)
2. ✅ Load DataFrame from CSV file (30 sec)
3. ✅ Inspect with head(), shape, dtypes (30 sec)
4. ✅ Explain why DataFrames matter (30 sec)

**Tips:**
- Increase font size (14pt+)
- Speak clearly and slowly
- Show outputs after each step
- Keep it under 2 minutes

## 📚 Files Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| `scripts/pandas_dataframe_fundamentals.py` | Complete working script | Quick demo, testing |
| `notebooks/pandas_dataframe_fundamentals.ipynb` | Interactive learning | Hands-on practice |
| `reports/pandas_dataframe_quick_reference.md` | Syntax reference | Quick lookup |
| `reports/pandas_dataframe_video_guide.md` | Video instructions | Recording prep |
| `reports/dataframe_milestone_checklist.md` | Completion tracking | Progress check |
| `reports/dataframe_milestone_summary.md` | Full overview | Understanding scope |

## ✅ Completion Checklist

Minimum requirements:

- [ ] Understand what a DataFrame is
- [ ] Create DataFrame from dictionary
- [ ] Load DataFrame from CSV
- [ ] Use `.head()`, `.shape`, `.dtypes`
- [ ] Record 2-minute video
- [ ] Submit as required

## 🆘 Quick Troubleshooting

### Pandas not installed?
```bash
pip install pandas
```

### File not found error?
```python
# Use correct relative path
df = pd.read_csv('data/raw/employees.csv')
```

### Import error?
```python
# Always import pandas first
import pandas as pd
```

### Encoding error?
```python
# Specify encoding
df = pd.read_csv('file.csv', encoding='utf-8')
```

## 🎓 Key Concepts (30-Second Summary)

1. **DataFrame** = 2D table with labeled rows and columns
2. **Create from dict** = `pd.DataFrame(dictionary)`
3. **Load from file** = `pd.read_csv('file.csv')`
4. **Inspect** = `.head()`, `.shape`, `.dtypes`, `.info()`
5. **Why?** = Foundation for all data analysis in Pandas

## 📊 Sample Output

When you run the script, you'll see:

```
============================================================
PANDAS DATAFRAME FUNDAMENTALS
============================================================

Student DataFrame:
      Name  Age Grade  Score
0    Alice   23     A     92
1      Bob   25     B     85
2  Charlie   22     A     95

Shape: 3 rows × 4 columns
Column Names: ['Name', 'Age', 'Grade', 'Score']
```

## 🔗 Next Steps

After completing this milestone:

1. **Practice** with your own CSV files
2. **Explore** data cleaning techniques
3. **Learn** data filtering and selection
4. **Apply** to TourMetrics tourism data
5. **Move on** to data transformation milestone

## 💡 Pro Tips

1. **Always inspect** data after loading
2. **Use descriptive names** for DataFrames
3. **Check shape and types** before analysis
4. **Keep examples simple** when learning
5. **Document your code** with comments

## 📞 Need Help?

- Review the quick reference guide
- Check the video guide for recording tips
- Run the sample script to see working examples
- Consult the milestone checklist for requirements

---

**Time to Complete:** 30 minutes - 2 hours (depending on depth)

**Difficulty:** Beginner

**Prerequisites:** Basic Python knowledge

**Output:** Working code + 2-minute video

---

**Ready? Start with:** `python scripts/pandas_dataframe_fundamentals.py`
