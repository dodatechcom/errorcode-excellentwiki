---
title: "[Solution] Go Out of Memory — Runtime Error Fix"
description: "Fix Go out of memory panic. Optimize memory usage, use streaming instead of buffering, and profile to find memory leaks."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["memory", "oom", "allocation", "gc", "panic"]
weight: 5
---

# Out of Memory — Runtime Error Fix

An out of memory error occurs when the Go runtime cannot allocate memory because the system has exhausted available RAM or the process exceeds its memory limit.

## Description

Go programs can run out of memory when they allocate more than the system can provide. The runtime will crash with `runtime: out of memory` or the OS will kill the process (OOM killer). Go's garbage collector handles most memory, but large allocations, memory leaks, and unbounded data growth can exhaust memory.

Common scenarios:

- **Loading entire files into memory** — reading multi-GB files with `ioutil.ReadAll`.
- **Unbounded slice growth** — appending to a slice without limit.
- **Goroutine leaks** — goroutines holding references to large data.
- **Large map allocation** — `make(map[K]V, hugeSize)` with large types.
- **Circular references** — Go's GC handles these, but excessive allocation still matters.

## Common Causes

```go
// Cause 1: Reading entire large file into memory
data, err := os.ReadFile("huge_file.log") // May exhaust memory

// Cause 2: Unbounded slice growth
var s []int
for i := 0; i < 1e9; i++ {
    s = append(s, i) // Grows without bound
}

// Cause 3: Large map pre-allocation with big value type
m := make(map[int][1024 * 1024]byte, 10000) // 10GB+

// Cause 4: Goroutine leak accumulating data
func leakyWorker(ch <-chan int) {
    results := []int{}
    for v := range ch {
        results = append(results, v) // Never freed
    }
}
```

## How to Fix

### Fix 1: Stream large files instead of loading entirely

```go
// Wrong
data, err := os.ReadFile("huge_file.log")
if err != nil {
    log.Fatal(err)
}

// Correct — read line by line
file, err := os.Open("huge_file.log")
if err != nil {
    log.Fatal(err)
}
defer file.Close()

scanner := bufio.NewScanner(file)
for scanner.Scan() {
    line := scanner.Text()
    process(line)
}
```

### Fix 2: Use bounded buffers and channel sizes

```go
// Wrong — unbounded growth
var results []int
for i := 0; i < 1e9; i++ {
    results = append(results, i)
}

// Correct — process in chunks
const chunkSize = 10000
for i := 0; i < 1e9; i += chunkSize {
    chunk := make([]int, 0, chunkSize)
    for j := 0; j < chunkSize && i+j < 1e9; j++ {
        chunk = append(chunk, i+j)
    }
    processChunk(chunk)
}
```

### Fix 3: Profile memory usage

```go
import "runtime"

// Print memory statistics
var m runtime.MemStats
runtime.ReadMemStats(&m)
fmt.Printf("Alloc = %v MB\n", m.Alloc/1024/1024)
fmt.Printf("TotalAlloc = %v MB\n", m.TotalAlloc/1024/1024)
fmt.Printf("Sys = %v MB\n", m.Sys/1024/1024)
```

### Fix 4: Limit goroutine concurrency

```go
// Wrong — spawns millions of goroutines
for i := 0; i < 1e6; i++ {
    go func(n int) {
        process(n) // Each goroutine uses memory
    }(i)
}

// Correct — use a worker pool
sem := make(chan struct{}, 100) // Max 100 concurrent
for i := 0; i < 1e6; i++ {
    sem <- struct{}{} // Acquire
    go func(n int) {
        defer func() { <-sem }() // Release
        process(n)
    }(i)
}
```

### Fix 5: Use streaming encoders/decoders

```go
// Wrong — loads entire JSON into memory
data, _ := os.ReadFile("huge.json")
var items []Item
json.Unmarshal(data, &items)

// Correct — stream decode
file, _ := os.Open("huge.json")
defer file.Close()
decoder := json.NewDecoder(file)
for decoder.More() {
    var item Item
    decoder.Decode(&item)
    process(item)
}
```

## Examples

```go
// This triggers: runtime: out of memory (if system has limited RAM)
package main

func main() {
    // Allocates ~8GB on a 64-bit system
    s := make([]int64, 1e9)
    _ = s
}
```

## Related Errors

- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines consuming memory without releasing it.
- [stack-overflow]({{< relref "/languages/go/stack-overflow" >}}) — goroutine stack exceeds limit.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — system cannot allocate more memory.
