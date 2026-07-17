---
title: "[Solution] FPE: division by zero in assembly"
description: "Fix assembly floating-point exceptions caused by division by zero operations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["fpe", "division", "zero", "floating-point", "exception", "assembly"]
weight: 5
---

## What This Error Means

A floating-point exception (SIGFPE) from division by zero occurs when assembly code attempts to divide an integer or floating-point value by zero. The CPU raises an exception for this undefined operation.

## Common Causes

- Integer division by zero (idiv instruction)
- Floating-point division by zero (divss/divsd)
- Uninitialized divisor register
- Missing zero-check before division
- Incorrect register values

## How to Fix

```asm
; WRONG: Division without zero check
section .text
    mov rax, 100
    mov rcx, 0
    cqo
    idiv rcx      ; SIGFPE: division by zero

; CORRECT: Check divisor before division
    mov rax, 100
    mov rcx, 0
    test rcx, rcx
    jz .div_by_zero
    cqo
    idiv rcx
    jmp .done
.div_by_zero:
    ; Handle error
    mov rax, 0
.done:
```

```asm
; WRONG: Floating-point division by zero
section .text
    vxorps xmm0, xmm0, xmm0
    vxorps xmm1, xmm1, xmm1
    vdivss xmm2, xmm0, xmm1  ; SIGFPE

; CORRECT: Check for zero
    vxorps xmm0, xmm0, xmm0
    vxorps xmm1, xmm1, xmm1
    vcomiss xmm1, xmm0
    je .fp_div_by_zero
    vdivss xmm2, xmm0, xmm1
    jmp .fp_done
.fp_div_by_zero:
    ; Handle or return infinity
    vxorps xmm2, xmm2, xmm2
.fp_done:
```

```asm
; CORRECT: Safe integer division function
; Input: rax = dividend, rcx = divisor
; Output: rax = quotient, rdx = remainder
section .text
    global safe_div
safe_div:
    test rcx, rcx
    jz .error
    cqo
    idiv rcx
    ret
.error:
    xor rax, rax
    xor rdx, rdx
    ret
```

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Overflow](asm-out-of-memory-v2) - arithmetic errors
- [General Protection](asm-general-protection-v2) - protection faults
