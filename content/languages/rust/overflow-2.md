---
title: "[Solution] Rust Arithmetic Overflow — Overflowed Value Computation"
description: "Fix Rust arithmetic overflow panic. Learn why integer overflow panics in debug builds and how to use wrapping, saturating, and checked arithmetic."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Arithmetic Overflow — Overflowed Value Computation

A panic with the message "attempt to compute an overflowed value" occurs when an arithmetic operation exceeds the representable range of the integer type in debug mode.

## Description

Rust checks for integer overflow in debug builds by default, converting undefined behavior into a predictable panic. In release builds, overflow wraps silently (two's complement). This means code that works in release may panic in debug, which catches bugs during development.

Operations that can overflow include addition, subtraction, multiplication, left shift, and negation. Bitwise operations (`&`, `|`, `^`) and right shifts do not overflow.

Common scenarios:

- **Summing many values** — accumulating into a type too small for the result.
- **Left shifting by too many bits** — shifting `1u8 << 8`.
- **Negating the minimum value** — `-i8::MIN` overflows.
- **Multiplying large factors** — `100_000i32 * 100_000i32`.

## Common Causes

```rust
// Cause 1: Addition overflow
let a: u8 = 200;
let b: u8 = 100;
let sum = a + b; // panic: 300 > 255

// Cause 2: Subtraction underflow
let a: u8 = 5;
let b: u8 = 10;
let diff = a - b; // panic: wraps to huge number

// Cause 3: Multiplication overflow
let a: i16 = 500;
let product = a * a; // 250000 > 32767

// Cause 4: Left shift overflow
let x: u8 = 1;
let shifted = x << 8; // panic: shift by 8 on 8-bit type

// Cause 5: Negation overflow
let x: i8 = -128;
let negated = -x; // panic: 128 > 127
```

## Solutions

### Fix 1: Use saturating arithmetic

```rust
let a: u8 = 200;
let b: u8 = 100;
let sum = a.saturating_add(b); // 255 (clamped to max)
println!("{}", sum);
```

### Fix 2: Use wrapping arithmetic

```rust
let a: u8 = 200;
let b: u8 = 100;
let sum = a.wrapping_add(b); // 44 (wraps around)
println!("{}", sum);
```

### Fix 3: Use checked arithmetic with Option

```rust
let a: i16 = 500;
let product = a.checked_mul(a);
match product {
    Some(v) => println!("Product: {}", v),
    None => println!("Overflow detected"),
}
```

### Fix 4: Use wider types for intermediate results

```rust
let a: i16 = 500;
let b: i16 = 500;
let product = (a as i32) * (b as i32); // no overflow
println!("{}", product); // 250000
```

## Examples

```rust
fn main() {
    let x: u8 = 150;
    let y: u8 = 200;

    let result = x + y;
    println!("{} + {} = {}", x, y, result);
}
```

Output (debug mode):
```
thread 'main' panicked at 'attempt to compute an overflowed value'
```

## Related Errors

- [Division by Zero]({{< relref "/languages/rust/division-by-zero-2" >}}) — dividing by zero.
- [Stack Overflow]({{< relref "/languages/rust/stack-overflow" >}}) — stack memory exhaustion from recursion.
- [Out of Memory]({{< relref "/languages/rust/out-of-memory" >}}) — heap allocation failure.
