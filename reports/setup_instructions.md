# Setup Instructions for Pandas Series Milestone

## Prerequisites
- Python 3.7 or higher installed
- Virtual environment (recommended)

## Installation Steps

### 1. Activate Your Virtual Environment

If you have a virtual environment (like `myenv`), activate it:

**Windows:**
```cmd
myenv\Scripts\activate
```

**macOS/Linux:**
```bash
source myenv/bin/activate
```

### 2. Install Required Packages

Install Pandas and NumPy:

```cmd
pip install pandas numpy jupyter
```

Or use the requirements file:

```cmd
pip install -r requirements.txt
```

### 3. Verify Installation

Check that packages are installed correctly:

```python
python -c "import pandas as pd; import numpy as np; print(f'Pandas: {pd.__version__}'); print(f'NumPy: {np.__version__}')"
```

## Running the Code

### Option 1: Run the Python Script

```cmd
python scripts/pandas_series_fundamentals.py
```

This will execute all examples and display output in the terminal.

### Option 2: Use Jupyter Notebook (Recommended for Learning)

1. Start Jupyter:
```cmd
jupyter notebook
```

2. Navigate to `notebooks/pandas_series_fundamentals.ipynb`

3. Run cells interactively to explore each concept

## Project Structure

```
├── scripts/
│   └── pandas_series_fundamentals.py    # Complete Python script
├── notebooks/
│   └── pandas_series_fundamentals.ipynb # Interactive Jupyter notebook
├── reports/
│   ├── pandas_series_quick_reference.md # Quick reference guide
│   ├── pandas_series_video_guide.md     # Video recording guide
│   └── setup_instructions.md            # This file
└── requirements.txt                      # Python dependencies
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution:** Install pandas using `pip install pandas`

### Issue: Virtual environment not activating
**Solution:** 
- Windows: Use `myenv\Scripts\activate.bat` or `myenv\Scripts\Activate.ps1`
- Ensure you're in the correct directory

### Issue: Jupyter notebook not opening
**Solution:** 
- Install Jupyter: `pip install jupyter`
- Try: `python -m jupyter notebook`

## Next Steps

1. Run the Python script to see all examples
2. Open the Jupyter notebook for interactive learning
3. Review the quick reference guide
4. Record your video walkthrough using the video guide
5. Practice creating your own Series examples

## Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Series API Reference](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
- [NumPy Documentation](https://numpy.org/doc/)
