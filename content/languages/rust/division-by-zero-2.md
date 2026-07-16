---
title: "[Solution] Rust Division by Zero — Integer Division Panic"
description: "Fix Rust division by zero. Learn why dividing an integer by zero panics and how to use checked_div to handle it safely."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["division", "zero", "arithmetic", "panic", "checked"]
weight: 5
---

# Division by Zero — Integer Division Panic

A panic with the message "attempt to divide by zero" occurs when you perform integer division or modulo where the divisor is zero.

## Description

Rust panics on integer division by zero rather than producing undefined behavior (which is what happens in C/C++). The `/` and `%` operators both panic when the right-hand operand is zero for integer types. Floating-point division by zero produces `inf` or `NaN` instead of panicking, which can cause silent bugs.

Common scenarios:

- **User-supplied divisor** — user enters 0 when prompted for a divisor.
- **Empty collection length** — dividing by `vec.len()` when the vec is empty.
- **Ratio calculation** — computing a percentage of a zero total.
- **Modulo with zero** — `x % 0` also panics.

## Common Causes

```rust
// Cause 1: Divisor from user input
let divisor: i32 = input.trim().parse().unwrap();
let result = 100 / divisor; // panics if divisor is 0

// Cause 2: Division by collection length
let items: Vec<i32> = vec![];
let avg = items.iter().sum::<i32>() / items.len() as i32; // panic: len is 0

// Cause 3: Modulo by zero
let remainder = 42 % 0; // panic

// Cause 4: Divisor from computation
let index = 0;
let bucket = (100 / index) % 10; // panic
```

## Solutions

### Fix 1: Use checked_div

```rust
let a: i32 = 100;
let b: i32 = 0;

match a.checked_div(b) {
    Some(result) => println!("Result: {}", result),
    None => println!("Division by zero"),
}
```

### Fix 2: Guard with an explicit check

```rust
fn safe_divide(a: i32, b: i32) -> Option<i32> {
    if b == 0 {
        None
    } else {
        Some(a / b)
    }
}

fn main() {
    let result = safe_divide(10, 0);
    println!("{:?}", result); // None
}
```

### Fix 3: Use checked_rem for modulo

```rust
let a = 10;
let b = 0;

match a.checked_rem(b) {
    Some(r) => println!("Remainder: {}", r),
    None => println!("Modulo by zero"),
}
```

### Fix 4: Filter before dividing

```rust
let data = vec![10, 0, 5, 0, 2];
for (i, &denom) in data.iter().enumerate() {
    if denom != 0 {
        println!("100 / {}[{}] = {}", denom, i, 100 / denom);
    } else {
        println!("Skipping zero divisor at index {}", i);
    }
}
```

## Examples

```rust
fn main() {
    let numerator = 42;
    let denominator = 0;

    let quotient = numerator / denominator;
    println!("{} / {} = {}", numerator, denominator, quotient);
}
```

Output:
```
thread 'main' panicked at 'attempt to divide by zero'
```

## Related Errors

- [Overflow]({{< relref "/languages/rust/overflow" >}}) — arithmetic overflow in computations.
- [Unwrap None]({{< relref "/languages/rust/unwrap-none" >}}) — calling unwrap on a None from checked operations.
- [Index Out of Bounds]({{< relref "/languages/rust/index-out-of-bounds-2" >}}) — zero-length collection access.
