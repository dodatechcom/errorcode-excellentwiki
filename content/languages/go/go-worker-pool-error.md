---
title: "[Solution] Go Worker Pool Error — How to Fix"
description: "Fix Go worker pool errors. Handle goroutine lifecycle, job queue overflow, graceful shutdown, and worker panic recovery."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Worker Pool Error

Fix Go worker pool errors. Handle goroutine lifecycle, job queue overflow, graceful shutdown, and worker panic recovery.

## Why It Happens

- Worker goroutines are not properly shut down when the pool receives a stop signal
- The job queue channel is unbounded causing memory to grow without limit
- A panic in a worker goroutine crashes the entire program without recovery
- Workers block on a full channel and the pool cannot drain remaining jobs

## Common Error Messages

```
panic: send on closed channel
```
```
worker pool: job queue full, dropping job
```
```
goroutine leak: worker pool goroutines still running
```
```
fatal error: all goroutines are asleep - deadlock
```

## How to Fix It

### Solution 1: Implement a worker pool with graceful shutdown

```go
type WorkerPool struct {
    jobs    chan Job
    results chan Result
    wg      sync.WaitGroup
    cancel  context.CancelFunc
}
func (p *WorkerPool) worker(ctx context.Context) {
    defer p.wg.Done()
    for {
        select {
        case <-ctx.Done():
            return
        case job, ok := <-p.jobs:
            if !ok { return }
            p.results <- process(job)
        }
    }
}
```

### Solution 2: Add panic recovery to workers

```go
func (p *WorkerPool) worker(ctx context.Context, id int) {
    defer p.wg.Done()
    for {
        select {
        case <-ctx.Done():
            return
        case job, ok := <-p.jobs:
            if !ok { return }
            func() {
                defer func() {
                    if r := recover(); r != nil {
                        log.Printf("worker %d: panic: %v", id, r)
                    }
                }()
                p.results <- process(job)
            }()
        }
    }
}
```

### Solution 3: Limit job queue with backpressure

```go
func (p *WorkerPool) Submit(ctx context.Context, job Job) error {
    select {
    case p.jobs <- job:
        return nil
    case <-ctx.Done():
        return ctx.Err()
    default:
        select {
        case p.jobs <- job:
            return nil
        case <-ctx.Done():
            return ctx.Err()
        case <-time.After(5 * time.Second):
            return fmt.Errorf("worker pool queue full")
        }
    }
}
```

### Solution 4: Track worker stats for monitoring

```go
type WorkerStats struct {
    mu            sync.Mutex
    JobsProcessed int64
    JobsFailed    int64
    ActiveWorkers int32
}
```

## Common Scenarios

- A web scraper worker pool crashes because one worker panics and takes down the whole process
- A task queue grows unbounded because workers process slower than jobs arrive
- A worker pool shutdown leaves goroutines hanging because the jobs channel is never closed

## Prevent It

- Always defer close(jobs) and wait for workers with sync.WaitGroup during shutdown
- Add panic recovery to each worker goroutine to prevent cascading failures
- Implement backpressure using select with default or timeout when submitting to a full queue
