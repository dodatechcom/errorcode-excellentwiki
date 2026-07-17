---
title: "[Solution] Go Interface Conversion Panic — Runtime Error Fix"
description: "Fix Go interface conversion panic. Use type assertions with ok pattern, check interface types before converting, and handle type switches safely."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Interface Conversion — Runtime Error Fix

An interface conversion panic occurs when you use a type assertion or type switch on an interface value that does not hold the expected concrete type.

## Description

Go interfaces hold a value and its type. When you assert that an interface holds a specific type using `x.(T)`, if the actual type doesn't match `T`, the runtime panics. Using the comma-ok pattern `x, ok := v.(T)` avoids the panic.

Common scenarios:

- **Unsafe type assertion** — `v.(MyStruct)` without checking ok.
- **Wrong type in type switch** — case doesn't match the underlying type.
- **nil interface** — asserting a type on a nil interface value.

## Common Causes

```go
// Cause 1: Unsafe type assertion
var i interface{} = "hello"
n := i.(int) // panic: interface conversion: interface {} is string, not int

// Cause 2: Nil interface assertion
var i interface{}
s := i.(string) // panic: interface conversion: interface {} is nil, not string

// Cause 3: Wrong type in type switch
var i interface{} = 42
switch v := i.(type) {
case string:
    fmt.Println(len(v)) // never reached, but if you had used assertion...
}

// Cause 4: Asserting wrong type after function return
func getData() interface{} {
    return nil
}

data := getData()
result := data.(string) // panic
```

## How to Fix

### Fix 1: Use the comma-ok pattern for type assertions

```go
// Wrong — panics if type doesn't match
var i interface{} = "hello"
n := i.(int)

// Correct — comma-ok pattern
n, ok := i.(int)
if !ok {
    fmt.Println("i is not an int")
    return
}
fmt.Println(n)
```

### Fix 2: Use type switches for multiple possible types

```go
// Wrong — multiple unsafe assertions
var i interface{} = "hello"
s := i.(string)    // works
n := i.(int)       // panic

// Correct — type switch
switch v := i.(type) {
case string:
    fmt.Println("string:", v)
case int:
    fmt.Println("int:", v)
case nil:
    fmt.Println("nil")
default:
    fmt.Printf("unknown type: %T\n", v)
}
```

### Fix 3: Check for nil interface before asserting

```go
// Wrong
func process(v interface{}) string {
    return v.(string) // panic if v is nil
}

// Correct
func process(v interface{}) string {
    if v == nil {
        return ""
    }
    s, ok := v.(string)
    if !ok {
        return ""
    }
    return s
}
```

### Fix 4: Use reflection for dynamic type checking

```go
import "reflect"

// Wrong
func getFieldName(v interface{}) string {
    return v.(struct{ Name string }).Name
}

// Correct
func getFieldName(v interface{}) (string, bool) {
    val := reflect.ValueOf(v)
    if val.Kind() == reflect.Ptr {
        val = val.Elem()
    }
    field := val.FieldByName("Name")
    if !field.IsValid() {
        return "", false
    }
    return field.String(), true
}
```

### Fix 5: Store typed values when possible

```go
// Wrong — everything goes into interface{}, requires assertion later
var cache = make(map[string]interface{})

// Correct — use typed values
var cache = make(map[string]string)

// Or use generics (Go 1.18+)
type TypedCache[T any] struct {
    mu sync.RWMutex
    m  map[string]T
}
```

## Examples

```go
// This triggers: panic: interface conversion: interface {} is int, not string
package main

import "fmt"

func main() {
    var i interface{} = 42
    s := i.(string)
    fmt.Println(s)
}
```

## Related Errors

- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — similar interface type assertion issues.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer.
- [reflect-type]({{< relref "/languages/go/reflect-type" >}}) — calling methods on zero reflect values.
