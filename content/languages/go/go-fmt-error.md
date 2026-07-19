---
title: "[Solution] Go gofmt / goimports error — Code Quality Fix"
description: "Fix Go formatting errors."
languages: ["go"]
error-types: ["code-quality"]
severities: ["error"]
weight: 5
---

# gofmt formatting issues

The `gofmt` tool detects formatting inconsistencies in Go code.

## How to Fix

### Fix 1: Auto-format all files

```bash
gofmt -w .
```

### Fix 2: Use goimports

```bash
goimports -w .
```

## Related Errors

- [syntax-error-unexpected]({{< relref "/languages/go/syntax-error-unexpected" >}}) — syntax errors.
- [go-build-error]({{< relref "/languages/go/go-build-error" >}}) — build error.
