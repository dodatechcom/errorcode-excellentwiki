---
title: "[Solution] Go json: syntax error — Encoding Error Fix"
description: "Fix Go JSON syntax error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# json: syntax error

The error `json: syntax error` occurs when the JSON parser encounters malformed JSON.

## How to Fix

### Fix 1: Use json.Valid before parsing

```go
if !json.Valid(data) {
    log.Println("invalid JSON")
    return
}
```

## Examples

```go
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    data := []byte(`{"key": "value",}`)
    var m map[string]string
    err := json.Unmarshal(data, &m)
    fmt.Println(err)
}
```

Output:
```
invalid character '}' looking for beginning of object key string
```

## Related Errors

- [json-unmarshal-error]({{< relref "/languages/go/json-unmarshal-error" >}}) — type mismatch.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
