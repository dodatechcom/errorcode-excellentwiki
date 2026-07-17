---
title: "[Solution] Pandas GroupBy KeyError Fix"
description: "Fix pandas groupby KeyError when grouping column does not exist. Verify column names, handle multi-level keys, and check DataFrame structure."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Pandas GroupBy KeyError Fix

A `KeyError` in pandas `groupby()` is raised when the specified grouping column does not exist in the DataFrame, or when accessing a column after grouping that is not available.

## What This Error Means

Common messages:

- `KeyError: 'column_name'`
- `KeyError: "Column(s) ['col'] not found in axis"`

Pandas cannot locate the column used for grouping. This can happen when the column was renamed, dropped, or never existed in the DataFrame.

## Common Causes

```python
import pandas as pd

# Cause 1: Column name does not exist
df = pd.DataFrame({"id": [1, 2], "score": [90, 80]})
df.groupby("name")["score"].mean()  # KeyError: 'name'

# Cause 2: Column name case mismatch
df = pd.DataFrame({"Department": ["A", "B"], "salary": [50, 60]})
df.groupby("department")["salary"].sum()  # KeyError: 'department'

# Cause 3: Column was renamed or dropped earlier
df = df.rename(columns={"Department": "dept"})
df.groupby("Department")["salary"].sum()  # KeyError: 'Department'

# Cause 4: Multi-column groupby with one missing
df.groupby(["id", "missing_col"]).sum()  # KeyError: 'missing_col'
```

## How to Fix

### Fix 1: List columns before grouping

```python
print(df.columns.tolist())
df.groupby("Department")["salary"].sum()
```

### Fix 2: Rename column to match

```python
df = df.rename(columns={"department": "Department"})
df.groupby("Department")["salary"].sum()
```

### Fix 3: Handle missing columns in multi-column groupby

```python
group_cols = [c for c in ["id", "name", "region"] if c in df.columns]
df.groupby(group_cols).sum()
```

### Fix 4: Use agg with column validation

```python
group_col = "Department"
if group_col in df.columns:
    result = df.groupby(group_col)["salary"].agg(["mean", "sum"])
else:
    raise ValueError(f"Column '{group_col}' not found. Available: {df.columns.tolist()}")
```

### Fix 5: Reset index after groupby to access columns

```python
grouped = df.groupby("Department").agg({"salary": "mean"})
grouped = grouped.reset_index()  # 'Department' is now a column, not an index
print(grouped["Department"])
```

## Related Errors

- {{< relref "keyerror" >}} — General Python KeyError.
- {{< relref "pandas-merge-error" >}} — Pandas merge key not found.
