---
title: "[Solution] R readr Parsing Error"
description: "Fix readr parsing errors when importing delimited files. Handle column type mismatches, encoding issues, and malformed data."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A readr parsing error occurs when the `readr` package cannot parse a file due to unexpected data types, encoding issues, or malformed delimiters. The error typically shows the problematic line and column.

## Common Causes

- Column type mismatch (e.g., text in a numeric column)
- Incorrect delimiter specification
- Encoding issues with special characters
- Inconsistent column counts across rows
- Header row issues

## How to Fix

```r
# WRONG: Letting readr guess types incorrectly
library(readr)
data <- read_csv("data.csv")  # Parsing error

# CORRECT: Specify column types explicitly
data <- read_csv("data.csv", col_types = cols(
  id = col_integer(),
  name = col_character(),
  date = col_date(),
  amount = col_double()
))
```

```r
# WRONG: Wrong delimiter
data <- read_csv("data.tsv")  # Tab-separated file

# CORRECT: Use read_tsv for tab-separated files
data <- read_tsv("data.tsv")
# Or specify delimiter
data <- read_delim("data.tsv", delim = "\t")
```

```r
# WRONG: Ignoring encoding
data <- read_csv("data.csv")  # Error with non-UTF-8 data

# CORRECT: Specify encoding
data <- read_csv("data.csv", locale = locale(encoding = "latin1"))
```

## Examples

```r
# Example 1: Preview file to understand structure
problems <- read_csv("data.csv", n_max = 100)
problems(problems)  # Show any parsing issues

# Example 2: Skip problematic lines
data <- read_csv("data.csv", skip_empty_rows = TRUE)

# Example 3: Use read_csv with progress and show_col_types
data <- read_csv(
  "data.csv",
  show_col_types = FALSE,
  progress = FALSE
)

# Example 4: Handle malformed CSV
data <- read_csv(
  "data.csv",
  na = c("", "NA", "N/A", "."),
  trim_ws = TRUE
)
```

## Related Errors

- [error-in-read.csv]({{< relref "/languages/r/error-in-read.csv" >}}) — base R CSV reading
- [error-in-read.table]({{< relref "/languages/r/error-in-read.table" >}}) — base R table reading
- [error-in-parse]({{< relref "/languages/r/error-in-parse" >}}) — parsing errors
