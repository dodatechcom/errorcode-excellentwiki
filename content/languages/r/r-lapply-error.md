---
title: "[Solution] R Error In Lapply Object Not Iterable Fix"
description: "Fix 'Error in lapply: object not iterable' in R. Resolve lapply and sapply issues when iterating over non-iterable objects."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# R Error In Lapply Object Not Iterable Fix

The `Error in lapply: object not iterable` error occurs when you try to use `lapply()` or `sapply()` on an object that is not a list, vector, or data frame.

## What This Error Means

The `lapply()` function iterates over elements of a list or vector. When you pass a non-iterable object (like a matrix used incorrectly, a single value, or NULL), it fails.

A typical error:

```
Error in lapply(X, FUN) : object 'x' is not iterable
```

## Why It Happens

Common causes include:

- **Passing NULL to lapply** — NULL is not iterable.
- **Passing a matrix without specifying dimension** — Matrix treated as atomic vector.
- **Object is not a list or vector** — Function, environment, or S4 object.
- **Variable not defined** — Typo in variable name.
- **Wrong function used** — lapply on data frame columns requires different approach.

## How to Fix It

### Fix 1: Check object type before lapply

```r
# RIGHT: Verify object is iterable
if (is.null(x) || !is.atomic(x) && !is.list(x)) {
    stop("Object is not iterable")
}
result <- lapply(x, my_func)
```

### Fix 2: Handle NULL values

```r
# RIGHT: Provide default for NULL
x <- NULL
result <- lapply(x %||% list(), my_func)

# Or check explicitly
if (!is.null(x)) {
    result <- lapply(x, my_func)
}
```

### Fix 3: Convert matrix to list

```r
# RIGHT: Split matrix into list of rows
mat <- matrix(1:12, nrow = 3)
mat_list <- lapply(1:nrow(mat), function(i) mat[i, ])
result <- lapply(mat_list, my_func)
```

### Fix 4: Use seq_len for safe iteration

```r
# RIGHT: Safe iteration over data frame
df <- data.frame(a = 1:3, b = 4:6)
result <- lapply(seq_len(nrow(df)), function(i) {
    row <- df[i, ]
    sum(row)
})
```

### Fix 5: Use vapply for type-safe iteration

```r
# RIGHT: vapply checks return type
result <- vapply(list(1, 2, 3), function(x) x * 2, numeric(1))
```

## Common Mistakes

- **Assuming all R objects are iterable** — Only lists, vectors, and data frames are.
- **Not handling NULL in lists** — Use `compact()` from purrr to remove NULLs.
- **Using lapply when sapply is simpler** — sapply returns simpler structures.

## Related Pages

- [R Apply Error](r-apply-error) — apply function issues
- [R Named List Error](r-named-list-error) — List naming issues
- [R Object Not Found](r-object-not-found) — Undefined variable errors
