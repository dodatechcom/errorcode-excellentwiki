---
title: "[Solution] Rust Called unwrap on None — Unwrap Panic on Option"
description: "Fix Rust unwrap() on None panic. Learn why calling unwrap on a None Option crashes your program and how to handle missing values safely."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Called unwrap on None — Unwrap Panic on Option

A panic with the message "called `Option::unwrap()` on a `None` value" occurs when you call `.unwrap()` on an `Option` that holds `None`.

## Description

`Option<T>` represents a value that may or may not exist — `Some(value)` or `None`. The `.unwrap()` method extracts the inner value or panics. While convenient in prototypes and tests, unwrap in production code is a common source of crashes whenever the optional value turns out to be missing.

Common scenarios:

- **Hash map lookups** — key not present in the map.
- **String parsing** — conversion to number fails.
- **First/last on empty collection** — `vec.first().unwrap()`.
- **Regex captures** — group didn't match.
- **Config values** — optional setting not provided.

## Common Causes

```rust
use std::collections::HashMap;

// Cause 1: Missing map key
let mut map = HashMap::new();
map.insert("name", "Alice");
let age = map.get("age").unwrap(); // panic: None

// Cause 2: Empty vec
let v: Vec<i32> = vec![];
let first = v.first().unwrap(); // panic

// Cause 3: Failed string parse
let num: Option<i32> = "not_a_number".parse().ok();
num.unwrap(); // panic

// Cause 4: Regex without match
let re = regex::Regex::new(r"(\d+)").unwrap();
let caps = re.captures("no digits here").unwrap(); // panic
```

## Solutions

### Fix 1: Use match or if let

```rust
let map = HashMap::from([("name", "Alice")]);
match map.get("age") {
    Some(age) => println!("Age: {}", age),
    None => println!("Age not found"),
}
```

### Fix 2: Use unwrap_or with a default

```rust
let map = HashMap::from([("name", "Alice")]);
let age = map.get("age").unwrap_or(&0);
println!("Age: {}", age);
```

### Fix 3: Use the ? operator to propagate

```rust
fn find_user_age(name: &str) -> Option<u32> {
    let map = HashMap::from([("Alice", 30), ("Bob", 25)]);
    let age = map.get(name)?;
    Some(*age)
}
```

### Fix 4: Use unwrap_or_else for lazy computation

```rust
let map = HashMap::from([("name", "Alice")]);
let age = map.get("age").unwrap_or_else(|| {
    eprintln!("Warning: age not found, defaulting to 18");
    &18
});
println!("Age: {}", age);
```

## Examples

```rust
use std::collections::HashMap;

fn main() {
    let scores: HashMap<&str, i32> = HashMap::new();
    let math = scores.get("math").unwrap();
    println!("Math score: {}", math);
}
```

Output:
```
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value'
```

## Related Errors

- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — unwrap on an Err Result.
- [Expect Fail]({{< relref "/languages/rust/expect-fail-2" >}}) — expect on an Err Result.
- [Index Out of Bounds]({{< relref "/languages/rust/index-out-of-bounds-2" >}}) — accessing invalid index.
