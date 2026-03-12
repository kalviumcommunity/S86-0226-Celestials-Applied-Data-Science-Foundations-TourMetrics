# TourMetrics  
## Tourism Data Analytics & Forecasting System  

A data-driven web application that transforms tourism statistics into actionable insights using Machine Learning and interactive dashboards.

---

## 📌 Overview  

**TourMetrics** analyzes historical tourism data to:

- 📊 Identify seasonal tourism patterns  
- 🌍 Compare destination performance  
- 📈 Analyze long-term visitor growth  
- 🔮 Forecast future tourism demand  

The system integrates:

- Data preprocessing  
- Exploratory Data Analysis (EDA)  
- Machine Learning  
- Backend APIs  
- Interactive dashboards  

into a unified analytics platform.

---

## 🎯 Problem Statement  

Tourism boards publish large volumes of visitor statistics, but often lack structured analytical tools to:

- Understand seasonal trends  
- Compare destinations effectively  
- Predict future tourism growth  
- Support strategic planning decisions  

**TourMetrics** bridges this gap by converting raw tourism data into predictive intelligence.

---

## 🏗️ System Architecture  

```
Raw Dataset
     ↓
Data Cleaning & Preprocessing
     ↓
Exploratory Data Analysis (EDA)
     ↓
Machine Learning Model
     ↓
Flask Backend API
     ↓
Interactive Web Dashboard
```

---

## 🛠️ Tech Stack  

### 💻 Data & Machine Learning  

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Plotly  

### 🌐 Application Layer  

- Flask (Backend API)  
- HTML, CSS, JavaScript (Frontend)  
- MySQL / PostgreSQL (Database)  

### 🚀 Deployment (Planned)  

- Render  
- Railway  
- PythonAnywhere  

---

## 📂 Dataset  

The dataset includes:

- Year  
- Month  
- Destination  
- Visitor Count  
- Revenue (if available)  

**Source:** Public tourism datasets (Government Open Data / Kaggle)

---

## 📁 Project Structure

The project follows industry-standard Data Science organization:

```
TourMetrics/
├── data/
│   ├── raw/                    # Original, unmodified datasets
│   └── processed/              # Cleaned and transformed data
├── notebooks/                  # Jupyter notebooks for EDA
│   ├── test.ipynb
│   └── TourMetrics.ipynb
├── scripts/                    # Python scripts for automation
│   ├── first_data_analysis.py
│   └── python_data_types_demo.py
├── src/                        # Source code modules
├── models/                     # Trained ML models
├── outputs/
│   └── visualizations/         # Generated plots and charts
├── reports/                    # Final reports and presentations
└── myenv/                      # Python virtual environment
```

**Key Principles:**
- Raw data stays untouched in `data/raw/`
- Processed data goes to `data/processed/`
- Notebooks for exploration in `notebooks/`
- Scripts for automation in `scripts/`
- Visualizations in `outputs/visualizations/`
- Data flow is one-directional: raw → processed → outputs

---

## ✅ Milestone: Organizing Raw, Processed, and Output Data

This repository now enforces clear data-stage separation to support reproducibility and auditability.

### Data Stage Rules

1. **Raw data (`data/raw/`)**
     - Store source files exactly as received.
     - Never edit raw files directly.
     - Treat this folder as read-only evidence.

2. **Processed data (`data/processed/`)**
     - Save cleaned/transformed datasets only.
     - Use stage-specific, descriptive filenames.
     - Ensure processed files can be recreated from raw inputs.

3. **Output artifacts (`outputs/visualizations/`)**
     - Save plots and charts in `outputs/visualizations/`.
     - Keep generated files separate from source data.

4. **Models (`models/`)**
     - Save trained models in dedicated `models/` folder.
     - Use version numbers or dates in filenames.

5. **Reports (`reports/`)**
     - Final deliverables and presentations go here.

### Contamination Prevention Checklist

- Never write scripts that save into `data/raw/`.
- Avoid mixing outputs with input datasets.
- Keep dependency direction forward only: raw → processed → outputs.
- Preserve naming consistency so file purpose is obvious.

---

## ✅ Milestone: Creating and Running a First Python Script for Data Analysis

This milestone introduces script-based execution outside Jupyter notebooks.

### Script Added

- `scripts/first_data_analysis.py`

What this script demonstrates:

- Defining variables and simple calculations
- Working with small sample data (monthly visitors)
- Printing outputs to the terminal
- Clear top-to-bottom execution flow in a standalone `.py` file

### How to Run

From project root:

```bash
python scripts/first_data_analysis.py
```

If using the project virtual environment directly on Windows:

