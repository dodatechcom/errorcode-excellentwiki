---
title: "[Solution] Deprecated Function Migration: fmt.Sprintf for errors to fmt.Errorf with %w"
description: "Migrate from deprecated fmt.Sprintf for error wrapping to fmt.Errorf with %w."
deprecated_function: "fmt.Sprintf()"
replacement_function: "fmt.Errorf()"
languages: ["go"]
deprecated_since: "Go 1.13+"
---

# [Solution] Deprecated Function Migration: fmt.Sprintf for errors to fmt.Errorf with %w

The `fmt.Sprintf("error: %v", err)` has been deprecated in favor of `fmt.Errorf("error: %w", err)`.

## Migration Guide

%w wraps errors properly.

## Before (Deprecated)

```go
return fmt.Errorf("failed: %v", err)
```

## After (Modern)

```go
return fmt.Errorf("failed: %w", err)
```

## Key Differences

- %w wraps errors properly
