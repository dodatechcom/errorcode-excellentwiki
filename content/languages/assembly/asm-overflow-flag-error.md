---
title: "[Solution] Assembly Overflow Flag Error — How to Fix"
description: "Fix overflow flag errors in assembly when arithmetic operations produce results that exceed the destination register size."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1016
---

# Overflow Flag Error

The overflow flag (OF, EFLAGS bit 11) is set when a signed arithmetic operation produces a result that cannot be represented in the destination operand. Using `INTO` or `JO` without handling overflow leads to unexpected behavior.

## Common Causes

- Adding two large positive signed integers that overflow into negative
- Multiplying INT_MAX * 2 in a 32-bit register
- Negating INT_MIN (no positive representation in same width)
- `ADD`/`SUB`/`IMUL` producing a result outside the signed range

## How to Fix

### Solution 1 — Check OF after arithmetic

```assembly
safe_add_s32:
    add edi, esi
    jo .overflow
    mov eax, edi
    ret
.overflow:
    mov eax, 0x7FFFFFFF    ; clamp to INT_MAX
    ret
```

### Solution 2 — Use INTO for automatic overflow trap

```assembly
    mov eax, 0x7FFFFFF0
    add eax, 0x20          ; OF=1
    into                    ; raises interrupt 4 if OF=1
```

### Solution 3 — Use wider registers for extended precision

```assembly
safe_add_i64:
    movsxd rax, edi        ; sign-extend 32-bit to 64-bit
    movsxd rcx, esi
    add rax, rcx           ; no overflow in 64-bit
    ret
```

### Solution 4 — Multiply with overflow check via EDX

```assembly
safe_imul:
    imul edi, esi          ; result in edi, OF set if truncated
    jo .overflow
    mov eax, edi
    ret
.overflow:
    ; use cdq + idiv for 64-bit result
    mov eax, edi
    cdq
    idiv ecx               ; full 64/32 division
    ret
```

## Examples

A financial calculator adds two 32-bit cent values. When the sum exceeds INT_MAX, OF is set and the result wraps to negative. Checking JO after the add and clamping prevents corrupt financial data.

## Related Errors

- [Carry Flag](/languages/assembly/asm-carry-flag-error) — unsigned overflow
- [Integer Overflow](/languages/assembly/asm-integer-overflow-asm) — general overflow
- [Division Overflow](/languages/assembly/asm-division-overflow-error) — quotient too large
