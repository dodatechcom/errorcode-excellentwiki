---
title: "[Solution] R data.frame Row Names Error"
description: "Fix data.frame row names errors including duplicate row names, invalid row name assignment, and merge issues."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A data.frame row names error occurs when R encounters issues with row names, such as duplicate row names, invalid row name values, or row name mismatches during operations like `merge()`, `rbind()`, or `cbind()`.

## Common Causes

- Duplicate row names in data frames
- Attempting to assign non-character or non-unique row names
- Row name conflicts when merging data frames
- Row names from different sources don't match

## How to Fix

```r
# WRONG: Duplicate row names
df <- data.frame(x = 1:3, row.names = c("a", "a", "b"))
df["a", ]  # Warning: duplicate row names

# CORRECT: Ensure unique row names
df <- data.frame(x = 1:3, row.names = c("a", "b", "c"))
df["a", ]
```

```r
# WRONG: Merging with conflicting row names
df1 <- data.frame(x = 1:3, row.names = c("a", "b", "c"))
df2 <- data.frame(y = 4:6, row.names = c("a", "b", "d"))
merge(df1, df2, by = "row.names")  # May give unexpected results

# CORRECT: Use merge with proper keys
df1$id <- rownames(df1)
df2$id <- rownames(df2)
merge(df1, df2, by = "id")
```

```r
# WRONG: rbind with different row names
df1 <- data.frame(a = 1:2, row.names = c("x", "y"))
df2 <- data.frame(a = 3:4, row.names = c("z", "w"))
rbind(df1, df2)  # May cause issues

# CORRECT: Reset row names before binding
rownames(df1) <- NULL
rownames(df2) <- NULL
rbind(df1, df2)
```

## Examples

```r
# Example 1: Reset row names
df <- data.frame(x = 1:5)
rownames(df) <- paste0("obs", 1:5)
df <- df[-3, ]  # Row 3 removed
rownames(df) <- NULL  # Reset to sequential

# Example 2: Check for duplicate row names
any(duplicated(rownames(df)))
# Fix duplicates
rownames(df) <- make.names(rownames(df), unique = TRUE)

# Example 3: Use tibble to avoid row name issues
library(tibble)
df <- tibble(x = 1:5)  # No row names by default
```

## Related Errors

- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}}) — index out of bounds
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — object not found
- [error-in-match]({{< relref "/languages/r/error-in-match" >}}) — matching issues
