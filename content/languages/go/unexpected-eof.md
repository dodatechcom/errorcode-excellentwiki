---
title: "[Solution] Go unexpected EOF — Input/Output Error Fix"
description: "Fix Go unexpected EOF error. Handle premature stream closure."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# unexpected EOF

The error `unexpected EOF` occurs when a reader encounters the end of input before the expected amount of data has been received.

## Common Causes

- **Truncated file** — file was partially written or corrupted
- **Connection dropped** — network interrupted mid-transfer

## How to Fix

### Fix 1: Use io.ReadFull

```go
_, err := io.ReadFull(reader, buf)
if err == io.ErrUnexpectedEOF {
    log.Println("incomplete read")
}
```

## Examples

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    reader := strings.NewReader("hello")
    buf := make([]byte, 10)
    _, err := io.ReadFull(reader, buf)
    fmt.Println(err)
}
```

Output:
```
unexpected EOF
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — normal end-of-file.
- [connection-reset]({{< relref "/languages/go/connection-reset" >}}) — connection reset.
