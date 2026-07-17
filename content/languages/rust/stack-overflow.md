---
title: "[Solution] Rust Stack Overflow — Thread Stack Overflow"
description: "Fix Rust stack overflow error. Learn why deep recursion causes stack overflow and how to increase stack size or rewrite recursively."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Stack Overflow — Thread Stack Overflow

A panic with the message "thread 'main' has overflowed its stack" occurs when a thread exceeds its allocated stack memory. This typically happens with deep or infinite recursion.

## Description

Each thread in Rust has a limited stack size (default: 8 MB on most platforms). The stack stores:

- Local variables
- Function call frames
- Return addresses

When recursion goes too deep or a function allocates large arrays on the stack, the stack space is exhausted. Rust detects this and panics rather than allowing undefined behavior (which would happen in C/C++).

Common scenarios:

- **Infinite recursion** — a function calls itself without a base case.
- **Deep recursion** — legitimate but very deep recursive calls.
- **Large stack allocations** — `let data = [0u8; 10_000_000];` on the stack.
- **Recursive data structures** — deeply nested `Vec` or `String`.

## Common Causes

```rust
// Cause 1: Infinite recursion
fn recurse() {
    recurse(); // no base case, infinite recursion
}

// Cause 2: Mutual infinite recursion
fn a() { b(); }
fn b() { a(); }

// Cause 3: Large stack allocation
fn allocate_large() {
    let data = [0u8; 10_000_000]; // 10 MB on stack
    println!("{}", data[0]);
}

// Cause 4: Deep but finite recursion
fn fibonacci(n: u64) -> u64 {
    if n <= 1 { return n; }
    fibonacci(n - 1) + fibonacci(n - 2) // deep recursion for large n
}
```

## Solutions

### Fix 1: Convert recursion to iteration

```rust
// Wrong — recursive
fn fibonacci(n: u64) -> u64 {
    if n <= 1 { return n; }
    fibonacci(n - 1) + fibonacci(n - 2)
}

// Correct — iterative
fn fibonacci(n: u64) -> u64 {
    if n <= 1 { return n; }
    let mut a = 0;
    let mut b = 1;
    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    b
}
```

### Fix 2: Use heap allocation for large data

```rust
// Wrong — large array on stack
fn process() {
    let data = [0u8; 10_000_000]; // stack overflow
    println!("{}", data[0]);
}

// Correct — use Vec (heap allocated)
fn process() {
    let data = vec![0u8; 10_000_000]; // heap allocated
    println!("{}", data[0]);
}
```

### Fix 3: Increase stack size for threads

```rust
use std::thread;

fn main() {
    let builder = thread::Builder::new()
        .stack_size(32 * 1024 * 1024); // 32 MB

    let handle = builder.spawn(|| {
        // Deep recursion now has more room
        recurse(1000);
    }).unwrap();

    handle.join().unwrap();
}

fn recurse(depth: u32) {
    if depth == 0 { return; }
    let _data = [0u8; 1024]; // some stack usage
    recurse(depth - 1);
}
```

### Fix 4: Use tail call optimization (when applicable)

```rust
// Tail-recursive form (compiler may optimize)
fn factorial_tail(n: u64, acc: u64) -> u64 {
    if n <= 1 { acc }
    else { factorial_tail(n - 1, n * acc) }
}

// Or use explicit loop
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
    fn infinite() {
        infinite();
    }
    infinite();
}
```

Output:
```
thread 'main' has overflowed its stack
fatal runtime error: stack overflow, aborting
```

## Related Errors

- [Thread Panic]({{< relref "/languages/rust/thread-panic" >}}) — general thread panics.
- [Out of Memory]({{< relref "/languages/rust/out-of-memory" >}}) — heap memory allocation failure.
- [Overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow.
