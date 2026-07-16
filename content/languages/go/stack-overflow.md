---
title: "[Solution] Go Stack Overflow — Runtime Error Fix"
description: "Fix Go runtime stack overflow panic. Eliminate infinite recursion, convert recursive functions to iteration, and increase stack size when needed."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["stack", "overflow", "recursion", "goroutine", "panic"]
weight: 5
---

# Stack Overflow — Runtime Error Fix

A stack overflow occurs when a goroutine's call stack exceeds the available memory, causing the runtime to panic.

## Description

Each goroutine starts with a small stack (typically 2-8 KB) that grows dynamically. When recursive calls or deep call chains exhaust the stack, the runtime panics with `runtime: stack overflow`. Go can grow stacks up to a maximum (default 1 GB on 64-bit systems).

Common scenarios:

- **Infinite recursion** — a function calls itself without a base case.
- **Mutual recursion** — two functions call each other in an infinite loop.
- **Very deep but legitimate recursion** — tree traversal on extremely deep structures.
- **Stack-eating allocations** — large stack-allocated variables consume stack space quickly.

## Common Causes

```go
// Cause 1: Infinite recursion
func count(n int) int {
    return count(n) // No base case, calls itself forever
}

// Cause 2: Missing base case
func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1) // Infinite if n starts negative
}

// Cause 3: Mutual recursion without base case
func isEven(n int) bool {
    if n == 0 {
        return true
    }
    return isOdd(n - 1)
}

func isOdd(n int) bool {
    if n == 0 {
        return false
    }
    return isEven(n - 1)
}

// isEven(-1) causes infinite recursion

// Cause 4: Large stack allocation
func recurse(n int) {
    var buf [1024 * 1024]byte // 1MB on stack
    _ = buf
    recurse(n + 1) // Each call uses 1MB of stack
}
```

## How to Fix

### Fix 1: Add a proper base case

```go
// Wrong
func countDown(n int) {
    fmt.Println(n)
    countDown(n - 1) // Infinite for any n
}

// Correct
func countDown(n int) {
    if n <= 0 {
        return
    }
    fmt.Println(n)
    countDown(n - 1)
}
```

### Fix 2: Convert recursion to iteration

```go
// Wrong — deep recursion
func sum(n int) int {
    if n == 0 {
        return 0
    }
    return n + sum(n-1)
}

// Correct — iterative
func sum(n int) int {
    total := 0
    for i := n; i > 0; i-- {
        total += i
    }
    return total
}
```

### Fix 3: Ensure mutual recursion terminates

```go
// Wrong — may not terminate for negative input
func isEven(n int) bool {
    if n == 0 {
        return true
    }
    return isOdd(n - 1)
}

// Correct — validate input
func isEven(n int) bool {
    if n < 0 {
        n = -n // Make positive
    }
    if n == 0 {
        return true
    }
    return isOdd(n - 1)
}
```

### Fix 4: Move large allocations to the heap

```go
// Wrong — 1MB per stack frame
func process(n int) {
    var buf [1024 * 1024]byte
    _ = buf
    process(n + 1)
}

// Correct — allocate on heap
func process(n int) {
    buf := new([1024 * 1024]byte) // Allocated on heap
    _ = buf
    process(n + 1)
}
```

### Fix 5: Use explicit stack for deep traversal

```go
// Wrong — recursive DFS
type TreeNode struct {
    Left, Right *TreeNode
}

func dfs(node *TreeNode) {
    if node == nil {
        return
    }
    dfs(node.Left)
    dfs(node.Right)
}

// Correct — iterative DFS with explicit stack
func dfsIterative(root *TreeNode) {
    if root == nil {
        return
    }
    stack := []*TreeNode{root}
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if node.Right != nil {
            stack = append(stack, node.Right)
        }
        if node.Left != nil {
            stack = append(stack, node.Left)
        }
    }
}
```

## Examples

```go
// This triggers: runtime: stack overflow (after growing stack to maximum)
package main

func recurse() {
    recurse()
}

func main() {
    recurse()
}
```

## Related Errors

- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck and consuming resources.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — running out of memory.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
