---
title: "[Solution] Rust FFI Gen Error — How to Fix"
description: "Fix FFI generation errors. Resolve unsafe extern declarations, type mismatches, and calling convention issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# FFI Gen Error

FFI gen errors occur when generating foreign function interface bindings using tools like `bindgen`, `cbindgen`, or `dlopen` — type mapping failures, missing `extern "C"` declarations, and ABI mismatches.

## Common Causes

```rust
// Missing extern "C" — Rust name mangling prevents linking
fn process(data: *const u8, len: usize) -> i32 { 0 } // Not callable from C

// Type mismatch between Rust and C
#[repr(C)]
struct Config { name: *const i8 } // Should be *const c_char

// Calling convention mismatch
extern "stdcall" fn windows_fn() {} // Wrong on Linux

// FFI safety: types that are not FFI-safe
fn callback(f: fn(i32) -> i32) {} // fn pointers have ABI issues
```

## How to Fix

1. **Use `extern "C"` and `#[no_mangle]` for C-compatible functions**

```rust
use std::os::raw::{c_char, c_int};

#[no_mangle]
pub extern "C" fn process_data(data: *const u8, len: c_int) -> c_int {
    if data.is_null() || len <= 0 { return -1; }
    let slice = unsafe { std::slice::from_raw_parts(data, len as usize) };
    slice.iter().sum::<u8>() as c_int
}
```

2. **Use `#[repr(C)]` for all shared types**

```rust
#[repr(C)]
pub struct Point {
    pub x: f64,
    pub y: f64,
}

#[repr(C, u8)]
pub enum Color {
    Red = 0,
    Green = 1,
    Blue = 2,
}
```

3. **Use bindgen to auto-generate bindings**

```rust
// build.rs
fn main() {
    println!("cargo:rerun-if-changed=wrapper.h");
    let bindings = bindgen::Builder::default()
        .header("wrapper.h")
        .parse_callbacks(Box::new(bindgen::CargoCallbacks::new()))
        .generate()
        .expect("Failed to generate bindings");
    let out_path = std::path::PathBuf::from(std::env::var("OUT_DIR").unwrap());
    bindings.write_to_file(out_path.join("bindings.rs")).unwrap();
}
```

## Examples

```rust
use std::os::raw::{c_char, c_int};
use std::ffi::{CStr, CString};

#[no_mangle]
pub extern "C" fn greet(name: *const c_char) -> *mut c_char {
    if name.is_null() { return std::ptr::null_mut(); }
    let name = unsafe { CStr::from_ptr(name) };
    let greeting = format!("Hello, {}!", name.to_str().unwrap_or("unknown"));
    CString::new(greeting).unwrap().into_raw()
}

#[no_mangle]
pub extern "C" fn free_string(s: *mut c_char) {
    if !s.is_null() { unsafe { let _ = CString::from_raw(s); } }
}

fn main() {
    let name = CString::new("Rust").unwrap();
    let result = greet(name.as_ptr());
    if !result.is_null() {
        let greeting = unsafe { CStr::from_ptr(result) };
        println!("{}", greeting.to_str().unwrap());
        free_string(result);
    }
}
```

## Related Errors

- [CBindgen Error]({{< relref "/languages/rust/rust-cbindgen-error" >}}) — C binding generation
- [NAPI Error]({{< relref "/languages/rust/rust-napi-error" >}}) — Node.js bindings
- [PyO3 Error]({{< relref "/languages/rust/rust-pyo3-error" >}}) — Python bindings
