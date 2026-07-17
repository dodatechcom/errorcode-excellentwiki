---
title: "[Solution] Go Unsafe Pointer Arithmetic Fix"
description: "Fix Go unsafe.Pointer misuse. Avoid invalid pointer arithmetic, use safe alternatives, and understand unsafe.Pointer rules."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Unsafe Pointer Arithmetic Fix

Misuse of `unsafe.Pointer` can lead to invalid memory access, segmentation faults, or undefined behavior. Go has strict rules for `unsafe.Pointer` that must be followed.

## Description

`unsafe.Pointer` bypasses Go's type safety, allowing direct memory manipulation. While powerful for CGo, low-level systems code, and performance optimization, incorrect usage leads to crashes or memory corruption. The Go specification defines five valid conversion patterns; violating them causes undefined behavior.

Common scenarios:

- **Invalid type conversion** — converting between unrelated pointer types.
- **Arithmetic beyond allocation** — pointer math that goes outside allocated memory.
- **Using unsafe.Pointer after GC** — garbage collector may move objects.
- **Converting between slices** — incorrect struct layout assumptions.

## Common Causes

```go
// Cause 1: Invalid pointer conversion
func main() {
    x := int64(42)
    p := unsafe.Pointer(&x)
    b := (*[3]byte)(p) // may not be 3 bytes
    fmt.Println(b)
}

// Cause 2: Arithmetic beyond allocation
func main() {
    x := new(int)
    p := unsafe.Pointer(x)
    q := uintptr(p) + 1024 // points to unknown memory
    (*int)(unsafe.Pointer(q)) // undefined behavior
}

// Cause 3: Using pointer after GC moves object
func main() {
    p := new(int)
    ptr := unsafe.Pointer(p)
    runtime.GC()
    // ptr may be invalid if GC moved the object
    *(*int)(ptr) // undefined behavior
}

// Cause 4: Incorrect struct layout assumption
type A struct{ x int32 }
type B struct{ x int32; y int32 }

func main() {
    a := A{x: 42}
    b := (*B)(unsafe.Pointer(&a))
    fmt.Println(b.y) // reads garbage
}
```

## How to Fix

### Fix 1: Follow the five rules of unsafe.Pointer

```go
// Rule 1: *T → Pointer → *T
// Rule 2: Pointer → uintptr → Pointer (in same expression)
// Rule 3: Pointer → uintptr → syscall
// Rule 4: reflect.Value.Pointer/UnsafeAddr → uintptr → Pointer
// Rule 5: Pointer → uintptr → Pointer (in reflect)
```

### Fix 2: Use unsafe.Add and unsafe.Slice (Go 1.17+)

```go
// Wrong
p := unsafe.Pointer(uintptr(unsafe.Pointer(&arr[0])) + offset)

// Correct
p := unsafe.Add(unsafe.Pointer(&arr[0]), offset)
```

### Fix 3: Use reflect for dynamic type access

```go
func setValue(p interface{}, val interface{}) {
    reflect.ValueOf(p).Elem().Set(reflect.ValueOf(val))
}
```

### Fix 4: Keep unsafe.Pointer alive

```go
func main() {
    x := new(int)
    p := unsafe.Pointer(x)
    runtime.KeepAlive(x) // ensures x is not collected before use
    *(*int)(p) = 42
}
```

## Examples

```go
// This triggers: runtime: pointer is not uintptr aligned (or similar)
package main

import (
    "fmt"
    "unsafe"
)

func main() {
    x := int64(42)
    p := unsafe.Pointer(&x)
    b := (*[100]byte)(p) // reading beyond allocation
    fmt.Println(b[99])
}
```

## Related Errors

- [invalid-memory-address]({{< relref "/languages/go/invalid-memory-address" >}}) — accessing invalid memory address.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing nil pointer.
- [reflect-type]({{< relref "/languages/go/reflect-type" >}}) — reflect call on zero value.
