---
title: "[Solution] Go version constraints conflict — Module Error Fix"
description: "Fix Go version constraints conflict."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# version constraints conflict

The error `version constraints conflict` occurs when dependencies require incompatible versions.

## How to Fix

### Fix 1: Use replace to force a version

```go
replace github.com/example/module => github.com/example/module v1.2.3
```

### Fix 2: Upgrade all dependencies

```bash
go get -u ./...
go mod tidy
```

## Related Errors

- [module-not-found]({{< relref "/languages/go/module-not-found" >}}) — module not found.
- [missing-replace]({{< relref "/languages/go/missing-replace" >}}) — missing replace directive.
