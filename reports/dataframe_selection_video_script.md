# DataFrame Selection Milestone - Video Script Template

**Total Duration: ~2 Minutes**

---

## 🎬 INTRODUCTION (0:00 - 0:15)

**[Show your face or dive straight into screen]**

"Hello! Today I'll demonstrate DataFrame selection techniques in Pandas - specifically indexing and slicing. Let me show you how to select columns, rows by position, rows by label, and combine selections."

**[Switch to Jupyter Notebook/Python script]**

"Here's our sample Tour Performance dataset with 8 tours across different cities."

```python
# Show the dataset
df_tours.head()
```

---

## 📊 SECTION 1: Column Selection (0:15 - 0:35)

"First, let's look at column selection."

**[Type and execute]**

```python
# Single column returns a Series
df_tours['City']
```

"Single brackets with a column name returns a Series."

**[Type and execute]**

```python
# Multiple columns returns a DataFrame
df_tours[['City', 'Attendance', 'Revenue']]
```

"Double brackets with a list of column names returns a DataFrame. This is useful when you need to work with multiple columns together."

---

## 🔢 SECTION 2: Row Selection by Position (.iloc) (0:35 - 1:00)

"Now let's select rows by position using dot iloc."

**[Type and execute]**

```python
# First row
df_tours.iloc[0]
```

"iloc uses integer positions starting from zero. This gets the first row."

**[Type and execute]**

```python
# First 3 rows
df_tours.iloc[0:3]
```

"Slicing with iloc is exclusive of the end index, so this gets rows 0, 1, and 2."

**[Type and execute]**

```python
# Last 2 rows
df_tours.iloc[-2:]
```

"Negative indexing works too - this gives us the last two rows."

---

## 🏷️ SECTION 3: Row Selection by Label (.loc) (1:00 - 1:25)

"For label-based selection, we use dot loc."

**[Type and execute]**

```python
# Set TourID as index
df_labeled = df_tours.set_index('TourID')
df_labeled
```

"First, let me set TourID as the index."

**[Type and execute]**

```python
# Select by label
df_labeled.loc['T003']
```

"Now I can select a specific tour by its ID."

**[Type and execute]**

```python
# Range selection with loc
df_labeled.loc['T002':'T005']
```

"Important: Unlike iloc, loc slicing is inclusive of both ends. So this includes T002 through T005 - all four tours."

---

## 🎯 SECTION 4: Combined Selection (1:25 - 1:50)

"Finally, let's combine row and column selection."

**[Type and execute]**

```python
# Position-based: rows and columns
df_tours.iloc[0:3, 1:4]
```

"With iloc, we can specify both rows and columns by position. First 3 rows, columns 1 through 3."

**[Type and execute]**

```python
# Label-based: specific rows and columns
df_labeled.loc['T001':'T003', ['City', 'Revenue']]
```

"With loc, we can select by labels. Tours T001 through T003, but only City and Revenue columns."

**[Type and execute]**

```python
# Single value extraction
df_labeled.loc['T005', 'Revenue']
```

"You can even extract a single value - here's the revenue for tour T005."

---

## 🎓 CONCLUSION (1:50 - 2:00)

"To summarize: Use iloc for position-based selection with exclusive slicing, and loc for label-based selection with inclusive slicing. The key is understanding when to use each method."

**[Optional: Show quick reference or final thoughts]**

"Accurate data selection is crucial for analysis. Practice these techniques, and you'll avoid common mistakes. Thanks for watching!"

---

## 📝 ALTERNATIVE NARRATION OPTIONS

### If you're short on time, use these concise versions:

**Column Selection (Compact):**
"Single brackets give you a Series, double brackets give you a DataFrame."

**iloc (Compact):**
"iloc uses positions - zero-based, slicing excludes the end."

**loc (Compact):**
"loc uses labels - slicing includes both ends."

**Combined (Compact):**
"Format is bracket-rows-comma-columns for both methods."

---

## 🎥 RECORDING TIPS

### Before Recording:
- [ ] Test your screen recording software
- [ ] Zoom browser/IDE to 125-150% for visibility
- [ ] Close unnecessary windows/tabs
- [ ] Test audio quality
- [ ] Have water nearby
- [ ] Practice once without recording

### During Recording:
- [ ] Speak clearly and at moderate pace
- [ ] Pause briefly after each code execution
- [ ] Point to important parts of output if possible
- [ ] Don't worry about small mistakes - keep going
- [ ] Show enthusiasm - it's contagious!

### After Recording:
- [ ] Watch the full video
- [ ] Check if code and output are clearly visible
- [ ] Verify audio is clear
- [ ] Confirm video is approximately 2 minutes
- [ ] Export in common format (MP4, MOV)

---

## 🎬 FILMING VARIATIONS

### Option 1: Face + Screen
- Show your face in introduction (5 seconds)
- Switch to screen capture for demonstrations
- Return to face for conclusion (optional)

### Option 2: Screen Only
- Dive straight into code
- Use clear voiceover throughout
- Let the code speak for itself

### Option 3: Picture-in-Picture
- Small face cam in corner throughout
- Main screen shows code and output
- More personal connection

**Choose what makes you comfortable!**

---

## ⏱️ TIME MANAGEMENT

| Section | Target Time | Key Points |
|---------|-------------|------------|
| Introduction | 15s | Name, topic, dataset overview |
| Column Selection | 20s | Single vs multiple, Series vs DataFrame |
| Row by Position | 25s | .iloc, positions, exclusive slicing |
| Row by Label | 25s | .loc, labels, inclusive slicing |
| Combined | 25s | Format [rows, cols], both methods |
| Conclusion | 10s | Summary, when to use each |
| **TOTAL** | **120s** | **~2 minutes** |

---

## 🗣️ SPEAKING TIPS

### Pace:
- Speak at normal conversational speed
- Pause for 1-2 seconds after executing code
- Don't rush through examples

### Clarity:
- Pronounce technical terms clearly: "eye-lock" and "low-see"
- Emphasize key differences: "EXCLUSIVE" vs "INCLUSIVE"
- Use signposting: "First...", "Now...", "Finally..."

### Energy:
- Sound interested in what you're teaching
- Vary your tone to maintain engagement
- Smile while speaking (yes, it affects your voice!)

---

## ✅ FINAL CHECKLIST

Before submitting your video:

**Technical Quality:**
- [ ] Video resolution is at least 720p
- [ ] Audio is clear without background noise
- [ ] Code is readable (font size 14+ recommended)
- [ ] Output is visible after each command
- [ ] Video length is 1:45 - 2:15 (some flexibility)

**Content Coverage:**
- [ ] Demonstrated column selection
- [ ] Showed .iloc for position-based selection
- [ ] Showed .loc for label-based selection
- [ ] Combined row and column selection
- [ ] Explained when to use each method

**Presentation:**
- [ ] Clear introduction and conclusion
- [ ] Logical flow between sections
- [ ] Examples are easy to follow
- [ ] Voice is clear and audible
- [ ] Professional and polished

---

## 🎉 YOU'VE GOT THIS!

Remember:
- It doesn't have to be perfect
- Focus on clarity over perfection
- Your knowledge is what matters
- Practice makes confidence

**Good luck with your recording! 🎥**

---

## 📤 SUBMISSION CHECKLIST

After recording:
- [ ] Video saved in required format
- [ ] Video uploaded to specified platform
- [ ] Link copied and ready
- [ ] Any additional documentation prepared
- [ ] Submit according to course instructions

**Milestone complete - great work! 🌟**
