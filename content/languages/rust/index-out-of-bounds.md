---
title: "[Solution] Rust Index Out of Bounds — Vec Index Error"
description: "Fix Rust index out of bounds panic. Learn why indexing a Vec or slice beyond its length causes a panic and how to safely access elements."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Index Out of Bounds — Vec Index Error

A panic with the message "index out of bounds: the len is X but the index is Y" occurs when you attempt to access an element at an index that is greater than or equal to the length of the collection.

## Description

Rust collections like `Vec`, arrays, and slices use zero-based indexing. A collection of length `n` has valid indices from `0` to `n-1`. Indexing outside this range causes a runtime panic. This is a deliberate safety check — Rust prevents out-of-bounds memory access, which would be undefined behavior in C/C++.

Common scenarios:

- **Off-by-one error** — accessing `vec[vec.len()]` instead of `vec[vec.len() - 1]`.
- **Empty collection access** — indexing index 0 of an empty `Vec`.
- **Hardcoded index** — assuming a collection always has a certain number of elements.
- **Stale index after modification** — using an index after elements have been removed.

## Common Causes

```rust
// Cause 1: Off-by-one error
let items = vec![1, 2, 3];
let value = items[3]; // panic: index out of bounds: the len is 3 but the index is 3

// Cause 2: Empty Vec access
let empty: Vec<i32> = vec![];
let value = empty[0]; // panic: index out of bounds: the len is 0 but the index is 0

// Cause 3: Hardcoded index without checking length
let data = vec![10, 20, 30];
println!("{}", data[10]); // panic: index out of bounds

// Cause 4: Using an index after removing elements
let mut v = vec![1, 2, 3, 4, 5];
let idx = 4;
v.remove(idx);
println!("{}", v[idx]); // panic: index out of bounds after removal
```

## Solutions

### Fix 1: Use .get() for safe access

```rust
// Wrong
let items = vec![1, 2, 3];
let value = items[3]; // panics

// Correct
let items = vec![1, 2, 3];
let value = items.get(3); // Returns Option<&T>, value is None
match items.get(3) {
    Some(v) => println!("Got: {}", v),
    None => println!("Index out of bounds"),
}
```

### Fix 2: Check length before indexing

```rust
// Wrong
let items = vec![1, 2, 3];
let value = items[3];

// Correct
let items = vec![1, 2, 3];
let idx = 3;
if idx < items.len() {
    let value = items[idx];
    println!("Got: {}", value);
} else {
    println!("Index {} is out of bounds for length {}", idx, items.len());
}
```

### Fix 3: Use iterators instead of index-based access

```rust
// Wrong
let items = vec![1, 2, 3];
for i in 0..items.len() {
    println!("{}", items[i]);
}

// Correct
let items = vec![1, 2, 3];
for item in &items {
    println!("{}", item);
}

// Or with index using enumerate
for (i, item) in items.iter().enumerate() {
    println!("{}: {}", i, item);
}
```

### Fix 4: Use .get().copied() for owned values

```rust
// Wrong
let items = vec![1, 2, 3];
let value: i32 = items[5]; // panics

// Correct
let items = vec![1, 2, 3];
let value: Option<i32> = items.get(5).copied();
let value = value.unwrap_or(0); // default to 0 if out of bounds
```

## Examples

```rust
fn main() {
    let v = vec![10, 20, 30];

    // This line panics
    let x = v[5];

    println!("Value: {}", x);
}
```

Output:
```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 5'
```

## Related Errors

- [Slice Index]({{< relref "/languages/rust/slice-index" >}}) — similar error when slicing beyond bounds.
- [Out of Memory]({{< relref "/languages/rust/out-of-memory" >}}) — allocation failures when creating large collections.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong type used in indexing expressions.
