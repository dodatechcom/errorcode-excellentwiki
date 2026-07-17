---
title: "[Solution] Rust Missing Lifetime Specifier — Lifetime Annotation Required"
description: "Fix Rust missing lifetime specifier error. Learn when the compiler needs lifetime annotations and how to add them correctly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Missing Lifetime Specifier — Lifetime Annotation Required

A compiler error with the message "missing lifetime specifier" occurs when the compiler cannot determine which input's lifetime a returned reference should be tied to.

## Description

Lifetimes ensure references never outlive their data. Most of the time the compiler infers lifetimes automatically. It requires explicit annotations when:

- A function returns a reference and takes two or more reference parameters.
- A struct holds a reference without a lifetime parameter.
- A trait object has ambiguous lifetime bounds.

The annotation syntax is `'a` — it tells the compiler "this reference lives at least as long as `'a`."

Common scenarios:

- **Two input references, one output** — compiler can't pick which one.
- **Struct with reference field** — struct needs a lifetime parameter.
- **Returning from match** — different branches reference different inputs.
- **Closures returning references** — ambiguous lifetime.

## Common Causes

```rust
// Cause 1: Two inputs, one output
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() { x } else { y }
} // Error: missing lifetime specifier

// Cause 2: Struct with reference
struct Wrapper {
    text: &str, // Error: missing lifetime
}

// Cause 3: Method returning ambiguous reference
struct Parser<'a> {
    input: &'a str,
}

impl<'a> Parser<'a> {
    fn pick(&self, other: &str) -> &str {
        if self.input.len() > other.len() { self.input } else { other }
    } // Error: missing lifetime
}

// Cause 4: Trait object lifetime
fn make_display() -> &dyn std::fmt::Display {
    &42 // Error: missing lifetime
}
```

## Solutions

### Fix 1: Add lifetime annotations

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let result;
    let s1 = String::from("long string");
    {
        let s2 = String::from("hi");
        result = longest(&s1, &s2);
        println!("Longest: {}", result);
    }
}
```

### Fix 2: Return owned values instead

```rust
fn longest(x: &str, y: &str) -> String {
    if x.len() > y.len() { x.to_string() } else { y.to_string() }
}

fn main() {
    let result = longest("hello", "hi");
    println!("Longest: {}", result);
}
```

### Fix 3: Use 'static for constant references

```rust
fn greeting() -> &'static str {
    "Hello, world!"
}

fn main() {
    println!("{}", greeting());
}
```

### Fix 4: Add lifetime to structs

```rust
struct Excerpt<'a> {
    text: &'a str,
}

fn main() {
    let novel = String::from("Call me Ishmael.");
    let excerpt = Excerpt {
        text: &novel[..15],
    };
    println!("{}", excerpt.text);
}
```

## Examples

```rust
fn first_or_second(a: &str, b: &str) -> &str {
    a
}

fn main() {
    let word = first_or_second("hello", "world");
    println!("{}", word);
}
```

Output:
```
error[E0106]: missing lifetime specifier
```

## Related Errors

- [Borrow Checker]({{< relref "/languages/rust/borrow-checker-2" >}}) — cannot borrow as mutable.
- [Clone]({{< relref "/languages/rust/clone-2" >}}) — value doesn't live long enough.
- [Move]({{< relref "/languages/rust/move-2" >}}) — using a value after it was moved.
