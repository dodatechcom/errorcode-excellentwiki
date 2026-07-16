---
title: "[Solution] Go Errors & Panics — Complete Reference"
description: "Find solutions for Go errors including nil pointer dereference, index out of range, goroutine leaks, and more with copy-paste code examples."
languages: ["go"]
---

Go errors and panics happen at runtime when something goes wrong — from dereferencing a nil pointer to concurrent map writes. Every entry below includes a clear explanation of what triggers the error and the exact code fix.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [nil-pointer](/languages/go/nil-pointer/) | Nil pointer dereference — calling a method or accessing a field on a nil pointer | Add nil checks before use, initialize structs properly, and use error-returning patterns |
| [index-out-of-range](/languages/go/index-out-of-range/) | Index out of range — accessing an array or slice with an invalid index | Check the length before indexing, use bounds checking, and avoid off-by-one errors |
| [deadlock](/languages/go/deadlock/) | All goroutines are asleep — deadlock detected by the runtime | Ensure channels are properly closed and goroutines can make progress |

## Quick Debug

```go
// Enable runtime race detector
// go run -race main.go
// go build -race -o myapp

// Print goroutine stack traces
import "runtime/pprof"
pprof.Lookup("goroutine").WriteTo(os.Stderr, 1)
```
