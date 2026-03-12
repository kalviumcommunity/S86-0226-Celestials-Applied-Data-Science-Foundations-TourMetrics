"""
Simple test script to verify matplotlib works
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("Loading data...")
df = pd.read_csv('data/raw/tours.csv')
print(f"Data loaded: {len(df)} rows")

print("Creating simple boxplot...")
fig, ax = plt.subplots()
ax.boxplot(df['Visitors'].dropna())
ax.set_title('Test Boxplot')
plt.savefig('outputs/visualizations/test_boxplot.png')
plt.close()
print("Boxplot saved successfully!")
