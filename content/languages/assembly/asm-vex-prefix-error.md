---
title: "[Solution] Assembly VEX Prefix Error -- Incorrect VEX Encoding"
description: "Fix assembly VEX prefix errors when encoding AVX instructions incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly VEX Prefix Error

This error occurs when VEX-prefixed instructions are encoded incorrectly, causing wrong register selection or operand size.

## Common Causes

- VEX.vvvv field selecting wrong source register
- Missing REX.V extension for high registers (R8-R15)
- 256-bit operation with 128-bit VEX.L
- Mixing VEX and legacy SSE encoding

## How to Fix

### Use correct VEX encoding

```asm
; WRONG: wrong register in VEX.vvvv
vaddps xmm0, xmm8, xmm1  ; VEX.vvvv must encode xmm8

; CORRECT: VEX.vvvv is inverted (NOT of register number)
; xmm8 = 1000, VEX.vvvv = 0111 (NOT of 1000)
vaddps xmm0, xmm8, xmm1
```

### Use assemblers for VEX

```asm
; Let assembler handle VEX encoding
vaddps ymm0, ymm1, ymm2
; assemblers encode VEX prefix automatically
```

## Examples

```asm
; AVX2 multiply
section .data
align 32
vec: dd 1, 2, 3, 4, 5, 6, 7, 8

section .text
vmul_vector:
    vmovdqu ymm0, [vec]
    vpmulld ymm1, ymm0, ymm0
    ret
```
