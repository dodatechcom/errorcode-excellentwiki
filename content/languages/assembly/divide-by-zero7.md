---
title: "Divide by zero"
description: "A divide by zero error occurs when the CPU attempts to divide an integer by zero, triggering a hardware exception."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["division", "zero", "arithmetic", "exception"]
weight: 5
---

## What This Error Means

A divide by zero error occurs when the CPU's `div` or `idiv` instruction attempts to divide a value by zero. Unlike some higher-level languages that may return infinity or NaN for floating-point division, integer division by zero raises a hardware exception (SIGFPE on Linux) that terminates the process immediately.

## Common Causes

- Divisor register not initialized or set to zero
- Incorrect calculation of the divisor before the division
- Missing validation of input values before performing division
- Loop counter or index accidentally reaching zero before the division

## How to Fix

```asm
; WRONG: Dividing without checking divisor
mov rax, 100
xor rbx, rbx           ; rbx = 0
div rbx                 ; SIGFPE - divide by zero

; CORRECT: Check divisor before dividing
mov rax, 100
xor rbx, rbx
test rbx, rbx
jz .handle_zero_div
div rbx                 ; safe to divide
jmp .done
.handle_zero_div:
    ; handle the zero case (return 0, error code, etc.)
    xor rdx, rdx
    xor rax, rax
.done:
```

```asm
; WRONG: Dividing user-controlled value directly
mov rax, [user_input]
mov rcx, [divisor]
div rcx                 ; divisor could be zero

; CORRECT: Validate before dividing
mov rax, [user_input]
mov rcx, [divisor]
test rcx, rcx
jz .division_error
div rcx
```

## Examples

```asm
section .data
    numerator dd 42
    divisor dd 0

section .text
    global _start

_start:
    mov eax, [numerator]
    mov ecx, [divisor]      ; ecx = 0
    xor edx, edx
    div ecx                 ; SIGFPE: divide by zero
                           ; process terminated

    mov rax, 60
    xor rdi, rdi
    syscall
```

## Related Errors

- [Arithmetic overflow](/languages/assembly/overflow-error)
- [Invalid memory access](/languages/assembly/memory-access)
