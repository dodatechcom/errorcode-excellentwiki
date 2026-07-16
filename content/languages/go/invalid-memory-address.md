---
title: "[Solution] Go Invalid Memory Address — Runtime Error Fix"
description: "Fix Go invalid memory address panic. Check pointers before use, avoid nil dereferences, and handle unsafe memory operations safely."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["memory", "address", "invalid", "pointer", "unsafe", "panic"]
weight: 5
---

# Invalid Memory Address — Runtime Error Fix

An invalid memory address panic occurs when your program attempts to access a memory address that is not valid, such as a nil pointer or an address outside the process's address space.

## Description

Go's runtime detects invalid memory accesses and panics with `runtime error: invalid memory address or nil pointer dereference`. This covers nil pointer dereferences, accessing freed memory, and invalid pointer arithmetic.

Common scenarios:

- **Nil pointer dereference** — the most common cause.
- **Using a pointer after the underlying value is freed** — dangling pointer.
- **Invalid unsafe.Pointer arithmetic** — creating invalid pointers with `unsafe`.
- **Slice header corruption** — invalid pointer in slice data field.

## Common Causes

```go
// Cause 1: Nil pointer dereference
type Config struct {
    Host string
}

func main() {
    var cfg *Config
    fmt.Println(cfg.Host) // panic: invalid memory address
}

// Cause 2: Pointer to local variable escaping incorrectly
func getPointer() *int {
    x := 42
    return &x // x escapes to heap, fine in Go
}

// Cause 3: Invalid unsafe.Pointer usage
import "unsafe"

func main() {
    p := unsafe.Pointer(uintptr(0))
    *(*int)(p) // panic: invalid memory address
}

// Cause 4: Concurrent access to pointer variable
var p *int
go func() {
    p = new(int)
    *p = 42
}()
fmt.Println(*p) // May race and panic
```

## How to Fix

### Fix 1: Always check pointers before dereferencing

```go
// Wrong
func getHost(cfg *Config) string {
    return cfg.Host
}

// Correct
func getHost(cfg *Config) string {
    if cfg == nil {
        return ""
    }
    return cfg.Host
}
```

### Fix 2: Return errors instead of nil pointers

```go
// Wrong
func findUser(id int) *User {
    // Returns nil if not found
    return nil
}

// Correct
func findUser(id int) (*User, error) {
    user, ok := users[id]
    if !ok {
        return nil, fmt.Errorf("user %d not found", id)
    }
    return user, nil
}
```

### Fix 3: Avoid unsafe.Pointer unless absolutely necessary

```go
// Wrong
import "unsafe"

func main() {
    p := unsafe.Pointer(uintptr(100))
    // Invalid address
}

// Correct — use normal Go types
func main() {
    x := 100
    p := &x
    fmt.Println(*p)
}
```

### Fix 4: Use atomic operations for concurrent pointer access

```go
// Wrong — race condition on pointer
var p *int

func writer() {
    p = new(int)
    *p = 42
}

func reader() int {
    return *p // May race
}

// Correct — use atomic.Pointer (Go 1.19+)
var p atomic.Pointer[int]

func writer() {
    v := new(int)
    *v = 42
    p.Store(v)
}

func reader() int {
    v := p.Load()
    if v == nil {
        return 0
    }
    return *v
}
```

### Fix 5: Initialize structs properly

```go
// Wrong — map values are nil pointers
type Node struct {
    Left, Right *Node
}

tree := make(map[int]*Node)
tree[1] = &Node{} // Left and Right are nil
fmt.Println(tree[1].Left.Left) // panic

// Correct — check before accessing
func (n *Node) GetLeft() *Node {
    if n == nil {
        return nil
    }
    return n.Left
}
```

## Examples

```go
// This triggers: runtime error: invalid memory address or nil pointer dereference
package main

import "fmt"

type Foo struct {
    Bar string
}

func main() {
    var f *Foo
    fmt.Println(f.Bar)
}
```

## Related Errors

- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — the most common form of invalid memory address.
- [unsafe-pointer]({{< relref "/languages/go/unsafe-pointer" >}}) — invalid unsafe.Pointer arithmetic.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — system cannot allocate memory.
