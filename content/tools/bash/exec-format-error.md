---
title: "[Solution] Exec Format Error"
description: "Resolve 'exec format error' when executing scripts or binaries."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Exec Format Error

The kernel cannot determine how to execute the file, usually due to architecture mismatch or missing shebang.

### Common Causes
- Binary compiled for different CPU architecture.
- Script missing `#!` shebang line.
- File is a data file, not executable.

### How to Fix
```bash
# Add shebang to script
#!/bin/bash
# or
#!/usr/bin/env bash

# Check binary architecture
readelf -h ./mybinary | grep Machine

# For cross-architecture binaries, use QEMU
qemu-arm ./arm-binary
```

### Example
```bash
# Broken (missing shebang)
echo "hello"

# Fixed
#!/bin/bash
echo "hello"
```
