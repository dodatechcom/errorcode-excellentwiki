---
title: "[Solution] Go Escape Analysis Error — How to Fix"
description: "Fix Go escape analysis errors. Handle heap allocation, pointer escapes, and escape to heap."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Escape Analysis Error

Fix Go escape analysis errors. Handle heap allocation, pointer escapes, and escape to heap.

## Why It Happens

- Function returns a pointer to a local variable causing heap allocation
- Interface conversion causes value to escape to heap
- Closure captures a variable causing it to escape to heap
- Escape analysis shows unexpected allocations causing GC pressure

## Common Error Messages

```
escapes to heap
```
```
moved to heap:
```
```
heap allocation
```
```
cannot inline function
```

## How to Fix It

### Solution 1: Check escape analysis

```bash
go build -gcflags="-m" ./...
go build -gcflags="-m -m" ./...  # More detail
```

### Solution 2: Avoid unnecessary escapes

```go
// Bad: value escapes to heap
func getSlice() []byte {
    buf := make([]byte, 1024)
    return buf  // escapes to heap
}
// Good: preallocate buffer
var buf [1024]byte
func getSlice() []byte {
    return buf[:]
}
```

### Solution 3: Use value types to prevent escapes

```go
// Bad: pointer causes heap allocation
func process(data *Data) { ... }
// Good: value type stays on stack
func process(data Data) { ... }
```

### Solution 4: Use buffer pools

```go
var bufPool = sync.Pool{
    New: func() interface{} {
        b := make([]byte, 0, 4096)
        return &b
    },
}
func process() {
    buf := bufPool.Get().(*[]byte)
    defer bufPool.Put(buf)
    // Use *buf
}
```

## Common Scenarios

- Escape analysis shows that a value escapes to heap unexpectedly
- Function return values cause heap allocations
- Interface conversions cause values to escape

## Prevent It

- Use go build -gcflags=-m to check escape analysis
- Prefer value types over pointer types when possible
- Use sync.Pool for frequently allocated buffers
