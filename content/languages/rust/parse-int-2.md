---
title: "[Solution] Rust Parse Int Error — Invalid Digit in String"
description: "Fix Rust parse int error. Learn why string to integer parsing fails and how to handle non-numeric characters and formatting issues."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Parse Int Error — Invalid Digit in String

An error with the message "invalid digit found in string" occurs when you try to parse a string into an integer but the string contains non-numeric characters.

## Description

Rust's `str::parse()` for integers expects only digits (0-9), an optional leading sign (`+` or `-`), and optionally a base prefix (`0x`, `0o`, `0b`). Any other character causes a `ParseIntError`.

Common scenarios:

- **Non-numeric characters** — `"abc"`, `"12.34"`.
- **Commas in numbers** — `"1,000"`.
- **Empty string** — `""`.
- **Whitespace** — `" 42 "`.
- **Hex without prefix** — `"ff"` instead of `"0xff"`.

## Common Causes

```rust
// Cause 1: Non-numeric characters
let n: i32 = "abc".parse()?;

// Cause 2: Decimal in integer
let n: i32 = "3.14".parse()?;

// Cause 3: Commas
let n: i32 = "1,000".parse()?;

// Cause 4: Empty string
let n: i32 = "".parse()?;

// Cause 5: Hex without prefix
let n: i32 = "ff".parse()?;
```

## Solutions

### Fix 1: Clean before parsing

```rust
let s = "1,000".replace(",", "");
let n: i32 = s.parse()?;

let n: i32 = " 42 ".trim().parse()?;
```

### Fix 2: Handle errors gracefully

```rust
fn parse_i32(s: &str) -> Option<i32> {
    s.trim().parse().ok()
}

fn main() {
    let inputs = vec!["42", "abc", "3.14", "1,000"];
    for input in inputs {
        match parse_i32(input) {
            Some(n) => println!("'{}' -> {}", input, n),
            None => println!("'{}' -> failed", input),
        }
    }
}
```

### Fix 3: Use from_str_radix for different bases

```rust
let n = i32::from_str_radix("ff", 16)?; // 255
let n = i32::from_str_radix("77", 8)?; // 63
let n = i32::from_str_radix("1010", 2)?; // 10
```

### Fix 4: Parse as float for decimals

```rust
let n: f64 = "3.14".parse()?; // works
let rounded: i32 = "3.14".parse::<f64>()?.round() as i32; // 3
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

- [Parse Float]({{< relref "/languages/rust/parse-float-2" >}}) — invalid float literal.
- [Type Mismatch]({{< relref "/languages/rust/type-mismatch-2" >}}) — wrong type in operations.
- [Unwrap Err]({{< relref "/languages/rust/unwrap-err-2" >}}) — panicking on parse failure.
