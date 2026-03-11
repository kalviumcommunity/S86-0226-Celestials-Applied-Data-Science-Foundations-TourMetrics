# Summary Statistics Video Guide

**Duration:** ~2 Minutes  
**Format:** Screen capture with narration  
**Date:** March 11, 2026

---

## Video Structure and Timing

### Part 1: Introduction (15 seconds)
**What to show:**
- Open your terminal/IDE
- Display the products DataFrame

**What to say:**
> "Hello! Today I'll demonstrate computing and interpreting summary statistics for Pandas DataFrames. Summary statistics help us understand data distribution, central tendency, and spread. Let's start by loading our products dataset."

**Code to run:**
```python
import pandas as pd
df = pd.read_csv('data/raw/products.csv')
print(df.head())
```

---

### Part 2: Selecting a Column (15 seconds)
**What to show:**
- Select the Price column
- Display it as a Series

**What to say:**
> "First, let's select a numeric column. I'll choose the Price column, which gives us a Pandas Series containing all product prices."

**Code to run:**
```python
price_column = df['Price']
print(price_column)
print(f"This is a {type(price_column)}")
```

---

### Part 3: Computing Statistics (30 seconds)
**What to show:**
- Compute each statistic one by one
- Display the results clearly

**What to say:**
> "Now let's compute summary statistics. The mean tells us the average price is $208.78. The median, at $84.99, is the middle value and less affected by outliers. Our minimum price is $4.99 and maximum is $899.99, giving us a wide range. The standard deviation of $306.20 indicates high variability in our prices."

**Code to run:**
```python
print(f"Mean:   ${price_column.mean():.2f}")
print(f"Median: ${price_column.median():.2f}")
print(f"Min:    ${price_column.min():.2f}")
print(f"Max:    ${price_column.max():.2f}")
print(f"Std:    ${price_column.std():.2f}")
```

---

### Part 4: Interpretation (30 seconds)
**What to show:**
- Compare mean vs median
- Calculate coefficient of variation
- Explain what the numbers mean

**What to say:**
> "Let's interpret these results. Notice the mean of $208 is much higher than the median of $85. This tells us the data is right-skewed, meaning some expensive products are pulling the average up. The coefficient of variation is 147%, indicating very high variability - our products range from budget to premium items. The large range and high standard deviation confirm we have diverse pricing."

**Code to run:**
```python
mean_val = price_column.mean()
median_val = price_column.median()
print(f"Mean: ${mean_val:.2f}")
print(f"Median: ${median_val:.2f}")
print(f"Difference: ${mean_val - median_val:.2f}")

cv = (price_column.std() / mean_val) * 100
print(f"Coefficient of Variation: {cv:.1f}%")
print("→ High variability indicates diverse pricing")
```

---

### Part 5: Comparison (30 seconds)
**What to show:**
- Compare Price vs Stock statistics
- Use describe() method
- Show comparison table

**What to say:**
> "Finally, let's compare Price with Stock levels. Both columns show right-skewed distributions where mean exceeds median. Price has higher variability at 147% compared to Stock at 106%. Pandas' describe method gives us a quick statistical summary. This comparison helps us understand each column's characteristics and identify patterns."

**Code to run:**
```python
# Comparison table
print(f"{'Statistic':<12} {'Price':>12} {'Stock':>12}")
print("-" * 38)
print(f"{'Mean':<12} {df['Price'].mean():>12.2f} {df['Stock'].mean():>12.2f}")
print(f"{'Median':<12} {df['Price'].median():>12.2f} {df['Stock'].median():>12.2f}")
print(f"{'Std Dev':<12} {df['Price'].std():>12.2f} {df['Stock'].std():>12.2f}")

# Use describe()
print("\nUsing describe() method:")
print(df[['Price', 'Stock']].describe())
```

---

## Recording Tips

