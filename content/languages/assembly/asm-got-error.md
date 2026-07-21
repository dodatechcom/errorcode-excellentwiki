---
title: "[Solution] Assembly GOT Error -- Global Offset Table Issues"
description: "Fix assembly GOT errors when accessing the Global Offset Table incorrectly."
languages: ["assembly"]
error-types: ["link-time"]
severities: ["error"]
---

# Assembly GOT Error

This error occurs when the Global Offset Table (GOT) is accessed incorrectly in position-independent code.

## Common Causes

- Using absolute addresses instead of GOT entries
- Not using @GOTPCREL for external symbol access
- GOT not properly initialized by dynamic linker
- Accessing PLT instead of GOT for function calls

## How to Fix

### Access symbols via GOT

```asm
; WRONG: absolute address
mov rax, [extern_var]

; CORRECT: use GOT entry
mov rax, [extern_var wrt ..got]
; or
mov rax, [extern_var@GOTPCREL]
```

### Call functions via PLT

```asm
; WRONG: direct call (not PIC)
call extern_func

; CORRECT: call via PLT
call extern_func wrt ..plt
; or
call extern_func@PLT
```

## Examples

```asm
; Position-independent access to extern
extern printf

section .text
    lea rdi, [fmt]
    xor eax, eax
    call printf@PLT

section .data
fmt: db "Hello", 10, 0
```
