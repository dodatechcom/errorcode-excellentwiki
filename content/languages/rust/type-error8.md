---
title: "[Solution] Rust Mismatched Types / Expected X Found Y — Compiler Error Fix"
description: "Fix Rust type mismatch errors. Understand type inference, coercion, and how to resolve 'expected X found Y' compiler messages."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Mismatched Types / Expected X Found Y

The error `mismatched types: expected X, found Y` occurs when you provide a value of one type where the compiler expects a different type. Rust is statically typed and does not perform implicit type conversions (except for a few safe coercions).

## Description

Rust's strong type system requires explicit type compatibility. The compiler infers types from context, but when two incompatible types are used in the same position, it produces a clear error message showing what was expected and what was found.

This covers a wide range of issues: wrong function argument types, incorrect return types, type annotation mismatches, and failed implicit coercions.

## Common Causes

- **Wrong function argument type** — passing `i32` where `f64` is expected
- **Incorrect return type** — returning `String` from a function declared to return `&str`
- **Type annotation mismatch** — explicit type annotation conflicts with the actual value
- **Numeric type confusion** — using `32` (i32) where `32.0` (f64) is expected

## How to Fix

### Fix 1: Use explicit type conversion

```rust
let x: i32 = 5;
let y: f64 = x as f64; // explicit cast
```

### Fix 2: Match the expected type

```rust
// Wrong
fn add(a: f64, b: f64) -> f64 { a + b }
let result = add(5, 10); // Error: expected f64, found i32

// Correct
let result = add(5.0, 10.0);
```

### Fix 3: Use From/Into for safe conversions

```rust
let s = String::from("hello");
let v: Vec<u8> = s.into(); // String -> Vec<u8>

let x: i64 = 42i32.into(); // i32 -> i64
```

### Fix 4: Remove or fix type annotations

```rust
// Wrong — annotation conflicts
let x: u32 = -1; // Error: expected u32, found i32

// Correct — let compiler infer or use correct type
let x: i32 = -1;
```

## Examples

```rust
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

fn main() {
    let x: i32 = 42;
    let greeting = greet(x); // Error: expected &str, found i32
    println!("{}", greeting);
}
```

Output:
```
error[E0308]: mismatched types
  --> src/main.rs:7:22
   |
7  |     let greeting = greet(x);
   |                    ----- ^ expected `&str`, found `i32`
   |                    |
   |                    arguments to this function are incorrect
```

## Related Errors

- [trait-error]({{< relref "/languages/rust/trait-error" >}}) — trait not implemented for a type.
- [serde]({{< relref "/languages/rust/serde" >}}) — serialization/deserialization type mismatches.
- [parse-int]({{< relref "/languages/rust/parse-int" >}}) — string-to-integer parsing failures.
