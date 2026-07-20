---
title: "[Solution] Rust CBindgen Error — How to Fix"
description: "Fix cbindgen errors for C header generation. Resolve type export, visibility, and configuration issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# CBindgen Error

CBindgen errors occur when generating C/C++ bindings from Rust code using the `cbindgen` tool. Common issues include unsupported type representations, missing `#[repr(C)]` attributes, and opaque type errors.

## Common Causes

```rust
// Missing #[repr(C)] — cbindgen cannot generate proper C layout
pub struct Config {
    pub width: u32,  // Rust may reorder fields
    pub height: u32,
}

// Using Rust-only types that have no C equivalent
pub fn process(data: Vec<u8>) -> HashMap<String, Vec<u8>> { todo!() } // Cannot bind

// Enums without #[repr(C)] or #[repr(u32)]
pub enum Status { Active, Inactive, Deleted } // Not representable in C
```

## How to Fix

1. **Add `#[repr(C)]` to all types you want to export**

```rust
#[repr(C)]
pub struct Config {
    pub width: u32,
    pub height: u32,
    pub name: *const std::ffi::c_char,
}
```

2. **Use `#[repr(C, u8)]` or `#[repr(C, u32)]` for enums**

```rust
#[repr(C, u8)]
pub enum Status {
    Active = 0,
    Inactive = 1,
    Deleted = 2,
}
```

3. **Wrap unrepresentable types in opaque pointers**

```rust
// In Rust:
pub struct OpaqueData { inner: Vec<u8> }

// cbindgen.toml: parse.expand.enabled = false for opaque types
// Export only the C-compatible API
#[no_mangle]
pub extern "C" fn create_data() -> *mut OpaqueData {
    Box::into_raw(Box::new(OpaqueData { inner: vec![] }))
}
```

## Examples

```rust
use std::os::raw::c_char;

#[repr(C)]
pub struct Point { pub x: f64, pub y: f64 }

#[repr(C)]
pub enum Color { Red = 0, Green = 1, Blue = 2 }

#[no_mangle]
pub extern "C" fn distance(a: Point, b: Point) -> f64 {
    ((a.x - b.x).powi(2) + (a.y - b.y).powi(2)).sqrt()
}
```

## Related Errors

- [FFI Gen Error]({{< relref "/languages/rust/rust-ffigen-error" >}}) — FFI binding generation
- [NAPI Error]({{< relref "/languages/rust/rust-napi-error" >}}) — Node.js N-API bindings
- [PyO3 Error]({{< relref "/languages/rust/rust-pyo3-error" >}}) — Python bindings
