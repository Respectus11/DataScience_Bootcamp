# Statistical Engine

A pure-Python statistical analysis engine built from scratch using only Python standard libraries. This project implements core statistical methods, Monte Carlo simulations, and demonstrates the Law of Large Numbers through practical applications.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Mathematical Logic](#mathematical-logic)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Acceptance Criteria](#acceptance-criteria)
- [License](#license)

## 🎯 Project Overview

This statistical engine provides:

1. **Core Statistical Analysis** - Complete implementation of descriptive statistics from scratch
2. **Monte Carlo Simulations** - Probabilistic modeling for real-world scenarios
3. **Law of Large Numbers Demonstration** - Interactive exploration of statistical convergence
4. **Comprehensive Testing** - Full unit test coverage using Python's built-in unittest framework

### Key Components

- **StatEngine Class**: Processes 1D numerical data with methods for central tendency, dispersion, and outlier detection
- **Monte Carlo Module**: Simulates server crash scenarios to demonstrate probability theory
- **Data Analysis**: Includes a mock dataset of 50 startup salaries for practical analysis

## ✨ Features

### Central Tendency Measures
- `get_mean()` - Arithmetic average
- `get_median()` - Middle value (handles both even and odd datasets)
- `get_mode()` - Most frequent value(s) with multimodal support

### Dispersion Metrics
- `get_variance(is_sample=True)` - Population or sample variance (Bessel's correction)
- `get_standard_deviation(is_sample=True)` - Population or sample standard deviation

### Outlier Detection
- `get_outliers(threshold=2)` - Z-score based outlier identification

### Advanced Features
- Automatic data cleaning and validation
- Comprehensive error handling for edge cases
- Support for both lists and tuples
- Caching for improved performance

## 📁 Folder Structure

```
statistical_engine/
│
├── data/
│   └── sample_salaries.json       # Mock dataset of 50 startup salaries
│
├── src/
│   ├── __init__.py                # Package initialization
│   ├── stat_engine.py             # StatEngine class implementation
│   └── monte_carlo.py             # Monte Carlo simulation functions
│
├── tests/
│   ├── __init__.py                # Test package initialization
│   └── test_stat_engine.py        # Comprehensive unit test suite
│
├── README.md                       # This file
└── main.py                         # Entry point for demonstrations
```

## 🧮 Mathematical Logic

### Variance Calculation

The engine implements both **Population Variance** and **Sample Variance**:

#### Population Variance (σ²)
```
σ² = Σ(xᵢ - μ)² / N
```
Where:
- `xᵢ` = each value in the dataset
- `μ` = population mean
- `N` = total number of values

#### Sample Variance (s²) - Bessel's Correction
```
s² = Σ(xᵢ - x̄)² / (N - 1)
```
Where:
- `x̄` = sample mean
- `N - 1` = degrees of freedom (Bessel's correction)

**Why Bessel's Correction?** When working with a sample rather than a population, dividing by `(N-1)` instead of `N` provides an unbiased estimator of the population variance.

### Median Calculation

The median is calculated differently based on dataset size:

#### Odd Number of Elements
```
median = x[(N+1)/2]
```
Returns the middle value after sorting.

#### Even Number of Elements
```
median = (x[N/2] + x[N/2 + 1]) / 2
```
Returns the average of the two middle values after sorting.

### Outlier Detection (Z-Score Method)

A data point is considered an outlier if:
```
|xᵢ - μ| > threshold × σ
```
Default threshold is 2 standard deviations.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Installation

1. **Clone the repository**
```bash
git clone <https://github.com/Respectus11/DataScience_Bootcamp >
cd statistical_engine
```

2. **Verify Python version**
```bash
python --version
```

3. **Run the main demonstration**
```bash
python main.py
```

### Running Specific Components

**Analyze salary data only:**
```bash
python -c "from main import analyze_salary_data; analyze_salary_data()"
```

**Run Monte Carlo simulation only:**
```bash
python -c "from main import demonstrate_monte_carlo; demonstrate_monte_carlo()"
```

## 📖 Usage

### Basic Usage

```python
from src.stat_engine import StatEngine

# Create a StatEngine instance
data = [1, 2, 3, 4, 5, 100]
engine = StatEngine(data)

# Calculate statistics
print(f"Mean: {engine.get_mean()}")
print(f"Median: {engine.get_median()}")
print(f"Mode: {engine.get_mode()}")
print(f"Variance (sample): {engine.get_variance(is_sample=True)}")
print(f"Standard Deviation: {engine.get_standard_deviation()}")
print(f"Outliers: {engine.get_outliers(threshold=2)}")

# Get comprehensive summary
summary = engine.get_summary()
```

### Monte Carlo Simulation

```python
from src.monte_carlo import simulate_crashes, demonstrate_law_of_large_numbers

# Simulate server crashes for 100 days
crashes, observed_prob = simulate_crashes(100)
print(f"Crashes: {crashes}, Observed probability: {observed_prob:.4f}")

# Demonstrate Law of Large Numbers
results = demonstrate_law_of_large_numbers(seed=42)
for days, data in results.items():
    print(f"{days} days: {data['observed_probability']:.4f} (error: {data['percent_error']:.2f}%)")
```

### Working with Different Data Types

```python
# Lists
engine1 = StatEngine([1, 2, 3, 4, 5])

# Tuples
engine2 = StatEngine((10, 20, 30, 40, 50))

# Numeric strings (automatically converted)
engine3 = StatEngine(['1', '2', '3', '4', '5'])

# Mixed int and float
engine4 = StatEngine([1, 2.5, 3, 4.5, 5])
```

## 🧪 Testing

### Run All Tests

```bash
# From the project root directory
python -m unittest discover -s tests
```

### Run Specific Test File

```bash
python tests/test_stat_engine.py
```

### Run Specific Test Class

```bash
python -m unittest tests.test_stat_engine.TestStatEngineMean -v
```

### Run with Verbose Output

```bash
python -m unittest discover -s tests -v
```

### Test Coverage

The test suite includes:

- ✅ **Mean Calculation** - Odd/even counts, decimals, negative numbers
- ✅ **Median Calculation** - Odd/even counts, unsorted data, duplicates
- ✅ **Mode Calculation** - Single mode, multimodal, all unique values
- ✅ **Variance Calculation** - Population vs sample, Bessel's correction
- ✅ **Standard Deviation** - Population vs sample, edge cases
- ✅ **Outlier Detection** - Basic detection, multiple outliers, custom thresholds
- ✅ **Error Handling** - Empty lists, None values, mixed data types
- ✅ **Data Validation** - Type conversion, numeric strings, mixed int/float

## ✅ Acceptance Criteria

### Core Functionality
- [x] **Mean Calculation** - Accurately computes arithmetic mean for any numeric dataset
- [x] **Median Calculation** - Correctly handles both even and odd length datasets
- [x] **Mode Calculation** - Returns all modes for multimodal distributions
- [x] **Mode Message** - Returns specific message when all values are unique
- [x] **Variance (Population)** - Implements σ² = Σ(x - μ)² / N
- [x] **Variance (Sample)** - Implements s² = Σ(x - x̄)² / (N-1) with Bessel's correction
- [x] **Standard Deviation** - Correctly computes √variance for both population and sample
- [x] **Outlier Detection** - Identifies values beyond threshold standard deviations

### Error Handling
- [x] **Empty List Handling** - Raises ValueError with descriptive message
- [x] **None Data Handling** - Raises ValueError with descriptive message
- [x] **Mixed Data Types** - Raises TypeError identifying problematic values
- [x] **Non-numeric Strings** - Raises TypeError with specific error details
- [x] **Single Value Sample Variance** - Raises ZeroDivisionError with guidance

### Advanced Features
- [x] **Multimodal Support** - Returns list of all modes when multiple exist
- [x] **Data Cleaning** - Automatically handles numeric strings and converts to float
- [x] **Tuple Support** - Accepts both lists and tuples as input
- [x] **Comprehensive Summary** - Provides all statistics in single dictionary
- [x] **Caching** - Implements performance optimization for repeated calculations

### Monte Carlo Simulation
- [x] **Basic Simulation** - Simulates binary outcomes with given probability
- [x] **LLN Demonstration** - Shows convergence with increasing sample sizes
- [x] **Interpretation** - Provides detailed explanation of statistical phenomena
- [x] **Reproducibility** - Supports random seed for consistent results

### Testing
- [x] **Unit Tests** - Comprehensive test suite covering all methods
- [x] **Edge Cases** - Tests for empty lists, single values, identical values
- [x] **Mathematical Accuracy** - Verifies against known mathematical outcomes
- [x] **Error Conditions** - Tests proper exception raising and messages

### Documentation
- [x] **README** - Complete project documentation
- [x] **Mathematical Formulas** - Clear explanation of all statistical methods
- [x] **Usage Examples** - Practical code examples for all features
- [x] **Setup Instructions** - Step-by-step installation and running guide

## 📊 Law of Large Numbers Explanation

### The Scenario
A startup's server has a theoretical 4.5% chance of crashing on any given day.

### Simulation Results
When we simulate this probability over different time periods:

- **10 days**: Observed probability varies wildly (0% to 20%+)
- **100 days**: Observed probability stabilizes somewhat (3% to 6%)
- **10,000 days**: Observed probability converges to ~4.5%

### Why Small Samples Are Dangerous for Budget Planning

Using only 10 days of data to predict yearly maintenance budget is extremely risky:

1. **High Variability** - Small samples have high variance, leading to unreliable estimates
2. **Misleading Estimates** - You might observe 0 crashes and budget for 0, when you should expect ~16 crashes/year
3. **Financial Risk** - Under-budgeting leads to unexpected costs and service disruptions
4. **Over-Budgeting** - Observing 2 crashes in 10 days (20%) might lead to 4x over-budgeting

### Recommendation
- Collect data over as many days as possible
- Use theoretical probability if available from engineering specifications
- Apply confidence intervals to account for uncertainty
- Use Monte Carlo simulations to stress-test budgets
---