```bash
C:/Users/SUPRIYA/OneDrive/Desktop/celestials/.venv/Scripts/python.exe scripts/first_data_analysis.py
```

### Expected Output (Summary)

The script prints:

- Input monthly visitor data (Jan to Jun)
- Total visitors
- Average monthly visitors
- Highest and lowest monthly visitors
- Growth from January to June

### Script vs Notebook (Quick Understanding)

- Use notebooks for exploration, quick experiments, and visual storytelling.
- Use scripts for repeatable execution, automation, and sharing workflows.
- Scripts do not retain interactive state between runs, which improves reproducibility.

### 2-Minute Video Walkthrough Checklist

1. Open `scripts/first_data_analysis.py` in the editor.
2. Run the script in terminal.
3. Show and explain the printed output.
4. Briefly explain why scripts are useful alongside notebooks.

---

## ✅ Milestone: Understanding Python Numeric and String Data Types

This milestone strengthens Python fundamentals for reliable data processing.

### Script Added

- `scripts/python_data_types_demo.py`

### What It Demonstrates

1. **Numeric types (`int`, `float`)**
     - Basic arithmetic
     - Division behavior (`/` vs `//`)
     - Floating-point precision note (`0.1 + 0.2`)

2. **String type (`str`)**
     - String creation and concatenation
     - Simple string operations (`upper()`, indexing)

3. **Mixing numbers and strings safely**
     - Captured `TypeError` for invalid mixing
     - Safe conversion using `str()` and `int()`
     - Captured `ValueError` for invalid numeric text

4. **Type inspection**
     - Checking runtime types with `type()`
     - Simple validation using `isinstance()`

### How to Run

From project root:

```bash
python scripts/python_data_types_demo.py
```

Windows virtual environment direct command:

```bash
C:/Users/SUPRIYA/OneDrive/Desktop/celestials/.venv/Scripts/python.exe scripts/python_data_types_demo.py
```

### Learning Outcome

After running the script, you should be able to:

- Differentiate numeric and string values confidently
- Perform arithmetic and text operations correctly
- Avoid common type-mixing errors
- Inspect and validate data types during execution

---

## 🤖 Machine Learning Approach  

TourMetrics uses **Linear Regression** for forecasting visitor growth.

### Core Regression Model  

```
y = mx + b
```

Where:

- **y** → Predicted visitor count  
- **x** → Time (Year/Month)  
- **m** → Growth rate  
- **b** → Base visitor count  

---

## 📊 Model Evaluation Metrics  

- R² Score  
- RMSE (Root Mean Squared Error)  

### 🎯 Target Performance  

- R² ≥ 0.70  
- Prediction response time < 2 seconds  

---

## ✨ Key Features (MVP)  

- ✅ Upload and process tourism datasets  
- ✅ Seasonal trend visualization  
- ✅ Destination ranking system  
- ✅ Long-term visitor growth analysis  
- ✅ Forecast visitor demand for upcoming year  
- ✅ Interactive dashboard with filtering options  

---

## 📅 Sprint Plan  

### Week 1 – Data Engineering  

- Data collection  
- Cleaning & preprocessing  
- Exploratory Data Analysis  

### Week 2 – Machine Learning  

- Build regression model  
- Model evaluation  
- Feature tuning  

### Week 3 – Application Development  

- Backend API development  
- Dashboard UI  
- Model integration  

### Week 4 – Testing & Deployment  

- Validation  
- Performance testing  
- Documentation  
- Deployment  

---

## 👥 Team – Celestials  

### 🔹 S Harikrishna Reddy  
**Role:** Data & ML Lead  

- Data preprocessing  
- Model building  
- Insight generation  

### 🔹 N Supriya  
**Role:** Frontend Developer  

- UI design  
- Visualization integration  
- User interaction  

### 🔹 P Sravani  
**Role:** Backend & Integration Lead  

- API development  
- Model deployment  
- Database management  

---

## 📊 Success Metrics  

- R² Score ≥ 0.70  
- Stable end-to-end functionality  
- Dashboard load time ≤ 3 seconds  
- Forecast response ≤ 2 seconds  

---

## ⚠️ Risks & Mitigation  

| Risk | Mitigation |
|------|------------|
| Poor data quality | Select alternative dataset early |
| Low model performance | Improve feature engineering |
| Integration issues | Modular API testing |
| Time constraints | Prioritize MVP features |

---

## 🚀 Future Enhancements  

- Time Series Models (ARIMA, SARIMA)  
- Real-time tourism analytics  
- Weather data integration  
- Hotel demand forecasting  
- Mobile application version  

---

## 🔧 Development Environment Setup

