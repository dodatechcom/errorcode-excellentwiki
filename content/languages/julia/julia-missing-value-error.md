---
title: "Julia Nullable Missing Value Handling Error"
description: "Fix Julia missing value errors when using `missing` in operations that require concrete values."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Julia uses `missing` for absent data (like SQL NULL). Operations on `missing` propagate `missing` by default, which can cause unexpected results when concrete values are needed.

## Common Causes

- Arithmetic with missing values returns missing
- Comparison with missing returns missing, not boolean
- Functions that require non-missing values receive missing
- Aggregation functions propagate missing
- Filtering missing values from collections

## How to Fix

```julia
# WRONG: Missing propagation surprises
x = missing
y = x + 1  # missing, not an error

# CORRECT: Check for missing first
x = missing
ismissing(x) && error("value is missing")
y = x + 1
```

```julia
# WRONG: Comparison with missing
missing > 5  # missing, not false

# CORRECT: Use ismissing or coalesce
ismissing(missing)  # true
coalesce(missing, 0)  # 0
```

## Examples

```julia
# Example 1: Filter missing values
data = [1, missing, 3, missing, 5]
filtered = filter(!ismissing, data)  # [1, 3, 5]

# Example 2: Replace missing
data = [1, missing, 3]
clean = replace(data, missing => 0)  # [1, 0, 3]

# Example 3: Aggregation with missing
data = [1, missing, 3, 4]
sum(skipmissing(data))  # 8
mean(skipmissing(data))  # 2.666...

# Example 4: Conditional with missing
function safe_div(a, b)
    ismissing(a) || ismissing(b) ? missing : a / b
end
```

## Related Errors

- [TypeError](julia-type-error) -- type assertion failures
- [MethodError](julia-method-error) -- method not found
