---
title: "[Solution] Assembly: x87 floating-point exception"
description: "Fix Assembly x87 FPU exceptions by checking status flags and handling IEEE special values."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An x87 floating-point exception in Assembly occurs when an FPU instruction encounters an error condition such as division by zero, overflow, underflow, invalid operation, or denormalized operand. The x87 FPU raises exceptions through the status register (FPSW) and can deliver SIGFPE on Linux if exceptions are unmasked. Each exception type has a corresponding bit in the status word and a mask bit in the control word. When an unmasked exception occurs and the corresponding mask is not set, the CPU delivers a hardware exception.

## Why It Happens

x87 FPU exceptions occur from several arithmetic conditions. Invalid operation exceptions happen when computing 0/0, infinity - infinity, or sqrt of a negative number. Division by zero occurs when dividing a non-zero value by zero. Overflow happens when a result exceeds the maximum representable value (approximately 1.8e308 for double precision). Underflow occurs when a result is too small to represent as a normalized number. Inexact result exceptions occur when the true mathematical result cannot be exactly represented. Using FPU instructions on non-numeric data (NaN, infinity) can also trigger exceptions. Not initializing the FPU before use, or using x87 instructions after switching to SSE mode, produces unexpected exceptions.

## How to Fix It

**Check FPU status after operations:**

```asm
section .text
global safe_fpu_divide

safe_fpu_divide:
    ; EDX:EAX = numerator (64-bit integer)
    ; EBX:ECX = denominator (64-bit integer)
    push rbp
    mov rbp, rsp
    sub rsp, 16

    ; Initialize FPU
    finit

    ; Load numerator
    push rdx
    push rax
    fild qword [rsp]
    add rsp, 16

    ; Load denominator
    push rbx
    push rcx
    fild qword [rsp]
    add rsp, 16

    ; Check for zero denominator
    ftst
    fstsw ax
    sahf
    je .division_by_zero

    ; Perform division
    fdivp st1, st0

    ; Check FPU status for exceptions
    fstsw ax
    sahf
    jc .fpu_error       ; Carry = invalid operation
    jo .fpu_overflow     ; Overflow flag
    jz .fpu_underflow    ; Zero flag (underflow)

    ; Store result
    fstp qword [rbp-8]
    mov rax, [rbp-8]
    leave
    ret

.division_by_zero:
.fpu_overflow:
.fpu_underflow:
.fpu_error:
    fldz                ; Return 0.0 on error
    fstp qword [rbp-8]
    mov rax, [rbp-8]
    leave
    ret
```

**Mask FPU exceptions for non-critical computation:**

```asm
setup_fpu:
    finit
    ; Set FPU control word to mask all exceptions
    ; Bits 0-5: exception masks (1 = masked)
    ; Bit 6: precision control
    ; Bits 8-9: rounding control
    push word 0x037F    ; Mask all exceptions, round to nearest
    fldcw [rsp]
    add rsp, 2
    ret

    ; Now FPU operations will not raise hardware exceptions
    ; Results will be Inf, -Inf, NaN, or 0 instead
```

**Use SSE instead of x87 for modern code:**

```asm
section .text
; SSE2 division (preferred over x87)
sse_divide:
    movsd xmm0, [numerator]   ; Load double
    movsd xmm1, [denominator]
    divsd xmm0, xmm1          ; Divide
    movsd [result], xmm0      ; Store
    ; Check for NaN/Inf with ucomisd
    ucomisd xmm0, xmm0        ; Compare with itself
    jp .result_is_nan
    ret
.result_is_nan:
    ; Handle NaN result
    ret


## Common Mistakes

- Not calling `finit` before using FPU instructions
- Assuming x87 exceptions are masked by default (they may not be)
- Not checking FPSW after FPU operations for silent errors
- Using x87 instructions when SSE/SSE2 is available and preferred
- Forgetting that NaN comparisons always return unordered

## Related Pages

- [SSE illegal instruction in Assembly](/languages/assembly/assembly-sse-error-new)
- [General protection fault in Assembly](/languages/assembly/assembly-alignment-fault-new)
- [Invalid opcode in Assembly](/languages/assembly/assembly-invalid-opcode-new)
- [Page fault in Assembly](/languages/assembly/assembly-page-fault-new)
