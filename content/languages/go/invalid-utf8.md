---
title: "[Solution] Go invalid UTF-8 encoding — String Error Fix"
description: "Fix Go invalid UTF-8 encoding error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# invalid UTF-8 encoding

The error `invalid UTF-8 encoding` occurs when Go encounters bytes that are not valid UTF-8.

## How to Fix

### Fix 1: Validate UTF-8 before processing

```go
if !utf8.Valid(data) {
    log.Println("invalid UTF-8, using replacement")
    data = []byte(string(data))
}
```

## Examples

```go
package main

import (
    "fmt"
    "unicode/utf8"
)

func main() {
    s := string([]byte{0xff, 0xfe})
    fmt.Println(utf8.ValidString(s))
    for range s {
    }
}
```

Output:
```
panic: invalid UTF-8 string
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
- [unexpected-eof]({{< relref "/languages/go/unexpected-eof" >}}) — unexpected EOF.
