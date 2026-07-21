---
title: "[Solution] Assembly Position Independent Code Error -- PIC/PIE Issues"
description: "Fix assembly position independent code errors when creating PIE executables."
languages: ["assembly"]
error-types: ["link-time"]
severities: ["error"]
---

# Assembly Position Independent Code Error

This error occurs when code is not position-independent, causing issues with PIE executables or shared libraries.

## Common Causes

- Using absolute addresses instead of RIP-relative
- Not using PIC-compatible addressing
- Absolute relocations in shared library code
- Missing -fPIC or -pie flags

## How to Fix

### Use RIP-relative addressing

```asm
; WRONG: absolute addressing
mov rax, [my_data]  ; absolute address

; CORRECT: RIP-relative
lea rax, [rel my_data]  ; position-independent
```

### Link as PIE

```bash
nasm -f elf64 myfile.asm -o myfile.o
ld -pie myfile.o -o myfile
```

## Examples

```asm
; Position-independent data access
section .data
my_var: dq 42

section .text
get_var:
    lea rax, [rel my_var]
    mov rax, [rax]
    ret
```
