---
title: "[Solution] Go Reflect Set Type Mismatch Fix"
description: "Fix Go reflect.Set value of type X not assignable to type Y error. Use correct types in reflect operations and convert values properly."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["reflect", "set", "type", "assignable", "runtime", "conversion"]
weight: 5
---

# Reflect Set Type Mismatch Fix

The `reflect.Set: value of type X is not assignable to type Y` error occurs when attempting to set a reflect value with an incompatible type.

## Description

`reflect.Value.Set` requires that the new value's type matches the target's type exactly (or be assignable to it). Go's type system is strict — you cannot set an `int` field with a `string` value, or set an `int32` with an `int64`. The `Set` method panics with a descriptive error message.

Common scenarios:

- **Type mismatch from interface** — stored value has different type than expected.
- **Int size mismatch** — `int64` vs `int32` or `int`.
- **Pointer vs value** — setting a pointer type with a value type.
- **Unexported field** — attempting to set an unexported struct field.

## Common Causes

```go
// Cause 1: Wrong type in Set
func main() {
    var x int32 = 42
    v := reflect.ValueOf(&x).Elem()
    v.Set(reflect.ValueOf(int64(100))) // panic: int64 not assignable to int32
}

// Cause 2: Interface type mismatch
func setField(obj interface{}, field string, val interface{}) {
    v := reflect.ValueOf(obj).Elem()
    f := v.FieldByName(field)
    f.Set(reflect.ValueOf(val)) // panic if val type doesn't match
}

// Cause 3: Pointer vs value
func main() {
    var s string
    v := reflect.ValueOf(&s).Elem()
    v.Set(reflect.ValueOf(new(string))) // panic: *string not assignable to string
}

// Cause 4: Unexported field
type Config struct {
    secret string
}

func main() {
    c := Config{}
    v := reflect.ValueOf(&c).Elem()
    f := v.FieldByName("secret")
    f.SetString("value") // panic: unexported field
}
```

## How to Fix

### Fix 1: Ensure types match exactly

```go
func setInt(obj interface{}, field string, val int) error {
    v := reflect.ValueOf(obj).Elem()
    f := v.FieldByName(field)
    if f.Kind() != reflect.Int {
        return fmt.Errorf("field %s is not int", field)
    }
    f.SetInt(int64(val))
    return nil
}
```

### Fix 2: Convert value to match target type

```go
func setField(obj interface{}, field string, val interface{}) error {
    v := reflect.ValueOf(obj).Elem()
    f := v.FieldByName(field)
    if !f.IsValid() {
        return fmt.Errorf("field %s not found", field)
    }

    newVal := reflect.ValueOf(val)
    if !newVal.Type().ConvertibleTo(f.Type()) {
        return fmt.Errorf("cannot convert %s to %s", newVal.Type(), f.Type())
    }
    f.Set(newVal.Convert(f.Type()))
    return nil
}
```

### Fix 3: Handle pointer types correctly

```go
func setStringPtr(obj interface{}, field string, val string) {
    v := reflect.ValueOf(obj).Elem()
    f := v.FieldByName(field)
    if f.Kind() == reflect.Ptr {
        ptr := reflect.New(f.Type().Elem())
        ptr.Elem().SetString(val)
        f.Set(ptr)
    }
}
```

### Fix 4: Check CanSet before setting

```go
func safeSet(obj interface{}, field string, val interface{}) error {
    v := reflect.ValueOf(obj).Elem()
    f := v.FieldByName(field)
    if !f.CanSet() {
        return fmt.Errorf("cannot set field %s (unexported or unaddressable)", field)
    }
    f.Set(reflect.ValueOf(val))
    return nil
}
```

## Examples

```go
// This triggers: reflect.Set: value of type string is not assignable to type int
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var x int
    v := reflect.ValueOf(&x).Elem()
    v.Set(reflect.ValueOf("hello"))
    fmt.Println(x)
}
```

## Related Errors

- [reflect-type]({{< relref "/languages/go/reflect-type" >}}) — reflect call on zero Value.
- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — interface type mismatch.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion on wrong type.
