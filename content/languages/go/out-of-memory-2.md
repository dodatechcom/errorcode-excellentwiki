---
title: "[Solution] Go Out of Memory — Runtime Error Fix"
description: "Fix Go out of memory panic. Identify excessive allocations, use streaming for large data, and profile memory usage."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Out of Memory — Runtime Error Fix

An out of memory condition occurs when the Go runtime cannot allocate more memory, either because the system is exhausted or the allocation exceeds the garbage collector's limits.

## Description

Go's garbage collector manages memory automatically, but programs can still run out of memory by allocating faster than the GC can reclaim, or by holding references to large data sets. The runtime may panic with `runtime: out of memory` or the OS may kill the process.

Common scenarios:

- **Reading entire large file into memory** — loading multi-GB files with `io.ReadAll`.
- **Unbounded slice growth** — appending without limit in a loop.
- **Memory leak via goroutine** — goroutines holding references to large objects.
- **Caching too much** — in-memory cache that grows without eviction.

## Common Causes

```go
// Cause 1: Reading entire large file into memory
func main() {
    data, err := os.ReadFile("/var/log/huge.log") // 10GB file
    if err != nil {
        log.Fatal(err)
    }
    _ = data
}

// Cause 2: Unbounded slice growth
func collect() []int {
    var result []int
    for {
        result = append(result, generateNumber())
        // grows forever
    }
}

// Cause 3: Goroutine holding large reference
func leak() {
    huge := make([]byte, 1<<30) // 1GB
    go func() {
        time.Sleep(time.Hour)
        _ = huge // prevents GC
    }()
}

// Cause 4: Map growing without bound
func main() {
    m := make(map[string][]byte)
    for i := 0; ; i++ {
        m[fmt.Sprintf("key-%d", i)] = make([]byte, 1<<20) // 1MB each
    }
}
```

## How to Fix

### Fix 1: Stream large files instead of reading all

```go
// Wrong
data, _ := os.ReadFile("huge.bin")

// Correct — process line by line
file, _ := os.Open("huge.bin")
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    processLine(scanner.Text())
}
```

### Fix 2: Bound slice growth

```go
// Wrong
func collect(maxSize int) []int {
    var result []int
    for {
        result = append(result, generate())
    }
}

// Correct
func collect(maxSize int) []int {
    result := make([]int, 0, maxSize)
    for len(result) < maxSize {
        result = append(result, generate())
    }
    return result
}
```

### Fix 3: Limit goroutine lifetime and data scope

```go
func process(data []byte) {
    // Process and release immediately
    result := transform(data)
    sendResult(result)
    // data can now be GC'd
}
```

### Fix 4: Use runtime.MemStats to monitor

```go
import "runtime"

func logMemory() {
    var m runtime.MemStats
    runtime.ReadMemStats(&m)
    fmt.Printf("Alloc = %v MB\n", m.Alloc/1024/1024)
    fmt.Printf("Sys = %v MB\n", m.Sys/1024/1024)
}
```

## Examples

```go
// This triggers: runtime: out of memory
package main

func main() {
    // Allocate memory until the system runs out
    for i := 0; i < 1000; i++ {
        _ = make([]byte, 100*1024*1024) // 100MB each
    }
}
```

## Related Errors

- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines holding memory without releasing.
- [stack-overflow]({{< relref "/languages/go/stack-overflow" >}}) — stack grows beyond limits.
- [too-many-open-files]({{< relref "/languages/go/too-many-open-files" >}}) — resource exhaustion (file descriptors).
