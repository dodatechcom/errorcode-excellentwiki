---
title: "[Solution] Assembly BSS Segment Error -- Uninitialized Data Issues"
description: "Fix assembly BSS segment errors when using uninitialized data incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly BSS Segment Error

This error occurs when BSS segment data is accessed before being initialized or when BSS is used incorrectly.

## Common Causes

- Accessing BSS data without initializing it first
- Using `db` instead of `resb/resw/resd/resq` in BSS
- BSS section too small for the data being stored
- Assuming BSS is zero-initialized on all platforms

## How to Fix

### Initialize BSS data

```asm
; WRONG: BSS data not initialized before use
section .bss
    buffer resb 256

section .text
    mov al, [buffer]  ; contains garbage

; CORRECT: initialize first
section .bss
    buffer resb 256

section .text
    ; Zero-fill buffer
    cld
    xor al, al
    mov rdi, buffer
    mov rcx, 256
    rep stosb
    ; Now safe to use
```

### Use correct BSS directives

```asm
section .bss
    byte_var resb 1    ; reserve 1 byte
    word_var resw 1    ; reserve 1 word (2 bytes)
    dword_var resd 1   ; reserve 1 dword (4 bytes)
    qword_var resq 1   ; reserve 1 qword (8 bytes)
    array resb 1024    ; reserve 1024 bytes
```

## Examples

```asm
section .bss
    accumulator resd 1

section .text
    ; Initialize accumulator
    mov dword [accumulator], 0
    ; ... use accumulator ...
```
