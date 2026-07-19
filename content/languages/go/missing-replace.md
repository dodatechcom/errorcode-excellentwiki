---
title: "[Solution] Go missing replace directive — Module Error Fix"
description: "Fix Go missing replace directive error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# missing replace directive

The error `missing replace directive` occurs when a module requires a replacement not specified.

## How to Fix

```bash
go mod edit -replace=github.com/example/module=../local-module
```

## Related Errors

- [version-constraints-conflict]({{< relref "/languages/go/version-constraints-conflict" >}}) — version conflict.
- [module-not-found]({{< relref "/languages/go/module-not-found" >}}) — module not found.
