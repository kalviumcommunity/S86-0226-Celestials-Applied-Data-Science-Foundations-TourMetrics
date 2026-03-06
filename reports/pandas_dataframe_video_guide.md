# Pandas DataFrame Video Guide

## Video Recording Instructions

Create a 2-minute screen-capture video demonstrating Pandas DataFrame fundamentals.

## Required Equipment

- Screen recording software (OBS, Loom, QuickTime, Windows Game Bar, etc.)
- Python environment with Pandas installed
- Jupyter Notebook or Python script ready

## Video Structure (~2 Minutes)

### Introduction (15 seconds)
- State your name
- Mention: "Demonstrating Pandas DataFrame fundamentals"
- Show your screen with code editor ready

### Section 1: Creating DataFrame from Dictionary (30 seconds)

**What to show:**
```python
import pandas as pd

# Create dictionary
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 25, 22],
    'Grade': ['A', 'B', 'A']
}

# Convert to DataFrame
df = pd.DataFrame(student_data)
print(df)
```

**What to say:**
- "First, I'll create a DataFrame from a Python dictionary"
- "The dictionary keys become column names"
- "Each list becomes a column of data"
- Run the code and show the output

### Section 2: Loading DataFrame from File (30 seconds)

**What to show:**
```python
# Load from CSV
df_employees = pd.read_csv('data/raw/employees.csv')
print(df_employees)
```

**What to say:**
- "Now I'll load data from a CSV file"
- "Using pd.read_csv() with the file path"
- "The first row becomes column headers automatically"
- Show the loaded DataFrame

### Section 3: Inspecting DataFrame (30 seconds)

**What to show:**
```python
# Inspect structure
print(df_employees.head())
print(f"Shape: {df_employees.shape}")
print(df_employees.columns.tolist())
print(df_employees.dtypes)
```

**What to say:**
- "Let's inspect the DataFrame structure"
- "head() shows the first few rows"
- "shape tells us rows and columns"
- "dtypes shows data types for each column"

### Section 4: Why DataFrames Matter (15 seconds)

**What to say:**
- "DataFrames are essential because they:"
- "Organize data like spreadsheets"
- "Support different data types per column"
- "Are the foundation for all Pandas analysis"

## Recording Checklist

Before recording:
- [ ] Close unnecessary applications
- [ ] Clear desktop clutter
- [ ] Increase font size in editor (14-16pt minimum)
- [ ] Test microphone audio
- [ ] Prepare code in advance
- [ ] Have sample CSV file ready
- [ ] Test run the code once

During recording:
- [ ] Speak clearly and at moderate pace
- [ ] Show your face (if required) or screen only
- [ ] Execute code step by step
- [ ] Pause briefly after each output
- [ ] Point out key observations
- [ ] Keep within 2-minute limit

After recording:
- [ ] Review video for clarity
- [ ] Check audio quality
- [ ] Verify all code is visible
- [ ] Ensure outputs are readable
- [ ] Export in common format (MP4, MOV)

## Sample Script

```
[0:00-0:15] Introduction
"Hi, I'm [Name]. Today I'm demonstrating Pandas DataFrame fundamentals - 
how to create, load, and inspect DataFrames in Python."

[0:15-0:45] Dictionary to DataFrame
"First, let's create a DataFrame from a dictionary. I have a dictionary 
with student data - names, ages, and grades. When I pass this to 
pd.DataFrame(), the keys become column names and the lists become columns. 
Let me run this... and here's our DataFrame with 3 students."

[0:45-1:15] Loading from File
"Next, I'll load data from a CSV file using pd.read_csv(). I'm loading 
an employees file from the data folder. When I print it, you can see 
Pandas automatically used the first row as column headers. We have 
employee names, departments, salaries, and years of experience."

[1:15-1:45] Inspecting Structure
"Now let's inspect the structure. The head() method shows the first few rows. 
The shape attribute tells us we have 5 rows and 4 columns. We can see the 
column names as a list. And dtypes shows that Name and Department are text, 
while Salary and Years are numbers."

[1:45-2:00] Conclusion
"DataFrames are crucial because they organize data like spreadsheets, 
support different data types, and are the foundation for all data analysis 
in Pandas. Thanks for watching!"
```

## Technical Tips

### Font Size
- Minimum 14pt for code
- Minimum 16pt for output
- Use high contrast theme

### Screen Resolution
- Record at 1920x1080 or 1280x720
- Avoid 4K (file size too large)

### Audio
- Use external microphone if possible
- Reduce background noise
- Speak 6-12 inches from mic

### Editing (Optional)
- Trim dead space at start/end
- Add title slide (optional)
- Speed up slow sections slightly
- Add captions if required

## Common Mistakes to Avoid

1. **Going too fast** - Pause after each output
2. **Font too small** - Viewers can't read code
3. **Not explaining outputs** - Say what you see
4. **Skipping errors** - If error occurs, explain it
5. **Exceeding time limit** - Practice to stay under 2 minutes
6. **Poor audio** - Test before full recording
7. **Cluttered screen** - Close unnecessary windows

## File Submission

### Video Format
- MP4 (preferred) or MOV
- H.264 codec
- 720p or 1080p resolution
- Under 100MB file size

### Naming Convention
```
pandas_dataframe_fundamentals_[YourName].mp4
```

### Upload Options
- YouTube (unlisted or public)
- Google Drive (with link sharing)
- Vimeo
- Direct file upload (if platform supports)

### Submission Information
Include with video:
- Your name
- Date recorded
- Brief description
- Link to code files (if separate)

## Example Video Outline

```
00:00 - Title: "Pandas DataFrame Fundamentals"
00:03 - Import pandas
00:05 - Create dictionary with data
00:10 - Convert to DataFrame
00:15 - Display DataFrame
00:20 - Explain structure
00:25 - Load CSV file
00:30 - Display loaded data
00:35 - Show head()
00:40 - Show shape
00:45 - Show columns
00:50 - Show dtypes
00:55 - Show info()
01:00 - Explain why DataFrames matter
01:10 - Quick recap
01:15 - Thank you / End
```

## Quality Checklist

Your video should demonstrate:
- ✓ Clear audio throughout
- ✓ Readable code (large font)
- ✓ Visible outputs
- ✓ Smooth execution (no errors)
- ✓ Clear explanations
- ✓ Professional presentation
- ✓ Within time limit (2 minutes)
- ✓ All required topics covered

## Resources

### Screen Recording Software
- **Windows**: Xbox Game Bar (built-in), OBS Studio
- **Mac**: QuickTime, OBS Studio
- **Cross-platform**: OBS Studio, Loom, Camtasia

### Video Editing (Optional)
- **Free**: DaVinci Resolve, OpenShot, Shotcut
- **Paid**: Camtasia, Adobe Premiere

### Video Hosting
- YouTube
- Vimeo
- Google Drive
- Dropbox

---

**Remember:** The goal is to demonstrate understanding, not perfection. Focus on clear explanation and visible code execution.
