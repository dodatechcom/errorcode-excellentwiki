---
title: "[Solution] Go cannot find module providing package — Module Error Fix"
description: "Fix Go cannot find module providing package error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# cannot find module providing package

The error `cannot find module providing package X` occurs when the package cannot be resolved.

## How to Fix

### Fix 1: Set up private module access

```bash
export GOPRIVATE=github.com/myorg/*
export GONOSUMCHECK=github.com/myorg/*
```

### Fix 2: Use replace directive

```go
replace github.com/example/module => ./vendor-local
```

## Related Errors

- [module-not-found]({{< relref "/languages/go/module-not-found" >}}) — module not found.
- [no-required-module]({{< relref "/languages/go/no-required-module" >}}) — no required module.
