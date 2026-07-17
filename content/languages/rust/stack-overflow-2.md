---
title: "[Solution] Rust Stack Overflow — Thread Stack Exhaustion"
description: "Fix Rust stack overflow. Learn why deep recursion or large stack allocations overflow the thread stack and how to fix it."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Stack Overflow — Thread Stack Exhaustion

A panic with the message "thread 'main' has overflowed its stack" occurs when a thread exceeds its allocated stack memory, typically from deep or infinite recursion.

## Description

Each thread has a limited stack (default ~8 MB on Linux). The stack stores local variables, function frames, and return addresses. When recursion goes too deep or a function allocates large arrays on the stack, the space is exhausted. Rust detects this and panics rather than corrupting memory.

Common scenarios:

- **Infinite recursion** — no base case.
- **Large stack arrays** — `let buf = [0u8; 10_000_000];`.
- **Deep recursion** — legitimate but very deep.
- **Recursive data structures** — deeply nested types.

## Common Causes

```rust
// Cause 1: Infinite recursion
fn recurse() { recurse(); }

// Cause 2: Mutual recursion
fn a() { b(); }
fn b() { a(); }

// Cause 3: Large stack allocation
fn allocate() {
    let data = [0u8; 10_000_000]; // 10 MB on stack
    println!("{}", data[0]);
}

// Cause 4: Deep recursion
fn fibonacci(n: u64) -> u64 {
    if n <= 1 { return n; }
    fibonacci(n - 1) + fibonacci(n - 2)
}
```

## Solutions

### Fix 1: Convert to iteration

```rust
fn fibonacci(n: u64) -> u64 {
    if n <= 1 { return n; }
    let (mut a, mut b) = (0u64, 1u64);
    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    b
}
```

### Fix 2: Use heap allocation

```rust
fn process() {
    let data = vec![0u8; 10_000_000]; // heap allocated
    println!("{}", data[0]);
}
```

### Fix 3: Increase thread stack size

```rust
use std::thread;

fn main() {
    let builder = thread::Builder::new().stack_size(32 * 1024 * 1024);
    let h = builder.spawn(|| {
        recurse(1000);
    }).unwrap();
    h.join().unwrap();
}

fn recurse(depth: u32) {
    if depth == 0 { return; }
    let _ = [0u8; 1024];
    recurse(depth - 1);
}
```

### Fix 4: Use tail-call-friendly patterns

```rust
fn factorial(n: u64) -> u64 {
    let mut result = 1;
    for i in 2..=n {
        result *= i;
    }
    result
}
```

## Examples

```rust
fn main() {
    fn infinite() { infinite(); }
    infinite();
}
```

Output:
```
thread 'main' has overflowed its stack
fatal runtime error: stack overflow, aborting
```

## Related Errors

- [Thread Panic]({{< relref "/languages/rust/thread-panic-2" >}}) — general thread panics.
- [Out of Memory]({{< relref "/languages/rust/out-of-memory-2" >}}) — heap allocation failure.
- [Overflow]({{< relref "/languages/rust/overflow-2" >}}) — arithmetic overflow.
