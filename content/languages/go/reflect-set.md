---
title: "[Solution] Go Reflect Set Type Mismatch Error Fix"
description: "Fix Go reflect.Set: value of type X is not assignable to type Y error. Ensure reflect values match target types when using reflection."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["reflect", "set", "type", "mismatch", "assignable"]
weight: 5
---

# Reflect.Set: Value Type Not Assignable — Fix

A "reflect.Set: value of type X is not assignable to type Y" error occurs when you try to set a reflect value to a value of a different type.

## Description

Go's `reflect.Value.Set()` requires the new value to be assignable to the target type. If the types don't match — even if they're similar (like `int` vs `int64`) — the call panics.

Common scenarios:

- **Setting int to int64 field** — `reflect.ValueOf(42).Set(reflect.ValueOf(int64(42)))` on an `int` field.
- **Setting string to []byte field** — type mismatch.
- **Setting unexported field** — can't set unexported struct fields via reflection.
- **Setting non-pointer to pointer** — or vice versa.

## Common Causes

```go
// Cause 1: Type mismatch between int and int64
type Config struct {
    Port int
}

v := reflect.ValueOf(&Config{}).Elem()
field := v.FieldByName("Port")
field.Set(reflect.ValueOf(int64(8080))) // panic: int64 is not assignable to int

// Cause 2: Setting string to int field
field.Set(reflect.ValueOf("8080")) // panic: string is not assignable to int

// Cause 3: Setting to unexported field
type secret struct {
    password string // unexported
}

v := reflect.ValueOf(&secret{}).Elem()
field := v.FieldByName("password")
field.SetString("newpassword") // panic: reflect.Value.Set using value obtained using unexported field

// Cause 4: Setting nil to non-pointer type
v := reflect.ValueOf(&Config{}).Elem()
field := v.FieldByName("Port")
field.Set(reflect.ValueOf(nil)) // panic
```

## How to Fix

### Fix 1: Ensure types match before setting

```go
// Wrong
field.Set(reflect.ValueOf(int64(8080)))

// Correct
portValue := reflect.ValueOf(8080).Convert(field.Type())
field.Set(portValue)
```

### Fix 2: Use CanSet() to check before setting

```go
// Wrong
field := v.FieldByName("Name")
field.SetString("Alice")

// Correct
field := v.FieldByName("Name")
if !field.CanSet() {
    fmt.Println("cannot set field")
    return
}
field.SetString("Alice")
```

### Fix 3: Convert values to the correct type

```go
// Wrong — types don't match
func setField(v reflect.Value, name string, value interface{}) {
    field := v.FieldByName(name)
    field.Set(reflect.ValueOf(value))
}

// Correct — convert to target type
func setField(v reflect.Value, name string, value interface{}) error {
    field := v.FieldByName(name)
    if !field.IsValid() {
        return fmt.Errorf("field %s not found", name)
    }
    if !field.CanSet() {
        return fmt.Errorf("field %s is not settable", name)
    }

    val := reflect.ValueOf(value)
    if !val.Type().AssignableTo(field.Type()) {
        if val.Type().ConvertibleTo(field.Type()) {
            val = val.Convert(field.Type())
        } else {
            return fmt.Errorf("cannot assign %s to %s", val.Type(), field.Type())
        }
    }

    field.Set(val)
    return nil
}
```

### Fix 4: Handle pointer types correctly

```go
// Wrong — setting non-pointer to pointer field
type Config struct {
    Host *string
}

v := reflect.ValueOf(&Config{}).Elem()
field := v.FieldByName("Host")
field.Set(reflect.ValueOf("localhost")) // panic: string is not *string

// Correct — create pointer
host := "localhost"
field.Set(reflect.ValueOf(&host))
```

### Fix 5: Export struct fields for reflection access

```go
// Wrong — unexported field can't be set
type config struct {
    host string
}

v := reflect.ValueOf(&config{}).Elem()
field := v.FieldByName("host")
field.SetString("localhost") // panic

// Correct — export the field
type Config struct {
    Host string
}

v := reflect.ValueOf(&Config{}).Elem()
field := v.FieldByName("Host")
field.SetString("localhost") // Works
```

## Examples

```go
// This triggers: panic: reflect.Set: value of type string is not assignable to type int
package main

import (
    "fmt"
    "reflect"
)

type Config struct {
    Port int
}

func main() {
    cfg := &Config{}
    v := reflect.ValueOf(cfg).Elem()
    field := v.FieldByName("Port")
    field.Set(reflect.ValueOf("8080"))
    fmt.Println(cfg.Port)
}
```

## Related Errors

- [reflect-type]({{< relref "/languages/go/reflect-type" >}}) — reflect.Value.Type on zero Value.
- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — interface type assertion fails.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion panic.
