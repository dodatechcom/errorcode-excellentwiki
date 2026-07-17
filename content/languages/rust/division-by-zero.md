---
title: "[Solution] Rust Division by Zero — Attempt to Divide by Zero"
description: "Fix Rust division by zero panic. Learn why integer division by zero panics and how to handle it safely with checked arithmetic."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Division by Zero — Attempt to Divide by Zero

A panic with the message "attempt to divide by zero" occurs when you divide an integer by zero. Unlike floating-point division which produces `inf` or `NaN`, integer division by zero always panics in Rust.

## Description

Rust distinguishes between integer and floating-point division. Integer division (`/`) by zero causes an immediate panic. Float division by zero produces `inf`, `-inf`, or `NaN` depending on the numerator, which may cause subtle bugs rather than crashes. The modulo operator (`%`) also panics when the divisor is zero.

Common scenarios:

- **Direct division by zero** — `x / 0`.
- **Divisor computed from data** — the divisor happens to be zero at runtime.
- **User input** — entering zero when prompted for a divisor.
- **Modulo by zero** — `x % 0`.
- **Index calculation** — dividing to compute an array index.

## Common Causes

```rust
// Cause 1: Direct division by zero
let result = 10 / 0; // panic: attempt to divide by zero

// Cause 2: Divisor from user input
let divisor: i32 = input.parse().unwrap();
let result = 100 / divisor; // panics if divisor is 0

// Cause 3: Modulo by zero
let remainder = 10 % 0; // panic: attempt to calculate the remainder with a divisor of zero

// Cause 4: Divisor from computation
let numbers = vec![10, 20, 0, 30];
for n in numbers {
    let result = 100 / n; // panics when n is 0
}

// Cause 5: Index calculation
let len = 0;
let index = 10 / len; // panic: attempt to divide by zero
```

## Solutions

### Fix 1: Check divisor before dividing

```rust
// Wrong
fn divide(a: i32, b: i32) -> i32 {
    a / b
}

// Correct
fn divide(a: i32, b: i32) -> Option<i32> {
    if b == 0 {
        None
    } else {
        Some(a / b)
    }
}
```

### Fix 2: Use checked_div for safe division

```rust
// Wrong
let result = 100 / divisor;

// Correct
let result = 100_i32.checked_div(divisor);
match result {
    Some(v) => println!("Result: {}", v),
    None => println!("Division by zero or overflow"),
}
```

### Fix 3: Filter out zero values before dividing

```rust
// Wrong
let numbers = vec![10, 20, 0, 30];
for n in numbers {
    let result = 100 / n; // panics on 0
}

// Correct
let numbers = vec![10, 20, 0, 30];
for n in numbers {
    if n != 0 {
        let result = 100 / n;
        println!("100 / {} = {}", n, result);
    } else {
        println!("Skipping zero divisor");
    }
}
```

### Fix 4: Use floating-point for division that may encounter zero

```rust
// Wrong
let result = 100_f64 / 0.0; // Produces inf, not a panic, but may cause bugs

// Better — explicit check
fn safe_divide(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 {
        None
    } else {
        Some(a / b)
    }
}
```

## Examples

```rust
fn main() {
    let a = 10;
    let b = 0;

    // This panics
    let result = a / b;
    println!("Result: {}", result);
}
```

Output:
```
thread 'main' panicked at 'attempt to divide by zero'
```

## Related Errors

- [Overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow in computations.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong types in arithmetic operations.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none" >}}) — calling unwrap on a None from checked operations.
