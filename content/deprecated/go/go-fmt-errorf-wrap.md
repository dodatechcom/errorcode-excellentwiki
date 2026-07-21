---
title: "[Solution] Deprecated Function Migration: fmt.Errorf with %v to %w"
description: "Migrate from deprecated fmt.Errorf with %v to error wrapping with %w."
deprecated_function: "fmt.Errorf()"
replacement_function: "fmt.Errorf()"
languages: ["go"]
deprecated_since: "Go 1.13+"
---

# [Solution] Deprecated Function Migration: fmt.Errorf with %v to %w

The `fmt.Errorf("error: %v", err)` has been deprecated in favor of `fmt.Errorf("error: %w", err)`.

## Migration Guide

%w wraps errors for errors.Is/As

Using %v discards the error chain.

## Before (Deprecated)

```go
if err != nil {
    return fmt.Errorf("failed: %v", err)
}
```

## After (Modern)

```go
if err != nil {
    return fmt.Errorf("failed: %w", err)
}
```

## Key Differences

- %w wraps the error for unwrapping
- errors.Is/As can traverse the chain
