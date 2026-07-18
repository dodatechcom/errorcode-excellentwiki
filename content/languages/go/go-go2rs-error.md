---
title: "[Solution] Go to Rust FFI Error — How to Fix"
description: "Fix Go-to-Rust FFI errors. Handle cgo and rust interop, memory management, and function signatures."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go to Rust FFI Error

Fix Go-to-Rust FFI errors. Handle cgo and rust interop, memory management, and function signatures.

## Why It Happens

- Go cannot call Rust functions because of wrong FFI configuration
- Memory allocated in Rust is not properly freed by Go
- FFI function signatures do not match causing crashes

## Common Error Messages

```
cgo: cannot call Rust function
```
```
cgo: invalid function signature
```
```
cgo: memory leak
```
```
cgo: signal: segmentation fault
```

## How to Fix It

### Solution 1: Set up Rust library for Go FFI

```rust
// lib.rs
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

### Solution 2: Call Rust from Go

```go
// #cgo LDFLAGS: -L. -lmyrust
// extern int add(int a, int b);
import "C"
import "fmt"

func main() {
    result := C.add(2, 3)
    fmt.Println(result) // 5
}
```

### Solution 3: Handle string passing

```rust
// Rust side
#[no_mangle]
pub extern "C" fn process_string(input: *const c_char) -> *mut c_char {
    let c_str = unsafe { CStr::from_ptr(input) };
    let result = format!("processed: {}", c_str.to_str().unwrap());
    CString::new(result).unwrap().into_raw()
}
```

### Solution 4: Build Rust for Go

```bash
# Build Rust as static library
cargo build --release
cp target/release/libmyrust.a .
# Build Go
cgo LDFLAGS=-L. CGO_LDFLAGS="-lmyrust" go build
```

## Common Scenarios

- Go cannot find Rust library because of wrong LDFLAGS
- Memory leak occurs because Rust allocated strings are not freed
- FFI crashes because function signatures do not match

## Prevent It

- Use #[no_mangle] and extern "C" in Rust functions
- Always free Rust-allocated memory with a corresponding free function
- Ensure Go and Rust agree on function signatures and calling conventions
