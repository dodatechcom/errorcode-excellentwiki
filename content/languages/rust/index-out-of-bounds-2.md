---
title: "[Solution] Rust Index Out of Bounds — Vec Length Exceeded"
description: "Fix Rust index out of bounds panic. Learn why indexing a Vec or slice beyond its length causes a runtime panic and how to handle it safely."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["index", "bounds", "vec", "slice", "panic", "len"]
weight: 5
---

# Index Out of Bounds — Vec Length Exceeded

A panic with the message "index out of bounds: the len is X but the index is Y" occurs when you access an element at an index that exceeds the collection's length.

## Description

Rust prevents undefined behavior by bounds-checking every array, Vec, and slice access. If the index Y is greater than or equal to the length X, the runtime panics immediately. This catch prevents memory corruption that would occur in unchecked languages.

The error specifies both the actual length and the attempted index, making it straightforward to diagnose. The index is zero-based, so a Vec of length 3 has valid indices 0, 1, and 2.

Common scenarios:

- **Dynamic index from computation** — an arithmetic expression produces an out-of-range index.
- **Loop boundary error** — `for i in 0..=vec.len()` instead of `0..vec.len()`.
- **After filter or drain** — collection shrunk but index wasn't updated.
- **Negative index wrapped to usize** — casting a negative `i32` to `usize` wraps to a huge number.

## Common Causes

```rust
// Cause 1: Off-by-one with inclusive range
let items = vec![10, 20, 30];
for i in 0..=items.len() {    // 0..=3 means i goes up to 3
    println!("{}", items[i]);  // panics when i == 3
}

// Cause 2: Computed index overflowing
let len = items.len();
let idx = len + 2;
let val = items[idx]; // panic

// Cause 3: Signed-to-unsigned cast
let offset: i32 = -1;
let idx = offset as usize; // wraps to usize::MAX
let val = items[idx]; // panic

// Cause 4: Stale length after mutation
let mut v = vec![1, 2, 3, 4, 5];
let len = v.len();
v.clear();
println!("{}", v[len - 1]); // panic
```

## Solutions

### Fix 1: Use .get() for safe access

```rust
let items = vec![10, 20, 30];

match items.get(5) {
    Some(val) => println!("Value: {}", val),
    None => println!("Index 5 is out of bounds (len={})", items.len()),
}
```

### Fix 2: Use .checked_sub() for safe index arithmetic

```rust
let v = vec![1, 2, 3, 4, 5];
let offset: i32 = -1;

if let Some(idx) = v.len().checked_add_signed(offset) {
    if let Some(val) = v.get(idx) {
        println!("Value: {}", val);
    }
}
```

### Fix 3: Use iterators to avoid manual indexing

```rust
let items = vec![10, 20, 30];
for (i, item) in items.iter().enumerate() {
    println!("[{}] = {}", i, item);
}
```

### Fix 4: Use .get_mut() for safe mutable access

```rust
let mut items = vec![10, 20, 30];
if let Some(slot) = items.get_mut(1) {
    *slot = 99;
}
println!("{:?}", items); // [10, 99, 30]
```

## Examples

```rust
fn main() {
    let data = vec![42, 17, 8];
    let index = 10;

    let value = data[index];
    println!("Found: {}", value);
}
```

Output:
```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 10'
```

## Related Errors

- [Slice Index]({{< relref "/languages/rust/slice-index-2" >}}) — range-based slice out of bounds.
- [Overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow in index computation.
- [Move]({{< relref "/languages/rust/move" >}}) — value moved before indexing.