### Before Recording
- [ ] Close unnecessary applications
- [ ] Set up clean IDE/terminal window
- [ ] Increase font size for visibility (16-18pt recommended)
- [ ] Test audio levels
- [ ] Have script nearby but don't read verbatim
- [ ] Run through code once to ensure it works

### During Recording
- [ ] Speak clearly and at moderate pace
- [ ] Explain what you're doing as you type
- [ ] Pause briefly after each output
- [ ] Point out key numbers with cursor
- [ ] Be enthusiastic but professional
- [ ] If you make a mistake, pause and restart that section

### After Recording
- [ ] Watch the video to check clarity
- [ ] Verify audio is clear
- [ ] Check that code and outputs are visible
- [ ] Verify timing is ~2 minutes (±15 seconds is fine)
- [ ] Export in standard format (MP4, 1080p recommended)

---

## Screen Setup Recommendations

### Terminal/IDE Settings
- **Font Size:** 16-18pt minimum
- **Theme:** High contrast (dark or light)
- **Window Size:** Maximize or large enough for visibility
- **Line Length:** Keep code lines short (<80 characters)

### Screen Recording
- **Resolution:** 1920x1080 (1080p) or 1280x720 (720p)
- **Frame Rate:** 30fps minimum
- **Format:** MP4 (widely compatible)
- **Zoom:** Use screen zoom if needed for small text

### Audio
- **Microphone:** Use headset or external mic (not laptop mic)
- **Environment:** Quiet room with minimal echo
- **Volume:** Test to ensure clarity
- **Pacing:** Speak slightly slower than normal conversation

---

## Alternative Video Script (Condensed)

If you need a shorter or more concise version:

### 2-Minute Condensed Script

**Introduction (10s):**
> "Hi! I'm demonstrating summary statistics in Pandas. Here's our products dataset."

**Computing (50s):**
> "Let's analyze the Price column. Mean is $208, median is $85. The big difference suggests outliers. Min is $4.99, max is $899.99. Standard deviation of $306 shows high variability."

**Interpretation (30s):**
> "The coefficient of variation is 147%, indicating very diverse pricing. Mean exceeding median means right-skewed distribution - some expensive items pull the average up."

**Comparison (30s):**
> "Comparing Price and Stock: both right-skewed, both variable. Price has higher CV at 147% vs 106%. Pandas describe() gives quick summaries. These statistics help us understand our data before analysis."

---

## Common Video Mistakes to Avoid

❌ **Don't:**
- Rush through explanations
- Use small fonts
- Skip explaining what statistics mean
- Read directly from script (sound natural)
- Record with poor audio quality
- Show personal information on screen
- Have cluttered desktop visible

✓ **Do:**
- Explain each statistic briefly
- Use large, readable fonts
- Show enthusiasm for the topic
- Speak naturally and conversationally
- Test audio before final recording
- Keep screen clean and professional
- Show outputs clearly

---

## Video Checklist

### Pre-Recording
- [ ] Script reviewed and understood
- [ ] Code tested and working
- [ ] Screen size and fonts optimized
- [ ] Audio tested
- [ ] Recording software ready
- [ ] Distractions minimized

### Recording
- [ ] Introduction complete (15s)
- [ ] Column selection shown (15s)
- [ ] Statistics computed (30s)
- [ ] Interpretation provided (30s)
- [ ] Comparison demonstrated (30s)

### Post-Recording
- [ ] Video reviewed for quality
- [ ] Audio clear and understandable
- [ ] Code and outputs visible
- [ ] Total time ~2 minutes
- [ ] Uploaded to required platform
- [ ] Link submitted as instructed

---

## Example File Names for Organization

```
summary_statistics_milestone.py         # Main implementation
test_summary_statistics.py              # Test script
summary_statistics_milestone.md         # Documentation
summary_statistics_video_guide.md       # This file
summary_statistics_demo_video.mp4       # Your recorded video
```

---

## Submission Instructions

