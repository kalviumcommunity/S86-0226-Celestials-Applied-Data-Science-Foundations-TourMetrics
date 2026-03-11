# Design Document: Data Standardization Milestone

## Overview

The data standardization system provides a modular, configurable framework for cleaning and normalizing Pandas DataFrames. The design emphasizes composability, allowing users to apply individual standardization operations or chain multiple operations together. The system processes CSV files from a designated directory and provides comprehensive inspection capabilities to verify transformations.

The architecture follows a functional approach where each standardization operation is a pure transformation that can be applied independently or composed with others. This design supports both interactive data exploration and automated data pipeline integration.

## Architecture

The system consists of four main layers:

1. **Data Loading Layer**: Handles CSV file reading with encoding detection and delimiter inference
2. **Standardization Layer**: Implements individual transformation operations for columns, text, numbers, and dates
3. **Configuration Layer**: Manages user preferences and default behaviors
4. **Inspection Layer**: Provides comparison, reporting, and export capabilities

```
┌─────────────────────────────────────────────────────┐
│                  User Interface                      │
└─────────────────────────────────────────────────────┘
                         │
┌─────────────────────────────────────────────────────┐
│              Configuration Manager                   │
│  (Stores user preferences and defaults)             │
└─────────────────────────────────────────────────────┘
                         │
┌─────────────────────────────────────────────────────┐
│           Standardization Orchestrator               │
│  (Coordinates transformation pipeline)               │
└─────────────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼──────┐  ┌──────▼──────┐  ┌─────▼──────┐
│   Column     │  │    Text     │  │  Numeric   │
│ Standardizer │  │ Normalizer  │  │  & Date    │
│              │  │             │  │ Converter  │
└──────────────┘  └─────────────┘  └────────────┘
                         │
┌─────────────────────────────────────────────────────┐
│              Inspection & Reporting                  │
│  (Change summaries, comparisons, exports)           │
└─────────────────────────────────────────────────────┘
                         │
┌─────────────────────────────────────────────────────┐
│                 Data Loading Layer                   │
│  (CSV reading, encoding detection)                  │
└─────────────────────────────────────────────────────┘
```

## Components and Interfaces

### 1. DataLoader

Responsible for loading CSV files with automatic encoding and delimiter detection.

```python
class DataLoader:
    def load_csv(file_path: str, encoding: Optional[str] = None, 
                 delimiter: Optional[str] = None) -> pd.DataFrame:
        """
        Load a CSV file into a DataFrame.
        
        Args:
            file_path: Path to CSV file (relative to data/raw/)
            encoding: Character encoding (auto-detected if None)
            delimiter: Column delimiter (auto-detected if None)
            
        Returns:
            DataFrame with original data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file cannot be parsed as CSV
        """
        
    def detect_encoding(file_path: str) -> str:
        """Detect file encoding using chardet library."""
        
    def detect_delimiter(file_path: str, encoding: str) -> str:
        """Detect CSV delimiter by analyzing first few lines."""
```

### 2. ColumnStandardizer

Transforms column names to follow consistent naming conventions.

```python
class ColumnStandardizer:
    def standardize_columns(df: pd.DataFrame, 
                           config: ColumnConfig) -> pd.DataFrame:
        """
        Standardize all column names in DataFrame.
        
        Args:
            df: Input DataFrame
            config: Configuration for column standardization
            
        Returns:
            DataFrame with standardized column names
        """
        
    def to_snake_case(name: str) -> str:
        """Convert string to snake_case format."""
        
    def remove_special_chars(name: str) -> str:
        """Remove non-alphanumeric characters except underscores."""
        
    def collapse_underscores(name: str) -> str:
        """Replace consecutive underscores with single underscore."""
        
    def ensure_unique_names(names: List[str]) -> List[str]:
        """Add numeric suffixes to duplicate names."""
```

### 3. TextNormalizer

Normalizes text data within DataFrame cells.

```python
class TextNormalizer:
    def normalize_text(df: pd.DataFrame, columns: List[str], 
                      config: TextConfig) -> pd.DataFrame:
        """
        Normalize text data in specified columns.
        
        Args:
            df: Input DataFrame
            columns: List of column names to normalize
            config: Configuration for text normalization
            
        Returns:
            DataFrame with normalized text
        """
        
    def strip_whitespace(text: str) -> str:
        """Remove leading/trailing whitespace and collapse internal spaces."""
        
    def normalize_case(text: str, case_type: CaseType) -> str:
        """Convert text to specified case (lower, upper, title)."""
        
    def standardize_categories(values: pd.Series, 
                              mapping: Dict[str, str]) -> pd.Series:
        """Map equivalent categorical values to canonical forms."""
```

### 4. NumericConverter

Converts and standardizes numeric data.

```python
class NumericConverter:
    def convert_numeric(df: pd.DataFrame, columns: List[str], 
                       config: NumericConfig) -> Tuple[pd.DataFrame, List[ConversionError]]:
        """
        Convert string representations to numeric types.
        
        Args:
            df: Input DataFrame
            columns: List of column names to convert
            config: Configuration for numeric conversion
            
        Returns:
            Tuple of (DataFrame with converted values, list of conversion errors)
        """
        
    def clean_numeric_string(value: str) -> str:
        """Remove commas, currency symbols, and percentage signs."""
        
    def parse_percentage(value: str) -> float:
        """Parse percentage string and convert to decimal."""
        
    def round_to_precision(value: float, decimals: int) -> float:
        """Round numeric value to specified decimal places."""
```

