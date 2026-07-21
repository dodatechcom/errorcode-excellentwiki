---
title: "[Solution] Deprecated Function Migration: strings.Title to cases.Title"
description: "Migrate from deprecated strings.Title to cases.Title."
deprecated_function: "strings.Title(s)"
replacement_function: "cases.Title(language.Und).String(s)"
languages: ["go"]
deprecated_since: "Go 1.18+"
---

# [Solution] Deprecated Function Migration: strings.Title to cases.Title

The `strings.Title(s)` has been deprecated in favor of `cases.Title(language.Und).String(s)`.

## Migration Guide

strings.Title has Unicode bugs

strings.Title incorrectly handles Unicode.

## Before (Deprecated)

```go
result := strings.Title("hello world")
```

## After (Modern)

```go
import "golang.org/x/text/cases"
import "golang.org/x/text/language"
c := cases.Title(language.Und)
result := c.String("hello world")
```

## Key Differences

- strings.Title has Unicode bugs
- cases.Title handles Unicode correctly
