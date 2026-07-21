---
title: "[Solution] Assembly String Instruction Error -- Incorrect MOVS/CMPS Usage"
description: "Fix assembly string instruction errors when using MOVS, CMPS, or SCAS incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly String Instruction Error

This error occurs when string instructions are used with incorrect direction flag or register setup.

## Common Causes

- DF (Direction Flag) not cleared before forward operations
- RSI/RDI not loaded with correct source/destination
- RCX not set for REP prefix count
- Using wrong string instruction for the operation

## How to Fix

### Clear direction flag for forward operations

```asm
; WRONG: DF may be set, causing backward copy
mov rsi, src
mov rdi, dst
mov rcx, len
rep movsb  ; may go backwards!

; CORRECT: clear DF first
cld
mov rsi, src
mov rdi, dst
mov rcx, len
rep movsb
```

### Use correct registers

```asm
; SCASB: scan AL in [RDI]
cld
mov rdi, buffer
mov al, 'A'
mov rcx, buffer_len
repne scasb  ; find first 'A'
```

## Examples

```asm
; String length using SCASB
strlen:
    cld
    xor al, al
    mov rdi, rdi      ; string pointer
    mov rcx, -1       ; maximum count
    repne scasb
    not rcx
    dec rcx
    mov rax, rcx
    ret
```