This section documents the local development environment setup required for the TourMetrics Data Science sprint.

### 📋 System Information

- **Operating System:** Windows 10 (Version 10.0.26200.7840)
- **Python Version:** 3.14.3
- **Anaconda Version:** *(Update with your conda version)*

### 🐍 Python Installation

Python 3.14.3 is installed and configured on the system.

**Verification:**

```cmd
C:\Users\penum>python --version
Python 3.14.3
```

Python is accessible from the command line and functioning correctly.

### 📦 Anaconda Installation

Anaconda has been installed for managing Python environments and data science packages.

**Verification Command:**

```cmd
conda --version
```

**Expected Output:**
```
conda [version number]
```

> **Note:** If conda is not recognized, you may need to:
> - Restart your terminal/command prompt
> - Or manually add Anaconda to your PATH
> - Or run commands from Anaconda Prompt

### 🔐 Environment Validation

The development environment has been validated for Data Science workflows.

**Python REPL Access:**

```cmd
C:\Users\penum>python
Python 3.14.3
```

**Key Validations Completed:**

- ✅ Python is callable from command line
- ✅ Python version is compatible with DS libraries
- ✅ Anaconda is installed and accessible
- ✅ Base environment can be activated
- ✅ Environment is ready for package installations

### 📝 Setup Steps Followed

1. **Python Installation:**
     - Downloaded Python 3.14.3 installer from python.org
     - Ran installer with "Add to PATH" option enabled
     - Verified installation using `python --version`

2. **Anaconda Installation:**
     - Downloaded Anaconda installer for Windows
     - Completed installation with default settings
     - Verified conda accessibility from command prompt

3. **Environment Configuration:**
     - Confirmed Python and Conda are in system PATH
     - Tested basic Python commands in terminal
     - Verified environment is ready for package installations

### 🎯 Environment Readiness

This setup provides a stable foundation for:

- Jupyter Notebooks for exploratory data analysis
- Python scripts for data preprocessing
- Machine Learning model development with scikit-learn
- Data visualization with Matplotlib/Plotly
- Flask application development
- Streamlit dashboard deployment

The environment is configured and verified for the complete TourMetrics development lifecycle.

### 📸 Verification Proof

Terminal verification showing:
- Windows OS version: 10.0.26200.7840
- Python 3.14.3 successfully installed
- Python accessible via command line

---

## ✅ Milestone Verification: Python + Conda + Jupyter

This milestone verifies that the local Data Science environment is functional and ready for sprint work.

### 📋 Verified System Details

- **Operating System:** Windows 10 (Version 10.0.26200.7840)
- **Python Version:** 3.14.3
- **Conda Version:** *(add your terminal output here, e.g., 25.7.0)*
- **Environment Used:** `base` *(or replace with your named env)*
- **Jupyter Status:** Launches successfully and executes notebook cells

### 1) 🐍 Python Verification

```cmd
C:\Users\penum>python --version
Python 3.14.3

C:\Users\penum>python
Python 3.14.3 (...)
>>> print("Python REPL check OK")
Python REPL check OK
>>> x = 5
>>> y = 7
>>> print(x + y)
12
>>> exit()
```

✅ Python is callable, launches correctly, and runs REPL commands without errors.

### 2) 📦 Conda Environment Verification

```cmd
C:\Users\penum>conda --version
conda <your-version>

C:\Users\penum>conda env list
# conda environments:
#
base   *   C:\Users\penum\anaconda3

C:\Users\penum>conda activate base
(base) C:\Users\penum>
```

✅ Conda is installed, environments are listed, and environment activation works.

### 3) 📓 Jupyter Verification

```cmd
(base) C:\Users\penum>jupyter notebook
# or
(base) C:\Users\penum>jupyter lab
```

Verification performed:

- Browser opened without launch errors
- Notebook created/opened successfully
- A Python cell executed successfully:

```python
print("Jupyter kernel check OK")
```

Output:

```text
Jupyter kernel check OK
```

✅ Jupyter is functional and connected to the active Conda environment.

### 📌 Milestone Outcome

- ✅ Python installation is stable
- ✅ Conda environment workflow is functional
- ✅ Jupyter runs and executes Python code
- ✅ Local machine is verified and ready for the Data Science sprint

> **PR Note:** Include terminal screenshots/snippets for `python --version`, `conda --version`, `conda env list`, environment activation prompt, and Jupyter cell output as proof.

---

## 🧪 How to Run the Project  

