---
title: "[Solution] Rust Type Mismatch — Mismatched Types Error"
description: "Fix Rust mismatched types error. Learn why Rust's strong type system rejects type mismatches and how to convert between types correctly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["type", "mismatch", "conversion", "inference", "casting"]
weight: 5
---

# Type Mismatch — Mismatched Types Error

A compiler error with the message "mismatched types" occurs when you try to use a value of one type where a different type is expected. Rust's strong, static type system prevents this at compile time.

## Description

Rust is strongly typed and performs type checking at compile time. The "mismatched types" error appears when:

- A function receives the wrong argument type.
- A variable is assigned a value of the wrong type.
- A return value doesn't match the declared return type.
- Pattern matching arms return different types.
- Numeric types are mixed without explicit conversion.

Unlike dynamically typed languages, Rust won't implicitly convert between most types. You must be explicit about type conversions.

Common scenarios:

- **String vs &str** — passing `String` where `&str` is expected (or vice versa).
- **Numeric type confusion** — mixing `i32` and `f64` without casting.
- **Bool vs int** — using a boolean where a number is expected.
- **Option vs value** — passing `Option<T>` where `T` is expected.
- **Result vs value** — passing `Result<T, E>` where `T` is expected.

## Common Causes

```rust
// Cause 1: String vs &str
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

let name = String::from("Alice");
greet(name); // Error: expected `&str`, found `String`

// Cause 2: Numeric type mismatch
let x: i32 = 5;
let y: f64 = 3.14;
let sum = x + y; // Error: cannot add `f64` to `i32`

// Cause 3: Wrong return type
fn get_number() -> i32 {
    "42" // Error: expected `i32`, found `&str`
}

// Cause 4: Bool where number expected
let flag = true;
let count: i32 = flag; // Error: expected `i32`, found `bool`
```

## Solutions

### Fix 1: Use proper type conversions

```rust
// Wrong
fn greet(name: &str) {
    println!("Hello, {}!", name);
}
let name = String::from("Alice");
greet(name);

// Correct — borrow the String
greet(&name);

// Or convert String to &str
fn greet(name: &str) {
    println!("Hello, {}!", name);
}
let name = String::from("Alice");
greet(name.as_str());
```

### Fix 2: Cast numeric types explicitly

```rust
// Wrong
let x: i32 = 5;
let y: f64 = 3.14;
let sum = x + y;

// Correct
let sum = x as f64 + y;
// Or
let sum = x as f64 + y as f64;
```

### Fix 3: Return the correct type

```rust
// Wrong
fn get_number() -> i32 {
    "42"
}

// Correct
fn get_number() -> i32 {
    42
}

// Or parse the string
fn get_number() -> i32 {
    "42".parse().unwrap()
}
```

### Fix 4: Use .into() for types that implement From

```rust
// Wrong
fn greet(name: &str) {
    println!("Hello, {}!", name);
}
let name = String::from("Alice");
greet(name);

// Correct — String implements Into<&str>
greet(&name);
```

## Examples

```rust
fn main() {
    let x: i32 = 5;
    let y: bool = true;

    // This causes the error
    let result = x + y;
    println!("{}", result);
}
```

Output:
```
error[E0277]: cannot add `bool` to `i32`
```

## Related Errors

- [Variant Not Found]({{< relref "/languages/rust/variant-not-found" >}}) — wrong enum variant used.
- [Missing Field]({{< relref "/languages/rust/missing-field" >}}) — missing field in struct initialization.
- [Parse Int]({{< relref "/languages/rust/parse-int" >}}) — failing to parse a string as an integer.
