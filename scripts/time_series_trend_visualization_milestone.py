"""
Time-Series Trend Visualization Milestone

This script demonstrates how to identify and visualize trends over time using line plots.
It covers temporal data handling, line plot creation, trend identification, and anomaly detection.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class TimeSeriesVisualizer:
    """Main class for time-series visualization and analysis"""
    
    def __init__(self):
        self.df = None
        self.time_column = None
        
    def load_data(self, filepath):
        """Load dataset from CSV file"""
        try:
            self.df = pd.read_csv(filepath)
            print(f"✓ Dataset loaded successfully: {filepath}")
            print(f"  Shape: {self.df.shape}")
            return self.df
        except FileNotFoundError:
            print(f"✗ Error: File not found - {filepath}")
            return None
        except Exception as e:
            print(f"✗ Error loading file: {e}")
            return None
    
    def identify_temporal_columns(self):
        """Identify columns that contain temporal data"""
        if self.df is None:
            print("✗ No dataset loaded")
            return []
        
        temporal_cols = []
        for col in self.df.columns:
            # Check if column name suggests temporal data
            if any(keyword in col.lower() for keyword in ['date', 'time', 'year', 'month', 'day']):
                temporal_cols.append(col)
            # Try parsing as datetime
            else:
                try:
                    pd.to_datetime(self.df[col], errors='raise')
                    temporal_cols.append(col)
                except:
                    pass
        
        print(f"\n✓ Temporal columns identified: {temporal_cols}")
        return temporal_cols
    
    def parse_temporal_column(self, column_name):
        """Parse and validate temporal column"""
        if self.df is None:
            print("✗ No dataset loaded")
            return False
        
        if column_name not in self.df.columns:
            print(f"✗ Column '{column_name}' not found")
            return False
        
        try:
            self.df[column_name] = pd.to_datetime(self.df[column_name])
            self.time_column = column_name
            print(f"✓ Temporal column '{column_name}' parsed successfully")
            return True
        except Exception as e:
            print(f"✗ Error parsing temporal column: {e}")
            return False
    
    def sort_by_time(self):
        """Sort dataframe by temporal column"""
        if self.time_column is None:
            print("✗ No temporal column set")
            return False
        
        original_len = len(self.df)
        self.df = self.df.sort_values(by=self.time_column).reset_index(drop=True)
        
        print(f"✓ Data sorted by '{self.time_column}'")
        print(f"  All {original_len} data points preserved")
        return True
    
    def create_line_plot(self, value_column, title=None, figsize=(10, 6)):
        """Create a line plot for time-series data"""
        if self.df is None or self.time_column is None:
            print("✗ Data not ready for plotting")
            return None
        
        if value_column not in self.df.columns:
            print(f"✗ Column '{value_column}' not found")
            return None
        
        # Create figure
        fig, ax = plt.subplots(figsize=figsize)
        
        # Plot line
        ax.plot(self.df[self.time_column], self.df[value_column], 
                linewidth=2, marker='o', markersize=4, color='#2E86AB')
        
        # Formatting
        ax.set_xlabel(self.time_column, fontsize=12, fontweight='bold')
        ax.set_ylabel(value_column, fontsize=12, fontweight='bold')
        ax.set_title(title or f'{value_column} Over Time', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')
        
        # Rotate x-axis labels for readability
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        print(f"✓ Line plot created for '{value_column}'")
        return fig
    
    def identify_trend(self, value_column):
        """Identify the overall trend in the data"""
        if self.df is None or value_column not in self.df.columns:
            print("✗ Cannot identify trend")
            return None
        
        values = self.df[value_column].dropna()
        
        if len(values) < 3:
            print("✗ Insufficient data points for trend analysis (minimum 3 required)")
            return None
        
        # Calculate linear regression slope
        x = np.arange(len(values))
        y = values.values
        slope = np.polyfit(x, y, 1)[0]
        
        # Calculate percent change
        start_val = values.iloc[0]
        end_val = values.iloc[-1]
        percent_change = ((end_val - start_val) / start_val) * 100 if start_val != 0 else 0
        
        # Classify trend
        if abs(percent_change) < 5:
            direction = "stable"
        elif slope > 0:
            direction = "upward"
        else:
            direction = "downward"
        
        trend_result = {
            'direction': direction,
            'slope': slope,
            'percent_change': percent_change,
            'start_value': start_val,
            'end_value': end_val
        }
        
        print(f"\n✓ Trend Analysis for '{value_column}':")
        print(f"  Direction: {direction.upper()}")
        print(f"  Change: {percent_change:.2f}%")
        print(f"  Start value: {start_val:.2f}")
        print(f"  End value: {end_val:.2f}")
        
        return trend_result
    
    def detect_anomalies(self, value_column, threshold=2.0):
        """Detect anomalies using z-score method"""
        if self.df is None or value_column not in self.df.columns:
            print("✗ Cannot detect anomalies")
            return []
        
        values = self.df[value_column].dropna()
        mean = values.mean()
        std = values.std()
        
        if std == 0:
            print("✗ No variation in data - cannot detect anomalies")
            return []
        
        # Calculate z-scores
        z_scores = np.abs((values - mean) / std)
        anomalies = []
        
        for idx, z_score in enumerate(z_scores):
            if z_score > threshold:
                anomalies.append({
                    'index': idx,
                    'timestamp': self.df[self.time_column].iloc[idx],
                    'value': values.iloc[idx],
                    'z_score': z_score
                })
        
        print(f"\n✓ Anomaly Detection for '{value_column}':")
        print(f"  Threshold: {threshold} standard deviations")
        print(f"  Anomalies found: {len(anomalies)}")
        
        if anomalies:
            for anomaly in anomalies:
                print(f"    - {anomaly['timestamp']}: {anomaly['value']:.2f} (z-score: {anomaly['z_score']:.2f})")
        
        return anomalies
    
    def create_comprehensive_plot(self, value_column, show_anomalies=True):
        """Create a comprehensive plot with trend line and anomalies"""
        fig = self.create_line_plot(value_column, 
                                     title=f'{value_column} Over Time - Trend Analysis')
        
        if fig is None:
            return None
        
        ax = fig.axes[0]
        
        # Add trend line
        values = self.df[value_column].dropna()
        x = np.arange(len(values))
        z = np.polyfit(x, values.values, 1)
        p = np.poly1d(z)
        
        ax.plot(self.df[self.time_column], p(x), 
                "--", linewidth=2, color='red', alpha=0.7, label='Trend Line')
        
        # Highlight anomalies
        if show_anomalies:
            anomalies = self.detect_anomalies(value_column)
            if anomalies:
                anomaly_times = [a['timestamp'] for a in anomalies]
                anomaly_values = [a['value'] for a in anomalies]
                ax.scatter(anomaly_times, anomaly_values, 
                          color='red', s=100, marker='X', 
                          label='Anomalies', zorder=5)
        
        ax.legend()
        plt.tight_layout()
        
        return fig


def generate_sample_data():
    """Generate sample time-series data for demonstration"""
    # Create date range
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='W')
    
    # Generate trend with noise
    n = len(dates)
    trend = np.linspace(100, 150, n)
    noise = np.random.normal(0, 5, n)
    values = trend + noise
    
    # Add some anomalies
    values[10] = 180  # Spike
    values[25] = 70   # Drop
    
    df = pd.DataFrame({
        'date': dates,
        'sales': values,
        'temperature': np.random.normal(20, 5, n)
    })
    
    return df


def main():
    """Main demonstration function"""
    print("=" * 60)
    print("TIME-SERIES TREND VISUALIZATION MILESTONE")
    print("=" * 60)
    
    # Initialize visualizer
    visualizer = TimeSeriesVisualizer()
    
    # Generate sample data
    print("\n1. GENERATING SAMPLE DATA")
    print("-" * 60)
    df = generate_sample_data()
    df.to_csv('data/processed/sample_timeseries.csv', index=False)
    print("✓ Sample data generated and saved")
    
    # Load data
    print("\n2. LOADING DATA")
    print("-" * 60)
    visualizer.load_data('data/processed/sample_timeseries.csv')
    
    # Identify temporal columns
    print("\n3. IDENTIFYING TEMPORAL COLUMNS")
    print("-" * 60)
    temporal_cols = visualizer.identify_temporal_columns()
    
    # Parse temporal column
    print("\n4. PARSING TEMPORAL DATA")
    print("-" * 60)
    visualizer.parse_temporal_column('date')
    
    # Sort by time
    print("\n5. SORTING DATA BY TIME")
    print("-" * 60)
    visualizer.sort_by_time()
    
    # Create line plot
    print("\n6. CREATING LINE PLOT")
    print("-" * 60)
    fig1 = visualizer.create_line_plot('sales')
    if fig1:
        plt.savefig('outputs/timeseries_line_plot.png', dpi=300, bbox_inches='tight')
        print("  Saved: outputs/timeseries_line_plot.png")
    
    # Identify trend
    print("\n7. IDENTIFYING TRENDS")
    print("-" * 60)
    trend = visualizer.identify_trend('sales')
    
    # Detect anomalies
    print("\n8. DETECTING ANOMALIES")
    print("-" * 60)
    anomalies = visualizer.detect_anomalies('sales', threshold=2.0)
    
    # Create comprehensive plot
    print("\n9. CREATING COMPREHENSIVE PLOT")
    print("-" * 60)
    fig2 = visualizer.create_comprehensive_plot('sales')
    if fig2:
        plt.savefig('outputs/timeseries_comprehensive.png', dpi=300, bbox_inches='tight')
        print("✓ Comprehensive plot saved: outputs/timeseries_comprehensive.png")
    
    print("\n" + "=" * 60)
    print("MILESTONE COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("• Time-series data must be sorted chronologically")
    print("• Line plots show continuity and trends over time")
    print("• Trends can be upward, downward, or stable")
    print("• Anomalies are detected using statistical methods")
    print("• Visualization helps identify patterns and changes")
    
    plt.show()


if __name__ == "__main__":
    main()
