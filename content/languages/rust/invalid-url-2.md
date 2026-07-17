---
title: "[Solution] Rust Invalid URL — URL Parsing Error"
description: "Fix Rust invalid URL error. Learn why URL parsing fails with invalid characters and how to properly encode and construct URLs."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Invalid URL — URL Parsing Error

An error with the message "invalid URL character" occurs when you try to parse a string that doesn't conform to URL syntax.

## Description

URLs have strict rules (RFC 3986). Valid URLs need a valid scheme, valid characters in each component, and proper percent-encoding for special characters. Spaces, braces, pipes, and other special characters are not allowed unencoded.

Common scenarios:

- **Spaces in URL** — `http://example.com/my page`.
- **Invalid characters** — `{`, `}`, `|`, `\`, `^` in URL.
- **Missing scheme** — `example.com/path` instead of `http://example.com/path`.
- **Malformed port** — `http://example.com:abc`.
- **Invalid percent-encoding** — `%zz`.

## Common Causes

```rust
use url::Url;

// Cause 1: Spaces
let url: Url = "http://example.com/my page".parse()?;

// Cause 2: Invalid characters
let url: Url = "http://example.com/path?q=hello world".parse()?;

// Cause 3: Missing scheme
let url: Url = "example.com/path".parse()?; // parsed as path

// Cause 4: Malformed port
let url: Url = "http://example.com:notaport".parse()?;

// Cause 5: Invalid percent-encoding
let url: Url = "http://example.com/path%zz".parse()?;
```

## Solutions

### Fix 1: Use proper percent-encoding

```rust
use url::Url;

let url = Url::parse("http://example.com")?;
let mut url = url;
url.set_path("my page"); // auto-encodes
println!("{}", url); // http://example.com/my%20page
```

### Fix 2: Use base URL for relative paths

```rust
use url::Url;

let base = Url::parse("http://example.com")?;
let url = base.join("path/to/page")?;
println!("{}", url); // http://example.com/path/to/page
```

### Fix 3: Validate before using

```rust
fn validate_url(s: &str) -> Result<String, String> {
    let url = Url::parse(s).map_err(|e| format!("Invalid URL: {}", e))?;
    if url.scheme().is_empty() {
        return Err("Must have a scheme".into());
    }
    if url.host_str().is_none() {
        return Err("Must have a host".into());
    }
    Ok(url.to_string())
}

fn main() {
    let urls = vec![
        "http://example.com/path",
        "not a url",
        "ftp://files.example.com",
    ];
    for url in urls {
        match validate_url(url) {
            Ok(valid) => println!("Valid: {}", valid),
            Err(e) => println!("Invalid: {}", e),
        }
    }
}
```

### Fix 4: Encode special characters manually

```rust
fn encode_path(s: &str) -> String {
    s.bytes().map(|b| match b {
        b'A'..=b'Z' | b'a'..=b'z' | b'0'..=b'9' | b'-' | b'_' | b'.' | b'~' | b'/' => {
            (b as char).to_string()
        }
        _ => format!("%{:02X}", b),
    }).collect()
}

fn main() {
    let path = encode_path("hello world/test");
    println!("{}", path); // hello%20world%2Ftest
}
```

## Examples

```rust
use url::Url;

fn main() {
    match "http://example.com/my page".parse::<Url>() {
        Ok(url) => println!("Parsed: {}", url),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: invalid URL character
```

## Related Errors

- [JSON Parse]({{< relref "/languages/rust/json-parse-2" >}}) — invalid JSON syntax.
- [Parse Int]({{< relref "/languages/rust/parse-int-2" >}}) — invalid integer in string.
- [Reqwest]({{< relref "/languages/rust/reqwest-2" >}}) — HTTP request errors.
