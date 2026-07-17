---
title: "Division by zero in Assembly"
description: "Division by zero in Assembly causes a hardware exception (SIGFPE) when the DIV or IDIV instruction divides by zero."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The x86/x64 `DIV` and `IDIV` instructions raise a hardware exception (SIGFPE on Linux) when the divisor is zero. Unlike some higher-level languages, this is an immediate hardware trap.

## Common Causes

- Divisor register not initialized
- Computed divisor resulting in zero
- Missing zero-check before division
- Data loaded from uninitialized memory

## How to Fix

```asm
; WRONG: Dividing without checking
section .text
    mov rax, 100
    xor rdx, rdx
    mov rbx, 0
    div rbx       ; SIGFPE: division by zero

; CORRECT: Check divisor first
    mov rax, 100
    xor rdx, rdx
    mov rbx, 0
    test rbx, rbx
    jz .handle_error
    div rbx       ; Safe division
```

```asm
; CORRECT: Use safe division wrapper
safe_div:
    ; Input: rax = dividend, rbx = divisor
    ; Output: rax = quotient, rdx = remainder
    test rbx, rbx
    jz .divide_by_zero
    xor rdx, rdx
    div rbx
    ret
.divide_by_zero:
    ; Handle error: return 0 or signal
    xor rax, rax
    ret
```

## Examples

```asm
section .text
    mov rax, 42
    xor rdx, rdx
    mov rcx, 0
    div rcx    ; SIGFPE: floating point exception (misnamed)
```

## Related Errors

- [Segmentation Fault](/languages/assembly/segmentation-fault) - memory errors
- [General Protection Fault](/languages/assembly/asm-general-protection) - protection errors
