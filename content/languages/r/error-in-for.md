---
title: "[Solution] R Error — Invalid 'For' Loop Sequence Fix"
description: "Fix R 'invalid for loop sequence' error when loop variable is not a vector or sequence. Ensure iteration object is valid."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["for-loop", "loop-sequence", "iteration"]
weight: 5
---

# Invalid 'For' Loop Sequence — Fix

The error `Error in for (var in sequence) : invalid for loop sequence` occurs when the loop sequence in a `for` loop is not a valid vector, list, or sequence. The sequence must be an iterable object.

## Common Causes

```r
# Cause 1: Using a function that returns NULL
for (i in grep("pattern", character(0))) {
  print(i)
}
# Error: invalid for loop sequence (grep returns integer(0))

# Cause 2: Using a single value instead of sequence
for (i in length(1:5)) {
  print(i)
}
# Error: invalid for loop sequence (length returns single number)

# Cause 3: NULL sequence
seq <- NULL
for (i in seq) {
  print(i)
}
# Error: invalid for loop sequence

# Cause 4: Non-vector object
for (i in list()) {
  print(i)
}
# Error: invalid for loop sequence
```

## How to Fix

### Fix 1: Ensure sequence is a vector

```r
# Wrong
for (i in NULL) {
  print(i)
}

# Correct
for (i in 1:5) {
  print(i)
}
```

### Fix 2: Check sequence length before loop

```r
# Wrong
indices <- which(x > 10)
for (i in indices) {
  print(x[i])
}

# Correct
indices <- which(x > 10)
if (length(indices) > 0) {
  for (i in indices) {
    print(x[i])
  }
}
```

### Fix 3: Use seq_along() for safe iteration

```r
# Wrong — seq could be empty
for (i in 1:length(x)) {
  print(x[i])
}

# Correct — seq_along handles empty vectors
for (i in seq_along(x)) {
  print(x[i])
}
```

### Fix 4: Convert to explicit sequence

```r
# Wrong
for (i in grep("pattern", text)) {
  print(i)
}

# Correct
matches <- grep("pattern", text)
if (length(matches) > 0) {
  for (i in seq_along(matches)) {
    print(matches[i])
  }
}
```

## Examples

```r
# Example 1: NULL sequence
x <- NULL
for (i in x) print(i)
# Error in for (i in x) : invalid for loop sequence

# Example 2: Empty vector from function
result <- grep("xyz", c("a", "b", "c"))
for (i in result) print(i)
# Error in for (i in result) : invalid for loop sequence

# Example 3: Wrong use of length
for (i in length(1:5)) print(i)
# Error in for (i in length(1:5)) : invalid for loop sequence

# Example 4: Non-iterable object
val <- 5
for (i in val) print(i)
# Error in for (i in val) : invalid for loop sequence
```

## Related Errors

- [error-in-while]({{< relref "/languages/r/error-in-while" >}}) — while loop condition error
- [subscript-out-of-bounds]({{< relref "/languages/r/subscript-out-of-bounds" >}}) — index beyond bounds
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
