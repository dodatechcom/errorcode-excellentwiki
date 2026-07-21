---
title: "[Solution] Assembly Loop Instruction Error -- Incorrect LOOP Usage"
description: "Fix assembly loop instruction errors when using LOOP, LOOPE, or LOOPNE incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly Loop Instruction Error

This error occurs when the LOOP instruction is used incorrectly, such as wrong counter register or missing initialization.

## Common Causes

- RCX not initialized before LOOP
- LOOP only works with RCX (64-bit) or ECX (32-bit)
- LOOPE/LOOPNE checking wrong flags
- LOOP performance issues on modern CPUs

## How to Fix

### Initialize RCX before loop

```asm
; WRONG: RCX not set
.loop:
    ; ... body ...
    loop .loop  ; RCX undefined!

; CORRECT: initialize RCX
mov rcx, 10
.loop:
    ; ... body ...
    loop .loop  ; decrements RCX, loops if != 0
```

### Use modern loop constructs

```asm
; LOOP is slow on modern CPUs, prefer:
    xor ecx, ecx
.loop:
    inc ecx
    cmp ecx, 10
    jl .loop
```

## Examples

```asm
; Sum array using LOOP
sum_array:
    xor eax, eax
    mov rcx, rdx       ; count
.loop:
    add eax, [rdi + rcx*4 - 4]
    loop .loop
    ret
```