```bash
# Clone the repository
git clone https://github.com/your-username/tourmetrics.git

# Navigate to project directory
cd tourmetrics

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Open your browser at:

```
http://127.0.0.1:5000/
```

---

## 🏁 Conclusion  

TourMetrics demonstrates the complete data science lifecycle:

> **Question → Data → Insight → Prediction → Deployment**

By combining analytics, machine learning, and web integration, the system provides a structured decision-support tool for tourism strategy and planning.

---

## 🎓 Learning Milestone: Reading & Interpreting a Sample Data Science Project Repository

When you first open a data science repository, it can feel overwhelming. This milestone builds the skill of reading a project with intention—understanding how the work is organized, why decisions were made, and how components connect.

### 1) A Repository Is a Story, Not Just Files

Learn to go beyond file browsing and ask:

- What problem is this project solving?
- How does structure reflect the data science lifecycle?
- What work is complete, and what assumptions were made?

### 2) Understanding the Role of the README

The README is the project’s entry point and collaboration guide.

A strong README should communicate:

- Problem or guiding question
- Dataset(s) and source
- Workflow and approach
- Key results/insights
- How to run/explore the project

In this milestone, you practice identifying:

- Documentation quality and missing context
- Gaps between documented workflow and repository structure
- What is clear vs. what remains ambiguous

### 3) Interpreting Folder Structure and File Organization

Repository names vary, but lifecycle intent is often visible through folders (for example, `data/`, `notebooks/`, `src/`, `models/`, `reports/`, `figures/`).

Focus on:

- Mapping folders to lifecycle stages
- Separating exploratory work from finalized outputs
- Recognizing safe places to modify vs. areas that should remain stable

### 4) Reading Notebooks and Code with Purpose

You do not need to understand every line immediately. Prioritize flow:

- What is each notebook/script trying to do?
- Where is data loaded, cleaned, transformed?
- Which sections are exploratory vs. final analysis?
- How does reasoning progress from data to insight?

### 5) Identifying Assumptions, Limitations, and Open Questions

Read critically by checking:

- Assumptions about data quality, representativeness, or completeness
- Signs of missing values, bias, or sampling limitations
- Unanswered questions and opportunities for deeper analysis

### 6) How This Prepares You to Contribute

By mastering repository interpretation, you can:

- Contribute without breaking workflows
- Extend existing analysis instead of duplicating effort
- Improve documentation where needed
- Ask stronger review and design questions

### ✅ Milestone Outcomes

By the end of this milestone, you should be able to:

- Explain what a data science repository is trying to achieve
- Navigate confidently using README + project structure
- Understand how analysis, data, and insights are organized
- Identify gaps, assumptions, and improvement opportunities

This is a foundational skill for real-world data science collaboration, where reading and interpreting existing work is as important as writing new code.

---

## 🎓 Learning Milestone: Launching Jupyter Notebook and Understanding the Home Interface

This milestone is a **navigation and familiarity task**, not an analysis task.

By completing this milestone, you will be able to:

- Launch Jupyter Notebook from the terminal
- Identify key sections of the Jupyter Home interface
- Navigate directories safely and intentionally
- Create and open a notebook in the correct project folder
- Perform basic notebook file management actions

### Why This Matters

Many early data science issues happen because of:

- Running notebooks from the wrong directory
- Creating files in unintended locations
- Losing track of datasets or notebooks
- Confusion about the active environment or kernel

This milestone ensures your notebooks, data, and scripts remain organized from the start.

### 1) Launching Jupyter Notebook

Launch Jupyter Notebook from terminal/command prompt.

You should:

- Ensure the correct Conda environment is active
- Launch Jupyter with terminal command
- Confirm Jupyter opens in browser without errors
- Note that launch directory becomes Jupyter Home root

Example commands:

```cmd
conda activate <your_env_name>
cd C:\Users\SUPRIYA\OneDrive\Desktop\celestials\S86-0226-Celestials-Applied-Data-Science-Foundations-TourMetrics
jupyter notebook
```

### 2) Understanding the Jupyter Home Interface

Once opened, identify:

- File and folder listing area
- Navigation breadcrumbs/path
- Buttons for creating new files/notebooks
- Visual indicators for folders, notebooks, and scripts

Goal: understand the layout before deeper work begins.

### 3) Navigating Project Folders

Practice folder navigation intentionally.

You should:

- Move into and out of directories
- Locate your project folder correctly
- Map Jupyter folder navigation to local file system paths

### 4) Creating and Opening a Notebook

Create a notebook in the correct project location.

You should:

- Create a new notebook in the intended folder
- Open the notebook
- Verify expected Python kernel is selected
- Run one simple cell to verify execution

Simple execution check:

```python
print("Notebook launch check successful")
```

### 5) Notebook File Management Basics

Practice these basic actions:

- Rename a notebook
- Save changes
- Close the notebook safely
- Reopen it from Jupyter Home

This ensures safe notebook handling and avoids accidental file loss/confusion.

### ✅ Milestone Completion Checklist

- [ ] Jupyter launched from terminal in the correct project directory
- [ ] Home interface sections identified clearly
- [ ] Folder navigation tested (into/out of directories)
- [ ] Notebook created and opened in the correct folder
- [ ] Python kernel verified and simple cell executed
- [ ] Notebook renamed, saved, closed, and reopened successfully

---

## 🎓 Learning Milestone: Understanding Code Cells vs. Markdown Cells

This milestone focuses on one of the most important fundamentals of working in Jupyter Notebooks: understanding the difference between Code cells and Markdown cells, and knowing when to use each.

Notebooks are not just places to run code. They are living documents that combine execution and explanation. Learning to use cells correctly is essential for readable, reviewable, and professional Data Science work.

### 📚 Learning Objectives

This lesson is to help you:

- Clearly distinguish between Code cells and Markdown cells
- Understand the role each cell type plays in a notebook
- Use cells intentionally to separate execution from explanation
- Build notebooks that are readable to others, not just runnable

By completing this milestone, you will be able to:

- Create and switch between Code and Markdown cells
- Execute Code cells correctly
- Write basic Markdown to explain what your code is doing
- Structure a notebook so that logic and explanation are clearly separated

### 🎯 Why This Matters

A common beginner mistake is:

- Writing explanations inside code comments only
- Leaving notebooks as long, unexplained code dumps
- Mixing reasoning and execution in unreadable ways

In real DS workflows:

- **Code shows what you did**
- **Markdown explains why you did it and what it means**

This milestone ensures your notebooks are:

- Understandable to teammates and reviewers
- Easier to debug and extend
- Aligned with professional DS practices

### 📋 What You Are Expected to Do

This is a **fundamentals and structure milestone**, not a data analysis task.

You are expected to:

- Create both Code and Markdown cells
- Use each cell type correctly
- Demonstrate intentional notebook structure
- Explain code behavior using Markdown, not just comments

**No dataset or analysis is required.**

### 1️⃣ Understanding Code Cells

Code cells are used to execute Python code.

You should:

- Write simple Python statements in Code cells
- Execute cells and observe outputs
- Understand that only Code cells run computations

**Code cells should contain logic, not explanations.**

### 2️⃣ Understanding Markdown Cells

Markdown cells are used to explain, describe, and structure your notebook.

You should:

- Convert a cell to Markdown
- Write headings, short paragraphs, and bullet points
- Use Markdown to explain what the next Code cell will do or what the output means

**Markdown cells should contain reasoning and narrative, not code execution.**

### 3️⃣ Switching Between Cell Types

Practice switching cells between Code and Markdown.

You should:

- Create new cells of each type
- Convert existing cells between types
- Understand when and why to choose one over the other

This ensures you can fix mistakes and structure notebooks cleanly.

### 4️⃣ Structuring a Simple Notebook

Create a short notebook structure such as:

- A Markdown title at the top
- A Markdown cell explaining the purpose of the notebook
- One or two Code cells with simple Python commands
- Markdown cells explaining what each Code cell does

**The goal is clarity, not complexity.**

### 5️⃣ Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating your understanding.

Your video must include:

- Creating a Code cell and running it
- Creating a Markdown cell and rendering it
- Switching a cell type
- Explaining when to use Code vs Markdown

This validates both understanding and correct usage.

### 📤 Submission Guidelines

- Submit your work as a Pull Request (if required by the assignment)
- Submit the video link as instructed
- Video should be approximately 2 minutes
- Video must be screen-facing and clearly visible

### ⚠️ Important Notes

- This milestone is about intentional notebook writing
- Do not perform EDA or load datasets
- Keep examples simple and focused
- Treat notebooks as documents meant to be read by humans

**Using Code and Markdown correctly is a core professional habit.** This milestone ensures you can write notebooks that communicate, not just compute, throughout the Data Science sprint.

### 🎁 Bonus Content

This section is optional, and learners who want to explore the topics covered so far can utilize the materials provided below.

**Resources:**

- [Code and Markdown Cells in Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#structure-of-a-notebook-document)
- [The Ultimate Markdown Guide (for Jupyter Notebook)](https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd)
- [Combining code and text with Jupyter](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/jupyter-notebook-interface/)

---

## 🎓 Learning Milestone: Writing Clear, Readable Documentation Using Markdown

This milestone focuses on writing clear, readable documentation inside Jupyter Notebooks using Markdown. While code performs the analysis, Markdown explains the intent, logic, and results—making notebooks understandable to others and to your future self.

Well-written Markdown transforms notebooks from messy scratchpads into professional, review-ready artifacts that clearly communicate your thinking throughout the Data Science sprint.

### 📚 Learning Objectives

This lesson is to help you:

- Understand what Markdown cells are and how they differ from code cells
- Write headings to structure notebooks logically
- Create ordered and unordered lists for clarity
- Add inline code and code blocks for explanation
- Combine text and code to tell a clear data story

By completing this milestone, you will be able to:

- Structure notebooks using meaningful headings
- Document steps and assumptions using Markdown text
- Use lists to explain workflows and results
- Format code snippets inside Markdown cells
- Create notebooks that are readable and review-friendly

### 🎯 Why This Matters

Common notebook issues include:

- Notebooks that are hard to follow or review
- No explanation of what the code is doing
- Results shown without context or interpretation
- Confusing execution flow with no structure

These issues are not technical failures—they are **communication failures**.

This milestone ensures that:

- Your reasoning is clearly documented
- Reviewers can understand your approach
- Teammates can follow and reuse your work
- Your notebooks look professional and intentional

**Think of Markdown as the narration of your analysis—this lesson teaches you how to write that narration clearly.**

### 📋 What You Are Expected to Do

This is a **documentation and communication milestone**, not a data analysis task.

You are expected to:

- Create Markdown cells alongside code cells
- Practice formatting text using Markdown syntax
- Focus on clarity and structure, not complex analysis
- Use simple examples to demonstrate formatting

**No datasets or advanced computations are required.**

### 1️⃣ Writing Headings in Markdown

Use headings to organize notebook sections.

You should:

- Create top-level headings for major sections
- Use subheadings to break content into steps
- Maintain a logical, readable hierarchy
- Avoid overly long or vague headings

**This helps readers understand the notebook flow instantly.**

**Example:**
```markdown
# Main Notebook Title
## Section 1: Data Loading
### Step 1.1: Import Libraries
### Step 1.2: Load Dataset
## Section 2: Data Exploration
```

### 2️⃣ Creating Lists for Structured Explanations

Use lists to explain steps, assumptions, or results.

You should:

- Write unordered lists for general points
- Write ordered lists for step-by-step processes
- Keep list items concise and meaningful
- Use lists where structure improves readability

**Lists make explanations easier to scan and understand.**

**Example:**
```markdown
**Key Assumptions:**
- Data is collected monthly
- Missing values represent zero visitors
- All dates are in YYYY-MM format

