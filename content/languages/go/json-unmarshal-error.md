---
title: "[Solution] Go json.Unmarshal error — Encoding Error Fix"
description: "Fix Go JSON unmarshal errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# json.Unmarshal error

The error `json: cannot unmarshal` occurs when JSON data doesn't match the target Go type.

## How to Fix

### Fix 1: Use json.Number

```go
dec := json.NewDecoder(reader)
dec.UseNumber()
var result map[string]interface{}
dec.Decode(&result)
```

## Examples

```go
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    data := []byte(`{"name": "Alice", "age": "thirty"}`)
    var user struct {
        Name string `json:"name"`
        Age  int    `json:"age"`
    }
    err := json.Unmarshal(data, &user)
    fmt.Println(err)
}
```

Output:
```
json: cannot unmarshal string into Go struct field User.age of type int
```

## Related Errors

- [json-syntax-error]({{< relref "/languages/go/json-syntax-error" >}}) — JSON syntax error.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion failed.
