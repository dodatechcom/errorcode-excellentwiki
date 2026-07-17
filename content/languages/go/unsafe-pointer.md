---
title: "[Solution] Go Unsafe Pointer Arithmetic Error Fix"
description: "Fix Go unsafe pointer arithmetic errors. Avoid unsafe.Pointer when possible, use proper conversions, and follow the unsafe.Pointer rules."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Unsafe Pointer Arithmetic — Fix

An unsafe pointer arithmetic error occurs when using `unsafe.Pointer` incorrectly, leading to invalid memory access or violations of Go's safety rules.

## Description

Go's `unsafe` package provides ways to bypass the type system and perform low-level memory operations. However, misuse of `unsafe.Pointer` can cause panics, memory corruption, and undefined behavior. The `unsafe` package has strict rules about valid pointer conversions.

Common scenarios:

- **Invalid pointer conversion** — converting between incompatible types.
- **Arithmetic on nil pointer** — adding offsets to nil.
- **Using unsafe after garbage collection** — pointer may be invalidated.
- **Converting between unrelated types** — not following the rule chain.

## Common Causes

```go
// Cause 1: Invalid pointer arithmetic
import "unsafe"

func main() {
    p := unsafe.Pointer(uintptr(0))
    p = unsafe.Add(p, 8) // May be invalid
}

// Cause 2: Converting wrong type
type Foo struct{ X int }
type Bar struct{ Y string }

func main() {
    foo := &Foo{X: 42}
    bar := (*Bar)(unsafe.Pointer(foo)) // Unsafe conversion
    _ = bar.Y // Undefined behavior
}

// Cause 3: Using unsafe with garbage collected memory
import "unsafe"

func main() {
    var p unsafe.Pointer
    x := new(int)
    p = unsafe.Pointer(x)
    x = nil
    // x may be garbage collected, p is dangling
    *(*int)(p) // May access freed memory
}

// Cause 4: Arithmetic past allocation boundary
func main() {
    x := new(int)
    p := unsafe.Pointer(x)
    p = unsafe.Add(p, 1000000) // Way past the allocation
    *(*int)(p) // Invalid access
}
```

## How to Fix

### Fix 1: Avoid unsafe.Pointer when possible

```go
// Wrong — using unsafe to access struct field
type User struct {
    Name string
    Age  int
}

func getAge(u *User) int {
    return *(*int)(unsafe.Pointer(uintptr(unsafe.Pointer(u)) + unsafe.Offsetof(User{}.Age)))
}

// Correct — just access the field directly
func getAge(u *User) int {
    return u.Age
}
```

### Fix 2: Follow the unsafe.Pointer rule chain

```go
import "unsafe"

// Wrong — invalid conversion
func intToBytes(n int) []byte {
    p := unsafe.Pointer(&n)
    return *(*[]byte)(p) // Invalid: int and slice have different layouts
}

// Correct — follow the rules
func intToBytes(n int) []byte {
    // Rule: *T1 -> unsafe.Pointer -> *T2 (when sizes match)
    return *(*[8]byte)(unsafe.Pointer(&n))[:]
}
```

### Fix 3: Use reflect for type-safe alternatives

```go
import "unsafe"

// Wrong — unsafe field access
func setField(obj interface{}, fieldName string, value interface{}) {
    ptr := reflect.ValueOf(obj).Pointer()
    field := reflect.TypeOf(obj).Elem().Field(0)
    p := unsafe.Pointer(ptr + field.Offset)
    // Type conversion may be wrong
}

// Correct — use reflect for safe field access
func setField(obj interface{}, fieldName string, value interface{}) {
    v := reflect.ValueOf(obj).Elem()
    f := v.FieldByName(fieldName)
    if f.IsValid() && f.CanSet() {
        f.Set(reflect.ValueOf(value))
    }
}
```

### Fix 4: Use atomic operations instead of unsafe pointer tricks

```go
import "unsafe"

// Wrong — unsafe atomic operation
func increment(addr *int64) {
    p := unsafe.Pointer(addr)
    *(*int64)(p) = *(*int64)(p) + 1
}

// Correct — use sync/atomic
import "sync/atomic"

func increment(addr *int64) {
    atomic.AddInt64(addr, 1)
}
```

### Fix 5: Pin objects when using unsafe with goroutines

```go
import "unsafe"

// Wrong — object may move during GC
func dangerous() {
    x := new(int)
    p := unsafe.Pointer(x)
    go func() {
        // x may have been moved by GC
        *(*int)(p) // Undefined behavior
    }()
}

// Correct — keep a reference alive
func safe() {
    x := new(int)
    p := unsafe.Pointer(x)
    runtime.GC() // Force GC to see if it's safe
    go func() {
        _ = x // Keep x alive
        *(*int)(p) // p is valid as long as x is alive
    }()
}
```

## Examples

```go
// This may trigger: panic: runtime error: invalid memory address or nil pointer dereference
package main

import (
    "fmt"
    "unsafe"
)

func main() {
    var p unsafe.Pointer
    p = unsafe.Pointer(uintptr(0))
    p = unsafe.Add(p, 8)
    *(*int)(p) // Invalid access
    fmt.Println("unreachable")
}
```

## Related Errors

- [invalid-memory-address]({{< relref "/languages/go/invalid-memory-address" >}}) — accessing invalid memory.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — nil pointer dereference.
- [unsafe-pointer]({{< relref "/languages/go/unsafe-pointer" >}}) — unsafe pointer arithmetic issues.
