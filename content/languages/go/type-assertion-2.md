---
title: "[Solution] Go Type Assertion Panic — Runtime Error Fix"
description: "Fix Go type assertion panic when asserting interface {} to a concrete type. Always use the comma-ok idiom for safe type assertions."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Type Assertion Panic — Runtime Error Fix

A type assertion panic occurs when you assert that an `interface{}` value holds a specific type, but it actually holds a different type.

## Description

The `interface{}` (empty interface) type can hold any value. When you use a type assertion `x.(T)` on an empty interface, the runtime checks if the concrete type matches `T`. If not, it panics with `interface conversion: interface {} is X, not Y`. This is especially common when deserializing JSON or working with generic APIs that return `interface{}`.

Common scenarios:

- **JSON deserialization** — `json.Unmarshal` returns `interface{}` that needs casting.
- **Function returning empty interface** — caller assumes a specific type.
- **Channel of interface values** — receiving and asserting without checking.
- **Map with interface{} values** — stored different types under the same key.

## Common Causes

```go
// Cause 1: Unmarshaling JSON into interface{}
func main() {
    data := []byte(`{"count": 5}`)
    var result interface{}
    json.Unmarshal(data, &result)

    m := result.(map[string]int)       // panic: is map[string]interface{}
    fmt.Println(m["count"])
}

// Cause 2: Returning interface{} from function
func getValue() interface{} {
    return 42
}

func main() {
    s := getValue().(string) // panic: is int, not string
}

// Cause 3: Map with mixed types
func main() {
    m := map[string]interface{}{
        "name": "Alice",
        "age":  30,
    }
    name := m["age"].(string) // panic: is int, not string
}

// Cause 4: Channel receive and assert
func main() {
    ch := make(chan interface{}, 1)
    ch <- 42
    v := <-ch
    s := v.(string) // panic
}
```

## How to Fix

### Fix 1: Always use comma-ok for type assertions

```go
// Wrong
s := getValue().(string)

// Correct
v := getValue()
s, ok := v.(string)
if !ok {
    fmt.Printf("expected string, got %T\n", v)
    return
}
```

### Fix 2: Use type switch on empty interfaces

```go
// Wrong
func handle(v interface{}) {
    str := v.(string)
    fmt.Println(str)
}

// Correct
func handle(v interface{}) {
    switch val := v.(type) {
    case string:
        fmt.Println("string:", val)
    case float64:
        fmt.Println("number:", val)
    case bool:
        fmt.Println("bool:", val)
    default:
        fmt.Printf("unsupported type: %T\n", val)
    }
}
```

### Fix 3: Unmarshal into typed struct instead of interface{}

```go
// Wrong
var result interface{}
json.Unmarshal(data, &result)
m := result.(map[string]interface{})

// Correct
type Response struct {
    Count int `json:"count"`
}
var resp Response
json.Unmarshal(data, &resp)
```

### Fix 4: Use reflection as last resort

```go
import "reflect"

func toString(v interface{}) (string, bool) {
    val := reflect.ValueOf(v)
    if val.Kind() == reflect.String {
        return val.String(), true
    }
    return "", false
}
```

## Examples

```go
// This triggers: interface conversion: interface {} is float64, not string
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    data := []byte(`{"value": 123}`)
    var m map[string]interface{}
    json.Unmarshal(data, &m)
    s := m["value"].(string) // JSON numbers decode as float64
    fmt.Println(s)
}
```

## Related Errors

- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — interface conversion between concrete types.
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — invalid JSON input causes parsing errors.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing nil pointers (related nil-value issue).