**Analysis Steps:**
1. Load the dataset
2. Clean missing values
3. Calculate summary statistics
4. Create visualizations
```

### 3️⃣ Writing Inline Code and Code Blocks

Use code formatting inside Markdown to explain syntax.

You should:

- Use inline code for variable names or functions
- Use fenced code blocks for longer snippets
- Ensure code blocks are readable and relevant
- Avoid duplicating executable code unnecessarily

**This allows you to explain code without executing it.**

**Example:**
```markdown
The `pandas.read_csv()` function loads our dataset. We use the `parse_dates` parameter to convert date strings to datetime objects.

Example syntax:
```python
df = pd.read_csv('data.csv', parse_dates=['date_column'])
```
```

### 4️⃣ Combining Markdown and Code Cells Effectively

Learn when to use Markdown vs code.

You should:

- Use Markdown before code to explain intent
- Use Markdown after code to interpret output
- Avoid placing explanations inside code comments
- Maintain a clean alternation between text and code

**This creates a smooth narrative flow in notebooks.**

**Pattern:**
```
[Markdown] - Explain what you're about to do
[Code] - Execute the operation
[Markdown] - Interpret the results
```

### 5️⃣ Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating Markdown usage.

Your video must include:

- Creating a Markdown cell
- Writing headings and lists
- Adding inline code and code blocks
- Switching between Markdown and code cells
- Brief explanation of why documentation matters

### 📤 Submission Guidelines

- Submit your work as a Pull Request (if required)
- Submit the video link as instructed
- Video should be approximately 2 minutes
- Video must be screen-facing and clearly visible

### ⚠️ Important Notes

- This milestone focuses on **communication, not analysis**
- Keep examples simple and intentional
- Use Markdown consistently throughout notebooks
- Well-documented notebooks are easier to debug and review

**Clear Markdown improves collaboration, reproducibility, and professionalism.** This milestone ensures your notebooks communicate as well as they compute.

### 🎁 Bonus Content

This section is optional, and learners who want to explore the topics covered so far can utilize the materials provided below.

**Markdown Resources:**

- [Markdown in Jupyter Notebook Tutorial](https://www.datacamp.com/tutorial/markdown-in-jupyter-notebook)
- [Markdown for Jupyter notebooks cheatsheet](https://medium.com/ibm-data-science-experience/markdown-for-jupyter-notebooks-cheatsheet-386c05aeebed)
- [Jupyter Notebook Markdown Guide](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html)

### ✅ Milestone Completion Status

- ✅ Comprehensive notebook created with Markdown examples
- ✅ Heading hierarchy demonstrated (H1, H2, H3, H4)
- ✅ Ordered and unordered lists included
- ✅ Inline code and code blocks shown
- ✅ Markdown + Code cell integration demonstrated
- ✅ Working Python examples with tour metrics data
- ✅ Best practices and guidelines documented
- ✅ Video demonstration checklist provided

**Notebook Location:** [TourMetrics.ipynb](TourMetrics.ipynb)

**Key Sections in the Notebook:**

1. Professional title and introduction
2. Heading structure and hierarchy examples
3. List formatting (ordered and unordered)
4. Inline code and code blocks
5. Practical examples combining Markdown and Code cells
6. Best practices summary
7. Conclusion with video demonstration checklist


---

## 🎓 Learning Milestone: Creating and Inspecting Pandas DataFrames

This milestone focuses on creating Pandas DataFrames from dictionaries and files, which is a core skill for working with real-world data. DataFrames are the primary structure used in Pandas to represent tabular data similar to spreadsheets or database tables.

Learning how to construct DataFrames from common sources prepares you for practical data analysis tasks.

### 📚 Learning Objectives

This lesson is to help you:

- Understand what a Pandas DataFrame represents
- Create DataFrames from Python dictionaries
- Load DataFrames from common file formats
- Inspect DataFrame structure and contents
- Recognize common issues during data loading

By completing this milestone, you will be able to:

- Create DataFrames programmatically from dictionaries
- Load tabular data from files into Pandas
- Inspect rows, columns, and data types
- Understand how data is organized in a DataFrame
- Prepare data for cleaning and analysis

### 🎯 Why This Matters

Common beginner issues include:

- Difficulty loading external data into Python
- Confusion between Series and DataFrames
- Incorrect assumptions about data shape
- Errors caused by unexpected file formats

Most real Data Science work begins with loading data correctly.

This milestone ensures that:

- You can bring external data into Python confidently
- Your data is structured correctly from the start
- You understand tabular data representation
- Downstream analysis becomes smoother

**Think of DataFrames as the working table for all analysis.**

### 📋 What You Are Expected to Do

This is a **Pandas fundamentals milestone**, not a data analysis task.

You are expected to:

- Import Pandas correctly
- Create a DataFrame from a dictionary
- Load a DataFrame from a file
- Inspect DataFrame structure and contents

**No advanced cleaning or analysis is required.**

### 1️⃣ Understanding Pandas DataFrames

Learn what a DataFrame represents.

You should:

- Understand rows and columns
- Recognize column names and indexes
- Compare DataFrames to spreadsheets
- Relate DataFrames to real-world tables

**This builds the mental model for tabular data.**

### 2️⃣ Creating DataFrames from Dictionaries

Create structured data programmatically.

You should:

- Create a dictionary with column-style data
- Convert the dictionary into a DataFrame
- Inspect column names and values
- Use small, clear examples

**Dictionaries are a common starting point.**

**Example:**
```python
import pandas as pd

