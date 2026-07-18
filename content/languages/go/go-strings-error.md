---
title: "[Solution] Go strings Error — How to Fix"
description: "Fix Go strings errors. Handle string manipulation, conversion, and performance."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go strings Error

Fix Go strings errors. Handle string manipulation, conversion, and performance.

## Why It Happens

- String concatenation in loop causes O(n²) performance
- String conversion between byte slice and string causes unnecessary allocation
- String comparison is case-sensitive when case-insensitive is needed
- String trimming removes too much or too little

## Common Error Messages

```
strings: invalid UTF-8
```
```
strings: index out of range
```
```
strings: invalid separator
```
```
strings: negative length
```

## How to Fix It

### Solution 1: Optimize string building

```go
var sb strings.Builder
for _, item := range items {
    sb.WriteString(item)
    sb.WriteString(",")
}
result := sb.String()
```

### Solution 2: Use strings functions

```go
strings.Contains(s, "substr")
strings.HasPrefix(s, "prefix")
strings.HasSuffix(s, "suffix")
strings.ToLower(s)
strings.Fields(s)       // split by whitespace
strings.Split(s, ",")  // split by separator
strings.TrimSpace(s)
```

### Solution 3: Convert between string and []byte efficiently

```go
// []byte to string
b := []byte("hello")

// string to []byte  
s := string(b)

// For zero-copy in Go 1.20+
s := string(b)  // compiler may optimize this
```

### Solution 4: Handle unicode

```go
// Get rune count
n := utf8.RuneCountInString(s)
// Iterate over runes
for i, r := range s {
    fmt.Printf("%d: %c\n", i, r)
}
```

## Common Scenarios

- String concatenation in a loop is very slow
- String to []byte conversion allocates memory unnecessarily
- String comparison does not work as expected for unicode

## Prevent It

- Use strings.Builder for efficient string concatenation
- Use strings.EqualFold for case-insensitive comparison
- Use utf8.RuneCountInString for accurate character count
