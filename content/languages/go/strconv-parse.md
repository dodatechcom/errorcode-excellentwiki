---
title: "[Solution] Go Strconv Parse Error Fix"
description: "Fix Go strconv parsing error. Validate input before converting, handle parse errors, and use safe parsing functions."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["strconv", "parse", "conversion", "integer", "float"]
weight: 5
---

# Strconv: Parsing Invalid Syntax — Fix

A strconv parse error occurs when you try to convert a string to a number (int, float, etc.) but the string doesn't contain a valid number.

## Description

Go's `strconv` package provides functions like `Atoi`, `ParseInt`, `ParseFloat`, and `ParseBool` that return errors for invalid input. Unlike some languages, Go doesn't silently convert invalid strings to zero.

Common scenarios:

- **Non-numeric string** — `strconv.Atoi("abc")`.
- **Empty string** — `strconv.Atoi("")`.
- **Overflow** — number too large for the target type.
- **Invalid format** — `strconv.ParseFloat("1.2.3", 64)`.
- **Trailing characters** — `strconv.Atoi("123abc")`.

## Common Causes

```go
// Cause 1: Non-numeric input
n, err := strconv.Atoi("hello")
// strconv.Atoi: parsing "hello": invalid syntax

// Cause 2: Empty string
n, err := strconv.Atoi("")
// strconv.Atoi: parsing "": invalid syntax

// Cause 3: Overflow
n, err := strconv.ParseInt("99999999999999999999", 10, 64)
// strconv.ParseInt: parsing "99999999999999999999": value out of range

// Cause 4: Invalid float format
f, err := strconv.ParseFloat("1.2.3", 64)
// strconv.ParseFloat: parsing "1.2.3": invalid syntax

// Cause 5: Using wrong base
n, err := strconv.ParseInt("ff", 10, 64)
// strconv.ParseInt: parsing "ff": invalid syntax (ff is hex, not decimal)
```

## How to Fix

### Fix 1: Validate input before parsing

```go
// Wrong
n, err := strconv.Atoi(userInput)

// Correct
func safeAtoi(s string) (int, error) {
    s = strings.TrimSpace(s)
    if s == "" {
        return 0, fmt.Errorf("empty input")
    }
    n, err := strconv.Atoi(s)
    if err != nil {
        return 0, fmt.Errorf("invalid integer %q: %w", s, err)
    }
    return n, nil
}
```

### Fix 2: Use appropriate base for ParseInt

```go
// Wrong — "ff" is not decimal
n, err := strconv.ParseInt("ff", 10, 64)

// Correct — use base 16 for hex
n, err := strconv.ParseInt("ff", 16, 64)
fmt.Println(n) // 255

// Auto-detect base with base 0
n, err = strconv.ParseInt("0xff", 0, 64) // Hex
n, err = strconv.ParseInt("077", 0, 64)  // Octal
n, err = strconv.ParseInt("42", 0, 64)   // Decimal
```

### Fix 3: Handle overflow with bounds checking

```go
// Wrong — may overflow
n, err := strconv.ParseInt(userInput, 10, 64)

// Correct — check bounds
func safeParseInt(s string, bits int) (int64, error) {
    n, err := strconv.ParseInt(s, 10, bits)
    if err != nil {
        if numErr, ok := err.(*strconv.NumError); ok {
            if numErr.Err == strconv.ErrRange {
                return 0, fmt.Errorf("number out of range for %d-bit int: %s", bits, s)
            }
        }
        return 0, err
    }
    return n, nil
}
```

### Fix 4: Use custom parsing for flexible input

```go
// Wrong — strict parsing
n, err := strconv.Atoi("  42  ")

// Correct — trim whitespace first
n, err := strconv.Atoi(strings.TrimSpace(userInput))

// Or use regexp for complex patterns
var numRe = regexp.MustCompile(`^-?\d+(\.\d+)?$`)
if !numRe.MatchString(userInput) {
    return 0, fmt.Errorf("not a valid number: %s", userInput)
}
```

### Fix 5: Create a helper function with default value

```go
func atoiDefault(s string, defaultVal int) int {
    s = strings.TrimSpace(s)
    if s == "" {
        return defaultVal
    }
    n, err := strconv.Atoi(s)
    if err != nil {
        return defaultVal
    }
    return n
}

// Usage
port := atoiDefault(os.Getenv("PORT"), 8080)
```

## Examples

```go
// This triggers: strconv.Atoi: parsing "abc": invalid syntax
package main

import (
    "fmt"
    "strconv"
)

func main() {
    n, err := strconv.Atoi("abc")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(n)
}
```

## Related Errors

- [division-by-zero]({{< relref "/languages/go/division-by-zero" >}}) — division by zero after failed parsing.
- [regexp-compile]({{< relref "/languages/go/regexp-compile" >}}) — invalid regex pattern.
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — invalid JSON input.
