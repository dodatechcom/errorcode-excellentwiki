---
title: "[Solution] Deprecated Function Migration: time.Now() with manual formatting to time.Format"
description: "Migrate from deprecated manual time formatting to time.Format."
deprecated_function: "time.Now()"
replacement_function: "time.Now().Format(time.RFC3339)"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: time.Now() with manual formatting to time.Format

The `time.Now().Format("2006-01-02")` has been deprecated in favor of `time.Now().Format(time.RFC3339)`.

## Migration Guide

time.Format uses reference time.

## Before (Deprecated)

```go
t := time.Now()
s := t.Format("2006-01-02 15:04:05")
```

## After (Modern)

```go
t := time.Now()
s := t.Format(time.RFC3339)
```

## Key Differences

- time.Format uses reference time
