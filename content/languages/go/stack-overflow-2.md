---
title: "[Solution] Go Stack Overflow — Runtime Error Fix"
description: "Fix Go stack overflow panic caused by unbounded recursion. Use iterative algorithms, increase stack size, or add recursion depth limits."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["stack", "overflow", "recursion", "panic", "runtime", "goroutine"]
weight: 5
---

# Stack Overflow — Runtime Error Fix

A stack overflow occurs when a goroutine's stack grows beyond the runtime limit due to deep or infinite recursion.

## Description

Each goroutine starts with a small stack (typically 2KB) that grows dynamically up to a limit (default 1GB on 64-bit systems). When recursion or deeply nested calls exhaust this space, the runtime panics with `runtime: stack overflow`. This is distinct from C-style stack overflow — Go can grow its stack, but infinite recursion still exhausts it.

Common scenarios:

- **Infinite recursion** — a function that calls itself with no base case.
- **Mutual recursion** — two functions calling each other in a loop.
- **Large stack frames** — functions with large local arrays or many variables.
- **Deep tree traversal** — very deep binary trees or linked lists.

## Common Causes

```go
// Cause 1: Infinite recursion — missing base case
func countdown(n int) {
    fmt.Println(n)
    countdown(n - 1) // never stops
}

// Cause 2: Mutual recursion without termination
func isEven(n int) bool {
    if n == 0 { return true }
    return isOdd(n - 1)
}

func isOdd(n int) bool {
    if n == 0 { return false }
    return isEven(n - 1)
}

func main() {
    isEven(100000) // may overflow
}

// Cause 3: Large stack frame
func bigStack() {
    var buf [1024 * 1024]byte // 1MB local variable
    _ = buf
    bigStack() // overflows quickly
}

// Cause 4: Recursive data processing
func processNode(node *Node) int {
    return node.Val + processNode(node.Next) // infinite if cyclic
}
```

## How to Fix

### Fix 1: Add a proper base case

```go
// Wrong
func factorial(n int) int {
    return n * factorial(n-1)
}

// Correct
func factorial(n int) int {
    if n <= 1 {
        return 1
    }
    return n * factorial(n-1)
}
```

### Fix 2: Convert recursion to iteration

```go
// Wrong — recursive
func sumList(node *Node) int {
    if node == nil { return 0 }
    return node.Val + sumList(node.Next)
}

// Correct — iterative
func sumList(node *Node) int {
    sum := 0
    for node != nil {
        sum += node.Val
        node = node.Next
    }
    return sum
}
```

### Fix 3: Use explicit stack for tree traversal

```go
// Wrong — recursive DFS
func traverse(n *Node) {
    if n == nil { return }
    process(n)
    traverse(n.Left)
    traverse(n.Right)
}

// Correct — iterative with explicit stack
func traverse(root *Node) {
    stack := []*Node{root}
    for len(stack) > 0 {
        n := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if n == nil { continue }
        process(n)
        stack = append(stack, n.Right, n.Left)
    }
}
```

### Fix 4: Limit recursion depth

```go
func process(n int, depth int) int {
    if depth > 10000 {
        return 0 // stop recursing
    }
    return process(n-1, depth+1)
}
```

## Examples

```go
// This triggers: runtime: stack overflow
package main

func recurse(n int) int {
    return recurse(n + 1)
}

func main() {
    recurse(0)
}
```

## Related Errors

- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck in loops without making progress.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — memory exhausted before stack limit.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
