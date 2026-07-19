---
title: "[Solution] Go unknown directive in go.mod — Module Error Fix"
description: "Fix Go unknown directive in go.mod error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# unknown directive in go.mod

The error `unknown directive in go.mod` occurs when the parser encounters a non-valid directive.

## How to Fix

```bash
rm go.mod
go mod init example.com/mymodule
go mod tidy
```

## Related Errors

- [go-mod-unexpected-eof]({{< relref "/languages/go/go-mod-unexpected-eof" >}}) — go.mod parse error.
- [go-mod-no-module-directive]({{< relref "/languages/go/go-mod-no-module-directive" >}}) — no module directive.
