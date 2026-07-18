---
title: "[Solution] Go sync.Pool Error — How to Fix"
description: "Fix Go sync.Pool errors. Handle object reuse, Reset methods, GC eviction, and type assertion failures in pooled objects."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go sync.Pool Error

Fix Go sync.Pool errors. Handle object reuse, Reset methods, GC eviction, and type assertion failures in pooled objects.

## Why It Happens

- Pooled objects are returned without resetting state causing data corruption for next user
- sync.Pool objects are evicted during garbage collection leading to high allocation rates
- Type assertions on pooled objects fail because different types are stored in the pool
- A nil value is retrieved from pool and used without a nil check

## Common Error Messages

```
panic: interface conversion: interface {} is nil, not <type>
```
```
runtime: object allocated on stack escapes to heap
```
```
sync: pool is empty and New is nil
```
```
goroutine stack growth exceeds limit
```

## How to Fix It

### Solution 1: Reset objects before returning to pool

```go
var bufPool = sync.Pool{New: func() interface{} { return new(bytes.Buffer) }}
func GetBuffer() *bytes.Buffer { return bufPool.Get().(*bytes.Buffer) }
func PutBuffer(buf *bytes.Buffer) { buf.Reset(); bufPool.Put(buf) }
```

### Solution 2: Handle nil returns from pool.Get

```go
val := pool.Get()
if val == nil {
    return createNew()
}
obj := val.(*Obj)
if obj.IsClosed() { return createNew() }
```

### Solution 3: Use a typed pool wrapper

```go
type BufferPool struct{ pool sync.Pool }
func (p *BufferPool) Get() *[]byte { return p.pool.Get().(*[]byte) }
func (p *BufferPool) Put(buf *[]byte) {
    if buf == nil { return }
    *buf = (*buf)[:0]
    p.pool.Put(buf)
}
```

### Solution 4: Benchmark pool effectiveness

```go
func BenchmarkPool(b *testing.B) {
    pool := sync.Pool{New: func() interface{} { return new(bytes.Buffer) }}
    for i := 0; i < b.N; i++ {
        buf := pool.Get().(*bytes.Buffer)
        buf.Reset()
        buf.Write([]byte("test"))
        pool.Put(buf)
    }
}
```

## Common Scenarios

- A high-throughput server reuses buffers but stale data leaks between requests
- A serialization library pools encoders but the pool returns nil after GC
- A game engine pools objects but they retain state from previous frames

## Prevent It

- Always call Reset on pooled objects before Get and Put
- Provide a non-nil New function in sync.Pool for empty pool after GC
- Benchmark pool usage to verify it actually reduces allocations
