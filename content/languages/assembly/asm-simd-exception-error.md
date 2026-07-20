---
title: "[Solution] Assembly SIMD Exception — How to Fix"
description: "Fix SIMD floating-point exceptions in assembly caused by SSE/AVX instruction errors with MXCSR flags."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1011
---

# SIMD Floating-Point Exception (#XF, INT 19)

SSE and AVX instructions signal floating-point exceptions through the MXCSR register. When an unmasked exception occurs during a SIMD instruction, interrupt 19 fires.

## Common Causes

- `DIVPS`/`DIVSS` with a denominator of zero and ZM flag unmasked
- `SQRTPS`/`SQRTSS` with a negative operand and IM flag unmasked
- Result too large for single-precision (overflow) with OM unmasked
- Denormal operand with DM unmasked
- MXCSR defaults to masking all exceptions, but code may unmask them

## How to Fix

### Solution 1 — Mask all SIMD exceptions

```assembly
mask_all_simd:
    stmxcsr [old_mxcsr]
    mov eax, [old_mxcsr]
    or eax, 0x1F80         ; set mask bits for all 5 exceptions
    mov [new_mxcsr], eax
    ldmxcsr [new_mxcsr]
```

### Solution 2 — Check MXCSR exceptions after computation

```assembly
safe_simd_div:
    divps xmm0, xmm1
    stmxcsr [mxcsr_val]
    test dword [mxcsr_val], 0x01  ; IE (Invalid Operation)
    jnz .invalid
    test dword [mxcsr_val], 0x04  ; ZE (Zero Divide)
    jnz .zero_div
    ret
.invalid:
.zero_div:
    ; handle error
    ret
```

### Solution 3 — Use denormal-free operations (DAZ/FTZ)

```assembly
enable_ftz_daz:
    stmxcsr [old_mxcsr]
    mov eax, [old_mxcsr]
    or eax, 0x0040         ; DAZ — Denormals Are Zero
    or eax, 0x8000         ; FTZ — Flush To Zero
    mov [new_mxcsr], eax
    ldmxcsr [new_mxcsr]
```

### Solution 4 — Validate SIMD operands before computation

```assembly
simd_safe_sqrt:
    ; Check for negative values in xmm0
    movaps xmm1, xmm0
    andps xmm1, [sign_mask]  ; isolate sign bit
    ptest xmm1, xmm1
    jnz .negative_input
    sqrtss xmm0, xmm0
    ret
.negative_input:
    ; return NaN
    movss xmm0, [nan_val]
    ret

section .data
sign_mask: dd 0x80000000, 0x80000000, 0x80000000, 0x80000000
nan_val:   dd 0x7FC00000
```

## Examples

A graphics engine enables FPU exceptions for debugging. A divide-by-zero in a texture coordinate calculation triggers #XF. The fix is to mask SIMD exceptions during rendering and only unmask them in debug builds.

## Related Errors

- [FPU Error](/languages/assembly/asm-fpu-error) — x87 exceptions
- [Alignment Check](/languages/assembly/asm-alignment-check-error) — MOVAPS alignment
- [SIGFPE](/languages/assembly/asm-sigfpe-error) — integer divide by zero
