---
title: "[Solution] Go strconv ParseInt Error Fix"
description: "Fix Go strconv.ParseInt invalid syntax error. Validate input strings, handle parsing errors, and use appropriate integer conversion methods."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# strconv.ParseInt Error Fix

The `strconv.ParseInt: parsing "...": invalid syntax` error occurs when a string cannot be converted to an integer using `strconv.ParseInt`.

## Description

`strconv.ParseInt` converts a string representation of a base-10 (or other base) integer to `int64`. If the string contains non-numeric characters, is empty, or overflows the target type, it returns an error. The error message includes the specific reason.

Common scenarios:

- **Non-numeric characters** — letters, spaces, or symbols in the string.
- **Empty string** — parsing an empty or whitespace-only string.
- **Overflow** — number exceeds `int64` range.
- **Leading/trailing whitespace** — whitespace not trimmed before parsing.
- **Decimal number** — `strconv.ParseInt` doesn't handle floats.

## Common Causes

```go
// Cause 1: Non-numeric characters
func main() {
    n, err := strconv.ParseInt("abc", 10, 64)
    // Error: invalid syntax
}

// Cause 2: Empty string
func main() {
    n, err := strconv.ParseInt("", 10, 64)
    // Error: invalid syntax
}

// Cause 3: Overflow
func main() {
    n, err := strconv.ParseInt("999999999999999999999", 10, 64)
    // Error: value out of range
}

// Cause 4: Decimal number
func main() {
    n, err := strconv.ParseInt("3.14", 10, 64)
    // Error: invalid syntax
}
```

## How to Fix

### Fix 1: Trim whitespace before parsing

```go
func parseAge(s string) (int64, error) {
    s = strings.TrimSpace(s)
    return strconv.ParseInt(s, 10, 64)
}
```

### Fix 2: Check for empty string first

```go
func parseCount(s string) (int64, error) {
    if s == "" {
        return 0, fmt.Errorf("empty string")
    }
    return strconv.ParseInt(s, 10, 64)
}
```

### Fix 3: Use ParseFloat for decimal numbers

```go
func parseNumber(s string) (float64, error) {
    return strconv.ParseFloat(s, 64)
}
```

### Fix 4: Handle overflow gracefully

```go
func parseWithFallback(s string, fallback int64) int64 {
    n, err := strconv.ParseInt(s, 10, 64)
    if err != nil {
        return fallback
    }
    return n
}
```

## Examples

```go
// This triggers: strconv.ParseInt: parsing "abc": invalid syntax
package main

import (
    "fmt"
    "strconv"
)

func main() {
    n, err := strconv.ParseInt("abc", 10, 64)
    fmt.Println(n, err)
}
```

## Related Errors

- [regexp-compile]({{< relref "/languages/go/regexp-compile" >}}) — regex pattern compilation errors.
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON parsing errors.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type conversion errors.