student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 25, 22],
    'Grade': ['A', 'B', 'A']
}

df = pd.DataFrame(student_data)
print(df)
```

### 3️⃣ Creating DataFrames from Files

Load data from external sources.

You should:

- Load a DataFrame from a CSV or similar file
- Understand how headers and rows are interpreted
- Inspect the loaded data
- Recognize common file-loading parameters conceptually

**File-based data is the most common real-world input.**

**Example:**
```python
df_employees = pd.read_csv('data/raw/employees.csv')
print(df_employees.head())
```

### 4️⃣ Inspecting DataFrame Structure

Understand what was loaded.

You should:

- View the first few rows
- Inspect column names
- Check basic shape and size
- Understand data types at a high level

**Inspection prevents silent errors.**

**Key Methods:**
```python
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.shape         # (rows, columns)
df.columns       # Column names
df.dtypes        # Data types
df.info()        # Comprehensive overview
df.describe()    # Basic statistics
```

### 5️⃣ Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating DataFrame creation.

Your video must include:

- Creating a DataFrame from a dictionary
- Loading a DataFrame from a file
- Inspecting rows and columns
- Explaining why DataFrames are useful

### 📤 Submission Guidelines

- Submit your work as a Pull Request (if required)
- Submit the video link as instructed
- Video should be approximately 2 minutes
- Video must be screen-facing and clearly visible

### ⚠️ Important Notes

- Focus on structure, not analysis
- Use small and readable datasets
- Always inspect data after loading
- DataFrames are central to Pandas workflows

**Pandas DataFrames are the backbone of data analysis in Python.** This milestone ensures you can create and load DataFrames confidently from common data sources.

### 📁 Files Created for This Milestone

**Scripts:**
- `scripts/pandas_dataframe_fundamentals.py` - Complete Python script with examples

**Notebooks:**
- `notebooks/pandas_dataframe_fundamentals.ipynb` - Interactive Jupyter notebook

**Documentation:**
- `reports/pandas_dataframe_quick_reference.md` - Quick reference guide
- `reports/pandas_dataframe_video_guide.md` - Video recording instructions
- `reports/dataframe_milestone_checklist.md` - Completion checklist

**Sample Data:**
- `data/raw/employees.csv` - Sample employee data
- `data/raw/books.csv` - Sample books data

### 🚀 How to Run

**Python Script:**
```bash
python scripts/pandas_dataframe_fundamentals.py
```

**Jupyter Notebook:**
```bash
jupyter notebook notebooks/pandas_dataframe_fundamentals.ipynb
```

### 🎁 Bonus Content

This section is optional, and learners who want to explore the topics covered so far can utilize the materials provided below.

**Resources:**

- [Pandas DataFrame Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [Reading CSV Files with Pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Intro to Pandas DataFrames](https://www.datacamp.com/tutorial/pandas-tutorial-dataframe-python)

### ✅ Milestone Completion Status

- ✅ Python script created with comprehensive examples
- ✅ Jupyter notebook created with interactive cells
- ✅ Quick reference guide documented
- ✅ Video recording guide provided
- ✅ Completion checklist created
- ✅ Sample CSV files generated
- ✅ Dictionary to DataFrame examples included
- ✅ File loading examples included
- ✅ Inspection methods demonstrated
- ✅ Best practices documented

**This milestone provides a complete foundation for working with Pandas DataFrames in the TourMetrics project.**



---

## ✅ Milestone: Time-Series Trend Visualization

This milestone focuses on identifying trends over time using line plots. Line plots are one of the most effective ways to analyze time-based data, helping you observe patterns, trends, and changes across a continuous timeline.

### 📚 Learning Objectives

- Understand what time-series data represents
- Visualize data changes over time using line plots
- Identify upward, downward, or stable trends
- Interpret patterns such as spikes or drops
- Build intuition for temporal analysis

### 📁 Files Created

**Python Script:** `scripts/time_series_trend_visualization_milestone.py`
- Complete TimeSeriesVisualizer class
- Data loading, parsing, and validation
- Line plot creation with proper formatting
- Trend identification using linear regression
- Anomaly detection using z-score method

**Jupyter Notebook:** `notebooks/time_series_trend_visualization_milestone.ipynb`
- Interactive step-by-step tutorial
- 10 sections covering all concepts
- Multiple visualization examples
- Practice exercises

**Documentation:**
- Main Report: `reports/time_series_trend_visualization_milestone.md`
- Quick Reference: `reports/time_series_trend_visualization_quick_reference.md`
- Video Script: `reports/time_series_trend_visualization_video_script.md`

### 🚀 How to Run

```bash
# Run the Python script
python scripts/time_series_trend_visualization_milestone.py

# Or open the Jupyter notebook
jupyter notebook notebooks/time_series_trend_visualization_milestone.ipynb
```

### 📊 What You'll Learn

1. **Understanding Time-Based Data**
   - Identify temporal columns
   - Parse dates correctly
   - Sort data chronologically

2. **Creating Line Plots**
   - Basic line plot creation
   - Proper axis labeling
   - Grid lines and formatting

3. **Identifying Trends**
   - Calculate trend direction
   - Measure percent change
   - Add trend lines to plots

4. **Detecting Anomalies**
   - Use z-score method
   - Highlight unusual patterns
   - Interpret spikes and drops

### ✅ Key Takeaways

- Time-series data must be sorted chronologically
- Line plots show continuity and trends over time
- Trends can be upward, downward, or stable
- Anomalies are detected using statistical methods
- Visualization helps identify patterns and changes

### 📝 Next Steps

1. Run the demonstration script
2. Open and explore the Jupyter notebook
3. Review the quick reference guide
4. Record your video walkthrough using the provided script
5. Practice with your own time-series data

**Status:** ✅ COMPLETED
