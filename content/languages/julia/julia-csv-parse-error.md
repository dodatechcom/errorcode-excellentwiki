---
title: "Julia CSV Parse Error Missing Delimiter"
description: "Fix Julia CSV.jl parse errors when CSV files have inconsistent delimiters, quoting issues, or encoding problems."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

CSV.jl parse errors occur when the CSV file format does not match expected structure, including wrong delimiters, unquoted fields with special characters, or encoding mismatches.

## Common Causes

- File uses comma but CSV.jl expects semicolon (locale settings)
- Quoted fields contain unescaped quote characters
- File encoding is not UTF-8
- Header row missing or has different column count than data
- Mixed line endings (CRLF and LF)

## How to Fix

```julia
# WRONG: Default delimiter mismatch
using CSV
df = CSV.read("european_data.csv", DataFrame)
# European CSVs use semicolons

# CORRECT: Specify delimiter
using CSV
df = CSV.read("european_data.csv", DataFrame; delim=';')
```

```julia
# WRONG: File encoding issue
df = CSV.read("data.csv", DataFrame)
# Error: invalid UTF-8

# CORRECT: Specify encoding
df = CSV.read("data.csv", DataFrame; encoding=enc"latin1")
```

## Examples

```julia
# Example 1: Basic CSV read
using CSV, DataFrames
df = CSV.read("sales.csv", DataFrame)
println(first(df, 5))

# Example 2: Custom delimiter and options
df = CSV.read("data.tsv", DataFrame;
    delim='\t',
    skipto=2,        # skip header
    header=["col1", "col2", "col3"],
    missingstring=["NA", "NULL", ""]
)

# Example 3: Write CSV
CSV.write("output.csv", df)
CSV.write("output.tsv", df; delim='\t')
```

## Related Errors

- [CSV error](julia-csv-jl-error) -- CSV.jl package issues
- [IO error](julia-io-stream-error) -- file reading problems
