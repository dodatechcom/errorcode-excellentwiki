---
title: "[Solution] Go invalid go version in go.mod / cannot use go version — Module Error Fix"
description: "Fix Go invalid go version in go.mod error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# invalid go version in go.mod

The error `invalid go version in go.mod` occurs when the `go` directive specifies an incompatible version.

## How to Fix

### Fix 1: Use correct format

```
module example.com/mymodule

go 1.21
```

### Fix 2: Downgrade go directive

```bash
go mod edit -go=1.20
```

## Related Errors

- [go-mod-unexpected-eof]({{< relref "/languages/go/go-mod-unexpected-eof" >}}) — go.mod parse error.
- [go-mod-no-module-directive]({{< relref "/languages/go/go-mod-no-module-directive" >}}) — no module directive.
