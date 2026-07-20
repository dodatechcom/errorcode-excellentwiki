---
title: "[Solution] Rust WASM Bindgen Error — How to Fix"
description: "Fix wasm-bindgen errors. Resolve JavaScript interop, type mapping, and WebAssembly compilation issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# WASM Bindgen Error

WASM bindgen errors occur when using `wasm-bindgen` to generate JavaScript bindings for Rust WebAssembly — type conversion failures, missing imports, and browser compatibility issues.

## Common Causes

```rust
use wasm_bindgen::prelude::*;

// Returning non-WASM-safe types
#[wasm_bindgen]
fn bad_return() -> Vec<String> { // Vec<String> needs conversion
    vec!["hello".into()]
}

// Missing #[wasm_bindgen] attribute
fn exported_to_js() -> i32 { 42 } // Not visible in JS

// Using std types not available in WASM
use std::net::TcpStream; // Not available in wasm32
```

## How to Fix

1. **Use WASM-compatible types**

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

#[wasm_bindgen]
pub fn fibonacci(n: u32) -> u64 {
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
```

2. **Use `js_sys` and `web_sys` for browser APIs**

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn get_window_title() -> String {
    web_sys::window()
        .and_then(|w| w.document())
        .and_then(|d| d.title())
        .unwrap_or_default()
}

#[wasm_bindgen]
pub fn set_element_text(id: &str, text: &str) -> Result<(), JsValue> {
    let window = web_sys::window().unwrap();
    let document = window.document().unwrap();
    let element = document.get_element_by_id(id).unwrap();
    element.set_text_content(Some(text))?;
    Ok(())
}
```

3. **Handle console logging from WASM**

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);
}

macro_rules! console_log {
    ($($t:tt)*) => (log(&format_args!($($t)*).to_string()))
}

#[wasm_bindgen]
pub fn process_data(data: &str) -> String {
    console_log!("Processing: {}", data);
    data.to_uppercase()
}
```

## Examples

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Counter {
    value: i32,
}

#[wasm_bindgen]
impl Counter {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Counter {
        Counter { value: 0 }
    }

    pub fn increment(&mut self) {
        self.value += 1;
    }

    pub fn get_value(&self) -> i32 {
        self.value
    }
}
```

```javascript
// In JavaScript
const { Counter } = require('./my_wasm_pkg');
const counter = new Counter();
counter.increment();
console.log(counter.get_value()); // 1
```

## Related Errors

- [NAPI Error]({{< relref "/languages/rust/rust-napi-error" >}}) — Node.js bindings
- [PyO3 Error]({{< relref "/languages/rust/rust-pyo3-error" >}}) — Python bindings
- [FFI Gen Error]({{< relref "/languages/rust/rust-ffigen-error" >}}) — FFI generation
