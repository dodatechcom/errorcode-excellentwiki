---
title: "[Solution] Go Stack Growth Error — How to Fix"
description: "Fix Go stack growth errors. Handle goroutine stack overflow, stack size configuration, and stack management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Stack Growth Error

Fix Go stack growth errors. Handle goroutine stack overflow, stack size configuration, and stack management.

## Why It Happens

- Goroutine stack overflows because of deep recursion
- Goroutine stack is too large because of excessive local variables
- Stack growth causes performance issues because of copying
- Stack size limit is reached causing runtime crash

## Common Error Messages

```
goroutine stack grows beyond limit
```
```
runtime: stack overflow
```
```
goroutine running with stack size > 1GB
```
```
runtime: cannot allocate stack
```

## How to Fix It

### Solution 1: Understand goroutine stack growth

```go
// Go goroutines start with 2KB stack and grow dynamically
// Stack is copied when it needs to grow
// Use runtime.Stack to check current size
```

### Solution 2: Monitor stack size

```go
buf := make([]byte, 1<<20)
n := runtime.Stack(buf, true)
fmt.Printf("%s\n", buf[:n])
```

### Solution 3: Avoid stack overflow

```go
// Avoid deep recursion - use iteration instead
func factorial(n int) int {
    if n <= 1 { return 1 }
    return n * factorial(n-1)  // may overflow
}
// Use iteration
func factorialIterative(n int) int {
    result := 1
    for i := 2; i <= n; i++ { result *= i }
    return result
}
```

### Solution 4: Set custom stack size

```go
// runtime.GOMAXSTACK is not directly settable
// But you can use runtime/debug.SetMaxStack
import "runtime/debug"
debug.SetMaxStack(1 << 25) // 32MB
```

## Common Scenarios

- Goroutine stack overflows because of deep recursion
- A goroutine uses too much stack memory because of large local arrays
- Stack growth is too slow causing goroutine to be killed

## Prevent It

- Convert deep recursion to iteration
- ['Check stack size with runtime.Stack', '```go\nbuf := make([]byte, 1<<20)\nn := runtime.Stack(buf, false)\nfmt.Printf("stack size: %d bytes\\n", n)\n```']
- Use runtime/debug.SetMaxStack to increase stack size limit
