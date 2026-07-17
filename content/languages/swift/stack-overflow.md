---
title: "[Solution] Swift Error — EXC_BAD_ACCESS Stack Overflow"
description: "Fix Swift stack overflow errors. Learn why infinite recursion and deep call stacks exhaust the stack and how to prevent EXC_BAD_ACCESS."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# EXC_BAD_ACCESS — Stack Overflow

A stack overflow occurs when a program uses more stack space than is available, typically due to infinite recursion or extremely deep call chains. The result is an `EXC_BAD_ACCESS` crash.

## Description

Each thread has a limited stack (typically 512KB on iOS). Every function call allocates a stack frame for local variables and return addresses. Infinite recursion or very deep recursion exhausts this space. The OS delivers an `EXC_BAD_ACCESS` signal when the stack guard page is hit.

Common patterns:

- **Infinite recursion** — function calling itself without a base case.
- **Mutual recursion** — two functions calling each other without termination.
- **Deep UI hierarchy** — extremely nested view controller presentations.
- **Large stack allocations** — allocating large arrays on the stack.

## Common Causes

```swift
// Cause 1: Infinite recursion — missing base case
func countDown(n: Int) {
    print(n)
    countDown(n: n) // Never terminates
}
countDown(n: 10) // Stack overflow

// Cause 2: Mutual recursion
func ping() { pong() }
func pong() { ping() }
ping() // Stack overflow

// Cause 3: Delegate cycle causing recursive calls
class A {
    weak var b: B?
    func call() { b?.call() }
}
class B {
    weak var a: A?
    func call() { a?.call() }
}

// Cause 4: Recursive computed property
struct Node {
    var value: Int {
        return value // Infinite recursion
    }
}
```

## How to Fix

### Fix 1: Add proper base cases to recursion

```swift
// Wrong
func countDown(n: Int) {
    print(n)
    countDown(n: n - 1)
}

// Correct
func countDown(n: Int) {
    guard n > 0 else { return } // Base case
    print(n)
    countDown(n: n - 1)
}
```

### Fix 2: Convert recursion to iteration

```swift
// Wrong — recursive
func factorial(_ n: Int) -> Int {
    return n <= 1 ? 1 : n * factorial(n - 1)
}

// Correct — iterative
func factorial(_ n: Int) -> Int {
    var result = 1
    for i in 2...n { result *= i }
    return result
}
```

### Fix 3: Break delegate cycles

```swift
class Parent {
    weak var child: Child? // Use weak to break cycles
}
class Child {
    weak var parent: Parent? // Use weak to break cycles
}
```

### Fix 4: Use iterative approaches for deep operations

```swift
// Wrong — recursive tree traversal without limit
func traverse(_ node: TreeNode) {
    for child in node.children {
        traverse(child) // May overflow on deep trees
    }
}

// Correct — use explicit stack
func traverse(_ root: TreeNode) {
    var stack = [root]
    while let node = stack.popLast() {
        stack.append(contentsOf: node.children)
    }
}
```

## Examples

```swift
// Example 1: Recursive property access
struct File {
    var size: Int {
        return size // Stack overflow: calls itself
    }
}

// Example 2: Missing guard in recursive function
func fibonacci(_ n: Int) -> Int {
    return fibonacci(n - 1) + fibonacci(n - 2) // No base case check
}

// Example 3: Deep view controller presentation
func presentNext() {
    let vc = UIViewController()
    present(vc, animated: true) {
        presentNext() // Stack overflow after many levels
    }
}
```

## Related Errors

- [EXC_BAD_ACCESS]({{< relref "/languages/swift/memory-access" >}}) — general memory access crash.
- [Thread Sanitizer Error]({{< relref "/languages/swift/thread-sanitizer" >}}) — related concurrency issue.
- [Arithmetic Overflow]({{< relref "/languages/swift/overflow" >}}) — related runtime crash.
