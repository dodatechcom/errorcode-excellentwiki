---
title: "[Solution] R Error — Argument 'X' Is Missing in Readline Fix"
description: "Fix R 'argument is missing' error in readline(). Provide the prompt argument correctly."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["readline", "input", "prompt", "missing-argument"]
weight: 5
---

# Argument 'X' Is Missing in Readline — Fix

The error `Error in readline(prompt) : argument "prompt" is missing` occurs when `readline()` is called without the required `prompt` argument.

## Common Causes

```r
# Cause 1: Empty readline call
x <- readline()  # Error: argument "prompt" is missing

# Cause 2: Missing prompt variable
prompt_text <- NULL
x <- readline(prompt_text)  # May error

# Cause 3: Using readline in non-interactive mode
readline("Enter value: ")  # May error in batch mode

# Cause 4: Forgetting prompt argument
input <- readline()  # Error
```

## How to Fix

### Fix 1: Always provide prompt argument

```r
# Wrong
x <- readline()

# Correct
x <- readline(prompt = "Enter value: ")
```

### Fix 2: Ensure prompt is a character string

```r
# Wrong
x <- readline(123)  # Numeric prompt

# Correct
x <- readline(prompt = "Enter a number: ")
```

### Fix 3: Check interactive mode

```r
# Wrong — may error in non-interactive
x <- readline("Enter: ")

# Correct — check interactive mode first
if (interactive()) {
  x <- readline("Enter: ")
} else {
  x <- "default_value"
}
```

### Fix 4: Use readLines for non-interactive input

```r
# Wrong — readline requires interaction
x <- readline("Enter: ")

# Correct — read from stdin in non-interactive
x <- readLines(file("stdin"), n = 1)
```

## Examples

```r
# Example 1: Empty readline
readline()
# Error in readline() : argument "prompt" is missing

# Example 2: Working readline
name <- readline(prompt = "What is your name? ")
cat("Hello,", name, "\n")

# Example 3: Numeric input
age <- as.integer(readline(prompt = "Enter your age: "))
cat("You are", age, "years old\n")

# Example 4: Loop with readline
for (i in 1:3) {
  val <- readline(prompt = paste("Enter value", i, ": "))
  cat("You entered:", val, "\n")
}
```

## Related Errors

- [wrong-number-args]({{< relref "/languages/r/wrong-number-args" >}}) — missing required argument
- [error-in-read.csv]({{< relref "/languages/r/error-in-read.csv" >}}) — reading data files
- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — undefined variable
