---
title: "[Solution] Rust Parse Int Error — Invalid Digit in String"
description: "Fix Rust parse int error. Learn why string to integer parsing fails and how to handle invalid digits properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["parse", "int", "integer", "digit", "conversion"]
weight: 5
---

# Parse Int Error — Invalid Digit in String

An error with the message "invalid digit found in string" occurs when you try to parse a string into an integer but the string contains characters that aren't valid digits (or sign characters).

## Description

Rust's `str::parse()` method converts strings to numeric types. For integers, the string must contain only digits (0-9), an optional leading sign (`+` or `-`), and optionally a prefix (`0x` for hex, `0o` for octal, `0b` for binary). Any other character causes a `ParseIntError`.

Common scenarios:

- **Non-numeric characters** — `"abc"`, `"12.34"`, `"1,000"`.
- **Empty string** — `""`.
- **Whitespace** — `" 42 "` (leading/trailing spaces).
- **Overflow** — number too large for the target type.
- **Hex/octal without prefix** — `"ff"` instead of `"0xff"`.

## Common Causes

```rust
// Cause 1: Non-numeric characters
let n: i32 = "abc".parse()?; // invalid digit

// Cause 2: Decimal point in integer
let n: i32 = "3.14".parse()?; // invalid digit '.'

// Cause 3: Commas in number
let n: i32 = "1,000".parse()?; // invalid digit ','

// Cause 4: Empty string
let n: i32 = "".parse()?; // invalid digit

// Cause 5: Hex without prefix
let n: i32 = "ff".parse()?; // invalid digit 'f'

// Cause 6: Leading/trailing whitespace
let n: i32 = " 42 ".parse()?; // may fail depending on method
```

## Solutions

### Fix 1: Clean the string before parsing

```rust
// Wrong
let n: i32 = "1,000".parse()?;

// Correct — remove commas
let s = "1,000".replace(",", "");
let n: i32 = s.parse()?;

// Or use trim for whitespace
let n: i32 = " 42 ".trim().parse()?;
```

### Fix 2: Handle parse errors gracefully

```rust
fn parse_i32(s: &str) -> Option<i32> {
    s.trim().parse().ok()
}

fn main() {
    let inputs = vec!["42", "abc", "3.14", "1,000", "0xff"];

    for input in inputs {
        match parse_i32(input) {
            Some(n) => println!("Parsed '{}' as {}", input, n),
            None => println!("Failed to parse '{}'", input),
        }
    }
}
```

### Fix 3: Use from_str_radix for different bases

```rust
use std::i32;

// Wrong — hex without prefix
let n: i32 = "ff".parse()?;

// Correct — specify radix
let n = i32::from_str_radix("ff", 16)?;
println!("{}", n); // 255

let n = i32::from_str_radix("77", 8)?;
println!("{}", n); // 63

let n = i32::from_str_radix("1010", 2)?;
println!("{}", n); // 10
```

### Fix 4: Parse floats with from_str for decimal numbers

```rust
// Wrong — trying to parse decimal as integer
let n: i32 = "3.14".parse()?;

// Correct — parse as float
let n: f64 = "3.14".parse()?;
println!("{}", n); // 3.14

// Or round to integer
let n: i32 = "3.14".parse::<f64>()?.round() as i32;
println!("{}", n); // 3
```

## Examples

```rust
fn main() {
    let input = "not a number";

    match input.parse::<i32>() {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: invalid digit found in string
```

## Related Errors

- [Parse Float]({{< relref "/languages/rust/parse-float" >}}) — invalid float literal.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch" >}}) — wrong type in operations.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err" >}}) — panicking on parse failure.
