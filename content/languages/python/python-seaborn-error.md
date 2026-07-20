---
title: "[Solution] Python Seaborn Error — Missing Data, Categorical & Palette Errors"
description: "Fix Python Seaborn errors by resolving data issues, categorical plot failures, and palette configuration problems. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 404
---

# Python Seaborn Error — Missing Data, Categorical & Palette Errors

Seaborn errors occur when input data contains unexpected NaN values, categorical plot types receive continuous data, color palettes have fewer colors than categories, or FacetGrid configurations are invalid.

## Common Causes

```python
import seaborn as sns
import pandas as pd

# 1. Missing data in plot columns
df = pd.DataFrame({"x": [1, 2, None], "y": [4, None, 6]})
sns.scatterplot(data=df, x="x", y="y")  # raises warning or error
```

```python
# 2. Categorical plot on continuous data
df = pd.DataFrame({"category": [1.5, 2.7, 3.1], "value": [10, 20, 30]})
sns.boxplot(data=df, x="category", y="value")  # unexpected plot
```

```python
# 3. Palette has fewer colors than categories
df = pd.DataFrame({
    "cat": list("ABCDEFG"),
    "val": range(7)
})
sns.barplot(data=df, x="cat", y="val", palette="Set2")  # ValueError
```

```python
# 4. Invalid FacetGrid col_wrap
import seaborn as sns
g = sns.FacetGrid(pd.DataFrame({"a": [1]}), col_wrap="invalid")  # TypeError
```

```python
# 5. Hue variable not in dataframe
df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
sns.scatterplot(data=df, x="x", y="y", hue="missing_col")  # ValueError
```

## How to Fix

### Fix 1: Handle missing data before plotting

```python
import seaborn as sns
import pandas as pd

df = pd.DataFrame({"x": [1, 2, None], "y": [4, None, 6]})

# Drop rows with NaN
df_clean = df.dropna()
sns.scatterplot(data=df_clean, x="x", y="y")

# Or fill NaN values
df_filled = df.fillna(0)
sns.scatterplot(data=df_filled, x="x", y="y")
```

### Fix 2: Convert continuous data to categories for categorical plots

```python
import seaborn as sns
import pandas as pd

df = pd.DataFrame({"score": [85, 92, 78, 95, 88], "name": ["A", "B", "C", "D", "E"]})

# Bin continuous data into categories
df["grade"] = pd.cut(df["score"], bins=[0, 80, 90, 100], labels=["C", "B", "A"])
sns.boxplot(data=df, x="grade", y="score")
```

### Fix 3: Generate palette with enough colors

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

categories = list("ABCDEFGH")
df = pd.DataFrame({"cat": categories, "val": range(8)})

# Use a palette with enough colors
palette = sns.color_palette("husl", n_colors=len(categories))
sns.barplot(data=df, x="cat", y="val", palette=palette)
plt.show()
```

### Fix 4: Validate hue column exists

```python
import seaborn as sns
import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

hue_col = "group"
if hue_col in df.columns:
    sns.scatterplot(data=df, x="x", y="y", hue=hue_col)
else:
    print(f"Warning: '{hue_col}' not in dataframe, plotting without hue")
    sns.scatterplot(data=df, x="x", y="y")
```

## Examples

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Complete plot with proper data handling
df = sns.load_dataset("tips")
df = df.dropna(subset=["total_bill", "tip", "day"])

g = sns.FacetGrid(df, col="day", col_wrap=2, height=3)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_titles("{col_name}")
plt.show()
```

## Related Errors

- [ValueError](/languages/python/valueerror/) — invalid argument
- [KeyError](/languages/python/keyerror/) — column not found
- [TypeError](/languages/python/typeerror/) — wrong type passed
