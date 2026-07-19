---
title: "[Solution] Go module not found / package not in GOROOT — Module Error Fix"
description: "Fix Go module not found error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# module not found / package not in GOROOT

The error `module not found` or `package X is not in GOROOT` occurs when Go cannot locate a module.

## How to Fix

### Fix 1: Download the module

```bash
go get github.com/example/module@latest
```

### Fix 2: Use local replace directive

```go
replace github.com/example/module => ../local-module
```

## Related Errors

- [cannot-find-module]({{< relref "/languages/go/cannot-find-module" >}}) — cannot find module.
- [no-required-module]({{< relref "/languages/go/no-required-module" >}}) — no required module.
