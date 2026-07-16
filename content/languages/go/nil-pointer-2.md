---
title: "[Solution] Go Nil Pointer Dereference — Runtime Error Fix (Advanced)"
description: "Advanced fixes for Go nil pointer dereference panic. Handle nil in chained method calls, map results, function closures, and embedded structs."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nil", "pointer", "dereference", "panic", "runtime"]
weight: 5
---

# Nil Pointer Dereference — Runtime Error Fix (Advanced)

A nil pointer dereference occurs when your program tries to read or write memory through a pointer that does not point to any valid memory location. The runtime catches this and panics.

## Description

Go pointers default to `nil`. Any attempt to dereference a nil pointer — reading a field, calling a method, or indexing through it — triggers a panic. This often surfaces in code that chains calls or relies on values returned from functions that may fail.

Common scenarios:

- **Chained method calls** — calling methods on a value that might be nil from a prior call.
- **Map value used without checking existence** — the zero-value pointer from a missing key.
- **Deferred closures capturing nil** — closures running after the enclosing scope has changed.
- **Embedded struct pointers** — an inner pointer field left nil.

## Common Causes

```go
// Cause 1: Chained method calls where an intermediate returns nil
type Builder struct {
    value string
}

func NewBuilder() *Builder {
    return nil
}

func (b *Builder) SetValue(v string) *Builder {
    b.value = v
    return b
}

func main() {
    NewBuilder().SetValue("x") // panic: nil pointer dereference
}

// Cause 2: Using map pointer value without checking key existence
func main() {
    m := map[string]*User{}
    u := m["missing"]
    fmt.Println(u.Name) // panic
}

// Cause 3: Deferred closure dereferences captured nil
func process() *Result {
    var r *Result
    defer func() {
        fmt.Println(r.Data) // panic if r is nil
    }()
    // r is never assigned
    return r
}

// Cause 4: Embedded struct pointer not initialized
type Inner struct {
    X int
}

type Outer struct {
    *Inner
}

func main() {
    var o Outer
    fmt.Println(o.X) // panic — Inner is nil
}
```

## How to Fix

### Fix 1: Guard chained calls with nil checks

```go
// Wrong
func main() {
    NewBuilder().SetValue("x") // panic if NewBuilder returns nil
}

// Correct
func main() {
    b := NewBuilder()
    if b == nil {
        fmt.Println("builder unavailable")
        return
    }
    b.SetValue("x")
}
```

### Fix 2: Use the two-value map idiom

```go
// Wrong
u := m["missing"]
fmt.Println(u.Name)

// Correct
u, ok := m["missing"]
if !ok || u == nil {
    fmt.Println("user not found")
    return
}
fmt.Println(u.Name)
```

### Fix 3: Initialize embedded struct pointers

```go
// Wrong
type Outer struct {
    *Inner
}

// Correct
func newOuter() *Outer {
    return &Outer{Inner: &Inner{}}
}
```

### Fix 4: Check receiver before deferred work

```go
// Wrong
func process() *Result {
    var r *Result
    defer func() {
        r.Finalize() // panic
    }()
    return r
}

// Correct
func process() *Result {
    var r *Result
    defer func() {
        if r != nil {
            r.Finalize()
        }
    }()
    return r
}
```

## Examples

```go
// This triggers: runtime error: invalid memory address or nil pointer dereference
package main

import "fmt"

type Node struct {
    Next *Node
    Val  int
}

func main() {
    head := &Node{Val: 1}
    // head.Next is nil
    fmt.Println(head.Next.Val) // panic
}
```

## Related Errors

- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — interface type assertion fails at runtime.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion on interface value panics without ok-check.
- [invalid-memory-address]({{< relref "/languages/go/invalid-memory-address" >}}) — accessing memory outside valid address space.
