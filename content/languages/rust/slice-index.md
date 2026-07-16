---
title: "[Solution] Rust Slice Index Out of Bounds — Slice Length Mismatch"
description: "Fix Rust slice index out of bounds panic. Learn why slicing beyond a Vec or slice length causes a panic and how to use safe slicing."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["slice", "index", "bounds", "vec", "range", "panic"]
weight: 5
---

# Slice Index Out of Bounds — Slice Length Mismatch

A panic with the message "index out of bounds: the len is X but the index is Y" occurs when you create a slice with a range that extends beyond the collection's bounds.

## Description

Slicing in Rust uses range syntax like `&vec[start..end]`. Both `start` and `end` must be within the bounds of the collection, and `start` must be less than or equal to `end`. Violating these constraints causes a runtime panic. This commonly happens when calculating slice ranges dynamically.

Common scenarios:

- **Range end exceeds length** — `&vec[0..len+1]`.
- **Start exceeds end** — `&vec[5..3]` (start > end).
- **Both bounds out of range** — `&vec[100..200]` on a 10-element Vec.
- **Off-by-one in half-open ranges** — using `..=` instead of `..`.

## Common Causes

```rust
// Cause 1: Range end exceeds length
let data = vec![1, 2, 3, 4, 5];
let slice = &data[0..6]; // panic: range end index 6 out of range for slice of length 5

// Cause 2: Start exceeds end
let slice = &data[3..1]; // panic: slice index starts at 3 but ends at 1

// Cause 3: Using wrong index from external source
let data = vec![10, 20, 30];
let start = 5;
let slice = &data[start..]; // panic: start index out of range

// Cause 4: Off-by-one with inclusive range
let data = vec![1, 2, 3];
let slice = &data[0..=3]; // panic: inclusive range 0..=3 out of bounds for length 3
```

## Solutions

### Fix 1: Use .get() range for safe slicing

```rust
// Wrong
let data = vec![1, 2, 3, 4, 5];
let slice = &data[0..6]; // panics

// Correct
let data = vec![1, 2, 3, 4, 5];
if let Some(slice) = data.get(0..6) {
    println!("Got slice: {:?}", slice);
} else {
    println!("Invalid slice range");
}
```

### Fix 2: Clamp range values to valid bounds

```rust
// Wrong
let data = vec![1, 2, 3, 4, 5];
let start = 2;
let end = 10;
let slice = &data[start..end]; // panics if end > len

// Correct
let data = vec![1, 2, 3, 4, 5];
let start = 2.min(data.len());
let end = 10.min(data.len());
let slice = &data[start..end]; // safe
```

### Fix 3: Use iterators for safe partial access

```rust
// Wrong
let data = vec![1, 2, 3, 4, 5];
let slice = &data[10..20]; // panics

// Correct
let data = vec![1, 2, 3, 4, 5];
let items: Vec<_> = data.iter().skip(2).take(3).collect();
println!("{:?}", items); // [3, 4, 5]
```

### Fix 4: Validate before slicing

```rust
fn safe_slice(data: &[i32], start: usize, end: usize) -> Option<&[i32]> {
    if start <= end && end <= data.len() {
        Some(&data[start..end])
    } else {
        None
    }
}

fn main() {
    let data = vec![1, 2, 3, 4, 5];
    match safe_slice(&data, 1, 3) {
        Some(slice) => println!("Slice: {:?}", slice),
        None => println!("Invalid slice range"),
    }
}
```

## Examples

```rust
fn main() {
    let v = vec![10, 20, 30, 40, 50];

    // This panics because index 8 exceeds the length of 5
    let slice = &v[2..8];
    println!("{:?}", slice);
}
```

Output:
```
thread 'main' panicked at 'range end index 8 out of range for slice of length 5'
```

## Related Errors

- [Index Out of Bounds]({{< relref "/languages/rust/index-out-of-bounds" >}}) — accessing a single element outside bounds.
- [Move]({{< relref "/languages/rust/move" >}}) — using a value after it has been moved.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong types in slice operations.
