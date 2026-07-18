---
title: "[Solution] Go Race Detector Error — How to Fix"
description: "Fix Go race detector errors. Handle data race detection, goroutine synchronization, and race-free patterns."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Race Detector Error

Fix Go race detector errors. Handle data race detection, goroutine synchronization, and race-free patterns.

## Why It Happens

- Race detector finds concurrent read/write to shared variable
- Race detector is too slow for production workloads
- Race detector does not detect all types of races (e.g., logical races)
- Race detector produces false positives in cgo code

## Common Error Messages

```
WARNING: DATA RACE
```
```
race detected at
```
```
Previous write at
```
```
Goroutine running at
```

## How to Fix It

### Solution 1: Enable race detector

```bash
go test -race ./...
go run -race main.go
go build -race -o myapp
```

### Solution 2: Fix data races with mutex

```go
var mu sync.Mutex
var counter int
func increment() {
    mu.Lock()
    defer mu.Unlock()
    counter++
}
```

### Solution 3: Fix data races with channels

```go
ch := make(chan int)
go func() { ch <- computeResult() }()
result := <-ch
```

### Solution 4: Fix data races with atomic

```go
import "sync/atomic"
var counter int64
func increment() {
    atomic.AddInt64(&counter, 1)
}
```

## Common Scenarios

- Race detector finds a data race between two goroutines
- Race detector slows down the test suite significantly
- A race is detected but the code appears to be correct

## Prevent It

- Use channels or mutexes to protect shared state
- Run race detector in CI on every pull request
- Use -race flag with go test for comprehensive detection
