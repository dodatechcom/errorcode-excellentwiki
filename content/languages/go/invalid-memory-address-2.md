---
title: "[Solution] Go Invalid Memory Address — Runtime Error Fix"
description: "Fix Go invalid memory address panic. Avoid accessing freed memory, nil pointers, and incorrect unsafe.Pointer operations."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["memory", "address", "invalid", "pointer", "panic", "runtime", "unsafe"]
weight: 5
---

# Invalid Memory Address — Runtime Error Fix

An invalid memory address panic occurs when the program attempts to access a memory location that is not mapped or is outside valid address space.

## Description

Go's memory safety guarantees prevent most invalid memory access, but some operations can still trigger this panic. The error message is `runtime error: invalid memory address or nil pointer dereference`. While often the same error as nil pointer dereference, it can also arise from unsafe pointer operations or using memory after it has been freed.

Common scenarios:

- **Nil pointer dereference** — the most common cause (see also: nil-pointer).
- **Using unsafe.Pointer incorrectly** — converting to invalid address.
- **Slice header corruption** — modifying a slice's internal pointer via unsafe.
- **CGo memory misuse** — accessing C memory that was freed.

## Common Causes

```go
// Cause 1: Nil pointer dereference
func main() {
    var p *int
    fmt.Println(*p) // panic: invalid memory address
}

// Cause 2: Unsafe pointer to wrong type
import "unsafe"

func main() {
    x := int64(42)
    p := unsafe.Pointer(&x)
    b := (*byte)(p)
    fmt.Println(*b) // reads only the first byte, but valid
}

// Cause 3: Using freed C memory via CGo
/*
#include <stdlib.h>
void* alloc() { return malloc(100); }
void dealloc(void* p) { free(p); }
*/
import "C"

func main() {
    ptr := C.alloc()
    C.dealloc(ptr)
    // Accessing ptr after dealloc is undefined
}

// Cause 4: Nil slice internal pointer
func main() {
    var s []int
    p := (*reflect.SliceHeader)(unsafe.Pointer(&s))
    _ = uintptr(p.Data) // Data is 0 for nil slice
}
```

## How to Fix

### Fix 1: Always check for nil before dereferencing

```go
func readValue(p *int) int {
    if p == nil {
        return 0
    }
    return *p
}
```

### Fix 2: Avoid unsafe pointer conversions

```go
// Wrong
func bytesToInt(b []byte) int {
    p := unsafe.Pointer(&b[0])
    return *(*int)(p)
}

// Correct
func bytesToInt(b []byte) int {
    return int(binary.LittleEndian.Uint64(b[:8]))
}
```

### Fix 3: Set CGo pointers to nil after free

```go
// Correct
ptr := C.alloc()
C.dealloc(ptr)
ptr = nil // prevent accidental reuse
```

### Fix 4: Use runtime.KeepAlive for cgo pointers

```go
func process(ptr unsafe.Pointer) {
    runtime.SetFinalizer(ptr, func(p unsafe.Pointer) {
        C.free(p)
    })
    // Use ptr...
    runtime.KeepAlive(ptr) // ensures ptr is not freed during use
}
```

## Examples

```go
// This triggers: runtime error: invalid memory address or nil pointer dereference
package main

import "fmt"

func main() {
    var p *int
    fmt.Println(*p)
}
```

## Related Errors

- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — nil pointer dereference (same error, different focus).
- [unsafe-pointer]({{< relref "/languages/go/unsafe-pointer" >}}) — incorrect unsafe.Pointer usage.
- [interface-conversion]({{< relref "/languages/go/interface-conversion" >}}) — type assertion on nil interface value.
