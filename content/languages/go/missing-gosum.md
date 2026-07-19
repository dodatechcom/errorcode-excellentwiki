---
title: "[Solution] Go missing go.sum entry — Module Error Fix"
description: "Fix Go missing go.sum entry error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# missing go.sum entry

The error `missing go.sum entry for module` occurs when `go.sum` is out of sync with `go.mod`.

## How to Fix

### Fix 1: Regenerate go.sum

```bash
go mod tidy
```

### Fix 2: Delete and regenerate

```bash
rm go.sum
go mod tidy
```

## Related Errors

- [go-mod-unexpected-eof]({{< relref "/languages/go/go-mod-unexpected-eof" >}}) — go.mod parse error.
- [module-not-found]({{< relref "/languages/go/module-not-found" >}}) — module not found.
