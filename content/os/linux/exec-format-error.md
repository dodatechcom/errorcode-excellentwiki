---
title: "[Solution] Linux: exec-format-error — exec format error"
description: "Fix Linux exec-format-error errors. exec format error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 6
---
# Linux: Exec Format Error

"Exec format error" occurs when the kernel cannot execute a binary because of an invalid or unsupported format.

## Common Causes

- Binary compiled for a different architecture (ARM vs x86, 32-bit vs 64-bit)
- File is a script without proper shebang line (#!)
- Binary is corrupted or truncated
- No execute permission on the file
- Missing interpreter (e.g., ELF binary needs ld-linux)

## How to Fix

### 1. Check File Type

```bash
file /path/to/binary
```

### 2. Check Architecture

```bash
# If 32-bit binary on 64-bit system, enable multiarch
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libc6:i386
```

### 3. Check Permissions

```bash
chmod +x /path/to/binary
```

### 4. Check Shebang (for scripts)

```bash
head -1 /path/to/script
# Should be like: #!/bin/bash or #!/usr/bin/python3
```

### 5. Check Interpreter

```bash
# For ELF binaries
readelf -l /path/to/binary | grep interpreter
# If missing, install appropriate libraries
```

## Examples

```bash
$ file ./hello
./hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2

$ ./hello
-bash: ./hello: cannot execute binary file: Exec format error

$ ./hello_arm
-bash: ./hello_arm: cannot execute binary file: Exec format error

$ file ./hello_arm
./hello_arm: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV)
```
