# Time-Series Trend Visualization - Video Walkthrough Script (2 Minutes)

## Video Structure

**Total Duration:** ~2 minutes
**Format:** Screen capture with narration
**Tools Needed:** Screen recorder, Python environment, sample data

---

## Script

### Introduction (15 seconds)

**[Screen: Show title slide or IDE]**

"Hi! Today I'm demonstrating time-series trend visualization using line plots. We'll load temporal data, create visualizations, identify trends, and detect anomalies. Let's get started!"

---

### Section 1: Loading and Preparing Data (20 seconds)

**[Screen: Show code editor with data loading code]**

"First, I'm loading our time-series dataset. Notice I'm parsing the date column and sorting the data chronologically - this is critical for time-series analysis."

**[Run code, show output]**

```python
df = pd.read_csv('sample_timeseries.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
print(df.head())
```

"We have 52 weeks of sales data from 2024. The data is now properly ordered by time."

---

### Section 2: Creating a Line Plot (25 seconds)

**[Screen: Show plotting code]**

"Now let's create a line plot. Line plots are perfect for time-series because they show continuity and make trends visually obvious."

**[Run code, show plot]**

```python
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sales'], linewidth=2, marker='o')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time')
plt.grid(True)
plt.show()
```

**[Point to plot on screen]**

"See how the line connects the data points? This emphasizes the temporal progression and makes it easy to spot patterns."

---

### Section 3: Identifying the Trend (25 seconds)

**[Screen: Show trend analysis code]**

"Let's identify the overall trend. I'm using linear regression to calculate the trend direction and magnitude."

**[Run code, show output]**

```python
slope = np.polyfit(x, y, 1)[0]
percent_change = ((end_val - start_val) / start_val) * 100
print(f"Trend: UPWARD, Change: {percent_change:.2f}%")
```

**[Screen: Show plot with trend line]**

"The red dashed line shows the trend. Our sales have an upward trend with a 50% increase over the year. This is a clear growth pattern."

---

### Section 4: Detecting Anomalies (25 seconds)

**[Screen: Show anomaly detection code]**

"Now let's detect anomalies - unusual spikes or drops. I'm using the z-score method with a threshold of 2 standard deviations."

**[Run code, show output]**

```python
z_scores = np.abs((df['sales'] - mean) / std)
anomalies = df[z_scores > 2.0]
print(f"Anomalies found: {len(anomalies)}")
```

**[Screen: Show plot with anomalies highlighted]**

**[Point to red X markers]**

"The red X markers show our anomalies. Week 10 has an unusual spike, and week 25 has a significant drop. These warrant further investigation."

---

### Section 5: Why Line Plots for Time-Series (20 seconds)

**[Screen: Show comparison or summary slide]**

"So why use line plots for time-series data? Three key reasons:"

**[Show bullet points or highlight on plot]**

"One: They show continuity between time points.
Two: They make trends immediately visible.
Three: They highlight sudden changes and anomalies."

**[Screen: Show final comprehensive plot]**

"Line plots turn temporal data into a visual story, making patterns obvious that would be hidden in tables of numbers."

---

### Conclusion (10 seconds)

**[Screen: Show summary or final plot]**

"That's time-series trend visualization! Remember: always sort by time, use line plots for continuity, and look for both trends and anomalies. Thanks for watching!"

---

## Recording Tips

### Before Recording:
1. ✅ Prepare sample data and test all code
2. ✅ Close unnecessary applications
3. ✅ Set screen resolution to 1920x1080 or 1280x720
4. ✅ Increase font size in IDE for visibility
5. ✅ Test audio levels
6. ✅ Practice the script 2-3 times

### During Recording:
1. ✅ Speak clearly and at moderate pace
2. ✅ Use mouse cursor to point to important elements
3. ✅ Pause briefly between sections
4. ✅ Show code execution and results
5. ✅ Keep energy level consistent

### After Recording:
1. ✅ Review for clarity and timing
2. ✅ Add captions if possible
3. ✅ Export in common format (MP4, 1080p)
4. ✅ Test playback before submission

---

## Alternative Script (Shorter Version - 90 seconds)

### Quick Version

**[0:00-0:10] Introduction**
"Time-series trend visualization using line plots. Let's analyze sales data."

**[0:10-0:30] Load and Plot**
"Loading data, sorting by time, creating line plot. See the continuous trend?"

**[0:30-0:50] Trend Analysis**
"Adding trend line. Upward trend, 50% growth. Clear pattern."

**[0:50-1:10] Anomaly Detection**
"Detecting anomalies with z-scores. Two outliers found and highlighted."

**[1:10-1:30] Why Line Plots**
"Line plots show continuity, reveal trends, highlight changes. Perfect for time-series."

---

## Key Points to Emphasize

### Must Mention:
1. ✅ **Temporal ordering is critical** - always sort by time
2. ✅ **Line plots show continuity** - connects data points
3. ✅ **Trends become visually obvious** - easier than reading numbers
4. ✅ **Anomalies stand out** - unusual patterns are highlighted
5. ✅ **Why line plots for time-series** - emphasize temporal progression

### Visual Elements to Show:
1. ✅ Raw data with date column
2. ✅ Basic line plot
3. ✅ Line plot with trend line
4. ✅ Line plot with anomalies highlighted
5. ✅ Final comprehensive visualization

### Common Mistakes to Avoid:
- ❌ Don't rush through the code
- ❌ Don't skip showing the actual plots
- ❌ Don't forget to explain WHY line plots are used
- ❌ Don't use technical jargon without explanation
- ❌ Don't go over 2 minutes (aim for 1:45-2:00)

---

## Submission Checklist

Before submitting your video:

- [ ] Video is approximately 2 minutes long
- [ ] Screen is clearly visible (high resolution)
- [ ] Audio is clear and audible
- [ ] All code executes successfully on screen
- [ ] Line plot creation is demonstrated
- [ ] Trend identification is explained
- [ ] Anomalies are pointed out
- [ ] Explanation of why line plots suit time-series is included
- [ ] Video format is compatible (MP4, MOV, AVI)
- [ ] File size is reasonable (<100MB preferred)

---

## Example Narration Variations

### Formal Style:
"In this demonstration, I will illustrate the process of time-series trend visualization using line plots. We begin by loading and preparing our temporal dataset..."

### Conversational Style:
"Hey! Let's dive into time-series visualization. I've got some sales data here, and we're going to see how line plots help us spot trends and weird patterns..."

### Educational Style:
"Time-series data tells a story over time. Today, we'll learn how to visualize that story using line plots. First, let's understand why temporal ordering matters..."

**Choose the style that feels most natural to you!**

---

## Technical Setup

### Recommended Tools:
- **Screen Recording**: OBS Studio, Camtasia, QuickTime (Mac), or built-in Windows recorder
- **Code Editor**: VS Code, Jupyter Notebook, or PyCharm
- **Audio**: Built-in microphone (test quality first)
- **Resolution**: 1920x1080 or 1280x720

### Code Environment:
```bash
# Ensure these are installed
pip install pandas matplotlib numpy

# Test your code before recording
python scripts/time_series_trend_visualization_milestone.py
```

### Sample Data:
Use the generated sample data from the script, or create your own:
```python
dates = pd.date_range('2024-01-01', '2024-12-31', freq='W')
sales = np.linspace(100, 150, len(dates)) + np.random.normal(0, 5, len(dates))
```

---

**Good luck with your video! Remember: clarity and demonstration are more important than perfection.**
