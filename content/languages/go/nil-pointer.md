---
title: "[Solution] Go Nil Pointer Dereference — Runtime Error Fix"
description: "Fix Go nil pointer dereference panic. Learn to check for nil before use, initialize structs, and handle error returns safely."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nil", "pointer", "dereference", "panic", "runtime", "invalid-memory-address"]
weight: 5
---

# Nil Pointer Dereference — Runtime Error

The error `runtime error: invalid memory address or nil pointer dereference` occurs when your program attempts to read or write memory through a pointer that is `nil`. This is the most common runtime panic in Go.

## Description

In Go, pointers default to `nil` when declared but not initialized. Dereferencing a `nil` pointer — accessing a field, calling a method, or reading the pointed-to value — causes an immediate runtime panic. Unlike compiled errors, this cannot be caught at compile time.

Common scenarios include uninitialized struct pointers, failed function returns that produce `nil`, and unchecked map lookups returning zero-value pointers.

## Common Causes

- **Uninitialized struct pointer** — declaring `var p *MyStruct` without calling `new()` or using `&MyStruct{}`
- **Unchecked error returns** — ignoring an error from a function that returns `nil` on failure
- **Failed map lookup** — accessing a pointer value from a map key that does not exist
- **Interface nil trap** — an interface holding a nil concrete value is not itself nil

## How to Fix

### Fix 1: Always check for nil before dereferencing

```go
func getUserName(u *User) string {
    if u == nil {
        return "unknown"
    }
    return u.Name
}
```

### Fix 2: Initialize pointers before use

```go
// Wrong
var u *User
u.Name = "Alice" // panic

// Correct
u := &User{Name: "Alice"}
fmt.Println(u.Name)
```

### Fix 3: Handle errors from functions that return pointers

```go
u := findUser(999)
if u == nil {
    fmt.Println("user not found")
    return
}
fmt.Println(u.Name)
```

### Fix 4: Use the `if x != nil` idiom

```go
cfg := getConfig()
if cfg != nil {
    fmt.Println(cfg.Host)
} else {
    fmt.Println("no config available")
}
```

## Examples

```go
package main

import "fmt"

type Foo struct {
    Bar string
}

func main() {
    var f *Foo
    // f is nil — accessing f.Bar panics
    fmt.Println(f.Bar)
}
```

Output:
```
panic: runtime error: invalid memory address or nil pointer dereference
```

## Related Errors

- [index-out-of-range]({{< relref "/languages/go/index-out-of-range" >}}) — accessing a slice or array beyond its bounds.
- [map-not-init]({{< relref "/languages/go/map-not-init" >}}) — writing to a nil map causes a panic.
- [division-by-zero]({{< relref "/languages/go/division-by-zero" >}}) — another common runtime panic.
