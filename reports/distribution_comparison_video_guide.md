# Distribution Comparison Video Guide

**Duration:** ~2 Minutes  
**Format:** Screen capture with narration  
**Date:** March 11, 2026

---

## Video Structure and Timing

### Part 1: Introduction (15 seconds)
**What to show:**
- Open your terminal/IDE
- Display the products DataFrame
- Show that we'll compare two columns

**What to say:**
> "Hello! Today I'll demonstrate comparing distributions across multiple columns in Pandas. Single-column analysis is limited - comparison reveals patterns and context. Let's compare Price and Stock distributions in our products dataset."

**Code to run:**
```python
import pandas as pd
df = pd.read_csv('data/raw/products.csv')
print(df.head())
print("\nWe'll compare Price and Stock columns")
```

---

### Part 2: Computing Statistics for Both Columns (30 seconds)
**What to show:**
- Run describe() on multiple columns
- Show statistics side-by-side

**What to say:**
> "First, let's compute summary statistics for both columns simultaneously. Using describe(), we get a complete statistical overview. Price has mean $208, median $85. Stock has mean 48 units, median 27.5. Notice both columns show complete data with 14 values each."

**Code to run:**
```python
# Get statistics for both columns
print("Summary Statistics for Both Columns:")
print(df[['Price', 'Stock']].describe())

# Quick comparison
print("\nQuick Comparison:")
for col in ['Price', 'Stock']:
    print(f"{col}:")
    print(f"  Mean:   {df[col].mean():.2f}")
    print(f"  Median: {df[col].median():.2f}")
    print(f"  Range:  {df[col].min():.2f} to {df[col].max():.2f}")
```

---

### Part 3: Comparing Central Tendency (30 seconds)
**What to show:**
- Create comparison table for mean/median
- Calculate mean-median difference
- Explain skewness

**What to say:**
> "Let's compare central tendency. Both columns have mean greater than median - Price mean is $208 vs median $85, Stock mean is 48 vs median 27.5. This pattern indicates both distributions are right-skewed, meaning high values pull the average up. The consistency suggests similar distribution shapes across both variables."

**Code to run:**
```python
print(f"{'Measure':<15} {'Price':>12} {'Stock':>12}")
print("-" * 41)
print(f"{'Mean':<15} {df['Price'].mean():>12.2f} {df['Stock'].mean():>12.2f}")
print(f"{'Median':<15} {df['Price'].median():>12.2f} {df['Stock'].median():>12.2f}")

# Calculate skewness indicator
for col in ['Price', 'Stock']:
    diff_pct = ((df[col].mean() - df[col].median()) / df[col].mean()) * 100
    print(f"{col} skew: {diff_pct:.1f}% (mean > median = right-skewed)")
```

---

### Part 4: Comparing Spread and Variability (30 seconds)
**What to show:**
- Compare standard deviation and CV
- Interpret variability levels
- Show range comparison

**What to say:**
> "Now let's compare spread and variability. The coefficient of variation tells us relative variability. Price has CV of 147%, Stock has 106% - both are very high, indicating diverse values. Price is slightly more variable relative to its mean. The wide ranges confirm we have products spanning from budget to premium, with inventory from low to high stock."

**Code to run:**
```python
# Calculate CV for comparison
price_cv = (df['Price'].std() / df['Price'].mean()) * 100
stock_cv = (df['Stock'].std() / df['Stock'].mean()) * 100

print(f"{'Measure':<20} {'Price':>12} {'Stock':>12}")
print("-" * 46)
print(f"{'Std Deviation':<20} {df['Price'].std():>12.2f} {df['Stock'].std():>12.2f}")
print(f"{'Range':<20} {df['Price'].max()-df['Price'].min():>12.2f} {df['Stock'].max()-df['Stock'].min():>12.2f}")
print(f"{'CV (%)':<20} {price_cv:>12.1f} {stock_cv:>12.1f}")

print(f"\nBoth columns show very high variability (CV > 100%)")
```

---

### Part 5: Key Insights and Takeaways (30 seconds)
**What to show:**
- Summarize similarities and differences
- Explain practical implications
- Emphasize comparative thinking

**What to say:**
> "Key insights from our comparison: First, both distributions are right-skewed with similar patterns. Second, both show very high variability - diverse products and inventory. Third, Price is slightly more variable than Stock. This comparison reveals patterns we'd miss analyzing columns separately. Remember: context comes from comparison, not isolation. Always compare distributions to understand how variables relate and differ."

