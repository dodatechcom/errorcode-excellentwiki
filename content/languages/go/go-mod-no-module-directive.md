---
title: "[Solution] Go go.mod contains no module directive — Module Error Fix"
description: "Fix Go go.mod no module directive error."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# go.mod contains no module directive

The error `go.mod contains no module directive` occurs when `go.mod` is missing the `module` line.

## How to Fix

```bash
go mod init example.com/mymodule
```

## Related Errors

- [go-mod-unexpected-eof]({{< relref "/languages/go/go-mod-unexpected-eof" >}}) — go.mod parse error.
- [invalid-go-version]({{< relref "/languages/go/invalid-go-version" >}}) — invalid go version.
