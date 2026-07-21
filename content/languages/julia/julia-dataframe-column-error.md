---
title: "Julia DataFrame Column Not Found Error"
description: "Fix Julia DataFrames.jl errors when accessing columns that do not exist in the DataFrame."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

DataFrame column errors occur when you try to access a column by name that does not exist in the DataFrame, or when using incorrect syntax for column selection.

## Common Causes

- Column name typo
- Column was renamed or dropped
- Using dot notation for columns with special characters
- Wrong DataFrame variable name
- Column access before DataFrame is populated

## How to Fix

```julia
# WRONG: Column does not exist
using DataFrames
df = DataFrame(name=["Alice"], age=[30])
df[:salary]  # Error: column not found

# CORRECT: Check column names first
println(names(df))  # ["name", "age"]
df[!, :name]  # access existing column
```

```julia
# WRONG: Wrong DataFrame name
df = DataFrame(a=[1])
df2[:a]  # UndefVarError: df2 not defined

# CORRECT: Use correct variable
df[:a]
```

## Examples

```julia
# Example 1: Column access
using DataFrames
df = DataFrame(name=["Alice", "Bob"], age=[30, 25])
df[!, :name]  # ["Alice", "Bob"]
df[1, :name]  # "Alice"

# Example 2: Add column
df[!, :city] = ["NYC", "LA"]
println(names(df))  # ["name", "age", "city"]

# Example 3: Rename columns
rename!(df, :name => :full_name)
println(names(df))  # ["full_name", "age", "city"]
```

## Related Errors

- [DataFrames error](julia-dataframe-error) -- DataFrame operations
- [Key error](julia-key-error) -- key not found