**Code to run:**
```python
print("Summary of Distribution Comparison:")
print()
print("Similarities:")
print("  • Both right-skewed (mean > median)")
print("  • Both highly variable (CV > 100%)")
print("  • Similar distribution patterns")
print()
print("Differences:")
print(f"  • Price more variable (CV: {price_cv:.1f}% vs {stock_cv:.1f}%)")
print(f"  • Different scales (dollars vs units)")
print()
print("Key Takeaway:")
print("Always compare - never analyze in isolation!")
```

---

## Recording Tips

### Before Recording
- [ ] Review the script multiple times
- [ ] Practice running code smoothly
- [ ] Set up clean workspace (close unnecessary tabs)
- [ ] Increase font size (16-18pt minimum)
- [ ] Test screen recording software
- [ ] Test audio (use quality microphone)
- [ ] Have water nearby for clear speech

### During Recording
- [ ] Speak clearly and at moderate pace
- [ ] Explain what you're doing before typing
- [ ] Pause briefly after each output to let viewers read
- [ ] Use cursor to point at important numbers
- [ ] Show enthusiasm for comparative insights
- [ ] Stay focused on the comparison theme
- [ ] If you make a mistake, pause and re-record that section

### After Recording
- [ ] Watch full video for quality
- [ ] Verify all code and outputs are visible
- [ ] Check audio clarity throughout
- [ ] Verify timing is approximately 2 minutes
- [ ] Export in standard format (MP4, 1080p)
- [ ] Upload to required platform

---

## Alternative Script (Condensed Version)

If you need a tighter 2-minute version:

### Condensed 2-Minute Script

**Introduction (10s):**
> "Hi! Today I'm comparing distributions across DataFrame columns. Here's our products data with Price and Stock."

**Statistics (40s):**
> "Let's compute statistics for both. Price: mean $208, median $85. Stock: mean 48, median 27.5. Both show mean greater than median, indicating right-skewed distributions - high values pull averages up."

**Variability (40s):**
> "Comparing variability: Price CV is 147%, Stock is 106%. Both very high, showing diverse values. Price ranges $5 to $900, Stock ranges 12 to 200 units. Similar patterns suggest related behaviors."

**Conclusion (30s):**
> "Key insights: both right-skewed, both highly variable, Price slightly more so. This comparison reveals patterns single-column analysis misses. Always compare distributions - context comes from comparison, not isolation."

---

## Screen Setup Recommendations

### IDE/Terminal Settings
- **Font**: 16-18pt (Consolas, Courier New, or Source Code Pro)
- **Theme**: High contrast (recommend dark theme with light text)
- **Window**: Maximize or fill most of screen
- **Line wrapping**: Enable if needed

### Recording Settings
- **Resolution**: 1920x1080 (1080p) or 1280x720 (720p)
- **Frame rate**: 30fps minimum
- **Codec**: H.264 (widely compatible)
- **Format**: MP4
- **Audio**: 128kbps minimum, 44.1kHz

### Audio Setup
- **Microphone**: Headset or external (avoid laptop mic)
- **Environment**: Quiet room, minimal background noise
- **Distance**: 6-8 inches from mouth
- **Test**: Record 30 seconds and play back

---

## Common Video Mistakes to Avoid

