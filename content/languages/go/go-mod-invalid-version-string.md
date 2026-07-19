---
title: "[Solution] Go invalid go.mod version string — Module Error Fix"
description: "Fix Go invalid version string in go.mod."
languages: ["go"]
error-types: ["module-error"]
severities: ["error"]
weight: 5
---

# invalid go.mod version string

The error `invalid go.mod version string` occurs when a version is not valid semver.

## How to Fix

### Fix 1: Use correct semver format

```
require (
    github.com/pkg/errors v0.9.1
)
```

### Fix 2: Use go get

```bash
go get github.com/pkg/errors@v0.9.1
```

## Related Errors

- [invalid-go-version]({{< relref "/languages/go/invalid-go-version" >}}) — invalid go version.
- [go-mod-unexpected-eof]({{< relref "/languages/go/go-mod-unexpected-eof" >}}) — go.mod parse error.
