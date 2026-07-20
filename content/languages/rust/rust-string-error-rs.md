---
title: "[Solution] Rust String Error — How to Fix"
description: "Fix String and &str errors. Resolve UTF-8, string conversion, and lifetime issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# String Error

String errors occur when working with `String` and `&str` — UTF-8 conversion failures, indexing mistakes, and lifetime issues.

## Common Causes

```rust
// Indexing into a String
let s = String::from("hello");
let c = s[0]; // ERROR: cannot index String with usize

// UTF-8 conversion failure
let bytes = vec![0xFF, 0xFE];
let s = String::from_utf8(bytes).unwrap(); // ERROR: invalid UTF-8

// Moving out of String while borrowed
let s = String::from("hello");
let r = &s[..2];
s.push_str(" world"); // ERROR: cannot mutate while borrowed

// Slicing at non-character boundaries
let s = "hello world";
let hello = &s[0..4]; // ERROR: 'l' is 2 bytes, not at byte 4
```

## How to Fix

1. **Use `chars()` for character iteration**

```rust
let s = String::from("hello");

// Character iteration
for c in s.chars() {
    println!("{}", c);
}

// Character at index
let third = s.chars().nth(2);
println!("Third char: {:?}", third);

// Character count
println!("Chars: {}", s.chars().count());
```

2. **Handle UTF-8 conversion properly**

```rust
let bytes = vec![72, 101, 108, 108, 111]; // "Hello"

// Fallible conversion
match String::from_utf8(bytes) {
    Ok(s) => println!("String: {}", s),
    Err(e) => println!("Error: {} (bytes: {:?})", e, e.as_bytes()),
}

// Lossy conversion
let bad_bytes = vec![0xFF, 0xFE, 72, 101];
let s = String::from_utf8_lossy(&bad_bytes);
println!("Lossy: {}", s); // "��He"
```

3. **Use proper string slicing**

```rust
let s = "hello world";

// Byte slicing (be careful with UTF-8)
let hello = &s[0..5]; // Safe: "hello" is all ASCII
println!("{}", hello);

// Safer: use char indices
fn safe_slice(s: &str, start: usize, end: usize) -> &str {
    let start = s.char_indices().nth(start).map(|(i, _)| i).unwrap_or(s.len());
    let end = s.char_indices().nth(end).map(|(i, _)| i).unwrap_or(s.len());
    &s[start..end]
}

println!("{}", safe_slice("héllo", 0, 3)); // "hél"
```

## Examples

```rust
fn main() {
    let s = String::from("Hello, 世界!");

    // Iterate over chars
    for c in s.chars() {
        print!("[{}] ", c);
    }
    println!();

    // Count words
    let words: Vec<&str> = s.split_whitespace().collect();
    println!("Words: {:?}", words);

    // Replace
    let replaced = s.replace("世界", "Rust");
    println!("Replaced: {}", replaced);

    // Start/end checks
    println!("Starts with 'Hello': {}", s.starts_with("Hello"));
    println!("Ends with '!': {}", s.ends_with('!'));

    // Truncate
    let mut owned = String::from("Hello, World!");
    owned.truncate(5);
    println!("Truncated: {}", owned);
}
```

## Related Errors

- [Collections Error]({{< relref "/languages/rust/rust-collections-error" >}}) — collection issues
- [Iter Error]({{< relref "/languages/rust/rust-iter-error" >}}) — iterator issues
- [Vec Error]({{< relref "/languages/rust/rust-vec-error" >}}) — vector issues
