---
title: "[Solution] Rust Invalid URL — URL Parsing Error"
description: "Fix Rust invalid URL error. Learn why URL parsing fails and how to construct and validate URLs properly in Rust."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Invalid URL — URL Parsing Error

An error with the message "invalid URL character" or "invalid URL" occurs when you try to parse a string that doesn't conform to URL syntax. This typically happens with malformed URLs or URLs containing illegal characters.

## Description

URLs have strict syntax rules defined by RFC 3986. A valid URL must have:

- A valid scheme (`http`, `https`, `ftp`, etc.).
- Valid characters in each component.
- Proper percent-encoding for special characters.
- Correct delimiter placement (`://`, `?`, `#`, etc.).

Common scenarios:

- **Spaces in URL** — `http://example.com/my page` (should be `%20`).
- **Invalid characters** — `{`, `}`, `|`, `\`, `^`, `` ` `` in URL.
- **Missing scheme** — `example.com/path` (no `http://`).
- **Malformed port** — `http://example.com:abc`.
- **Unclosed brackets** — `http://example.com/path[`.

## Common Causes

```rust
use url::Url;

// Cause 1: Spaces in URL
let url: Url = "http://example.com/my page".parse()?; // invalid

// Cause 2: Invalid characters
let url: Url = "http://example.com/path?q=hello world".parse()?; // invalid

// Cause 3: Missing scheme
let url: Url = "example.com/path".parse()?; // treated as path, not URL

// Cause 4: Malformed port
let url: Url = "http://example.com:notaport".parse()?; // invalid port

// Cause 5: Invalid percent-encoding
let url: Url = "http://example.com/path%zz".parse()?; // invalid encoding
```

## Solutions

### Fix 1: Use proper URL encoding

```rust
use url::Url;

// Wrong — space in URL
let url: Url = "http://example.com/my page".parse()?;

// Correct — use percent-encoding
let url: Url = "http://example.com/my%20page".parse()?;

// Or use the url crate to build URLs
let url = Url::parse("http://example.com")?;
let mut url = url;
url.set_path("my page"); // Automatically encodes
println!("{}", url); // http://example.com/my%20page
```

### Fix 2: Use Url::parse_with_base for relative URLs

```rust
use url::Url;

// Wrong — missing scheme
let url: Url = "example.com/path".parse()?; // parsed as path

// Correct — use a base URL
let base = Url::parse("http://example.com")?;
let url = base.join("path")?;
println!("{}", url); // http://example.com/path
```

### Fix 3: Validate URLs before using them

```rust
fn is_valid_url(s: &str) -> bool {
    Url::parse(s).is_ok()
}

fn validate_url(s: &str) -> Result<String, String> {
    let url = Url::parse(s)
        .map_err(|e| format!("Invalid URL '{}': {}", s, e))?;

    if url.scheme().is_empty() {
        return Err("URL must have a scheme (http, https, etc.)".to_string());
    }

    if url.host_str().is_none() {
        return Err("URL must have a host".to_string());
    }

    Ok(url.to_string())
}

fn main() {
    let urls = vec![
        "http://example.com/path",
        "not a url",
        "ftp://files.example.com",
        "http://example.com:8080/path?q=1",
    ];

    for url in urls {
        match validate_url(url) {
            Ok(valid) => println!("Valid: {}", valid),
            Err(e) => println!("Invalid: {}", e),
        }
    }
}
```

### Fix 4: Handle URL encoding for special characters

```rust
use url::Url;
use percent_encoding::{utf8_percent_encode, NON_ALPHANUMERIC};

fn encode_url_component(s: &str) -> String {
    utf8_percent_encode(s, NON_ALPHANUMERIC).to_string()
}

fn build_search_url(base: &str, query: &str) -> Result<url::Url, url::ParseError> {
    let mut url = Url::parse(base)?;
    url.set_query(Some(&format!("q={}", encode_url_component(query))));
    Ok(url)
}

fn main() -> Result<(), url::ParseError> {
    let url = build_search_url("http://search.example.com", "hello world")?;
    println!("{}", url);
    // http://search.example.com?q=hello%20world
    Ok(())
}
```

## Examples

```rust
use url::Url;

fn main() {
    // This fails because of the space
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

- [Invalid URL]({{< relref "/languages/rust/invalid-url" >}}) — URL contains invalid characters.
- [JSON Parse]({{< relref "/languages/rust/json-parse" >}}) — invalid JSON syntax.
- [Parse Int]({{< relref "/languages/rust/parse-int" >}}) — invalid integer in string.
