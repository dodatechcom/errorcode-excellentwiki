---
title: "[Solution] Go workspace (go.work) error — Module Error Fix"
description: "Fix Go workspace configuration errors."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# go.work errors

The `go.work` file errors include invalid syntax, missing use directives, and version conflicts.

## How to Fix

### Fix 1: Valid go.work syntax

```
go 1.21

use (
    ./module1
    ./module2
)
```

### Fix 2: Regenerate go.work

```bash
rm go.work
go work init ./module1 ./module2
```

## Related Errors

- [go-mod-unexpected-eof]({{< relref "/languages/go/go-mod-unexpected-eof" >}}) — go.mod parse error.
- [unknown-directive]({{< relref "/languages/go/unknown-directive" >}}) — unknown directive.
