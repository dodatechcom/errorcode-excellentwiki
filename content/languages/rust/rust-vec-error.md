---
title: "[Solution] Rust Vec Error — How to Fix"
description: "Fix Vec errors. Resolve vector reallocation, index bounds, and capacity issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Vec Error

Vec errors occur when using `Vec<T>` — index out of bounds, capacity overflow, and borrowing conflicts.

## Common Causes

```rust
// Index out of bounds
let v = vec![1, 2, 3];
let x = v[10]; // PANIC: index out of bounds

// Capacity overflow
let mut v: Vec<i32> = Vec::with_capacity(1);
v.push(1);
v.push(2); // May reallocate, but capacity overflow on extreme cases

// Borrow conflict with iterator
let mut v = vec![1, 2, 3];
for item in &v {
    v.push(*item); // ERROR: cannot borrow `v` as mutable while iterating
}
```

## How to Fix

1. **Use `get()` for safe access**

```rust
let v = vec![1, 2, 3];

// Safe indexing
match v.get(1) {
    Some(val) => println!("Found: {}", val),
    None => println!("Index out of bounds"),
}

// Or use unwrap_or
let val = v.get(10).unwrap_or(&0);
println!("Value: {}", val);
```

2. **Collect before modifying**

```rust
let mut v = vec![1, 2, 3];

// Collect first, then modify
let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect();
v.push(4); // Safe — no active borrows
println!("Doubled: {:?}", doubled);
println!("Original: {:?}", v);
```

3. **Use `Vec::with_capacity` to pre-allocate**

```rust
let mut v = Vec::with_capacity(1000);
for i in 0..1000 {
    v.push(i); // No reallocations
}
assert_eq!(v.len(), 1000);
assert!(v.capacity() >= 1000);
```

## Examples

```rust
fn main() {
    let mut v = vec![1, 2, 3, 4, 5];

    // Remove by value
    v.retain(|&x| x != 3);
    println!("After retain: {:?}", v);

    // Insert at position
    v.insert(0, 0);
    println!("After insert: {:?}", v);

    // Sort and dedup
    let mut v = vec![3, 1, 4, 1, 5, 9, 2, 6, 5, 3];
    v.sort();
    v.dedup();
    println!("Sorted unique: {:?}", v);

    // Windows and chunks
    let data = vec![1, 2, 3, 4, 5];
    for window in data.windows(3) {
        println!("Window: {:?}", window);
    }
}
```

## Related Errors

- [Collections Error]({{< relref "/languages/rust/rust-collections-error" >}}) — collection issues
- [Heapless Error]({{< relref "/languages/rust/rust-heapless-error" >}}) — fixed-size vec
- [Iter Error]({{< relref "/languages/rust/rust-iter-error" >}}) — iterator issues
