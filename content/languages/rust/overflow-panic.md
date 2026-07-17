---
title: "[Solution] Rust Arithmetic Operation Overflowed — Panic Fix"
description: "Fix Rust arithmetic overflow panics. Use checked, wrapping, and saturating arithmetic operations to handle overflow safely."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Arithmetic Operation Overflowed — Panic

The error `attempt to add with overflow` (or multiply, subtract, divide) occurs when an arithmetic operation produces a value that exceeds the range of the integer type. In debug builds, Rust panics on overflow; in release builds, it wraps by default.

## Description

Rust's integer types have fixed ranges (e.g., `u8`: 0–255, `i32`: −2,147,483,648 to 2,147,483,647). Operations that produce values outside these ranges overflow. Debug mode catches this with a panic to help identify bugs early. Release mode silently wraps around by default.

Understanding overflow behavior is critical for security-sensitive code, counters, and any computation where unexpected wraparound could cause bugs.

## Common Causes

- **Unbounded counters** — incrementing past the type's maximum value
- **Unchecked user input** — parsing external data without validating range
- **Chain of operations** — intermediate results overflow before the final computation
- **Debug vs release behavior difference** — code works in debug but wraps in release

## How to Fix

### Fix 1: Use checked arithmetic

```rust
let a: u32 = u32::MAX;
let b: u32 = 1;

match a.checked_add(b) {
    Some(result) => println!("result: {}", result),
    None => println!("overflow detected!"),
}
```

### Fix 2: Use wrapping arithmetic for intentional wraparound

```rust
let a: u8 = 255;
let b: u8 = 1;
let result = a.wrapping_add(b); // result = 0
println!("{}", result);
```

### Fix 3: Use saturating arithmetic to clamp at bounds

```rust
let a: u8 = 255;
let b: u8 = 1;
let result = a.saturating_add(b); // result = 255
println!("{}", result);
```

### Fix 4: Use larger types for intermediate calculations

```rust
// Wrong — i8 overflows
let x: i8 = 100;
let y: i8 = 100;
let z = x + y; // overflow in debug

// Correct — use i32 for intermediate
let z = (x as i32) + (y as i32); // 200, fits in i32
```

## Examples

```rust
fn main() {
    let x: u8 = 200;
    let y: u8 = 200;
    let result = x + y; // overflow!
    println!("{}", result);
}
```

Output (debug mode):
```
thread 'main' panicked at 'attempt to add with overflow'
```

## Related Errors

- [overflow]({{< relref "/languages/rust/overflow" >}}) — general overflow handling patterns.
- [unwrap-none]({{< relref "/languages/rust/unwrap-none" >}}) — unwrap panics on Option/Result.
- [bounds-panic]({{< relref "/languages/rust/index-out-of-bounds" >}}) — index out of bounds panic.
