---
title: "[Solution] Go Type Assertion Panic — Runtime Error Fix"
description: "Fix Go type assertion panic: interface {} is X, not Y. Use comma-ok pattern, type switches, and validate interfaces before asserting."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["type-assertion", "interface", "comma-ok", "panic", "type-switch"]
weight: 5
---

# Type Assertion Panic — Runtime Error Fix

A type assertion panic occurs when asserting that an interface holds a concrete type it does not actually contain.

## Description

Go interfaces store a pair (type, value). A type assertion `v.(T)` extracts the value assuming the type is `T`. If the type doesn't match, the runtime panics with `interface conversion: interface {} is X, not Y`. The safe form uses `v, ok := x.(T)` and returns `false` instead of panicking.

Common scenarios:

- **Direct assertion without ok** — `x.(string)` on an `int` value.
- **Asserting on nil interface** — asserting any concrete type on a nil interface panics.
- **Mixed up assertion order** — asserting the wrong concrete type from a union interface.

## Common Causes

```go
// Cause 1: Direct assertion without ok check
var x interface{} = 42
s := x.(string) // panic: interface {} is int, not string

// Cause 2: Asserting on nil
var x interface{}
n := x.(int) // panic: interface {} is nil, not int

// Cause 3: Wrong type after interface function return
func parse(s string) interface{} {
    return 42 // returns int
}

v := parse("hello")
result := v.(string) // panic
```

## How to Fix

### Fix 1: Always use the comma-ok form

```go
// Wrong
var x interface{} = 42
n := x.(int)

// Correct
n, ok := x.(int)
if !ok {
    fmt.Println("x is not an int")
    return
}
fmt.Println(n)
```

### Fix 2: Use type switches

```go
// Wrong — multiple assertions
var x interface{} = "hello"
s := x.(string) // works
n := x.(int)    // panic

// Correct
switch v := x.(type) {
case string:
    fmt.Println("string:", v)
case int:
    fmt.Println("int:", v)
default:
    fmt.Printf("unexpected type %T\n", v)
}
```

### Fix 3: Check for nil before asserting

```go
// Wrong
func getString(v interface{}) string {
    return v.(string) // panics if v is nil
}

// Correct
func getString(v interface{}) string {
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

### Fix 4: Define interfaces instead of using empty interface

```go
// Wrong — everything is interface{}, requires assertions everywhere
func process(v interface{}) {
    s := v.(string)
    fmt.Println(s)
}

// Correct — use a specific interface
type Stringer interface {
    String() string
}

func process(v Stringer) {
    fmt.Println(v.String())
}
```

### Fix 5: Use generics for type-safe containers (Go 1.18+)

```go
// Wrong — requires type assertion
var cache interface{} = "hello"
s := cache.(string)

// Correct — generic function
func first[T any](s []T) T {
    return s[0]
}

// Or generic type
type Stack[T any] struct {
    items []T
}

func (s *Stack[T]) Push(item T) {
    s.items = append(s.items, item)
}
```

## Examples

```go
// This triggers: panic: interface conversion: interface {} is string, not int
package main

import "fmt"

func main() {
    var x interface{} = "hello"
    n := x.(int)
    fmt.Println(n)
}
```

## Related Errors

- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — similar interface conversion panic.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer.
- [reflect-type]({{< relref "/languages/go/reflect-type" >}}) — reflect methods on zero Value.
