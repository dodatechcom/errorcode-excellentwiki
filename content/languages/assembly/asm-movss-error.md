---
title: "[Solution] Assembly MOVSS Error -- Scalar Float Move Issues"
description: "Fix assembly MOVSS errors when using scalar single-precision float move instructions."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly MOVSS Error

This error occurs when MOVSS is used incorrectly, such as mixing scalar and packed operations.

## Common Causes

- Using MOVSS with packed data
- Forgetting that MOVSS zeroes upper bits of XMM register
- Mixing MOVSS with MOVAPS (packed vs scalar)
- Incorrect memory alignment for MOVSS

## How to Fix

### Use MOVSS for scalar operations

```asm
; WRONG: using packed add for scalar
addps xmm0, xmm1  ; adds all 4 floats

; CORRECT: use MOVSS for scalar
movss xmm0, [float1]
movss xmm1, [float2]
addss xmm0, xmm1  ; adds single float
```

### Understand zero-extension

```asm
; MOVSS zeros upper 128 bits of YMM
vmovss xmm0, [value]  ; YMM0[127:0] = value, YMM0[255:128] = 0
```

## Examples

```asm
; Scalar float addition
section .data
align 4
val_a: dd 3.14
val_b: dd 2.71

section .text
add_floats:
    vmovss xmm0, [val_a]
    vaddss xmm0, xmm0, [val_b]
    ret
```
