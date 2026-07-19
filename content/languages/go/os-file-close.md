---
title: "[Solution] Go os: file already closed — System Error Fix"
description: "Fix Go file already closed error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# os: file already closed

The error `file already closed` occurs when you call `Close()` on an already-closed file.

## How to Fix

### Fix 1: Only close once

```go
f, _ := os.Create("output.txt")
defer f.Close() // single close
```

## Related Errors

- [bad-file-descriptor]({{< relref "/languages/go/bad-file-descriptor" >}}) — bad file descriptor.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
