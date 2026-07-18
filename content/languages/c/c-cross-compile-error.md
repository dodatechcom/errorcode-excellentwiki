---
title: "[Solution] C Cross-Compilation Error — How to Fix"
description: "Fix cross-compilation errors including wrong toolchain and sysroot."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Cross-Compilation Error — How to Fix

Cross-compilation errors include wrong compiler, missing sysroot, and host library linking.

## Common Error Messages

- `cannot find -lc`
- `wrong ELF class`
- `cannot run C compiled programs`
- `target architecture mismatch`

## How to Fix It

### Correct cross-compiler

```bash
arm-linux-gnueabihf-gcc -o prog prog.c
aarch64-linux-gnu-gcc -o prog prog.c
```

### Configure with host

```bash
./configure --host=arm-linux-gnueabihf --build=x86_64-linux-gnu
```

### Set sysroot

```bash
arm-linux-gnueabihf-gcc --sysroot=/path/to/sysroot -o prog prog.c
```

### CMake toolchain

```cmake
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER arm-linux-gnueabihf-gcc)
```

## Common Scenarios

### Scenario 1: Using host compiler instead of cross-compiler

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Linking against host libraries

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: configure runs test programs on host

This occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Specify --host for configure
- **Tip 2:** Verify ELF format
- **Tip 3:** Use CMAKE_TOOLCHAIN_FILE
