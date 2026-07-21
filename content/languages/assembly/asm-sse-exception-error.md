---
title: "[Solution] Assembly SSE Exception Error -- SIMD Floating Point Issues"
description: "Fix assembly SSE exception errors when SIMD instructions cause floating point exceptions."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly SSE Exception Error

This error occurs when SSE floating-point instructions cause exceptions due to invalid operations, overflow, or denormalized numbers.

## Common Causes

- NaN propagation in SIMD operations
- Division by zero in packed float operations
- Unmasked SSE exceptions causing SIGFPE
- Denormalized numbers slowing operations

## How to Fix

### Mask SSE exceptions

```asm
; WRONG: exceptions unmasked
stmxcsr [old_mxcsr]
; MXCSR exceptions enabled

; CORRECT: mask exceptions
stmxcsr [old_mxcsr]
mov eax, [old_mxcsr]
or eax, 0x1F80       ; mask all SSE exceptions
ldmxcsr eax
```

### Handle denormals

```asm
; Set FTZ (flush-to-zero) and DAZ (denormals-are-zero)
stmxcsr [mxcsr]
or dword [mxcsr], (1 << 15) | (1 << 6)  ; FTZ | DAZ
ldmxcsr [mxcsr]
```

## Examples

```asm
section .text
init_sse:
    stmxcsr [mxcsr]
    or dword [mxcsr], 0x8040  ; mask overflow and precision
    ldmxcsr [mxcsr]
    ret
```
