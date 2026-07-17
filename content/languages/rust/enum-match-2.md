---
title: "[Solution] Rust Non-Exhaustive Patterns — Match Not Complete"
description: "Fix Rust non-exhaustive patterns error. Learn why match expressions must be exhaustive and how to handle all enum variants."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Non-Exhaustive Patterns — Match Not Complete

A compiler error with the message "non-exhaustive patterns" occurs when a `match` expression doesn't handle all possible cases.

## Description

Rust's `match` must be exhaustive — every possible value of the matched expression must have a corresponding arm. This prevents bugs from unhandled cases. The compiler knows all variants of an enum, all values of a bool, and can compute which integer/char ranges are uncovered.

Common scenarios:

- **New enum variant added** — existing matches become incomplete.
- **Matching only some bool cases** — missing `true` or `false`.
- **Integer ranges with gaps** — not all values covered.
- **Nested enums** — inner enum not fully matched.

## Common Causes

```rust
enum Season { Spring, Summer, Autumn, Winter }

// Cause 1: Missing variant
let s = Season::Spring;
match s {
    Season::Spring => println!("Planting"),
    Season::Summer => println!("Growing"),
    // Error: Autumn, Winter not covered
}

// Cause 2: Missing bool case
let flag = true;
match flag {
    true => println!("Yes"),
    // Error: false not covered
}

// Cause 3: Integer range gap
let n: u8 = 5;
match n {
    0..=4 => println!("Low"),
    6..=10 => println!("High"),
    // Error: 5 not covered
}
```

## Solutions

### Fix 1: Cover all variants

```rust
match s {
    Season::Spring => println!("Planting"),
    Season::Summer => println!("Growing"),
    Season::Autumn => println!("Harvesting"),
    Season::Winter => println!("Resting"),
}
```

### Fix 2: Use wildcard for remaining cases

```rust
match s {
    Season::Spring => println!("Planting"),
    _ => println!("Not planting"),
}
```

### Fix 3: Use if let for single-case

```rust
if let Season::Spring = s {
    println!("Time to plant!");
}
```

### Fix 4: Use exhaustive integer ranges

```rust
let n: u8 = 5;
match n {
    0..=4 => println!("Low"),
    5 => println!("Medium"),
    6..=10 => println!("High"),
    _ => println!("Other"),
}
```

## Examples

```rust
enum Day { Mon, Tue, Wed, Thu, Fri, Sat, Sun }

fn main() {
    let day = Day::Mon;
    match day {
        Day::Mon => println!("Monday"),
        Day::Fri => println!("Friday"),
    }
}
```

Output:
```
error[E0004]: non-exhaustive patterns: `Tue`, `Wed`, `Thu`, `Sat`, `Sun` not covered
```

## Related Errors

- [Variant Not Found]({{< relref "/languages/rust/variant-not-found-2" >}}) — referencing a variant that doesn't exist.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch-2" >}}) — wrong type in match arms.
- [Borrow Checker]({{< relref "/languages/rust/borrow-checker-2" >}}) — borrowing issues in match.
