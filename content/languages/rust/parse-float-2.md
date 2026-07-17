---
title: "[Solution] Rust Parse Float Error — Invalid Float Literal"
description: "Fix Rust parse float error. Learn why string to float parsing fails and how to handle commas, currency symbols, and special values."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Parse Float Error — Invalid Float Literal

An error with the message "invalid float literal" occurs when you try to parse a string into a floating-point number but the string doesn't conform to float syntax.

## Description

Rust's float parsing expects an optional sign, digits, an optional decimal point with digits, and an optional exponent. It also accepts `inf`, `-inf`, and `NaN` (case-sensitive).

Common scenarios:

- **Non-numeric characters** — `"abc"`, `"42px"`.
- **Multiple decimal points** — `"12.34.56"`.
- **Commas as separators** — `"1,000.50"`.
- **Currency symbols** — `"$10.99"`.
- **Empty string** — `""`.

## Common Causes

```rust
// Cause 1: Non-numeric characters
let n: f64 = "abc".parse()?;

// Cause 2: Multiple decimals
let n: f64 = "12.34.56".parse()?;

// Cause 3: Commas
let n: f64 = "1,000.50".parse()?;

// Cause 4: Currency symbols
let n: f64 = "$10.99".parse()?;

// Cause 5: Trailing characters
let n: f64 = "42px".parse()?;
```

## Solutions

### Fix 1: Strip non-numeric characters

```rust
let s = "$10.99".trim_start_matches(|c: char| !c.is_ascii_digit() && c != '.' && c != '-');
let n: f64 = s.parse()?;

let s = "1,234.56".replace(",", "");
let n: f64 = s.parse()?;
```

### Fix 2: Use parse with default

```rust
fn parse_f64(s: &str) -> f64 {
    s.trim().replace(",", "").parse().unwrap_or(0.0)
}

fn main() {
    let inputs = vec!["3.14", "abc", "1,000.5", "$10.99"];
    for input in inputs {
        println!("'{}' -> {}", input, parse_f64(input));
    }
}
```

### Fix 3: Handle special values

```rust
fn parse_float(s: &str) -> Option<f64> {
    match s.trim() {
        "inf" | "infinity" | "Infinity" => Some(f64::INFINITY),
        "-inf" | "-infinity" | "-Infinity" => Some(f64::NEG_INFINITY),
        "NaN" | "nan" => Some(f64::NAN),
        _ => s.parse().ok(),
    }
}
```

### Fix 4: Parse scientific notation

```rust
use std::str::FromStr;

let n = f64::from_str("1.23e4")?; // 12300
let n = f64::from_str("1.23E-4")?; // 0.000123
```

## Examples

```rust
fn main() {
    let input = "not a number";
    match input.parse::<f64>() {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: invalid float literal
```

## Related Errors

- [Parse Int]({{< relref "/languages/rust/parse-int-2" >}}) — invalid integer in string.
- [JSON Parse]({{< relref "/languages/rust/json-parse-2" >}}) — invalid JSON syntax.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch-2" >}}) — wrong type in operations.
