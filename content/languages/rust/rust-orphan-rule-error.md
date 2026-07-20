---
title: "[Solution] Rust Orphan Rule Error — How to Fix"
description: "Fix orphan rule errors. Resolve trait implementation restrictions for foreign types and traits."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Orphan Rule Error

Orphan rule errors occur when trying to implement a trait for a type where neither the trait nor the type is defined in the current crate — violating Rust's coherence rules.

## Common Causes

```rust
use std::fmt::Display;

// Cannot implement Display for Vec<i32> (both foreign)
impl Display for Vec<i32> { // ERROR: orphan rule
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result { write!(f, "vec") }
}

// Cannot implement From<String> for your type in some cases
// Cannot implement a foreign trait for a foreign type
impl From<String> for Vec<u8> { // ERROR: both String and Vec are foreign
    fn from(s: String) -> Self { s.into_bytes() }
}
```

## How to Fix

1. **Use the newtype pattern**

```rust
use std::fmt;

struct MyVec(Vec<i32>);

impl fmt::Display for MyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let strs: Vec<String> = self.0.iter().map(|x| x.to_string()).collect();
        write!(f, "[{}]", strs.join(", "))
    }
}

fn main() {
    let v = MyVec(vec![1, 2, 3]);
    println!("{}", v);
}
```

2. **Implement your own traits for foreign types using extension traits**

```rust
trait VecExt {
    fn sum_all(&self) -> i32;
}

impl VecExt for Vec<i32> {
    fn sum_all(&self) -> i32 {
        self.iter().sum()
    }
}

fn main() {
    let v = vec![1, 2, 3];
    println!("Sum: {}", v.sum_all());
}
```

3. **Use blanket implementations carefully**

```rust
trait Convert {
    type Output;
    fn convert(&self) -> Self::Output;
}

impl Convert for i32 { type Output = String; fn convert(&self) -> String { self.to_string() } }
impl Convert for f64 { type Output = String; fn convert(&self) -> String { format!("{:.2}", self) } }
impl Convert for bool { type Output = String; fn convert(&self) -> String { self.to_string() } }
```

## Examples

```rust
use std::fmt;

// Newtype pattern
struct Celsius(f64);
struct Fahrenheit(f64);

impl fmt::Display for Celsius {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result { write!(f, "{:.1}°C", self.0) }
}

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self { Fahrenheit(c.0 * 9.0 / 5.0 + 32.0) }
}

fn main() {
    let boiling = Celsius(100.0);
    println!("Boiling point: {}", boiling);
    let f: Fahrenheit = boiling.into();
    println!("In Fahrenheit: {:.1}°F", f.0);
}
```

## Related Errors

- [Blanket Impl Error]({{< relref "/languages/rust/rust-blanket-impl-error" >}}) — blanket implementations
- [Derive Error]({{< relref "/languages/rust/rust-derive-error" >}}) — derive macros
- [Trait Object Error]({{< relref "/languages/rust/rust-trait-object-error" >}}) — trait objects
