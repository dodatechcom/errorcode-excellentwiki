---
title: "[Solution] Rust JSON Parse Error — Invalid JSON Syntax"
description: "Fix Rust JSON parse error. Learn why serde_json fails with 'expected value' and how to validate and fix JSON input."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# JSON Parse Error — Invalid JSON Syntax

An error with the message "expected value at line X column Y" occurs when `serde_json` encounters invalid JSON syntax during parsing.

## Description

JSON has strict syntax rules: double-quoted keys/strings, no trailing commas, no comments, lowercase `null`/`true`/`false`, and numbers without leading zeros. `serde_json` provides exact line/column for the error.

Common scenarios:

- **Trailing commas** — `{"key": "value",}`.
- **Single quotes** — `{'key': 'value'}`.
- **Unquoted keys** — `{key: "value"}`.
- **Comments** — `// comment` or `/* comment */`.
- **Empty input** — parsing an empty string.

## Common Causes

```rust
use serde_json;

// Cause 1: Trailing comma
let json = r#"{"key": "value",}"#;
let _: serde_json::Value = serde_json::from_str(json)?;

// Cause 2: Single quotes
let json = r"{'key': 'value'}";
let _: serde_json::Value = serde_json::from_str(json)?;

// Cause 3: Unquoted keys
let json = r#"{key: "value"}"#;
let _: serde_json::Value = serde_json::from_str(json)?;

// Cause 4: Empty string
let _: serde_json::Value = serde_json::from_str("")?;

// Cause 5: Comments
let json = r#"{
    // this is a comment
    "key": "value"
}"#;
let _: serde_json::Value = serde_json::from_str(json)?;
```

## Solutions

### Fix 1: Use valid JSON syntax

```rust
use serde_json;

// Wrong: trailing comma
let json = r#"{"key": "value",}"#;

// Correct
let json = r#"{"key": "value"}"#;
let value: serde_json::Value = serde_json::from_str(json)?;
```

### Fix 2: Handle parse errors with context

```rust
use serde_json::Value;

fn parse_json(s: &str) -> Result<Value, String> {
    serde_json::from_str(s).map_err(|e| {
        format!("JSON error at line {} column {}: {}", e.line(), e.column(), e)
    })
}

fn main() {
    let inputs = vec![
        r#"{"valid": true}"#,
        r#"{"invalid":,}"#,
        "",
    ];
    for input in inputs {
        match parse_json(input) {
            Ok(v) => println!("Parsed: {}", v),
            Err(e) => println!("Error: {}", e),
        }
    }
}
```

### Fix 3: Preprocess to remove comments

```rust
fn strip_comments(s: &str) -> String {
    s.lines()
        .map(|line| {
            if let Some(pos) = line.find("//") {
                &line[..pos]
            } else {
                line
            }
        })
        .collect::<Vec<_>>()
        .join("\n")
}

fn main() {
    let json = r#"{
        // comment
        "key": "value"
    }"#;
    let cleaned = strip_comments(json);
    let value: serde_json::Value = serde_json::from_str(&cleaned).unwrap();
    println!("{}", value);
}
```

### Fix 4: Validate before parsing

```rust
use serde_json::Value;

fn is_valid_json(s: &str) -> bool {
    serde_json::from_str::<Value>(s).is_ok()
}

fn main() {
    let json = r#"{"name": "Alice"}"#;
    println!("Valid: {}", is_valid_json(json));
    println!("Invalid: {}", is_valid_json(r#"{"name": }"#));
}
```

## Examples

```rust
use serde_json::Value;

fn main() {
    let invalid = r#"{"name": "Alice",}"#;
    match serde_json::from_str::<Value>(invalid) {
        Ok(v) => println!("Parsed: {}", v),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: expected value at line 1 column 28
```

## Related Errors

- [Serde]({{< relref "/languages/rust/serde-2" >}}) — schema mismatch during deserialization.
- [Parse Int]({{< relref "/languages/rust/parse-int-2" >}}) — invalid integer in string.
- [Parse Float]({{< relref "/languages/rust/parse-float-2" >}}) — invalid float literal.
