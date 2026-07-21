---
title: "[Solution] Assembly AVX Error -- Incorrect AVX Instruction Usage"
description: "Fix assembly AVX errors when using AVX/AVX2 instructions incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly AVX Error

This error occurs when AVX instructions are used with incorrect operand forms or when the VEX prefix is missing.

## Common Causes

- Using legacy SSE encoding with VEX-encoded instructions
- Mixing VEX and non-VEX encoding
- YMM registers used without enabling AVX
- Missing VEX.L prefix for 256-bit operations

## How to Fix

### Use VEX encoding correctly

```asm
; WRONG: legacy SSE with 3 operands
addps xmm0, xmm1, xmm2  ; not valid SSE

; CORRECT: VEX encoding (AVX)
vaddps xmm0, xmm1, xmm2  ; VEX prefix implicit
```

### Enable AVX before use

```asm
; Check and enable AVX
enable_avx:
    push rbx
    mov eax, 7
    xor ecx, ecx
    cpuid
    test ebx, 1 << 28  ; AVX bit
    jz .no_avx
    
    ; Enable OSXSAVE
    mov eax, 1
    cpuid
    test ecx, 1 << 27  ; OSXSAVE
    jz .no_avx
    
    ; Enable AVX in XCR0
    xor ecx, ecx
    xgetbv
    or eax, 7           ; SSE + AVX state
    xsetbv
    pop rbx
    ret
```

## Examples

```asm
; AVX2 vector addition
section .data
align 32
vec_a: dd 1, 2, 3, 4, 5, 6, 7, 8
vec_b: dd 8, 7, 6, 5, 4, 3, 2, 1

section .text
vadd_vectors:
    vmovdqu ymm0, [vec_a]
    vmovdqu ymm1, [vec_b]
    vpaddd ymm2, ymm0, ymm1
    ret
```
