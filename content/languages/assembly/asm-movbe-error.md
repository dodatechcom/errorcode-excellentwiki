---
title: "[Solution] Assembly MOVBE Error -- Incorrect Byte-Order Move"
description: "Fix assembly MOVBE errors when using MOVBE instruction for byte-order conversion."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly MOVBE Error

This error occurs when the MOVBE instruction is used incorrectly for byte-order conversion during data movement.

## Common Causes

- Using MOVBE on unsupported CPUs (requires MOVBE feature)
- Wrong operand size for MOVBE
- Not checking CPUID for MOVBE support
- Using MOVBE where BSWAP would suffice

## How to Fix

### Check for MOVBE support

```asm
; Check CPUID for MOVBE
has_movbe:
    push rbx
    mov eax, 1
    cpuid
    pop rbx
    test ecx, 1 << 22  ; MOVBE bit
    setnz al
    movzx eax, al
    ret
```

### Use MOVBE correctly

```asm
; WRONG: wrong operand sizes
movbe eax, [mem]  ; loads 4 bytes, no swap needed for 32-bit

; CORRECT: use for multi-byte data
movbe eax, [mem]  ; load and byte-swap 32-bit
; equivalent to: bswap on loaded value
```

## Examples

```asm
; Load big-endian 32-bit value
load_be32:
    movbe eax, [rdi]  ; load and convert to little-endian
    ret

; Store as big-endian
store_be32:
    movbe [rdi], eax  ; convert and store
    ret
```
