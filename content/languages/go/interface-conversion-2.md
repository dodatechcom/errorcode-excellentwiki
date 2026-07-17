---
title: "[Solution] Go Interface Conversion Panic — Runtime Error Fix"
description: "Fix Go interface conversion panic when asserting a concrete type that doesn't match. Use comma-ok idiom or switch for safe type assertions."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Interface Conversion Panic — Runtime Error Fix

An interface conversion panic occurs when a type assertion or type switch attempts to convert an interface value to a concrete type that doesn't match.

## Description

Go interfaces hold a pair of values: the concrete type and the value itself. When you assert that an interface holds a specific type using a type assertion `x.(T)` or type switch, the runtime panics if the concrete type doesn't match `T`. The panic message reads `interface conversion: X is not Y`.

Common scenarios:

- **Missing comma-ok check** — bare type assertion without checking success.
- **Wrong type in type switch** — default case assumes an incorrect type.
- **HTTP request body** — asserting response body is a specific type when it's an error.
- **Generics-free code** — passing `interface{}` between packages without type safety.

## Common Causes

```go
// Cause 1: Bare type assertion without ok
func process(v interface{}) {
    s := v.(string) // panics if v is not string
    fmt.Println(s)
}

// Cause 2: Wrong type in type switch
func describe(v interface{}) {
    switch v.(type) {
    case int:
        fmt.Println("int:", v.(int))
    case string:
        fmt.Println("string:", v.(int)) // panic in string case
    }
}

// Cause 3: Asserting after error check
type Response struct {
    Data string
    Err  error
}

func handle(r *Response) {
    data := r.Data.(string) // panic if Data is nil
}

// Cause 4: Interface from external package
func handleJSON(data []byte) {
    var result interface{}
    json.Unmarshal(data, &result)
    m := result.(map[string]string) // may be map[string]interface{}
}
```

## How to Fix

### Fix 1: Always use the comma-ok idiom

```go
// Wrong
s := v.(string)

// Correct
s, ok := v.(string)
if !ok {
    fmt.Println("v is not a string")
    return
}
fmt.Println(s)
```

### Fix 2: Use type switch for multiple types

```go
// Wrong
func process(v interface{}) {
    s, ok := v.(string)
    if !ok {
        i, ok := v.(int)
        if !ok {
            fmt.Println("unknown type")
            return
        }
        fmt.Println(i)
        return
    }
    fmt.Println(s)
}

// Correct
func process(v interface{}) {
    switch val := v.(type) {
    case string:
        fmt.Println("string:", val)
    case int:
        fmt.Println("int:", val)
    default:
        fmt.Printf("unknown type: %T\n", val)
    }
}
```

### Fix 3: Validate struct fields before asserting

```go
func handle(r *Response) {
    if r.Data == nil {
        fmt.Println("no data")
        return
    }
    data, ok := r.Data.(string)
    if !ok {
        fmt.Println("data is not a string")
        return
    }
    fmt.Println(data)
}
```

### Fix 4: Use reflect for dynamic type checking

```go
import "reflect"

func safeAssert(v interface{}, target interface{}) bool {
    return reflect.TypeOf(v) == reflect.TypeOf(target)
}
```

## Examples

```go
// This triggers: interface conversion: interface {} is int, not string
package main

import "fmt"

func main() {
    var v interface{} = 42
    s := v.(string)
    fmt.Println(s)
}
```

## Related Errors

- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion on interface without comma-ok check.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer (related nil-value issue).
- [reflect-type]({{< relref "/languages/go/reflect-type" >}}) — calling reflect methods on zero values.
