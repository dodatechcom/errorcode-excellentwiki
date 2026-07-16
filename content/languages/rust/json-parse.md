---
title: "[Solution] Rust JSON Parse Error — Invalid JSON Syntax"
description: "Fix Rust JSON parse error. Learn why JSON deserialization fails and how to handle invalid JSON with serde_json properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["json", "parse", "serde", "deserialization", "syntax"]
weight: 5
---

# JSON Parse Error — Invalid JSON Syntax

An error with the message "expected value at line X column Y" occurs when `serde_json` encounters invalid JSON syntax during parsing. The error includes the exact position where parsing failed.

## Description

JSON has strict syntax rules:

- Keys and string values must use double quotes (`"`).
- No trailing commas allowed.
- No comments allowed.
- Numbers must not have leading zeros (except `0.x`).
- `null`, `true`, `false` are lowercase.

Common scenarios:

- **Trailing commas** — `{"key": "value",}`.
- **Single quotes** — `{'key': 'value'}`.
- **Unquoted keys** — `{key: "value"}`.
- **Comments** — `// comment` or `/* comment */`.
- **YAML-style syntax** — using tabs or wrong delimiters.
- **Empty input** — parsing an empty string.

## Common Causes

```rust
use serde_json;

// Cause 1: Trailing comma
let json = r#"{"key": "value",}"#;
let _value: serde_json::Value = serde_json::from_str(json)?; // error

// Cause 2: Single quotes
let json = r"{'key': 'value'}";
let _value: serde_json::Value = serde_json::from_str(json)?; // error

// Cause 3: Unquoted keys
let json = r#"{key: "value"}"#;
let _value: serde_json::Value = serde_json::from_str(json)?; // error

// Cause 4: Empty string
let json = "";
let _value: serde_json::Value = serde_json::from_str(json)?; // error

// Cause 5: Python dict syntax
let json = r#"{"key": 'value'}"#; // single quotes on value
let _value: serde_json::Value = serde_json::from_str(json)?; // error
```

## Solutions

### Fix 1: Use valid JSON syntax

```rust
use serde_json;

// Wrong — trailing comma
let json = r#"{"key": "value",}"#;

// Correct — no trailing comma
let json = r#"{"key": "value"}"#;
let value: serde_json::Value = serde_json::from_str(json)?;
println!("{}", value);
```

### Fix 2: Handle parse errors gracefully

```rust
use serde_json::Value;

fn parse_json(s: &str) -> Result<Value, String> {
    serde_json::from_str(s).map_err(|e| {
        format!("JSON parse error at line {} column {}: {}",
            e.line(), e.column(), e)
    })
}

fn main() {
    let inputs = vec![
        r#"{"valid": true}"#,
        r#"{"invalid":,}"#,
        "",
        r#"{"missing": "quote}"#,
    ];

    for input in inputs {
        match parse_json(input) {
            Ok(value) => println!("Parsed: {}", value),
            Err(e) => println!("Error: {}", e),
        }
    }
}
```

### Fix 3: Use serde_json with lenient mode (via JSON5 or serde_json_lenient)

```rust
// For JSON with trailing comments or relaxed syntax,
// consider using a more lenient parser

use serde_json;

// Strict mode (default)
fn parse_strict(s: &str) -> Result<serde_json::Value, serde_json::Error> {
    serde_json::from_str(s)
}

// You can also preprocess the JSON string
fn remove_json_comments(s: &str) -> String {
    s.lines()
        .map(|line| {
            // Simple comment removal (not perfect for all cases)
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
    let json_with_comments = r#"{
        // This is a comment
        "key": "value"
    }"#;

    let cleaned = remove_json_comments(json_with_comments);
    match serde_json::from_str::<serde_json::Value>(&cleaned) {
        Ok(value) => println!("Parsed: {}", value),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

### Fix 4: Validate JSON before parsing

```rust
use serde_json::Value;

fn is_valid_json(s: &str) -> bool {
    serde_json::from_str::<Value>(s).is_ok()
}

fn validate_and_parse(s: &str) -> Result<Value, String> {
    if s.trim().is_empty() {
        return Err("empty input".to_string());
    }

    serde_json::from_str(s)
        .map_err(|e| format!("Invalid JSON: {}", e))
}

fn main() {
    let json = r#"{"name": "Alice", "age": 30}"#;

    if is_valid_json(json) {
        let value: Value = serde_json::from_str(json).unwrap();
        println!("Valid JSON: {}", value);
    } else {
        println!("Invalid JSON");
    }
}
```

## Examples

```rust
use serde_json::Value;

fn main() {
    let invalid_json = r#"{"name": "Alice",}"#;

    match serde_json::from_str::<Value>(invalid_json) {
        Ok(value) => println!("Parsed: {}", value),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: expected value at line 1 column 28
```

## Related Errors

- [Serde]({{< relref "/languages/rust/serde" >}}) — serde deserialization errors (schema mismatch).
- [Parse Int]({{< relref "/languages/rust/parse-int" >}}) — invalid integer in string.
- [Parse Float]({{< relref "/languages/rust/parse-float" >}}) — invalid float literal.
