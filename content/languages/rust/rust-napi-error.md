---
title: "[Solution] Rust NAPI Error — How to Fix"
description: "Fix napi-rs errors for Node.js native modules. Resolve binding generation, type conversion, and async issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# NAPI Error

NAPI errors occur when using the `napi-rs` crate to build Node.js native addons — issues with type conversion, async tasks, and thread-safe function calls.

## Common Causes

```rust
use napi_derive::napi;

// Returning non-NAPI-safe types
#[napi]
fn bad_function() -> Vec<String> { // Vec<String> not directly NAPI-safe
    vec!["hello".into()]
}

// Missing #[napi] attribute on exported functions
fn exported() -> i32 { 42 } // Not visible to Node.js

// Thread safety issues with non-Send types
struct NonSend { data: *mut u8 } // !Send, cannot use in async tasks
```

## How to Fix

1. **Use NAPI-compatible types**

```rust
use napi_derive::napi;

#[napi]
fn greet(name: String) -> String {
    format!("Hello, {}!", name)
}

#[napi]
fn get_numbers() -> Vec<i32> {
    vec![1, 2, 3, 4, 5]
}

#[napi]
fn parse_json(input: String) -> napi::Result<serde_json::Value> {
    serde_json::from_str(&input).map_err(|e| napi::Error::from_reason(e.to_string()))
}
```

2. **Use `#[napi]` async functions for non-blocking operations**

```rust
use napi_derive::napi;

#[napi]
async fn fetch_data(url: String) -> napi::Result<String> {
    let body = reqwest::get(&url)
        .await
        .map_err(|e| napi::Error::from_reason(e.to_string()))?
        .text()
        .await
        .map_err(|e| napi::Error::from_reason(e.to_string()))?;
    Ok(body)
}
```

3. **Use thread-safe functions for callbacks from async contexts**

```rust
use napi::threadsafe_function::{ThreadsafeFunction, ErrorStrategy};
use napi_derive::napi;

type TsFn = ThreadsafeFunction<String, ErrorStrategy::Fatal>;

#[napi]
fn start_task(callback: TsFn) {
    std::thread::spawn(move || {
        callback.call("Result from thread".into(), napi::threadsafe_function::ThreadsafeFunctionCallMode::NonBlocking).ok();
    });
}
```

## Examples

```rust
use napi_derive::napi;
use napi::JsNumber;

#[napi]
fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a: u64 = 0;
            let mut b: u64 = 1;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

#[napi]
fn process_array(data: Vec<i32>) -> Vec<i32> {
    data.into_iter().filter(|x| x % 2 == 0).map(|x| x * 2).collect()
}
```

```javascript
// In JavaScript
const addon = require('./my-addon.node');
console.log(addon.fibonacci(10)); // 55
console.log(addon.processArray([1, 2, 3, 4, 5])); // [4, 8]
```

## Related Errors

- [PyO3 Error]({{< relref "/languages/rust/rust-pyo3-error" >}}) — Python bindings
- [FFI Gen Error]({{< relref "/languages/rust/rust-ffigen-error" >}}) — FFI generation
- [CBindgen Error]({{< relref "/languages/rust/rust-cbindgen-error" >}}) — C bindings
