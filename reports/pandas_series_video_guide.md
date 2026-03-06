# Pandas Series Video Walkthrough Guide

## Video Requirements
- **Duration**: Approximately 2 minutes
- **Format**: Screen capture with clear visibility
- **Content**: Demonstrate Pandas Series fundamentals

## Video Structure (~2 minutes)

### Introduction (15 seconds)
- Introduce yourself
- State the topic: "Pandas Series Fundamentals"
- Mention what will be covered

### Section 1: Creating Series from Lists (30 seconds)
**What to show:**
```python
import pandas as pd

# Create a Series from a list
temperatures = [72, 68, 75, 80, 77]
temp_series = pd.Series(temperatures)
print(temp_series)

# Create with custom index
scores = [95, 87, 92, 88, 90]
score_series = pd.Series(scores, index=["Alice", "Bob", "Charlie", "Diana", "Eve"])
print(score_series)
```

**What to say:**
- "A Series can be created from a Python list"
- "Notice the automatic index starting from 0"
- "We can also provide custom labels for the index"

### Section 2: Creating Series from NumPy Arrays (30 seconds)
**What to show:**
```python
import numpy as np

# Create from NumPy array
np_array = np.array([10, 20, 30, 40, 50])
np_series = pd.Series(np_array)
print(np_series)

# With custom index
random_data = np.random.randint(1, 100, size=5)
random_series = pd.Series(random_data, index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print(random_series)
```

**What to say:**
- "Series can also be created from NumPy arrays"
- "Data types are preserved from the array"
- "This bridges NumPy and Pandas workflows"

### Section 3: Understanding Index and Values (30 seconds)
**What to show:**
```python
products = pd.Series(
    [29.99, 49.99, 19.99, 99.99, 15.99],
    index=["Keyboard", "Mouse", "Cable", "Monitor", "Mousepad"]
)

# Show values and index
print(products.values)
print(products.index)

# Show different access methods
print(products.iloc[0])  # Positional
print(products['Mouse'])  # Label-based
```

**What to say:**
- "Every Series has values and an index"
- "Values are stored as a NumPy array"
- "We can access data by position or by label"

### Section 4: Why Series Are Useful (15 seconds)
**What to explain:**
- "Series add meaningful labels to data"
- "Labels make code more readable and intuitive"
- "Series are the building blocks for DataFrames"
- "They combine NumPy's performance with label-based access"

## Recording Tips

### Technical Setup
- Use screen recording software (OBS, Loom, QuickTime, etc.)
- Set resolution to at least 1280x720
- Increase terminal/IDE font size for visibility
- Use a clean, distraction-free environment

### Presentation Tips
- Speak clearly and at a moderate pace
- Run code live (don't just show static output)
- Point out key observations as code executes
- Keep energy positive and engaging

### Common Mistakes to Avoid
- Don't rush through the code
- Don't assume viewers know NumPy
- Don't skip explaining the index
- Don't forget to show both positional and label access

## Checklist Before Submitting

- [ ] Video is approximately 2 minutes long
- [ ] Screen is clearly visible
- [ ] Audio is clear and audible
- [ ] All four sections are covered
- [ ] Code runs without errors
- [ ] Series creation from list is demonstrated
- [ ] Series creation from NumPy array is demonstrated
- [ ] Index and values are explained
- [ ] Practical use case is mentioned

## Example Script

"Hi, I'm [Name], and today I'll demonstrate Pandas Series fundamentals.

First, let's create a Series from a Python list. [Run code] Notice how Pandas automatically creates an index starting from zero. We can also provide custom labels. [Run code]

Next, Series can be created from NumPy arrays. [Run code] The data types are preserved, which is important for numerical operations. [Run code with custom index]

Every Series has two components: values and index. [Show .values and .index] We can access data by position using iloc, or by label using the bracket notation. [Demonstrate both]

Series are powerful because they add meaningful labels to data, making our code more readable and intuitive. They're the foundation for DataFrames and essential for data science workflows.

Thanks for watching!"

## Submission
- Upload video to preferred platform (YouTube, Vimeo, Google Drive, etc.)
- Ensure video is accessible (public or unlisted with link)
- Submit the link as instructed
