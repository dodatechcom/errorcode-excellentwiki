---
title: "[Solution] Rust Iterator Error — How to Fix"
description: "Fix iterator errors. Resolve iterator trait implementation, adapter usage, and consumption issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Iterator Error

Iterator errors occur when using Rust iterators incorrectly — consuming iterators, using them after exhaustion, or violating iterator protocol.

## Common Causes

```rust
// Consuming iterator then trying to reuse
let v = vec![1, 2, 3];
let iter = v.iter();
for val in iter { print!("{} ", val); }
// iter is consumed — cannot iterate again

// Borrowing issues with iterator chains
let mut v = vec![1, 2, 3];
let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect();
v.push(4); // v was borrowed, may have issues

// Using .next() incorrectly on peekable
use std::iter::Peekable;
let mut iter = [1, 2, 3].iter().peekable();
iter.peek(); // Returns Some
// Not consuming the peeked value
```

## How to Fix

1. **Clone iterators if you need to reuse them**

```rust
let v = vec![1, 2, 3];

// Method 1: Create new iterator each time
for val in v.iter() { print!("{} ", val); }
println!();
for val in v.iter() { print!("{} ", val); }
println!();

// Method 2: Use clone on the iterator
let iter = v.iter().cloned();
let collected: Vec<_> = iter.clone().collect();
let sum: i32 = iter.sum();
```

2. **Use `peekable` correctly**

```rust
let mut iter = vec![1, 2, 3].into_iter().peekable();

while iter.peek().is_some() {
    let val = iter.next().unwrap();
    println!("Processing: {}", val);
}
```

3. **Collect before mutating the source**

```rust
let mut v = vec![1, 2, 3];
let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect(); // Collect first
v.push(4); // Safe — no active borrows
println!("{:?}", doubled);
```

## Examples

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // Filter even numbers
    let evens: Vec<&i32> = numbers.iter().filter(|&&x| x % 2 == 0).collect();
    println!("Evens: {:?}", evens);

    // Map and collect
    let squared: Vec<i32> = numbers.iter().map(|&x| x * x).collect();
    println!("Squared: {:?}", squared);

    // Fold to compute sum
    let sum: i32 = numbers.iter().fold(0, |acc, &x| acc + x);
    println!("Sum: {}", sum);

    // Chained operations
    let result: String = numbers.iter()
        .filter(|&&x| x % 2 == 0)
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join(", ");
    println!("Even numbers: {}", result);
}
```

## Related Errors

- [Collections Error]({{< relref "/languages/rust/rust-collections-error" >}}) — collection issues
- [Vec Error]({{< relref "/languages/rust/rust-vec-error" >}}) — vector issues
- [Stream Error]({{< relref "/languages/rust/rust-stream-error-rs" >}}) — async iterators
