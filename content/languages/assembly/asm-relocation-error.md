---
title: "[Solution] Assembly Relocation Error -- Linker Symbol Issues"
description: "Fix assembly relocation errors when the linker cannot resolve symbol references."
languages: ["assembly"]
error-types: ["link-time"]
severities: ["error"]
---

# Assembly Relocation Error

This error occurs when the linker cannot resolve references to symbols defined in other object files or libraries.

## Common Causes

- Using undefined symbols
- Missing EXTERN declarations
- Incorrect section declarations
- 32-bit absolute addresses in position-independent code

## How to Fix

### Declare external symbols

```asm
; WRONG: using undefined symbol
section .text
    call printf  ; linker error if not declared

; CORRECT: declare extern
extern printf
section .text
    call printf
```

### Use position-independent code

```asm
; WRONG: absolute addressing in PIC
mov rax, [my_data]  ; absolute address

; CORRECT: RIP-relative addressing
lea rax, [rel my_data]  ; RIP-relative
```

## Examples

```asm
; Proper external declarations
extern malloc
extern free

section .text
allocate:
    push rdi
    call malloc
    pop rdi
    ret
```
