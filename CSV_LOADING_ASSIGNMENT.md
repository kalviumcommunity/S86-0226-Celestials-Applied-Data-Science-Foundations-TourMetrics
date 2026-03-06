# CSV Loading Milestone Assignment

## 📚 Overview

This assignment teaches you the essential skills for loading and inspecting CSV files using Pandas - the foundation of any data science workflow. You'll learn to load data correctly, inspect it thoroughly, and catch errors before they affect your analysis.

## 🎯 Learning Objectives

By completing this assignment, you will be able to:

- ✅ Load CSV files into Pandas DataFrames using `pd.read_csv()`
- ✅ Inspect DataFrame structure using head(), tail(), info(), and describe()
- ✅ Verify data integrity using shape, columns, dtypes, and len()
- ✅ Identify and troubleshoot common CSV loading issues
- ✅ Handle errors gracefully with proper error handling
- ✅ Prepare data safely for further analysis

## 📋 Prerequisites

### Required Knowledge
- Basic Python syntax (variables, functions, imports)
- Understanding of tabular data (rows and columns)
- Familiarity with file paths

### Required Software
- Python 3.7 or higher
- Pandas library: `pip install pandas`
- Jupyter Notebook (optional): `pip install jupyter`

## 📁 Assignment Structure

```
.
├── data/
│   └── raw/
│       ├── books.csv           # Sample dataset: Classic books
│       └── employees.csv       # Sample dataset: Employee information
├── notebooks/
│   └── csv_loading_milestone.ipynb  # Interactive learning notebook
├── scripts/
│   └── csv_loading_demo.py     # Demonstration script
├── reports/
│   └── csv_loading_milestone.md     # Comprehensive documentation
└── CSV_LOADING_ASSIGNMENT.md   # This file
```

## 🚀 Getting Started

### Step 1: Set Up Your Environment

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install required packages:
```bash
pip install pandas jupyter
```

3. Verify installation:
```bash
python -c "import pandas; print(f'Pandas version: {pandas.__version__}')"
```

### Step 2: Explore the Materials

You have three learning resources:

1. **Jupyter Notebook** (Recommended for beginners)
   ```bash
   jupyter notebook notebooks/csv_loading_milestone.ipynb
   ```
   - Interactive cells you can run and modify
   - Explanations alongside code
   - Practice exercises included

2. **Python Script** (For command-line learners)
   ```bash
   python scripts/csv_loading_demo.py
   ```
   - Complete demonstration of all concepts
   - Well-commented code
   - Shows expected outputs

3. **Documentation** (For reference)
   - Open `reports/csv_loading_milestone.md`
   - Comprehensive reference guide
   - Troubleshooting section
   - Practice exercises with solutions

## 📝 Assignment Tasks

### Task 1: Run the Demonstration Script ✅

Execute the demonstration script to see all concepts in action:

```bash
python scripts/csv_loading_demo.py
```

**What to observe:**
- How CSV files are loaded
- Different inspection methods
- Error handling examples
- Structure verification techniques

### Task 2: Complete the Jupyter Notebook ✅

Open and work through the interactive notebook:

```bash
jupyter notebook notebooks/csv_loading_milestone.ipynb
```

**What to do:**
1. Read each markdown cell carefully
2. Execute each code cell in order
3. Complete the practice exercises
4. Experiment with the code

**Key sections:**
- Understanding CSV Files
- Loading Your First CSV
- Inspecting Loaded Data
- Verifying Data Structure
- Practice Exercise (employees.csv)
- Common CSV Loading Issues

### Task 3: Practice with Real Data ✅

Apply what you've learned to the provided datasets:

**For books.csv:**
1. Load the file
2. Display the first 3 rows
3. Check the shape
4. Verify column names
5. Get statistical summary
6. Calculate the average publication year

**For employees.csv:**
1. Load the file
2. Display the last 2 rows
3. Check data types
4. Count total employees
5. Find the average salary
6. List all departments

### Task 4: Error Handling Challenge ✅

Practice handling common errors:

1. Try loading a non-existent file
2. Write code to check if a file exists before loading
3. Create a function that loads CSV files safely with error handling

### Task 5: Create Your Own CSV ✅

Demonstrate mastery by creating and loading your own CSV:

