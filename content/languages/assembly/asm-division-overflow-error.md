---
title: "[Solution] Assembly Division Overflow — How to Fix"
description: "Fix division overflow errors in assembly when the quotient is too large for the destination register."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1007
---

# Division Overflow

When using `DIV` (unsigned) or `IDIV` (signed), if the quotient does not fit in the destination register (AL/AX/EAX/RAX), the CPU raises a division error (SIGFPE on Linux). This is distinct from divide-by-zero.

## Common Causes

- Dividend much larger than divisor: `DX:AX / BX` where quotient > 0xFFFF
- Signed division of `INT_MIN / -1` produces INT_MIN overflow
- Dividend in RDX:RAX with RDX set too high for unsigned division
- Using 8-bit DIV when the quotient exceeds 255

## How to Fix

### Solution 1 — Pre-check quotient range

```assembly
safe_div_u64:
    ; rdx:rax / rsi → check if quotient fits in rax
    mov rdi, rdx
    xor edx, edx
    cmp rdi, rsi
    jae .overflow
    div rsi
    ret
.overflow:
    mov rax, -1
    ret
```

### Solution 2 — Handle INT_MIN / -1

```assembly
safe_div_s32:
    cmp eax, 0x80000000    ; INT_MIN
    jne .normal
    cmp ecx, -1
    je .overflow
.normal:
    cdq
    idiv ecx
    ret
.overflow:
    mov eax, 0x80000000   ; return INT_MIN as saturated result
    ret
```

### Solution 3 — Use wider division

```assembly
; If DX is non-zero and you need all bits, widen to 128-bit
    mov rax, dividend_lo
    mov rdx, dividend_hi
    div rsi               ; rdx:rax / rsi
```

### Solution 4 — Scale down before dividing

```assembly
; If dividing very large numbers, reduce first
    shr rax, 8            ; divide by 256
    shr rsi, 8
    div rsi               ; less likely to overflow
```

## Examples

A timing routine computes `rdx:rax / ecx` where rdx holds a large TSC delta. If rdx >= ecx, the quotient overflows. Pre-checking rdx against the divisor prevents the crash.

## Related Errors

- [Divide by Zero](/languages/assembly/asm-divide-error) — zero divisor
- [Integer Overflow](/languages/assembly/asm-integer-overflow-asm) — arithmetic overflow
- [SIGFPE](/languages/assembly/asm-sigfpe-error) — floating-point exception signal