### What to Submit
1. **Pull Request** (if required by course):
   - Include `summary_statistics_milestone.py`
   - Include test results or screenshots
   - Brief description of what you implemented

2. **Video Link:**
   - Upload to YouTube/Vimeo/required platform
   - Ensure visibility settings are correct
   - Submit link as instructed

3. **Documentation:**
   - May include this report if requested
   - Screenshots of successful test runs

### Submission Format Example
```
Summary Statistics Milestone Submission

Name: [Your Name]
Date: March 11, 2026

Files Included:
- scripts/summary_statistics_milestone.py
- reports/summary_statistics_milestone.md
- scripts/test_summary_statistics.py

Video Link: [Your Video URL]
Video Duration: 2:03

Description:
Implemented comprehensive summary statistics computation and interpretation
for DataFrame columns. Demonstrated mean, median, std, min, max calculations
with detailed interpretation and column comparison.

Test Results: All tests passed ✓
```

---

## Quick Reference Commands

### Run Full Interactive Demo
```bash
python scripts/summary_statistics_milestone.py
```

### Run Quick Test
```bash
python scripts/test_summary_statistics.py
```

### Import Functions
```python
from scripts.summary_statistics_milestone import (
    load_products_data,
    compute_single_column_statistics,
    interpret_statistics,
    compare_multiple_columns,
    demonstrate_pandas_describe
)
```

### Basic Statistics in Console
```python
import pandas as pd
df = pd.read_csv('data/raw/products.csv')

# Quick statistics
print(df['Price'].mean())
print(df['Price'].median())
print(df['Price'].describe())
```

---

## Additional Resources

### Screen Recording Software
- **Free:**
  - OBS Studio (powerful, open source)
  - Loom (easy to use, cloud-based)
  - ShareX (Windows only)
  - QuickTime (Mac only)

- **Paid:**
  - Camtasia (professional features)
  - ScreenFlow (Mac only)
  - Snagit (simple and effective)

### Video Hosting
- YouTube (public or unlisted)
- Vimeo (professional)
- Google Drive (direct sharing)
- OneDrive (direct sharing)
- Loom (built-in hosting)

### Learning Resources
- Pandas Documentation: Descriptive Statistics
- Khan Academy: Statistics Fundamentals
- StatQuest Videos: Understanding Statistics

---

## Practice Suggestions

Before recording your final video:

1. **Practice Run 1:** Focus on code execution
   - Just run the code
   - Verify outputs
   - Check timing

2. **Practice Run 2:** Add narration
   - Explain as you go
   - Refine your explanations
   - Check pacing

3. **Practice Run 3:** Full recording
   - Record everything
   - Review for issues
   - Make notes for improvements

4. **Final Recording:** Polished version
   - Confident delivery
   - Clear explanations
   - Professional quality

---

## Troubleshooting

### If Code Doesn't Run
- Verify pandas is installed: `pip install pandas`
- Check file path to CSV is correct
- Ensure virtual environment is activated

### If Recording Issues
- Restart recording software
- Check screen resolution settings
- Free up disk space
- Close resource-heavy applications

### If Audio Issues
- Check microphone permissions
- Use external mic if laptop mic is poor
- Record in quiet environment
- Test audio before full recording

---

## Success Criteria

Your video should demonstrate:
- ✓ Clear screen with readable code (16-18pt font)
- ✓ Working code that runs without errors
- ✓ Explanation of what each statistic means
- ✓ Interpretation of results
- ✓ Comparison of two columns
- ✓ Clear audio narration
- ✓ Professional presentation
- ✓ Duration of approximately 2 minutes

---

**Good luck with your video recording!** 🎥

Remember: It doesn't have to be perfect. Show your understanding of the concepts, explain clearly, and demonstrate the working code. Authenticity and clarity matter more than polish.

---

*This guide supports the Summary Statistics Milestone for TourMetrics Data Science Foundations.*
