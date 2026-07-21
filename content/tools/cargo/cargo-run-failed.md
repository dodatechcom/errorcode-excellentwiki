---
title: "[Solution] Cargo Run Failed -- Fix Program Execution Error"
description: "Fix cargo run failed errors when cargo build succeeds but the program crashes or panics at runtime. Debug the runtime error."
tools: ["cargo"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the program compiled successfully but panicked or crashed when executed by `cargo run`.

## Common Causes

- Runtime panic in the code
- Missing environment variables
- File not found errors
- Network errors at runtime

## How to Fix

### 1. Run with Backtrace

```bash
RUST_BACKTRACE=1 cargo run
```

### 2. Run in Debug Mode

```bash
cargo run 2>&1
```

### 3. Use GDB for Deep Debugging

```bash
cargo build
gdb ./target/debug/my-binary
```

### 4. Check Return Code

```bash
cargo run; echo $?
```

## Examples

```bash
$ cargo run
thread 'main' panicked at 'index out of bounds', src/main.rs:5

$ RUST_BACKTRACE=1 cargo run
thread 'main' panicked at 'index out of bounds', src/main.rs:5
stack backtrace:
   0: ...
```
