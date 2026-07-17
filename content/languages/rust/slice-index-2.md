---
title: "[Solution] Rust Slice Index Out of Bounds — Range Exceeds Length"
description: "Fix Rust slice index out of bounds. Learn why creating a slice with a range beyond a collection's length panics and how to safely slice."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Slice Index Out of Bounds — Range Exceeds Length

A panic with the message "index out of bounds: the len is X but the index is Y" occurs when you create a slice using a range whose end index exceeds the collection's length.

## Description

Slicing in Rust uses range syntax like `&vec[start..end]`. The end index must be less than or equal to the collection length, and the start must be less than or equal to the end. When a range extends past the end of the data, the runtime panics with the length and the offending index.

This differs from single-element indexing because slicing creates a view into contiguous memory — if the range is invalid, there's no memory to point to.

Common scenarios:

- **Half-open range past end** — `&vec[1..len+1]`.
- **Inclusive range at boundary** — `&vec[0..=len]` on a len-length Vec.
- **Dynamic range from user input** — range values not clamped to length.
- **Chained slices** — slicing a slice without accounting for the reduced length.

## Common Causes

```rust
// Cause 1: Inclusive range exceeding length
let data = vec![1, 2, 3, 4, 5];
let slice = &data[0..=5]; // panic: inclusive range 0..=5, len is 5

// Cause 2: Dynamic end index
let end = 20;
let data = vec![1, 2, 3];
let slice = &data[0..end]; // panic: end 20 > len 3

// Cause 3: Slicing a subslice without adjusting
let data = vec![1, 2, 3, 4, 5];
let sub = &data[1..4]; // sub has length 3
let deep = &sub[0..4]; // panic: sub len is 4, not 5

// Cause 4: Start greater than end
let data = vec![1, 2, 3];
let slice = &data[2..1]; // panic: range start 2 > end 1
```

## Solutions

### Fix 1: Use .get() for safe range access

```rust
let data = vec![1, 2, 3, 4, 5];
if let Some(slice) = data.get(2..10) {
    println!("Slice: {:?}", slice);
} else {
    println!("Range 2..10 is out of bounds for length {}", data.len());
}
```

### Fix 2: Clamp range values to valid bounds

```rust
let data = vec![1, 2, 3, 4, 5];
let start = 2;
let end = 10;
let safe_start = start.min(data.len());
let safe_end = end.min(data.len());
let slice = &data[safe_start..safe_end];
println!("{:?}", slice); // [3, 4, 5]
```

### Fix 3: Use .get() with a helper function

```rust
fn safe_slice<T>(data: &[T], start: usize, end: usize) -> Option<&[T]> {
    if start <= end && end <= data.len() {
        Some(&data[start..end])
    } else {
        None
    }
}

fn main() {
    let data = vec![10, 20, 30, 40, 50];
    match safe_slice(&data, 1, 8) {
        Some(s) => println!("Got: {:?}", s),
        None => println!("Invalid range"),
    }
}
```

### Fix 4: Use saturating arithmetic on indices

```rust
let data = vec![1, 2, 3, 4, 5];
let start = 10_usize;
let len = 3_usize;
let safe_start = start.min(data.len());
let safe_end = (start + len).min(data.len());
let slice = &data[safe_start..safe_end];
println!("{:?}", slice); // [] (empty, but no panic)
```

## Examples

```rust
fn main() {
    let numbers = vec![10, 20, 30, 40, 50];
    let slice = &numbers[3..8];
    println!("{:?}", slice);
}
```

Output:
```
thread 'main' panicked at 'range end index 8 out of range for slice of length 5'
```

## Related Errors

- [Index Out of Bounds]({{< relref "/languages/rust/index-out-of-bounds-2" >}}) — single-element access beyond bounds.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong types in range expressions.
- [Overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow computing range.
