---
title: "[Solution] Go pprof Error — How to Fix"
description: "Fix Go pprof errors. Handle profiling endpoint setup, CPU/memory profiling, goroutine leaks, and profile analysis."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go pprof Error

Fix Go pprof errors. Handle profiling endpoint setup, CPU/memory profiling, goroutine leaks, and profile analysis.

## Why It Happens

- pprof HTTP handler is not registered causing profiling endpoints to return 404
- CPU profiling runs for too short a duration producing incomplete data
- Memory profiling captures too many allocations causing excessive memory usage
- Profile data is written to a locked file causing write failures

## Common Error Messages

```
pprof: profile not available
```
```
pprof: too much write contention
```
```
pprof: encoding error
```
```
net/http: server closed before response completed
```

## How to Fix It

### Solution 1: Enable pprof in your application

```go
import _ "net/http/pprof"
go func() {
    log.Println(http.ListenAndServe("localhost:6060", nil))
}()
```

### Solution 2: Capture CPU profile

```go
f, _ := os.Create("cpu.prof")
pprof.StartCPUProfile(f)
defer pprof.StopCPUProfile()
```

### Solution 3: Analyze profiles with go tool

```go
// go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30
// go tool pprof http://localhost:6060/debug/pprof/heap
// go tool pprof -http=:8080 cpu.prof
```

### Solution 4: Use runtime.ReadMemStats for memory analysis

```go
var m runtime.MemStats
runtime.ReadMemStats(&m)
fmt.Printf("Alloc = %v MB\n", m.Alloc/1024/1024)
```

## Common Scenarios

- A production server has no profiling enabled making it impossible to debug performance
- CPU profile shows hot spots but the code looks efficient
- Memory profile shows high allocation but the code reuses objects

## Prevent It

- Enable pprof endpoints in production with authentication
- Collect CPU profiles during actual workload reproduction
- Use alloc_space to find allocation hotspots rather than inuse_space
