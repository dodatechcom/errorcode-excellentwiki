---
title: "[Solution] Assembly Calling Convention Error -- Parameter Passing Mistakes"
description: "Fix assembly calling convention errors when parameters are passed in wrong registers."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Calling Convention Error

This error occurs when function parameters are passed in registers that do not match the expected calling convention.

## Common Causes

- Using wrong registers for System V vs Windows x64 ABI
- Extra parameters not placed on stack correctly
- Return value expected in wrong register
- Mixed 32-bit and 64-bit calling conventions

## How to Fix

### Follow System V AMD64 ABI

```asm
; System V: RDI, RSI, RDX, RCX, R8, R9 for integer args
; Windows: RCX, RDX, R8, R9 for integer args

; WRONG for System V:
mov rax, rdi   ; putting first arg in RAX

; CORRECT for System V:
; First arg already in RDI from caller
```

### Windows x64 ABI

```asm
; Windows: RCX = first, RDX = second, R8 = third, R9 = fourth
my_func_win:
    mov rax, rcx  ; first argument
    add rax, rdx  ; second argument
    ret
```

## Examples

```asm
; System V: call printf("Hello %s", name)
section .data
    fmt db "Hello %s", 10, 0

section .text
    lea rdi, [fmt]     ; first arg
    lea rsi, [name]    ; second arg
    xor eax, eax       ; no vector args
    call printf
```
