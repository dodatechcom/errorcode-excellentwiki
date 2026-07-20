---
title: "[Solution] Python statistics Error — Statistics Module Calculation Errors"
description: "Fix Python statistics errors including StatisticsError, mean/median/mode failures, empty data, and single-value statistics. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 227
---

# Python statistics Error — Statistics Module Calculation Errors

The `statistics` module provides mathematical statistics functions. Errors arise from empty data, single-value calculations, multimode ambiguity, and invalid inputs.

## Common Causes

```python
import statistics

# Error: Mean of empty data
statistics.mean([])
# statistics.StatisticsError: no mean for empty data
```

```python
import statistics

# Error: Median of empty data
statistics.median([])
# statistics.StatisticsError: no median for empty data
```

```python
import statistics

# Error: Stdev requires at least two data points
statistics.stdev([5])
# statistics.StatisticsError: stdev requires at least two data points
```

```python
import statistics

# Error: Mode with no unique mode
statistics.mode([1, 1, 2, 2])
# statistics.StatisticsError: no unique mode found
```

```python
import statistics

# Error: Variance of empty data
statistics.variance([])
# statistics.StatisticsError: no variance for empty data
```

## How to Fix

### Fix 1: Check Data Is Non-Empty Before Computing

```python
import statistics

def safe_mean(data):
    if not data:
        raise ValueError("Cannot compute mean of empty data")
    return statistics.mean(data)

try:
    result = safe_mean([])
except ValueError as e:
    print(e)  # Cannot compute mean of empty data

result = safe_mean([1, 2, 3, 4, 5])
print(result)  # 3
```

### Fix 2: Use multimode for Ambiguous Modes

```python
import statistics

# Use multimode when multiple values tie for most common
data = [1, 1, 2, 2, 3]
modes = statistics.multimode(data)
print(modes)  # [1, 2]

# Or use Counter for full frequency analysis
from collections import Counter
freq = Counter(data)
max_count = max(freq.values())
modes = [k for k, v in freq.items() if v == max_count]
```

### Fix 3: Ensure Enough Data Points for Stdev and Variance

```python
import statistics

def safe_stdev(data):
    if len(data) < 2:
        raise ValueError("stdev requires at least two data points")
    return statistics.stdev(data)

def safe_variance(data):
    if len(data) < 2:
        raise ValueError("variance requires at least two data points")
    return statistics.variance(data)

print(safe_stdev([10, 20, 30]))  # 10.0
```

### Fix 4: Handle Single-Value Statistics Gracefully

```python
import statistics

data = [5]

# Mean works with single value
print(statistics.mean(data))  # 5

# Median works with single value
print(statistics.median(data))  # 5

# Stdev does not — use pstdev for population
print(statistics.pstdev(data))  # 0.0
```

## Examples

```python
import statistics

# Analyze a dataset with validation
def analyze(data):
    if not data:
        return {"error": "Empty dataset"}
    if len(data) == 1:
        return {
            "mean": data[0],
            "median": data[0],
            "stdev": 0,
        }
    return {
        "mean": round(statistics.mean(data), 2),
        "median": statistics.median(data),
        "stdev": round(statistics.stdev(data), 2),
        "modes": statistics.multimode(data),
    }

scores = [85, 90, 78, 92, 88, 76, 95, 89]
result = analyze(scores)
print(result)
```

## Related Errors

- [Python ValueError](/languages/python/python-valueerror/)
- [Python StatisticsError](/languages/python/python-statisticserror/)
- [Python ZeroDivisionError](/languages/python/python-zerodivisionerror/)
