---
title: "[Solution] Assembly Carry Flag Error — How to Fix"
description: "Fix carry flag errors in assembly when unsigned arithmetic produces a result that exceeds the register capacity."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1017
---

# Carry Flag Error

The carry flag (CF, EFLAGS bit 0) indicates that an unsigned arithmetic operation produced a result too large for the destination. Misusing CF after `ADD`/`SUB`/`CMP` or ignoring `ADC`/`SBB` in multi-precision arithmetic causes silent data corruption.

## Common Causes

- Adding two unsigned values that exceed the register width
- Not using ADC (add with carry) for multi-word addition
- Using JC/JNC after non-arithmetic instructions that modify CF
- SUB with borrow not propagated through SBB in big-number math

## How to Fix

### Solution 1 — Multi-precision addition with ADC

```assembly
; Add 128-bit numbers: RDX:RAX = RDX:RAX + R11:R10
    add rax, r10
    adc rdx, r11           ; adds with carry from low part
    ret
```

### Solution 2 — Check carry after unsigned compare

```assembly
compare_u64:
    cmp rdi, rsi
    jb .first_less         ; CF=1: first < second (unsigned)
    ja .first_greater
    ret                    ; equal
.first_less:
.first_greater:
    ret
```

### Solution 3 — Multi-word subtraction with SBB

```assembly
; Subtract 128-bit: RDX:RAX -= R11:R10
    sub rax, r10
    sbb rdx, r11           ; subtracts with borrow
    ret
```

### Solution 4 — Propagate carry through multiplication

```assembly
; 64×64→128 unsigned multiply
umul128:
    mul rsi                ; RDX:RAX = RAX * RSI
    ; result in RDX (high) : RAX (low)
    ret
```

## Examples

A bignum library adds two 256-bit numbers stored as four 64-bit limbs. Without ADC propagating carry between limbs, the result wraps at each limb boundary and produces an incorrect sum.

## Related Errors

- [Overflow Flag](/languages/assembly/asm-overflow-flag-error) — signed overflow
- [Integer Overflow](/languages/assembly/asm-integer-overflow-asm) — general overflow
- [Zero Flag](/languages/assembly/asm-zero-flag-error) — zero result detection
