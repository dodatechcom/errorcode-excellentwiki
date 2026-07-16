---
title: "[Solution] Rust Parse Float Error — Invalid Float Literal"
description: "Fix Rust parse float error. Learn why string to float parsing fails and how to handle invalid float literals properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["parse", "float", "f64", "f32", "conversion", "decimal"]
weight: 5
---

# Parse Float Error — Invalid Float Literal

An error with the message "invalid float literal" occurs when you try to parse a string into a floating-point number (`f32` or `f64`) but the string doesn't conform to float syntax.

## Description

Rust's `str::parse()` for floats expects:

- An optional sign (`+` or `-`).
- Digits before the decimal point (can be empty if decimal follows).
- An optional decimal point with digits.
- An optional exponent (`e` or `E` followed by digits and optional sign).
- Optionally `inf` or `NaN` (case-sensitive).

Common scenarios:

- **Non-numeric characters** — `"abc"`, `"12.34.56"`.
- **Commas** — `"1,000.50"` (European-style decimals).
- **Currency symbols** — `"$10.99"`, `"€5.50"`.
- **Empty string** — `""`.
- **Wrong NaN casing** — `"nan"` instead of `"NaN"`.

## Common Causes

```rust
// Cause 1: Non-numeric characters
let n: f64 = "abc".parse()?; // invalid float

// Cause 2: Multiple decimal points
let n: f64 = "12.34.56".parse()?; // invalid float

// Cause 3: Commas as decimal separator
let n: f64 = "1.000,50".parse()?; // invalid float

// Cause 4: Currency symbols
let n: f64 = "$10.99".parse()?; // invalid float

// Cause 5: Trailing characters
let n: f64 = "42px".parse()?; // invalid float

// Cause 6: Empty string
let n: f64 = "".parse()?; // invalid float
```

## Solutions

### Fix 1: Clean the string before parsing

```rust
// Wrong
let n: f64 = "$10.99".parse()?;

// Correct — strip non-numeric characters
let s = "$10.99".trim_start_matches('$');
let n: f64 = s.parse()?;

// Handle commas
let s = "1,234.56".replace(",", "");
let n: f64 = s.parse()?;
```

### Fix 2: Use parse with default value

```rust
fn parse_f64(s: &str) -> f64 {
    s.trim()
        .replace(",", "")
        .parse()
        .unwrap_or(0.0)
}

fn main() {
    let inputs = vec!["3.14", "abc", "1,000.5", "$10.99"];
    for input in inputs {
        println!("'{}' -> {}", input, parse_f64(input));
    }
}
```

### Fix 3: Handle special float values

```rust
fn parse_float_special(s: &str) -> Option<f64> {
    let s = s.trim();
    match s {
        "inf" | "infinity" | "Infinity" => Some(f64::INFINITY),
        "-inf" | "-infinity" | "-Infinity" => Some(f64::NEG_INFINITY),
        "NaN" | "nan" => Some(f64::NAN),
        _ => s.parse().ok(),
    }
}

fn main() {
    let inputs = vec!["3.14", "inf", "NaN", "-infinity", "abc"];
    for input in inputs {
        match parse_float_special(input) {
            Some(v) => println!("'{}' -> {}", input, v),
            None => println!("'{}' -> parse failed", input),
        }
    }
}
```

### Fix 4: Parse with from_str for scientific notation

```rust
use std::str::FromStr;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let n = f64::from_str("1.23e4")?;
    println!("{}", n); // 12300

    let n = f64::from_str("1.23E-4")?;
    println!("{}", n); // 0.000123

    let n = f64::from_str("-5.5")?;
    println!("{}", n); // -5.5

    Ok(())
}
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

- [Parse Int]({{< relref "/languages/rust/parse-int" >}}) — invalid integer in string.
- [JSON Parse]({{< relref "/languages/rust/json-parse" >}}) — invalid JSON syntax.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong type in operations.
