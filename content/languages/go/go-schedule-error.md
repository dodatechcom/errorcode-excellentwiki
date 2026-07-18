---
title: "[Solution] Go Scheduler Error — How to Fix"
description: "Fix Go scheduler errors. Handle goroutine scheduling, GOMAXPROCS configuration, and goroutine preemption."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Scheduler Error

Fix Go scheduler errors. Handle goroutine scheduling, GOMAXPROCS configuration, and goroutine preemption.

## Why It Happens

- Goroutine is stuck in a tight loop without yielding preventing other goroutines from running
- GOMAXPROCS is too low causing poor CPU utilization
- Goroutine stack is too large causing excessive memory usage
- Scheduler is not distributing work evenly across OS threads

## Common Error Messages

```
scheduler: goroutine stuck
```
```
scheduler: no goroutines to schedule
```
```
scheduler: stack overflow
```
```
scheduler: thread exhaustion
```

## How to Fix It

### Solution 1: Configure GOMAXPROCS

```go
import "runtime"
// Set to number of CPU cores (default)
runtime.GOMAXPROCS(runtime.NumCPU())
// Or limit to control concurrency
runtime.GOMAXPROCS(4)
```

### Solution 2: Use runtime.Goexit for goroutine control

```go
func worker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            runtime.Goexit()  // Clean exit
        default:
            doWork()
        }
    }
}
```

### Solution 3: Monitor goroutine count

```go
go func() {
    for {
        fmt.Printf("goroutines: %d\n", runtime.NumGoroutine())
        time.Sleep(time.Second)
    }
}()
```

### Solution 4: Use sync.Pool for reusable objects

```go
var pool = sync.Pool{
    New: func() interface{} { return new(bytes.Buffer) },
}
buf := pool.Get().(*bytes.Buffer)
defer pool.Put(buf)
```

## Common Scenarios

- Goroutine does not yield in a tight loop blocking other goroutines
- Application uses only one CPU core despite multiple cores available
- Goroutine memory usage grows because of large stacks

## Prevent It

- Add runtime.Gosched() in tight loops or use context for cancellation
- Set GOMAXPROCS to match available CPU cores
- Use pprof to monitor goroutine count and stack sizes