1. Create a CSV file with at least 3 columns and 5 rows
2. Save it in the `data/raw/` directory
3. Load it using Pandas
4. Inspect it using all methods learned
5. Verify the structure matches your expectations

## ✅ Submission Checklist

Before submitting, ensure you have:

- [ ] Executed the demonstration script successfully
- [ ] Completed all cells in the Jupyter notebook
- [ ] Finished the practice exercises for both datasets
- [ ] Implemented error handling examples
- [ ] Created and loaded your own CSV file
- [ ] Documented any issues or questions encountered

## 📊 Datasets Description

### books.csv
A collection of classic literature with the following columns:
- **Title**: Book title (string)
- **Author**: Author name (string)
- **Year**: Publication year (integer)
- **Pages**: Number of pages (integer)

**Sample data:**
```
Title,Author,Year,Pages
1984,George Orwell,1949,328
To Kill a Mockingbird,Harper Lee,1960,281
```

### employees.csv
Employee information with the following columns:
- **Name**: Employee name (string)
- **Department**: Department name (string)
- **Salary**: Annual salary (integer)
- **Years**: Years of experience (integer)

**Sample data:**
```
Name,Department,Salary,Years
John,Engineering,75000,3
Sarah,Marketing,65000,2
```

## 🎓 Key Concepts Covered

### 1. Loading CSV Files
- Using `pd.read_csv()` function
- Understanding file paths
- Handling different file formats

### 2. Inspection Methods
- `head()` - Preview first rows
- `tail()` - Preview last rows
- `info()` - DataFrame structure
- `describe()` - Statistical summary

### 3. Structure Verification
- `shape` - Dimensions (rows, columns)
- `columns` - Column names
- `dtypes` - Data types
- `len()` - Row count

### 4. Error Handling
- FileNotFoundError
- UnicodeDecodeError
- ParserError
- Data type issues

## 🔧 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'pandas'"**
- Solution: Install Pandas with `pip install pandas`

**Issue: "FileNotFoundError: No such file or directory"**
- Solution: Check your current directory with `os.getcwd()`
- Ensure you're running commands from the project root

**Issue: "Jupyter notebook won't open"**
- Solution: Install Jupyter with `pip install jupyter`
- Try `jupyter notebook --no-browser` if browser doesn't open

**Issue: "UnicodeDecodeError when loading CSV"**
- Solution: Try different encodings:
  ```python
  df = pd.read_csv('file.csv', encoding='latin-1')
  ```

## 📚 Additional Resources

### Official Documentation
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas IO Tools](https://pandas.pydata.org/docs/user_guide/io.html)

### Practice Datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Data.gov](https://www.data.gov/)

### Video Tutorials
- [Pandas Tutorial by Corey Schafer](https://www.youtube.com/watch?v=ZyhVh-qRZPA)
- [Data Analysis with Python](https://www.youtube.com/watch?v=r-uOLxNrNk8)

## 🏆 Success Criteria

You've successfully completed this assignment when you can:

1. ✅ Load any CSV file without errors
2. ✅ Inspect data structure confidently
3. ✅ Verify data integrity before analysis
4. ✅ Handle common loading errors gracefully
5. ✅ Explain why inspection is important
6. ✅ Apply these skills to new datasets

## 💡 Tips for Success

1. **Always inspect after loading** - Make it a habit
2. **Read error messages carefully** - They tell you what's wrong
3. **Experiment with the code** - Modify examples to learn
4. **Use the documentation** - It's your reference guide
5. **Practice with different datasets** - Build confidence
6. **Ask questions** - No question is too small

## 🎯 Next Steps

After completing this assignment, you'll be ready for:

- Data cleaning and preprocessing
- Handling missing values
- Data transformation and manipulation
- Exploratory data analysis
- Data visualization
- Statistical analysis

## 📞 Support

If you encounter issues or have questions:

1. Check the troubleshooting section in `reports/csv_loading_milestone.md`
2. Review the error handling examples in the notebook
3. Consult the official Pandas documentation
4. Ask your instructor or teaching assistant

## 🎉 Conclusion

CSV loading is the foundation of data science. Master these skills, and you'll have a solid base for all future data analysis work. Remember: **Always inspect your data after loading!**

Good luck, and happy data loading! 🚀

---

**Assignment Version:** 1.0  
**Last Updated:** 2026-03-06  
**Estimated Time:** 2-3 hours
