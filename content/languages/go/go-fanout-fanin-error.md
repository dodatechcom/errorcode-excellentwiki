---
title: "[Solution] Go Fan-Out Fan-In Error — How to Fix"
description: "Fix Go fan-out fan-in pattern errors. Handle goroutine coordination, channel merging, error aggregation, and resource cleanup."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Fan-Out Fan-In Error

Fix Go fan-out fan-in pattern errors. Handle goroutine coordination, channel merging, error aggregation, and resource cleanup.

## Why It Happens

- Fan-out goroutines are not bounded causing excessive memory and goroutine usage
- Fan-in merge function does not close the output channel causing consumers to block forever
- One fan-out worker failure cancels all others when independent error handling is needed
- Channels are not properly synchronized causing data races between fan-out and fan-in

## Common Error Messages

```
panic: close of closed channel
```
```
goroutine leak: fan-out worker blocked on channel write
```
```
runtime: goroutine stack exceeds 1000000-byte limit
```
```
fatal error: out of memory
```

## How to Fix It

### Solution 1: Implement bounded fan-out with fan-in merging

```go
func FanOut(ctx context.Context, input <-chan Job, workers int) <-chan Result {
    out := make(chan Result, workers*10)
    var wg sync.WaitGroup
    for i := 0; i < workers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for job := range input {
                select {
                case out <- process(job):
                case <-ctx.Done():
                    return
                }
            }
        }()
    }
    go func() { wg.Wait(); close(out) }()
    return out
}
```

### Solution 2: Merge multiple channels with proper cleanup

```go
func Merge(ctx context.Context, channels ...<-chan Result) <-chan Result {
    var wg sync.WaitGroup
    merged := make(chan Result, len(channels)*10)
    for _, ch := range channels {
        ch := ch
        wg.Add(1)
        go func() {
            defer wg.Done()
            for {
                select {
                case <-ctx.Done():
                    return
                case r, ok := <-ch:
                    if !ok { return }
                    select {
                    case merged <- r:
                    case <-ctx.Done():
                        return
                    }
                }
            }
        }()
    }
    go func() { wg.Wait(); close(merged) }()
    return merged
}
```

### Solution 3: Collect errors without cancelling others

```go
var mu sync.Mutex
var errs []error
g.Go(func() error {
    if err := process(job); err != nil {
        mu.Lock()
        errs = append(errs, err)
        mu.Unlock()
    }
    return nil
})
```

### Solution 4: Use errgroup for structured fan-out

```go
g, ctx := errgroup.WithContext(ctx)
g.SetLimit(20)
for job := range input {
    job := job
    g.Go(func() error { return process(ctx, job) })
}
return g.Wait()
```

## Common Scenarios

- An image processing pipeline spawns thousands of goroutines without bounds
- A fan-in merge function never closes its output channel causing the consumer goroutine to hang
- One failing worker in a fan-out group cancels the context causing all other workers to abort

## Prevent It

- Use sync.WaitGroup or errgroup to track fan-out goroutines and close the fan-in channel when done
- Limit fan-out concurrency with errgroup.SetLimit to prevent resource exhaustion
- Use independent error collection per worker when one failure should not affect other workers