### Technical Mistakes
❌ Small fonts (viewers can't read)
❌ Cluttered desktop showing
❌ Poor audio quality
❌ Rushing through code
❌ Not pausing for outputs to be read
❌ Technical errors during recording

### Content Mistakes
❌ Only showing statistics without interpretation
❌ Analyzing columns separately, not comparing
❌ Missing the "why comparison matters" message
❌ Too much technical jargon
❌ Not explaining practical implications

### Presentation Mistakes
❌ Reading directly from script (robotic)
❌ Monotone voice
❌ Too fast or too slow pace
❌ Not showing enthusiasm
❌ Forgetting to summarize key points

---

## What Makes a Great Video

### Must-Have Elements
✓ **Clear Introduction** - Set context immediately
✓ **Visible Code** - Large, readable fonts
✓ **Step-by-Step** - Build understanding progressively
✓ **Interpretation** - Explain what numbers mean
✓ **Comparison Focus** - Emphasize comparative thinking
✓ **Clear Audio** - Professional, understandable
✓ **Good Pacing** - Not rushed, not dragging
✓ **Strong Conclusion** - Summarize key takeaways

### Excellence Indicators
⭐ Explains WHY comparison matters, not just HOW
⭐ Makes connections between statistics
⭐ Uses real language ("more variable", "diverse")
⭐ Shows enthusiasm for insights
⭐ Emphasizes practical implications
⭐ Professional but not overly formal

---

## Troubleshooting

### If Code Errors During Recording
1. Pause recording
2. Fix the error
3. Restart from beginning of that section
4. Edit later if needed

### If Audio Issues
1. Stop recording immediately
2. Check microphone settings
3. Do test recording
4. Restart when confirmed working

### If Timing Is Off
- Too short (< 1:45): Add more interpretation
- Too long (> 2:15): Condense explanations
- Ideal range: 1:50 - 2:10

---

## Post-Recording Checklist

### Quality Check
- [ ] Video plays correctly
- [ ] Audio is clear throughout
- [ ] All code is visible (fonts large enough)
- [ ] All outputs are visible
- [ ] No long pauses or dead air
- [ ] No personal info visible
- [ ] Professional appearance

### Content Check
- [ ] Introduction covers topic clearly
- [ ] Statistics computed for both columns
- [ ] Central tendency compared
- [ ] Spread/variability compared
- [ ] Interpretation provided
- [ ] Comparison emphasized
- [ ] Conclusion summarizes key points

### Technical Check
- [ ] Duration approximately 2 minutes
- [ ] Format is MP4 or compatible
- [ ] Resolution is 720p or higher
- [ ] File size is reasonable (<100MB)
- [ ] Video plays on target platform

---

## Submission Instructions

### Upload Options
- **YouTube**: Upload as unlisted (recommended)
- **Vimeo**: Free tier works fine
- **Google Drive**: Set sharing to "Anyone with link"
- **OneDrive**: Set sharing appropriately
- **Course Platform**: If provided

### Submit
1. Upload video to chosen platform
2. Get shareable link
3. Test link in incognito/private window
4. Submit link as instructed
5. Include video duration in submission

### Submission Format
```
Distribution Comparison Milestone - Video Submission

Name: [Your Name]
Date: March 11, 2026
Video Link: [Your URL]
Duration: [MM:SS]
Platform: [YouTube/Vimeo/etc.]

Content Summary:
- Compared Price and Stock distributions
- Demonstrated central tendency comparison
- Showed spread and variability analysis
- Emphasized importance of comparative thinking
```

---

## Quick Reference During Recording

### Opening Line
"Hello! Today I'll demonstrate comparing distributions across multiple columns in Pandas."

### Key Messages
1. "Never analyze columns in isolation"
2. "Context comes from comparison"
3. "Both columns are right-skewed"
4. "Both show very high variability"
5. "Comparison reveals patterns"

### Closing Line
"Remember: always compare distributions - insights emerge from comparison, not isolation."

---

## Practice Recommendations

### Before Final Recording

**Practice Run 1: Code Only**
- Just execute the code
- Verify everything works
- Note timing

**Practice Run 2: Code + Partial Narration**
- Run code and explain briefly
- Work on pacing
- Time each section

**Practice Run 3: Full Rehearsal**
- Complete narration
- Full recording (don't save)
- Identify improvement areas

**Final Recording: Polished Version**
- Confident delivery
- Smooth code execution
- Clear explanations
- Professional quality

---

## Resources

### Screen Recording Software
**Free:**
- OBS Studio (powerful, professional)
- Loom (easy, cloud-based)
- ShareX (Windows)
- QuickTime (Mac)

**Paid:**
- Camtasia (industry standard)
- ScreenFlow (Mac)
- Snagit (simple, effective)

### Video Editing (if needed)
- DaVinci Resolve (free, professional)
- iMovie (Mac, free)
- Shotcut (free, cross-platform)
- Windows Video Editor (built-in)

---

**Good luck with your recording!** 🎥

Remember: Your goal is to demonstrate understanding of distribution comparison. Show that you can compute, interpret, and explain comparative statistics. Clarity and understanding matter more than perfection.

---

*This guide supports the Distribution Comparison Milestone for TourMetrics Data Science Foundations.*