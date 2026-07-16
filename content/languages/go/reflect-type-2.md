---
title: "[Solution] Go Reflect Value.Type on Zero Value Fix"
description: "Fix Go reflect call of reflect.Value.Type on zero Value error. Ensure reflect.Value is valid before calling methods, and handle zero values."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["reflect", "type", "zero", "value", "runtime", "meta"]
weight: 5
---

# Reflect Value.Type on Zero Value Fix

The `reflect: call of reflect.Value.Type on zero Value` error occurs when calling `.Type()` on an invalid `reflect.Value`.

## Description

`reflect.Value` is a struct that wraps a value and its type information. An "invalid" or "zero" `reflect.Value` is returned by operations that don't have a value (like `reflect.ValueOf(nil)` or accessing a non-existent map element). Calling `.Type()` on an invalid `reflect.Value` panics because there is no type to report.

Common scenarios:

- **reflect.ValueOf(nil)** — wrapping a nil value.
- **Map key not found** — `MapIndex` returns zero Value.
- **Struct field not found** — `FieldByName` returns zero Value.
- **Uninitialized reflect.Value** — using `reflect.Value{}` directly.

## Common Causes

```go
// Cause 1: reflect.ValueOf(nil)
func describe(v interface{}) {
    rv := reflect.ValueOf(v)
    fmt.Println(rv.Type()) // panics if v is nil
}

// Cause 2: Map lookup returns zero value
func main() {
    m := map[string]int{"a": 1}
    v := reflect.ValueOf(m).MapIndex(reflect.ValueOf("missing"))
    fmt.Println(v.Type()) // panics — zero Value
}

// Cause 3: FieldByName returns zero
func main() {
    type S struct{ Name string }
    s := S{Name: "Alice"}
    v := reflect.ValueOf(s)
    f := v.FieldByName("NonExistent")
    fmt.Println(f.Type()) // panics
}

// Cause 4: Uninitialized reflect.Value
func main() {
    var v reflect.Value
    fmt.Println(v.Type()) // panics
}
```

## How to Fix

### Fix 1: Check if Value is valid before using

```go
func describe(v interface{}) {
    if v == nil {
        fmt.Println("nil value")
        return
    }
    rv := reflect.ValueOf(v)
    fmt.Println(rv.Type())
}
```

### Fix 2: Check MapIndex result

```go
func getMapValue(m interface{}, key string) (reflect.Value, bool) {
    rv := reflect.ValueOf(m)
    if rv.Kind() != reflect.Map {
        return reflect.Value{}, false
    }
    keyVal := reflect.ValueOf(key)
    v := rv.MapIndex(keyVal)
    if !v.IsValid() {
        return reflect.Value{}, false
    }
    return v, true
}
```

### Fix 3: Check FieldByName result

```go
func getField(obj interface{}, name string) (reflect.Value, error) {
    rv := reflect.ValueOf(obj)
    if rv.Kind() == reflect.Ptr {
        rv = rv.Elem()
    }
    f := rv.FieldByName(name)
    if !f.IsValid() {
        return reflect.Value{}, fmt.Errorf("field %s not found", name)
    }
    return f, nil
}
```

### Fix 4: Use reflect.Value.IsValid()

```go
func safeType(v reflect.Value) string {
    if !v.IsValid() {
        return "<invalid>"
    }
    return v.Type().String()
}
```

## Examples

```go
// This triggers: reflect: call of reflect.Value.Type on zero Value
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var v reflect.Value
    fmt.Println(v.Type())
}
```

## Related Errors

- [reflect-set]({{< relref "/languages/go/reflect-set" >}}) — setting value of wrong type.
- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — interface type assertion fails.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing nil pointer.
