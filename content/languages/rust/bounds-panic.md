---
title: "[Solution] Rust Index Out of Bounds Panic — Fix"
description: "Fix Rust index out of bounds panics. Use safe indexing methods like get(), checked indexing, and bounds checking."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "bounds", "panic", "slice", "vector", "array", "indexing"]
weight: 5
---

# Index Out of Bounds Panic

The error `index out of bounds: the len is X but the index is Y` occurs when you use the `[]` operator with an index that exceeds the collection's length. This is a runtime panic, not a compile-time error.

## Description

Rust's indexing operator (`[]`) performs bounds checking at runtime. When the index is outside the valid range (0 to len-1), the program panics. Unlike some languages that return a default value or sentinel, Rust terminates the thread.

The `.get()` method provides a safe alternative that returns `Option<&T>` instead of panicking.

## Common Causes

- **Off-by-one errors** — using `<=` instead of `<` in loop conditions
- **User-supplied indices** — using external input as an index without validation
- **Empty collection access** — accessing index 0 on an empty vector or slice
- **String byte indexing** — indexing a `String` by byte position (may split UTF-8)

## How to Fix

### Fix 1: Use .get() for safe access

```rust
let v = vec![1, 2, 3];

// Panics:
// let x = v[5];

// Safe:
match v.get(5) {
    Some(x) => println!("value: {}", x),
    None => println!("index out of bounds"),
}
```

### Fix 2: Check bounds before indexing

```rust
let v = vec![1, 2, 3];
let index = 5;

if index < v.len() {
    println!("{}", v[index]);
} else {
    println!("index {} is out of bounds for length {}", index, v.len());
}
```

### Fix 3: Use iterators instead of indexing

```rust
let v = vec![1, 2, 3];
for (i, val) in v.iter().enumerate() {
    println!("{}: {}", i, val);
}
```

### Fix 4: Use char_indices for string iteration

```rust
// Wrong — byte indexing can panic on UTF-8
let s = String::from("hello");
// let c = s[0]; // may not be valid UTF-8

// Correct — iterate over characters
for (i, c) in s.char_indices() {
    println!("byte {}: {}", i, c);
}
```

## Examples

```rust
fn main() {
    let v = vec![10, 20, 30];
    let index = 10;
    println!("{}", v[index]); // panic
}
```

Output:
```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 10'
```

## Related Errors

- [unwrap-none]({{< relref "/languages/rust/unwrap-none" >}}) — unwrap panic on missing Option values.
- [overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow panics.
- [thread-panic]({{< relref "/languages/rust/thread-panic" >}}) — panics propagating across threads.
