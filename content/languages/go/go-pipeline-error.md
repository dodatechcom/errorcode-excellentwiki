---
title: "[Solution] Go Pipeline Error — How to Fix"
description: "Fix Go pipeline errors. Handle channel operations, stage failures, goroutine cleanup, and data flow between pipeline stages."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Pipeline Error

Fix Go pipeline errors. Handle channel operations, stage failures, goroutine cleanup, and data flow between pipeline stages.

## Why It Happens

- A pipeline stage sends on a closed channel causing a panic
- Goroutines in pipeline stages leak because channels are not properly closed
- An error in one stage is not propagated to upstream stages causing silent data loss
- Buffer channels are too small causing producers to block indefinitely

## Common Error Messages

```
panic: send on closed channel
```
```
goroutine leak: pipeline stage blocked
```
```
context canceled while pipeline stage is running
```
```
deadlock detected: all goroutines are asleep
```

## How to Fix It

### Solution 1: Build pipeline with proper channel closing

```go
func Pipeline(ctx context.Context, input <-chan int) <-chan int {
    out := make(chan int, 10)
    go func() {
        defer close(out)
        for val := range input {
            select {
            case <-ctx.Done():
                return
            case out <- val * 2:
            }
        }
    }()
    return out
}
```

### Solution 2: Propagate errors through stages

```go
type PipelineResult struct {
    Data []int
    Err  error
}
func processStage(ctx context.Context, in <-chan int, fn func(int)(int,error)) <-chan PipelineResult {
    out := make(chan PipelineResult, 10)
    go func() {
        defer close(out)
        for val := range in {
            result, err := fn(val)
            select {
            case <-ctx.Done():
                return
            case out <- PipelineResult{Data: []int{result}, Err: err}:
            }
        }
    }()
    return out
}
```

### Solution 3: Use WaitGroup for shutdown coordination

```go
var wg sync.WaitGroup
out := make(chan Result, 10)
wg.Add(1)
go func() {
    defer wg.Done()
    defer close(out)
    for d := range input {
        result, err := transform(d)
        if err != nil {
            select {
            case out <- Result{Err: err}:
            case <-ctx.Done():
                return
            }
        }
    }
}()
```

### Solution 4: Size channel buffers appropriately

```go
stage1Out := make(chan Data, batchSize)
stage2Out := make(chan Result, batchSize/2)
```

## Common Scenarios

- A data processing pipeline panics when consumer closes before producer finishes
- A log processing pipeline leaks goroutines because intermediate channels are never closed
- A video encoding pipeline blocks forever because the output channel buffer is too small

## Prevent It

- Always close channels in a defer or in the goroutine that creates them
- Use context.WithCancel to propagate shutdown signals to all stages
- Size channel buffers based on expected throughput between stages
