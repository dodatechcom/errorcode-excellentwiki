---
title: "[Solution] Go no required module provides package — Module Error Fix"
description: "Fix Go no required module provides package error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# no required module provides package

The error `no required module provides package X` occurs when importing a package not in `go.mod`.

## How to Fix

### Fix 1: Add the dependency

```bash
go get github.com/pkg/errors
```

### Fix 2: Use go mod tidy

```bash
go mod tidy
```

## Related Errors

- [module-not-found]({{< relref "/languages/go/module-not-found" >}}) — module not found.
- [cannot-find-module]({{< relref "/languages/go/cannot-find-module" >}}) — cannot find module.