### 5. DateConverter

Parses and standardizes date/time data.

```python
class DateConverter:
    def convert_dates(df: pd.DataFrame, columns: List[str], 
                     config: DateConfig) -> Tuple[pd.DataFrame, List[ConversionError]]:
        """
        Parse date strings into datetime objects.
        
        Args:
            df: Input DataFrame
            columns: List of column names to convert
            config: Configuration for date parsing
            
        Returns:
            Tuple of (DataFrame with converted dates, list of conversion errors)
        """
        
    def parse_date(value: str, formats: List[str]) -> datetime:
        """Attempt to parse date using multiple format strings."""
        
    def handle_timezone(dt: datetime, target_tz: Optional[str]) -> datetime:
        """Convert datetime to target timezone if specified."""
```

### 6. StandardizationOrchestrator

Coordinates the application of multiple standardization operations.

```python
class StandardizationOrchestrator:
    def __init__(self, config: StandardizationConfig):
        """Initialize with configuration."""
        
    def standardize(df: pd.DataFrame) -> StandardizationResult:
        """
        Apply all configured standardization operations.
        
        Args:
            df: Input DataFrame
            
        Returns:
            StandardizationResult containing transformed DataFrame and metadata
        """
        
    def apply_column_standardization(df: pd.DataFrame) -> pd.DataFrame:
        """Apply column name standardization."""
        
    def apply_text_normalization(df: pd.DataFrame) -> pd.DataFrame:
        """Apply text normalization to configured columns."""
        
    def apply_numeric_conversion(df: pd.DataFrame) -> pd.DataFrame:
        """Apply numeric conversion to configured columns."""
        
    def apply_date_conversion(df: pd.DataFrame) -> pd.DataFrame:
        """Apply date conversion to configured columns."""
```

### 7. InspectionReporter

Provides tools for inspecting and comparing standardization results.

```python
class InspectionReporter:
    def generate_summary(original: pd.DataFrame, 
                        standardized: pd.DataFrame,
                        errors: List[ConversionError]) -> StandardizationSummary:
        """
        Generate comprehensive summary of changes.
        
        Returns:
            Summary containing column changes, value transformations, and errors
        """
        
    def compare_dataframes(original: pd.DataFrame, 
                          standardized: pd.DataFrame) -> ComparisonReport:
        """Generate side-by-side comparison of changes."""
        
    def export_to_csv(df: pd.DataFrame, output_path: str) -> None:
        """Export standardized DataFrame to CSV file."""
```

## Data Models

### Configuration Classes

```python
@dataclass
class ColumnConfig:
    """Configuration for column name standardization."""
    to_lowercase: bool = True
    to_snake_case: bool = True
    remove_special_chars: bool = True
    collapse_underscores: bool = True
    strip_underscores: bool = True
    ensure_unique: bool = True

@dataclass
class TextConfig:
    """Configuration for text normalization."""
    strip_whitespace: bool = True
    collapse_spaces: bool = True
    case_type: Optional[CaseType] = None  # None, 'lower', 'upper', 'title'
    category_mappings: Dict[str, Dict[str, str]] = field(default_factory=dict)

@dataclass
class NumericConfig:
    """Configuration for numeric conversion."""
    remove_commas: bool = True
    remove_currency: bool = True
    parse_percentages: bool = True
    decimal_places: Optional[int] = None
    error_handling: str = 'warn'  # 'warn', 'raise', 'ignore'

@dataclass
class DateConfig:
    """Configuration for date conversion."""
    date_formats: List[str] = field(default_factory=lambda: ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y'])
    dayfirst: bool = False
    target_format: Optional[str] = None
    target_timezone: Optional[str] = None
    error_handling: str = 'warn'

@dataclass
class StandardizationConfig:
    """Master configuration for all standardization operations."""
    column_config: ColumnConfig = field(default_factory=ColumnConfig)
    text_config: TextConfig = field(default_factory=TextConfig)
    numeric_config: NumericConfig = field(default_factory=NumericConfig)
    date_config: DateConfig = field(default_factory=DateConfig)
    text_columns: List[str] = field(default_factory=list)
    numeric_columns: List[str] = field(default_factory=list)
    date_columns: List[str] = field(default_factory=list)
```

### Result Classes

```python
@dataclass
class ConversionError:
    """Record of a failed conversion."""
    column: str
    row_index: int
    original_value: Any
    error_message: str

@dataclass
class ColumnChange:
    """Record of a column name change."""
    original: str
    standardized: str

@dataclass
class StandardizationSummary:
    """Summary of all standardization operations."""
    column_changes: List[ColumnChange]
    values_transformed: Dict[str, int]  # column -> count
    conversion_errors: List[ConversionError]
    total_rows: int
    total_columns: int

@dataclass
class StandardizationResult:
    """Complete result of standardization process."""
    dataframe: pd.DataFrame
    summary: StandardizationSummary
    original_dataframe: pd.DataFrame
```

