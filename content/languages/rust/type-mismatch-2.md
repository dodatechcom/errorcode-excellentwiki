---
title: "[Solution] Rust Mismatched Types — Type Mismatch Error"
description: "Fix Rust mismatched types error. Learn why Rust's type system rejects type mismatches and how to convert between types correctly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Mismatched Types — Type Mismatch Error

A compiler error with the message "mismatched types" occurs when you use a value of one type where a different type is expected.

## Description

Rust is statically typed — every expression has a known type at compile time. The compiler rejects code where the actual type doesn't match the expected type. Unlike dynamic languages, Rust won't silently convert between most types.

Common scenarios:

- **String vs &str** — passing `String` where `&str` is expected.
- **Numeric mixing** — adding `i32` + `f64` without casting.
- **Wrong return type** — function returns wrong type.
- **Option vs value** — passing `Option<i32>` where `i32` is expected.
- **Result not unwrapped** — passing `Result<T, E>` where `T` is expected.

## Common Causes

```rust
// Cause 1: String vs &str
fn greet(name: &str) { println!("Hi {}", name); }
let name = String::from("Alice");
greet(name); // Error: expected &str, found String

// Cause 2: Numeric type mismatch
let x: i32 = 5;
let y: f64 = 3.14;
let sum = x + y; // Error: cannot add f64 to i32

// Cause 3: Wrong return type
fn get_number() -> i32 {
    "42" // Error: expected i32, found &str
}

// Cause 4: Bool where int expected
let flag = true;
let count: i32 = flag; // Error: expected i32, found bool
```

## Solutions

### Fix 1: Borrow or convert types

```rust
fn greet(name: &str) { println!("Hi {}", name); }
let name = String::from("Alice");

// Option A: borrow
greet(&name);

// Option B: convert
greet(name.as_str());
```

### Fix 2: Explicit numeric casting

```rust
let x: i32 = 5;
let y: f64 = 3.14;
let sum = x as f64 + y;
println!("{}", sum); // 8.14
```

### Fix 3: Return the correct type

```rust
fn get_number() -> i32 {
    42 // Return a number, not a string
}
```

### Fix 4: Use .into() for compatible types

```rust
fn greet(name: &str) { println!("Hi {}", name); }
let name = String::from("Alice");

// String implements Into<&str> via deref
greet(&name);
```

## Examples

```rust
fn main() {
    let x: i32 = 5;
    let y: bool = true;
    let result = x + y;
    println!("{}", result);
}
```

Output:
```
error[E0277]: cannot add `bool` to `i32`
```

## Related Errors

- [Parse Int]({{< relref "/languages/rust/parse-int-2" >}}) — string to integer conversion failure.
- [Variant Not Found]({{< relref "/languages/rust/variant-not-found-2" >}}) — wrong enum variant.
- [Missing Field]({{< relref "/languages/rust/missing-field-2" >}}) — missing struct field.
