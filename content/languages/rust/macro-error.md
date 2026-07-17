---
title: "[Solution] Rust Macro Error / Invalid Token Tree — Compiler Error Fix"
description: "Fix Rust macro errors and invalid token tree issues. Understand macro syntax, token trees, and common macro compilation failures."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Macro Error / Invalid Token Tree

The error `macro error: invalid token tree` or `unexpected token` occurs when a Rust macro receives input that does not match any of its defined patterns, or when the macro syntax itself is invalid.

## Description

Rust macros operate on token trees — sequences of tokens grouped by brackets, parentheses, or braces. Macros defined with `macro_rules!` match against patterns of token trees. When the input doesn't match any pattern, or when the macro expansion produces invalid syntax, the compiler reports these errors.

Common issues include mismatched brackets, wrong repetition syntax, and proc-macro errors that produce invalid token streams.

## Common Causes

- **Mismatched delimiters** — parentheses, brackets, or braces not properly closed
- **Wrong repetition syntax** — incorrect use of `$()*` or `$()+` in macro rules
- **Invalid proc-macro output** — procedural macro generating tokens that don't form valid Rust
- **Missing comma or separator** — required separator missing between macro arguments

## How to Fix

### Fix 1: Check delimiter matching

```rust
// Wrong — unclosed parenthesis
macro_rules! bad {
    ($($x:expr),*) => {
        $(println!("{}", $x))*, // missing semicolon separator
    };
}

// Correct
macro_rules! good {
    ($($x:expr),*) => {
        $(println!("{}", $x));* // semicolon before *
    };
}
```

### Fix 2: Use correct repetition operators

```rust
// $()* — zero or more with optional separator
// $()+ — one or more with separator
macro_rules! make_vec {
    ($($x:expr),* $(,)?) => {
        vec![$($x),*]
    };
}

let v = make_vec![1, 2, 3,]; // trailing comma OK
```

### Fix 3: Debug macro expansion with cargo expand

```bash
cargo install cargo-expand
cargo expand my_module
```

### Fix 4: Validate proc-macro output

```rust
use proc_macro::TokenStream;

#[proc_macro]
pub fn my_macro(input: TokenStream) -> TokenStream {
    // Ensure output is valid Rust syntax
    "fn hello() { println!(\"hello\"); }".parse().unwrap()
}
```

## Examples

```rust
macro_rules! count {
    ($($x:expr),*) => {
        // Wrong: missing separator in repetition
        0 $(+ $x)*
    };
}

fn main() {
    let n = count![1, 2, 3];
    println!("{}", n);
}
```

Output:
```
error: local scope leaks into closure argument
```

## Related Errors

- [enum-match]({{< relref "/languages/rust/enum-match" >}}) — exhaustive pattern matching for enums.
- [variant-not-found]({{< relref "/languages/rust/variant-not-found" >}}) — missing enum variant in match.
- [type-mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — type errors in macro expansion.
