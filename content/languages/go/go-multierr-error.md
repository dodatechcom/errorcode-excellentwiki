---
title: "[Solution] Go Multi-Error Error — How to Fix"
description: "Fix Go multi-error errors. Handle error collection, flattening, formatting, and error aggregation patterns."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Multi-Error Error

Fix Go multi-error errors. Handle error collection, flattening, formatting, and error aggregation patterns.

## Why It Happens

- Multiple errors are collected but only the first is returned to callers
- Error flattening does not handle nested multi-errors correctly
- Multi-error formatting produces unreadable output
- Error count is not checked leading to empty error returns being treated as failures

## Common Error Messages

```
multierr: no errors to combine
```
```
multierr: cannot append non-error
```
```
multierr: failed to format
```
```
multierr: unexpected error type
```

## How to Fix It

### Solution 1: Collect errors with multierr.Append

```go
var errs error
errs = multierr.Append(errs, validateName(name))
errs = multierr.Append(errs, validateEmail(email))
errs = multierr.Append(errs, validateAge(age))
if errs != nil { return errs }
```

### Solution 2: Check multi-error count

```go
if errs != nil {
    if multierr.Len(errs) == 1 {
        return errors.Unwrap(errs)
    }
    return fmt.Errorf("validation failed: %w", errs)
}
```

### Solution 3: Format multi-errors for display

```go
if errs != nil {
    lines := strings.Split(multierr.Error(errs), "\n")
    for i, line := range lines {
        fmt.Printf("Error %d: %s\n", i+1, line)
    }
}
```

### Solution 4: Use multierr for concurrent error collection

```go
var mu sync.Mutex
var errs error
for _, item := range items {
    item := item
    g.Go(func() error {
        if err := process(item); err != nil {
            mu.Lock()
            errs = multierr.Append(errs, err)
            mu.Unlock()
        }
        return nil
    })
}
```

## Common Scenarios

- A validation function collects errors but only the first is reported to the user
- Concurrent workers produce errors but they are lost because of race conditions
- Multi-error output is a single string that cannot be parsed by log aggregators

## Prevent It

- Use multierr.Append to collect all errors rather than stopping at the first
- Check multierr.Len() to determine if there is a single or multiple errors
- Use sync.Mutex when collecting errors from concurrent goroutines
