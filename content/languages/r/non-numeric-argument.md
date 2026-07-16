---
title: "[Solution] R Error — Non-Numeric Argument to Mathematical Function Fix"
description: "Fix R 'non-numeric argument to mathematical function' error when passing non-numeric data to math functions. Convert data to numeric first."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["non-numeric", "mathematical-function", "type-error", "conversion"]
weight: 5
---

# Non-Numeric Argument to Mathematical Function — Fix

The error `Error in Math.math_generic(x) : non-numeric argument to mathematical function` occurs when you pass a non-numeric value (like a character string or factor) to a mathematical function such as `sqrt()`, `log()`, `abs()`, or `sin()`.

## Common Causes

```r
# Cause 1: Character string passed to math function
x <- "10"
sqrt(x)  # Error: non-numeric argument to mathematical function

# Cause 2: Factor used in arithmetic
f <- factor(c(1, 2, 3))
sqrt(f)  # Error

# Cause 3: Data frame column is character type
df <- data.frame(value = c("1.5", "2.5", "3.5"))
sqrt(df$value)  # Error

# Cause 4: List containing mixed types
x <- list(1, "two", 3)
log(x)  # Error
```

## How to Fix

### Fix 1: Convert to numeric before math operations

```r
# Wrong
x <- "10"
result <- sqrt(x)

# Correct
x <- "10"
result <- sqrt(as.numeric(x))  # result: 3.162278
```

### Fix 2: Ensure data frame columns are numeric

```r
# Wrong
df <- data.frame(score = c("85", "90", "78"))
mean(df$score)  # Error

# Correct
df <- data.frame(score = c("85", "90", "78"))
df$score <- as.numeric(df$score)
mean(df$score)  # Works: 84.33333
```

### Fix 3: Check data type with str()

```r
# Diagnostic
df <- read.csv("data.csv")
str(df)  # Check if columns are numeric or character

# Fix any character columns
df$amount <- as.numeric(df$amount)
```

### Fix 4: Use sapply for vector math on lists

```r
# Wrong
x <- list(1, 4, 9)
sqrt(x)  # Error

# Correct
x <- list(1, 4, 9)
sapply(x, sqrt)  # Returns: 1, 2, 3
```

## Examples

```r
# Example 1: sqrt on character
x <- "16"
sqrt(x)
# Error: non-numeric argument to mathematical function

# Example 2: log on factor
f <- factor(c(10, 100, 1000))
log(f, base = 10)
# Error: non-numeric argument to mathematical function

# Example 3: sin on logical
x <- c(TRUE, FALSE, TRUE)
sin(x)
# Works but unexpected: sin(TRUE) = 0.841471

# Example 4: abs on character
x <- c("-5", "-10", "15")
abs(x)
# Error: non-numeric argument to mathematical function
```

## Related Errors

- [na-introduced]({{< relref "/languages/r/na-introduced" >}}) — NAs from coercion
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
- [error-in-read.csv]({{< relref "/languages/r/error-in-read.csv" >}}) — data import issues
