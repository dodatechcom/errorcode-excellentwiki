---
title: "[Solution] Rust Non-Exhaustive Patterns — Enum Match Error"
description: "Fix Rust non-exhaustive patterns error. Learn why Rust requires exhaustive match expressions and how to handle all enum variants."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Non-Exhaustive Patterns — Enum Match Error

A compiler error with the message "non-exhaustive patterns" occurs when a `match` expression doesn't cover all possible cases. Rust requires match expressions to be exhaustive — every possible value must be handled.

## Description

Rust's `match` expression must handle every possible variant or value. This prevents bugs where you forget to handle a case. The error appears when:

- Not all enum variants are covered in a match.
- Not all possible integer or char values are covered.
- A wildcard `_` arm is missing and not all cases are handled.

Exhaustive matching is one of Rust's key safety features — the compiler ensures you've considered every possibility.

Common scenarios:

- **Adding a new enum variant** — existing matches become non-exhaustive.
- **Matching on primitives** — not covering all values of `bool`, `char`, etc.
- **Nested enums** — inner enum variants not fully matched.
- **Using guards** — match arms with guards may not cover all cases.

## Common Causes

```rust
// Cause 1: Missing enum variant
enum Color {
    Red,
    Green,
    Blue,
}

let c = Color::Red;
match c {
    Color::Red => println!("Red"),
    Color::Green => println!("Green"),
    // Error: missing `Blue`
}

// Cause 2: Missing bool case
let flag = true;
match flag {
    true => println!("Yes"),
    // Error: missing `false` case
}

// Cause 3: Missing integer range
let num: u8 = 5;
match num {
    0..=4 => println!("Low"),
    6..=10 => println!("High"),
    // Error: missing 5
}

// Cause 4: Nested enum not fully matched
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

let s = Shape::Circle(5.0);
match s {
    Shape::Circle(r) => println!("Circle: {}", r),
    // Error: missing `Rectangle`
}
```

## Solutions

### Fix 1: Cover all enum variants

```rust
// Wrong
enum Color {
    Red,
    Green,
    Blue,
}

match c {
    Color::Red => println!("Red"),
    Color::Green => println!("Green"),
}

// Correct
match c {
    Color::Red => println!("Red"),
    Color::Green => println!("Green"),
    Color::Blue => println!("Blue"),
}
```

### Fix 2: Use a wildcard arm for remaining cases

```rust
// Wrong
match c {
    Color::Red => println!("Red"),
    Color::Green => println!("Green"),
}

// Correct
match c {
    Color::Red => println!("Red"),
    Color::Green => println!("Green"),
    _ => println!("Other color"),
}
```

### Fix 3: Use `if let` for single-case matching

```rust
enum Color {
    Red,
    Green,
    Blue,
}

// If you only care about one variant
if let Color::Red = c {
    println!("It's red!");
}
```

### Fix 4: Use exhaustive ranges for integers

```rust
let num: u8 = 5;

// Wrong
match num {
    0..=4 => println!("Low"),
    6..=10 => println!("High"),
}

// Correct
match num {
    0..=4 => println!("Low"),
    5 => println!("Middle"),
    6..=10 => println!("High"),
    _ => println!("Other"),
}
```

## Examples

```rust
enum Day {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

fn main() {
    let day = Day::Monday;

    match day {
        Day::Monday => println!("Start of work week"),
        Day::Friday => println!("End of work week"),
        // Error: non-exhaustive patterns: `Tuesday`, `Wednesday`,
        // `Thursday`, `Saturday`, `Sunday` not covered
    }
}
```

Output:
```
error[E0004]: non-exhaustive patterns: `Tuesday`, `Wednesday`, `Thursday`, `Saturday`, `Sunday` not covered
```

## Related Errors

- [Variant Not Found]({{< relref "/languages/rust/variant-not-found" >}}) — referencing a variant that doesn't exist.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong type in match arms.
- [Borrow Checker]({{< relref "/languages/rust/borrow-checker" >}}) — borrowing issues in match expressions.
