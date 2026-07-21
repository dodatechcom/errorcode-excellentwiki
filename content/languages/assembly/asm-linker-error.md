---
title: "[Solution] Assembly Linker Error -- Unresolved External Symbols"
description: "Fix assembly linker errors when external symbols cannot be resolved."
languages: ["assembly"]
error-types: ["link-time"]
severities: ["error"]
---

# Assembly Linker Error

This error occurs when the linker cannot find definitions for referenced symbols.

## Common Causes

- Missing EXTERN declarations
- Symbol defined in wrong section
- Linking order of object files matters
- Library not included in link command

## How to Fix

### Declare and define correctly

```asm
; WRONG: using undeclared external
call printf

; CORRECT: declare extern
extern printf

; In another file, define with global
global my_func
my_func:
    ; ...
```

### Fix link order

```bash
# WRONG: order matters
ld myfile.o -lc  # may fail

# CORRECT: objects before libraries
ld myfile.o -o myfile -lc
# or with gcc
gcc myfile.o -o myfile
```

## Examples

```asm
; main.asm
extern printf
section .text
global main
main:
    lea rdi, [fmt]
    xor eax, eax
    call printf
    ret
fmt: db "Hello", 10, 0
```
