---
title: "[Solution] Rust Collections Error — How to Fix"
description: "Fix collection errors. Resolve HashMap, BTreeMap, and other standard collection usage issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Collections Error

Collections errors occur when using Rust's standard collections (`Vec`, `HashMap`, `BTreeMap`, etc.) incorrectly — index out of bounds, borrow conflicts, or type mismatches.

## Common Causes

```rust
use std::collections::HashMap;

// Index out of bounds
let v = vec![1, 2, 3];
let x = v[5]; // PANIC: index out of bounds

// HashMap key type mismatch
let mut map = HashMap::new();
map.insert("key", 42);
map.get(&1i32); // ERROR: expected &str, found &i32

// Borrowing issues with HashMap
let mut map = HashMap::new();
map.insert("key".to_string(), vec![1, 2]);
let val = map.get("key").unwrap();
map.insert("key2".to_string(), vec![3]); // val still borrowed — cannot insert
```

## How to Fix

1. **Use `.get()` instead of indexing for safe access**

```rust
let v = vec![1, 2, 3];

// Safe: returns Option
match v.get(5) {
    Some(val) => println!("Found: {}", val),
    None => println!("Index out of bounds"),
}

// Or use unwrap_or for defaults
let val = v.get(5).unwrap_or(&0);
```

2. **Use entry API for HashMap operations**

```rust
use std::collections::HashMap;

let mut map: HashMap<String, Vec<i32>> = HashMap::new();

// Entry API avoids borrow conflicts
map.entry("key".to_string())
    .or_insert_with(Vec::new)
    .push(42);

// Count occurrences
let words = vec!["hello", "world", "hello", "rust"];
let mut counts = HashMap::new();
for word in &words {
    *counts.entry(word.to_string()).or_insert(0) += 1;
}
println!("{:?}", counts);
```

3. **Scope borrows correctly**

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key".to_string(), vec![1, 2]);

// Clone or collect before mutating
let val = map.get("key").cloned().unwrap_or_default();
map.insert("key2".to_string(), vec![3]);
println!("Original: {:?}", map.get("key"));
println!("Cloned: {:?}", val);
```

## Examples

```rust
use std::collections::HashMap;

fn main() {
    let mut scores: HashMap<&str, i32> = HashMap::new();
    scores.insert("Alice", 95);
    scores.insert("Bob", 87);
    scores.insert("Charlie", 92);

    // Safe access
    for (name, score) in &scores {
        println!("{}: {}", name, score);
    }

    // Update with entry
    scores.entry("Alice").and_modify(|s| *s += 5);

    // Remove and return
    if let Some(removed) = scores.remove("Bob") {
        println!("Bob's score was: {}", removed);
    }

    // Find highest
    if let Some((name, score)) = scores.iter().max_by_key(|(_, s)| *s) {
        println!("Highest: {} with {}", name, score);
    }
}
```

## Related Errors

- [Vec Error]({{< relref "/languages/rust/rust-vec-error" >}}) — vector issues
- [String Error]({{< relref "/languages/rust/rust-string-error-rs" >}}) — string issues
- [Iter Error]({{< relref "/languages/rust/rust-iter-error" >}}) — iterator issues
