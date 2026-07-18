---
title: "[Solution] R Apply FUN Value Must Be Length 1 Error Fix"
description: "Fix 'apply: FUN value must be length 1' in R. Resolve apply function return value length issues in matrix operations."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# R Apply FUN Value Must Be Length 1 Error Fix

The `apply: FUN value must be length 1` error occurs when the function passed to `apply()` returns a value of length other than 1, and R cannot simplify the result.

## What This Error Means

The `apply()` family of functions expects the applied function to return a single value per row/column when simplifying. When the function returns multiple values, R cannot create a simple matrix result.

A typical error:

```
Error in apply(mat, 1, my_func) : 
  dims [product 24] do not match the length of object [6]
```

## Why It Happens

Common causes include:

- **Function returns vector of length > 1** — Each call returns multiple values.
- **Missing simplify parameter** — apply tries to simplify and fails.
- **Function returns different lengths** — Inconsistent return values.
- **Using apply on data frame with non-numeric columns** — Type mismatches.
- **Wrong MARGIN** — Using margin 1 when 2 is needed.

## How to Fix It

### Fix 1: Use simplify = FALSE

```r
# RIGHT: Keep result as list
result <- apply(mat, 1, function(x) c(mean = mean(x), sd = sd(x)), simplify = FALSE)
```

### Fix 2: Use sapply or vapply instead

```r
# RIGHT: sapply for automatic simplification
result <- sapply(1:nrow(mat), function(i) mean(mat[i, ]))

# RIGHT: vapply with specified output type
result <- vapply(1:nrow(mat), function(i) mean(mat[i, ]), numeric(1))
```

### Fix 3: Return single value from function

```r
# WRONG: Returns two values
apply(mat, 1, function(x) c(mean(x), sd(x)))

# RIGHT: Return single value
apply(mat, 1, function(x) mean(x))
```

### Fix 4: Use rowSums and colSums

```r
# RIGHT: Built-in functions are faster
rowSums(mat)
colMeans(mat)
```

### Fix 5: Restructure result manually

```r
# RIGHT: Capture and restructure
result_list <- apply(mat, 1, function(x) list(mean = mean(x), sd = sd(x)))
result_matrix <- do.call(rbind, lapply(result_list, unlist))
```

## Common Mistakes

- **Assuming apply always returns matrix** — It depends on `simplify` parameter.
- **Using apply when vectorized function exists** — Prefer vectorized operations.
- **Not checking function return length** — Verify with `length()` before apply.

## Related Pages

- [R Lapply Error](r-lapply-error) — lapply iteration issues
- [R Dimension Error](r-dimension-error) — Dimension mismatch issues
- [R Type Error](r-type-error) — Type conversion errors
